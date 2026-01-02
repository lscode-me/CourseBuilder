# Case Studies
## System Design Interview & Real World Architectures

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- **Everything**: Владеть ВСЕМ материалом модулей 01-15.

- **Mental Models**: Уметь быстро переключаться между CAP, Sharding, Caching, Asynchrony.

- **Calculations**: Уметь умножать 100k на 1kb в уме.

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- **Synthesize**: Комбинировать компоненты (Redis, Kafka, Postgres, Bloom Filter) в работающие системы.

- **Calculate**: Делать "Back-of-the-envelope" расчеты на салфетке за 2 минуты.

- **Defend**: Защищать свои решения перед интервьюером (почему Cassandra, а не MySQL? Почему Push, а не Pull?).

- **Fail Gracefully**: Проектировать системы, которые ломаются частично, а не полностью (Bulkheads, Circuit Breakers).

---

## 1. Case Study 1: URL Shortener (TinyURL)

Классика жанра. Задача: сделать сервис `bit.ly`.

### 1.1 Requirements

*   **Functional**: `shorten(long_url) -> short_url`; `redirect(short_url) -> long_url`.

*   **Non-Functional**: High Availability (срок жизни ссылок — вечность), Low Latency redirect (<10ms).

*   **Scale**: 100M new links/month, 10B reads/month (100:1 ratio).

### 1.2 Back-of-the-envelope Math

*   **Write QPS**: $100M / (30 \times 24 \times 3600) \approx 40$ writes/sec. (Ничтожно).

*   **Read QPS**: $40 \times 100 = 4000$ reads/sec. (Тоже мало, один Nginx справится).

*   **Storage**: 5 лет. $100M \times 12 \times 5 = 6$ Billion links.
    *   ID (8b) + LongURL (500b) $\approx$ 500 bytes.
    *   $6B \times 500B \approx 3 TB$.
    *   3 ТБ влезет на 1 SSD. Но для HA нам нужно шардирование и репликация.

### 1.3 Design Decisions

*   **301 vs 302**:
    *   **301 (Permanent)**: Браузер кэширует. Нагрузка на сервер падает. Мы теряем статистику.
    *   **302 (Found)**: Запрос всегда идет на сервер. Мы считаем клики. Выбираем 302.
*   **ID Generation**:
    *   **Hash(URL)**: MD5 дает 128 бит. Нам нужно 7 символов Base62 ($62^7 \approx 3.5T$). MD5 придется обрезать -> Коллизии!
    *   **Random**: Генерировать, проверять в БД. Если занято — генерировать снова. Медленно.
    *   **Counter**: Инкремент `1000, 1001...` переводим в Base62.
        *   `1000 -> g8`.
        *   Плюс: Уникальность гарантирована.
        *   Минус: Предсказуемость (конкуренты узнают ваш объем).
    *   **Solution**: Distributed ID Gen (Snowflake / ZooKeeper) -> Base62.

**Реализация URL Shortener:**

```python
import hashlib
import base64

class URLShortener:
    """Сервис сокращения URL."""
    
    def __init__(self, db, cache):
        self.db = db  # PostgreSQL для персистентности
        self.cache = cache  # Redis для кэширования
    
    def shorten(self, long_url):
        """Сокращение URL."""
        # Генерируем короткий код
        short_code = self.generate_short_code(long_url)
        
        # Сохраняем в БД
        self.db.insert('urls', {
            'short_code': short_code,
            'long_url': long_url,
            'created_at': time.time()
        })
        
        # Кэшируем
        self.cache.set(f"url:{short_code}", long_url, ttl=3600)
        
        return f"https://short.ly/{short_code}"
    
    def generate_short_code(self, url):
        """Генерация короткого кода."""
        # Вариант 1: Hash-based
        hash_obj = hashlib.md5(url.encode())
        hash_hex = hash_obj.hexdigest()[:7]  # Первые 7 символов
        
        # Конвертируем в Base62
        return self.base62_encode(int(hash_hex, 16))
    
    def base62_encode(self, num):
        """Кодирование числа в Base62."""
        chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if num == 0:
            return chars[0]
        
        result = []
        while num > 0:
            result.append(chars[num % 62])
            num //= 62
        
        return ''.join(reversed(result))
    
    def redirect(self, short_code):
        """Редирект по короткому коду."""
        # Проверяем кэш
        long_url = self.cache.get(f"url:{short_code}")
        if long_url:
            return long_url
        
        # Читаем из БД
        result = self.db.query(
            "SELECT long_url FROM urls WHERE short_code = %s",
            (short_code,)
        )
        
        if result:
            long_url = result[0]['long_url']
            # Обновляем кэш
            self.cache.set(f"url:{short_code}", long_url, ttl=3600)
            return long_url
        
        return None
```

**Snowflake ID Generator:**

```python
class SnowflakeIDGenerator:
    """Генератор уникальных ID в стиле Twitter Snowflake."""
    
    def __init__(self, worker_id, datacenter_id):
        self.worker_id = worker_id  # ID воркера (0-31)
        self.datacenter_id = datacenter_id  # ID датацентра (0-31)
        self.sequence = 0
        self.last_timestamp = -1
        
        # Константы
        self.WORKER_ID_BITS = 5
        self.DATACENTER_ID_BITS = 5
        self.SEQUENCE_BITS = 12
        
        self.MAX_WORKER_ID = (1 << self.WORKER_ID_BITS) - 1
        self.MAX_DATACENTER_ID = (1 << self.DATACENTER_ID_BITS) - 1
        
        self.WORKER_ID_SHIFT = self.SEQUENCE_BITS
        self.DATACENTER_ID_SHIFT = self.SEQUENCE_BITS + self.WORKER_ID_BITS
        self.TIMESTAMP_LEFT_SHIFT = (self.SEQUENCE_BITS + self.WORKER_ID_BITS + 
                                     self.DATACENTER_ID_BITS)
        self.SEQUENCE_MASK = (1 << self.SEQUENCE_BITS) - 1
        
        # Epoch: 2020-01-01
        self.EPOCH = 1577836800000
    
    def next_id(self):
        """Генерация следующего ID."""
        timestamp = int(time.time() * 1000) - self.EPOCH
        
        if timestamp < self.last_timestamp:
            raise Exception("Clock moved backwards!")
        
        if timestamp == self.last_timestamp:
            # В той же миллисекунде - инкрементируем sequence
            self.sequence = (self.sequence + 1) & self.SEQUENCE_MASK
            if self.sequence == 0:
                # Sequence переполнился - ждем следующую миллисекунду
                timestamp = self.wait_next_millis(self.last_timestamp)
        else:
            self.sequence = 0
        
        self.last_timestamp = timestamp
        
        # Собираем ID
        id = ((timestamp << self.TIMESTAMP_LEFT_SHIFT) |
              (self.datacenter_id << self.DATACENTER_ID_SHIFT) |
              (self.worker_id << self.WORKER_ID_SHIFT) |
              self.sequence)
        
        return id
    
    def wait_next_millis(self, last_timestamp):
        """Ожидание следующей миллисекунды."""
        timestamp = int(time.time() * 1000) - self.EPOCH
        while timestamp <= last_timestamp:
            timestamp = int(time.time() * 1000) - self.EPOCH
        return timestamp

# Пример использования

generator = SnowflakeIDGenerator(worker_id=1, datacenter_id=1)
for _ in range(10):
    print(generator.next_id())
```

---

## 2. Case Study 2: Rate Limiter

Задача: API Gateway должен блокировать юзера после 10 запросов в секунду.

### 2.1 Algorithms

1.  **Token Bucket**: Ведро с монетами. Пополняется со скоростью R. Запрос забирает монету. Позволяет "всплески" (Bursts).
2.  **Leaky Bucket**: Дырявое ведро (Очередь FIFO). Вытекает с постоянной скоростью. Сглаживает трафик.
3.  **Fixed Window**: Счетчик `user:10:00:01`. Сброс каждую секунду. Проблема границ: 10 запросов в 00:00.999 и 10 в 00:01.001 -> 20 запросов за 2мс.
4.  **Sliding Window Log**: Храним таймстемпы всех 10 запросов. Точно, но жрет память.

### 2.2 Distributed Implementation (Redis)

Проблема Race Condition:

1.  User A (Current=9).
2.  User A (Current=9).
3.  Оба инкрементят.
4.  Current=10. Оба прошли. А должно быть 11 (один blocked).

Решение: Atomicity via Lua.

```lua
-- rate_limit.lua
local key = KEYS[1]
local limit = tonumber(ARGV[1])
local window = tonumber(ARGV[2]) 

local current = tonumber(redis.call('GET', key) or "0")
if current + 1 > limit then
    return 0 -- Reject
else
    redis.call("INCR", key)
    if current == 0 then
        redis.call("EXPIRE", key, window)
    end
    return 1 -- Allow
end
```

**Реализация Token Bucket:**

```python
class TokenBucket:
    """Token Bucket алгоритм для rate limiting."""
    
    def __init__(self, capacity, refill_rate):
        self.capacity = capacity  # Максимальное количество токенов
        self.refill_rate = refill_rate  # Токенов в секунду
        self.tokens = capacity  # Текущее количество токенов
        self.last_refill = time.time()
    
    def consume(self, tokens=1):
        """Потребление токенов."""
        self._refill()
        
        if self.tokens >= tokens:
            self.tokens -= tokens
            return True
        return False
    
    def _refill(self):
        """Пополнение токенов."""
        now = time.time()
        elapsed = now - self.last_refill
        
        # Добавляем токены пропорционально времени
        tokens_to_add = elapsed * self.refill_rate
        self.tokens = min(self.capacity, self.tokens + tokens_to_add)
        self.last_refill = now

# Пример использования

bucket = TokenBucket(capacity=10, refill_rate=2)  # 10 токенов, пополняется 2/сек

for i in range(15):
    if bucket.consume():
        print(f"Request {i}: Allowed")
    else:
        print(f"Request {i}: Rate limited")
    time.sleep(0.1)
```

**Sliding Window Log:**

```python
class SlidingWindowLog:
    """Sliding Window Log для точного rate limiting."""
    
    def __init__(self, max_requests, window_seconds):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = []  # Список таймстемпов запросов
    
    def is_allowed(self):
        """Проверка, разрешен ли запрос."""
        now = time.time()
        
        # Удаляем старые запросы
        cutoff = now - self.window_seconds
        self.requests = [ts for ts in self.requests if ts > cutoff]
        
        # Проверяем лимит
        if len(self.requests) < self.max_requests:
            self.requests.append(now)
            return True
        return False

# Пример

limiter = SlidingWindowLog(max_requests=10, window_seconds=60)

for i in range(15):
    if limiter.is_allowed():
        print(f"Request {i}: Allowed")
    else:
        print(f"Request {i}: Rate limited")
```

---

## 3. Case Study 3: Chat System (WhatsApp)

Задача: 1-on-1 и Групповые чаты. Статусы Sent/Delivered/Read.

### 3.1 Architecture

HTTP Request/Response неудобен (Client должен поллить).
Используем **WebSocket** (Full Duplex).

*   **Chat Server**: Держит 100k сокетов. Stateful.

*   **Service Discovery**: Zookeeper знает, на каком сервере сидит юзер.

*   **Message Store**: Cassandra/HBase/Scylla (Write Heavy, поиск по ChatID + Time).

### 3.2 The Group Chat Problem (Fan-out)

Юзер А пишет в группу (1000 человек).
Сервер должен клонировать сообщение 1000 раз.

*   **Async Queue (Kafka)**: Пишем в топик `group-messages`.

*   **Fan-out Service**: Читает, достает список участников, находит их сервера, пушит в их очереди.

---

## 4. Case Study 4: Search Typeahead (Google Suggest)

Задача: Юзер пишет "sys", мы подсказываем "system design", "systems theory".

### 4.1 Data Structure: Trie (Prefix Tree)

Дерево, где узлы — буквы.
`root -> s -> y -> s -> ...`
В каждом узле храним Top-5 популярных запросов, проходящих через него (Pre-computed).

### 4.2 Optimizations

*   **Caching**: Browser хранит результаты локально (Cache-Control).

*   **Sampling**: Логируем только 1 из 1000 запросов для обновления статистики.

*   **Z-Algorithm**: Хранение Tries в памяти (компактно).

---

## 5. Case Study 5: Youtube (Video Streaming)

### 5.1 Architecture

*   **Upload**: Юзер льет raw MP4.

*   **Encoding (DAG)**: Видео бьется на чанки. Параллельно кодируется в 360p, 720p, 1080p, 4K (H.264/VP9/AV1). Audio извлекается отдельно.

*   **Storage**: Metadata в SQL (Sharded). Chunks в Blob Storage (S3/GCS).

*   **Delivery (CDN)**: Это главное. Chunks копируются на Edge Servers по всему миру.

*   **Client**: Adaptive Bitrate (DASH/HLS). Плеер меряет скорость сети и переключает качество (360p -> 1080p) на лету.

---

## 6. The System Design Interview Framework: PEDALS

Как не провалить собеседование.

### 1. **P**rocess Requirements (5 min)

Не рисуйте сразу! Спрашивайте.

*   Functional: Что система делает?
*   Non-Functional: Latency, Availability, Consistency?
*   Constraints: DAU? Peak QPS?

### 2. **E**stimate Scale (5 min)

Покажите, что вы инженер.

*   Read/Write Ratio.
*   Total Storage (Text vs Video).
*   Bandwidth.

### 3. **D**esign Service / API (10 min)

*   Высокоуровневая диаграмма (Client -> LB -> Service -> DB).
*   API Definitions (REST/gRPC).

### 4. **A**rticulate Data Model (10 min)

*   Schema Design.
*   SQL vs NoSQL (обоснуйте!).
*   Sharding Key.

### 5. **L**ist Components (10 min)

*   "Здесь кэш".
*   "Здесь очередь".
*   "Здесь CDN".

### 6. **S**cale & Bottlenecks (5 min)

*   SPOF (Single Point of Failure).
*   Hotspots.
*   Monitoring.

---

## 📚 Appendix A: War Stories (Чужие ошибки)

### A.1 GitHub Outage 2018 (24 часа)

**Причина**: Рассинхронизация топологии (Topology Alienation).
Из-за разрыва оптики в ДЦ-1, Orchestrator (Orchestrator, не Kubernetes) решил переключить мастер MySQL в ДЦ-2.
Но ДЦ-1 "завис", а не упал.
Когда связь вернулась, данные в ДЦ-1 и ДЦ-2 разъехались.
Восстановление (Restore from backup) заняло сутки.

**Урок**: Cross-DC failover for Databases is HARD. Лучше потерять Availability на 10 минут, чем Consistency на 24 часа.

### A.2 GitLab `rm -rf`

Инженер запускает удаление логов. Ошибается окном. Удаляет продакшн базу.
Отменяет через 2 секунды. Но 300ГБ уже удалено.
Бэкапы?

1.  S3 bucket пуст (скрипт падал тихо).
2.  Azure snapshot (не включен).
3.  LVM snapshot (раз в 24 часа, данные за сегодня потеряны).
**Урок**: Проверяйте бэкапы (Restore Drills).

### A.3 Cloudflare Regex Outage

Инженер добавил правило WAF для защиты от XSS.
Regex был "паразитическим" ($O(2^N)$ backtracking).
Трафик пошел. CPU на всех Edge серверах (глобально!) ушел в 100%.

**Урок**: Не используйте backtracking regex engine (PCRE) на недоверенном вводе. Используйте Re2 (Google) или Rust Regex.

---

## 📚 Appendix B: FAQ (Interview Edition)

**Q1: Что делать, если я не знаю технологию X?**
**A**: Не врите. Скажите: "Я не работал с Cassandra, но я знаю, что это Wide-Column Store с AP характеристиками. Я бы использовал её для..." Это лучше, чем молчать.

**Q2: Рисовать монолит или микросервисы?**
**A**: На дизайне — сервисы (иначе нечего дизайнить). В реальности — начинайте с монолита.

**Q3: Когда использовать Push vs Pull модель (News Feed)?**
**A**:
*   **Pull (Fan-out on Read)**: Дешево писать (добавил в свою таблицу). Дорого читать (собрать посты 1000 друзей). Хорошо для малого графа.

*   **Push (Fan-out on Write)**: Дорого писать (размножить пост в 10M лент фолловеров). Дешево читать (взял готовую ленту).

*   **Hybrid**: Для знаменитостей (1M+ followers) используем Pull, для остальных Push.

**Q4: Как хранить пароли?**
**A**: `bcrypt` или `Argon2` + Salt. Никогда MD5.

**Q5: Что такое Circuit Breaker?**
**A**: Предохранитель. Если сервис Payment отдает 500 ошибки, мы перестаем его вызывать ("размыкаем цепь"), чтобы не добить его и не вешать свои потоки. Через 10 сек пробуем один запрос (Half-Open).

---

## 💡 Key Takeaways

1.  **Architecture is Trade-offs**: Быстро написали — сложно поддерживать. Быстро читаем — медленно пишем.
2.  **Keep it Simple**: Не усложняйте без нужды. Postgres вывозит 90% проектов до IPO.
3.  **Failures happen**: Проектируйте так, чтобы падение компонента не валило всю систему.
4.  **Back-of-the-envelope Math**: Умейте быстро оценивать масштаб системы на салфетке.
5.  **Design for Scale**: Но не переоптимизируйте преждевременно. Начинайте просто, масштабируйте по мере необходимости.

---

## 🚀 Final Words

Поздравляю! Вы прошли курс **Data Systems**.
Вы узнали, как данные живут на диске (B-Trees), как они путешествуют по сети (Replication), как они теряются (CAP) и как их находить (Indexing).
Теперь идите и стройте системы, которые не падают (или падают красиво).

**[End of Course]**


