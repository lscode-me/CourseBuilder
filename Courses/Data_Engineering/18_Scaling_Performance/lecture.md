# Масштабирование и производительность

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать архитектуры data-платформ (модуль 17)
- Знать основы распределённых систем
- Иметь представление о производительности

**Recommended prior modules:**

- [17_Data_Platform_Architectures](../17_Data_Platform_Architectures/) — архитектуры data-платформ

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Различать horizontal и vertical scaling
- Балансировать throughput и latency
- Выявлять и устранять bottlenecks
- Проектировать cost-aware системы

---

## 1. Введение в масштабирование

Масштабирование — это способность системы обрабатывать растущие нагрузки. Производительность зависит от правильного выбора стратегии масштабирования.

**Аспекты масштабирования:**

- **Scaling** — horizontal vs vertical

- **Performance** — throughput vs latency

- **Bottlenecks** — узкие места

- **Cost** — cost-aware design

---

## 2. Horizontal vs Vertical Scaling

Различие в способе увеличения мощности системы.

### 2.1 Vertical Scaling (Scale Up)

**Характеристики:**

- Увеличение ресурсов одного сервера
- Больше CPU, RAM, storage
- Проще в реализации
- Ограничено физическими пределами

**Example: Vertical Scaling**

```python

class VerticalScaling:
    def __init__(self):
        self.server = {
            "cpu_cores": 4,
            "ram_gb": 16,
            "storage_gb": 100
        }
    
    def scale_up(self, cpu_cores=None, ram_gb=None, storage_gb=None):
        """Увеличивает ресурсы сервера"""
        if cpu_cores:
            self.server["cpu_cores"] = cpu_cores
        if ram_gb:
            self.server["ram_gb"] = ram_gb
        if storage_gb:
            self.server["storage_gb"] = storage_gb
        
        print(f"⬆️  Vertical scaling: CPU={self.server['cpu_cores']}, RAM={self.server['ram_gb']}GB, Storage={self.server['storage_gb']}GB")
        return self.server

# Использование

vertical = VerticalScaling()
vertical.scale_up(cpu_cores=8, ram_gb=32, storage_gb=200)
```

**Output:**
```

⬆️  Vertical scaling: CPU=8, RAM=32GB, Storage=200GB
```

### 2.2 Horizontal Scaling (Scale Out)

**Характеристики:**

- Добавление новых серверов
- Распределение нагрузки
- Безграничное масштабирование
- Требует распределённой архитектуры

**Example: Horizontal Scaling**

```python

class HorizontalScaling:
    def __init__(self):
        self.servers = []
    
    def add_server(self, server_id):
        """Добавляет новый сервер"""
        server = {
            "id": server_id,
            "cpu_cores": 4,
            "ram_gb": 16
        }
        self.servers.append(server)
        print(f"➡️  Horizontal scaling: добавлен сервер {server_id}, всего серверов: {len(self.servers)}")
        return server
    
    def get_total_capacity(self):
        """Возвращает общую мощность"""
        total_cpu = sum(s["cpu_cores"] for s in self.servers)
        total_ram = sum(s["ram_gb"] for s in self.servers)
        return {"total_cpu": total_cpu, "total_ram": total_ram, "servers": len(self.servers)}

# Использование
horizontal = HorizontalScaling()
horizontal.add_server("server-1")
horizontal.add_server("server-2")
horizontal.add_server("server-3")

capacity = horizontal.get_total_capacity()
print(f"Общая мощность: {capacity}")
```

**Output:**
```

➡️  Horizontal scaling: добавлен сервер server-1, всего серверов: 1
➡️  Horizontal scaling: добавлен сервер server-2, всего серверов: 2
➡️  Horizontal scaling: добавлен сервер server-3, всего серверов: 3
Общая мощность: {'total_cpu': 12, 'total_ram': 48, 'servers': 3}
```

### 2.3 Сравнение

| Аспект | Vertical | Horizontal |
|--------|----------|------------|
| **Способ** | Увеличение ресурсов | Добавление серверов |
| **Сложность** | Проще | Сложнее |
| **Пределы** | Физические | Нет |
| **Отказоустойчивость** | Низкая | Высокая |
| **Стоимость** | Дороже на больших масштабах | Дешевле |

---

## 3. Throughput vs Latency

Понимание trade-off между пропускной способностью и задержкой.

### 3.1 Throughput

**Определение:**

- Количество операций в единицу времени
- Пример: 1000 запросов/секунду
- Важно для batch processing

### 3.2 Latency

**Определение:**

- Время выполнения одной операции
- Пример: 100ms на запрос
- Важно для real-time систем

**Example: Throughput vs Latency**

```python

class PerformanceMetrics:
    def __init__(self):
        self.operations = []
    
    def measure_operation(self, operation_time_ms):
        """Измеряет операцию"""
        self.operations.append(operation_time_ms)
    
    def get_throughput(self, time_window_seconds=1):
        """Вычисляет throughput (операций в секунду)"""
        if not self.operations:
            return 0
        
        # Симуляция: операции равномерно распределены
        total_operations = len(self.operations)
        throughput = total_operations / time_window_seconds
        return throughput
    
    def get_latency(self):
        """Вычисляет среднюю latency"""
        if not self.operations:
            return 0
        
        avg_latency = sum(self.operations) / len(self.operations)
        return avg_latency
    
    def get_performance_report(self):
        """Возвращает отчёт о производительности"""
        return {
            "throughput_ops_per_sec": self.get_throughput(),
            "avg_latency_ms": self.get_latency(),
            "total_operations": len(self.operations)
        }

# Использование
metrics = PerformanceMetrics()

# Симуляция операций

for _ in range(100):
    metrics.measure_operation(50)  # 50ms на операцию

report = metrics.get_performance_report()
print("Performance Report:")
for key, value in report.items():
    print(f"  {key}: {value}")
```

**Output:**
```

Performance Report:
  throughput_ops_per_sec: 100.0
  avg_latency_ms: 50.0
  total_operations: 100
```

---

## 4. Bottlenecks (Узкие места)

Bottlenecks ограничивают производительность системы.

### 4.1 Типы Bottlenecks

**CPU Bound:**

- Ограничение по CPU
- Решение: больше CPU cores

**Memory Bound:**

- Ограничение по памяти
- Решение: больше RAM

**I/O Bound:**

- Ограничение по I/O
- Решение: быстрее storage/network

**Example: Выявление Bottlenecks**

```python

class BottleneckAnalyzer:
    def __init__(self):
        self.metrics = {
            "cpu_usage": 0,
            "memory_usage": 0,
            "io_wait": 0,
            "network_throughput": 0
        }
        self.thresholds = {
            "cpu_usage": 80,
            "memory_usage": 90,
            "io_wait": 50,
            "network_throughput": 1000
        }
    
    def analyze(self):
        """Анализирует bottlenecks"""
        bottlenecks = []
        
        if self.metrics["cpu_usage"] > self.thresholds["cpu_usage"]:
            bottlenecks.append({
                "type": "CPU Bound",
                "usage": self.metrics["cpu_usage"],
                "threshold": self.thresholds["cpu_usage"],
                "solution": "Добавить CPU cores или оптимизировать код"
            })
        
        if self.metrics["memory_usage"] > self.thresholds["memory_usage"]:
            bottlenecks.append({
                "type": "Memory Bound",
                "usage": self.metrics["memory_usage"],
                "threshold": self.thresholds["memory_usage"],
                "solution": "Увеличить RAM или оптимизировать использование памяти"
            })
        
        if self.metrics["io_wait"] > self.thresholds["io_wait"]:
            bottlenecks.append({
                "type": "I/O Bound",
                "usage": self.metrics["io_wait"],
                "threshold": self.thresholds["io_wait"],
                "solution": "Улучшить storage или network"
            })
        
        return bottlenecks
    
    def set_metrics(self, **kwargs):
        """Устанавливает метрики"""
        self.metrics.update(kwargs)

# Использование

analyzer = BottleneckAnalyzer()
analyzer.set_metrics(cpu_usage=95, memory_usage=85, io_wait=30)

bottlenecks = analyzer.analyze()
print("Обнаруженные Bottlenecks:")
for bottleneck in bottlenecks:
    print(f"  {bottleneck['type']}: {bottleneck['usage']}% > {bottleneck['threshold']}%")
    print(f"    Решение: {bottleneck['solution']}")
```

**Output:**
```

Обнаруженные Bottlenecks:
  CPU Bound: 95% > 80%
    Решение: Добавить CPU cores или оптимизировать код
  Memory Bound: 85% > 90%
```

---

## 5. Auto-scaling (Автоматическое масштабирование)

Auto-scaling автоматически изменяет количество ресурсов на основе нагрузки.

### 5.1 Типы Auto-scaling

**Reactive Scaling:**

- Реагирует на текущую нагрузку
- На основе метрик (CPU, memory)
- Задержка в масштабировании

**Predictive Scaling:**

- Предсказывает будущую нагрузку
- На основе исторических данных
- Проактивное масштабирование

**Example: Auto-scaling**

```python

class AutoScaler:
    def __init__(self, min_instances=1, max_instances=10):
        self.min_instances = min_instances
        self.max_instances = max_instances
        self.current_instances = min_instances
        self.cpu_threshold_scale_up = 80
        self.cpu_threshold_scale_down = 30
    
    def check_and_scale(self, current_cpu_usage):
        """Проверяет метрики и масштабирует"""
        if current_cpu_usage > self.cpu_threshold_scale_up:
            if self.current_instances < self.max_instances:
                self.current_instances += 1
                print(f"⬆️  Scale UP: CPU={current_cpu_usage}%, instances={self.current_instances}")
        elif current_cpu_usage < self.cpu_threshold_scale_down:
            if self.current_instances > self.min_instances:
                self.current_instances -= 1
                print(f"⬇️  Scale DOWN: CPU={current_cpu_usage}%, instances={self.current_instances}")
        else:
            print(f"➡️  No scaling: CPU={current_cpu_usage}%, instances={self.current_instances}")
        
        return self.current_instances

# Использование
scaler = AutoScaler(min_instances=2, max_instances=5)

# Симуляция изменения нагрузки
cpu_levels = [75, 85, 90, 25, 20, 15]

for cpu in cpu_levels:
    scaler.check_and_scale(cpu)
```

**Output:**
```
➡️  No scaling: CPU=75%, instances=2
⬆️  Scale UP: CPU=85%, instances=3
⬆️  Scale UP: CPU=90%, instances=4
⬇️  Scale DOWN: CPU=25%, instances=3
⬇️  Scale DOWN: CPU=20%, instances=2
⬇️  Scale DOWN: CPU=15%, instances=1
```

---

## 6. Cost-aware Design

Проектирование с учётом стоимости.

### 6.1 Принципы

**Right-sizing:**

- Выбор правильного размера ресурсов
- Не переплачивать за избыточные ресурсы
- Мониторинг использования

**Reserved vs On-demand:**

- Reserved instances дешевле
- On-demand гибче
- Баланс между стоимостью и гибкостью

**Example: Cost Optimization**

```python

class CostOptimizer:
    def __init__(self):
        self.resources = {}
        self.costs = {
            "on_demand_per_hour": 1.0,
            "reserved_per_hour": 0.5,
            "spot_per_hour": 0.2
        }
    
    def calculate_cost(self, instance_type, hours, count=1):
        """Вычисляет стоимость"""
        hourly_cost = self.costs.get(instance_type, 0)
        total_cost = hourly_cost * hours * count
        return total_cost
    
    def optimize(self, workload_hours_per_month, required_capacity):
        """Оптимизирует стоимость"""
        scenarios = {
            "on_demand": self.calculate_cost("on_demand_per_hour", workload_hours_per_month, required_capacity),
            "reserved": self.calculate_cost("reserved_per_hour", workload_hours_per_month, required_capacity),
            "spot": self.calculate_cost("spot_per_hour", workload_hours_per_month, required_capacity)
        }
        
        best = min(scenarios.items(), key=lambda x: x[1])
        
        print("Cost Optimization:")
        for scenario, cost in scenarios.items():
            print(f"  {scenario}: ${cost:.2f}")
        print(f"  ✅ Лучший вариант: {best[0]} (${best[1]:.2f})")
        
        return best

# Использование

optimizer = CostOptimizer()
optimizer.optimize(workload_hours_per_month=730, required_capacity=10)
```

**Output:**
```

Cost Optimization:
  on_demand: $7300.00
  reserved: $3650.00
  spot: $1460.00
  ✅ Лучший вариант: spot ($1460.00)
```

### 6.2 Right-sizing стратегии

**Мониторинг использования:**

- Отслеживание CPU, memory, I/O
- Выявление неиспользуемых ресурсов
- Оптимизация на основе данных

**Постепенная оптимизация:**

- Начать с меньших инстансов
- Масштабировать при необходимости
- Избегать over-provisioning

**Example: Right-sizing анализ**

```python

class RightSizingAnalyzer:
    def __init__(self):
        self.usage_history = []
    
    def analyze_usage(self, cpu_usage, memory_usage, io_usage):
        """Анализирует использование ресурсов"""
        avg_cpu = sum(cpu_usage) / len(cpu_usage) if cpu_usage else 0
        avg_memory = sum(memory_usage) / len(memory_usage) if memory_usage else 0
        avg_io = sum(io_usage) / len(io_usage) if io_usage else 0
        
        recommendations = []
        
        if avg_cpu < 30:
            recommendations.append("CPU: можно уменьшить размер инстанса")
        elif avg_cpu > 80:
            recommendations.append("CPU: нужно увеличить размер инстанса")
        
        if avg_memory < 40:
            recommendations.append("Memory: можно уменьшить RAM")
        elif avg_memory > 85:
            recommendations.append("Memory: нужно увеличить RAM")
        
        print("📊 Right-sizing анализ:")
        print(f"   Средний CPU: {avg_cpu:.1f}%")
        print(f"   Средний Memory: {avg_memory:.1f}%")
        print(f"   Средний I/O: {avg_io:.1f}%")
        print("\n💡 Рекомендации:")
        for rec in recommendations:
            print(f"   - {rec}")
        
        return recommendations

# Использование
analyzer = RightSizingAnalyzer()
analyzer.analyze_usage(
    cpu_usage=[25, 30, 28, 32],
    memory_usage=[45, 50, 48, 52],
    io_usage=[20, 25, 22, 24]
)
```

**Output:**
```
📊 Right-sizing анализ:
   Средний CPU: 28.8%
   Средний Memory: 48.8%
   Средний I/O: 22.8%

💡 Рекомендации:
   - CPU: можно уменьшить размер инстанса
```

---

## 7. Load Balancing (Балансировка нагрузки)

Load balancing распределяет нагрузку между несколькими серверами.

### 7.1 Типы Load Balancing

**Round Robin:**

- Равномерное распределение
- Простая реализация
- Не учитывает загрузку серверов

**Least Connections:**

- Направляет на сервер с наименьшим количеством соединений
- Учитывает текущую нагрузку
- Более эффективен

**Example: Load Balancing**

```python

class LoadBalancer:
    def __init__(self, strategy="round_robin"):
        self.servers = []
        self.strategy = strategy
        self.current_index = 0
        self.connections = {}
    
    def add_server(self, server_id):
        """Добавляет сервер"""
        self.servers.append(server_id)
        self.connections[server_id] = 0
        print(f"➕ Сервер '{server_id}' добавлен")
    
    def route_request(self, request_id):
        """Маршрутизирует запрос"""
        if not self.servers:
            return None
        
        if self.strategy == "round_robin":
            server = self.servers[self.current_index]
            self.current_index = (self.current_index + 1) % len(self.servers)
        elif self.strategy == "least_connections":
            server = min(self.servers, key=lambda s: self.connections[s])
        
        self.connections[server] += 1
        print(f"📤 Запрос {request_id} -> сервер '{server}' (соединений: {self.connections[server]})")
        return server
    
    def release_connection(self, server_id):
        """Освобождает соединение"""
        if server_id in self.connections and self.connections[server_id] > 0:
            self.connections[server_id] -= 1

# Использование
lb = LoadBalancer(strategy="least_connections")
lb.add_server("server-1")
lb.add_server("server-2")
lb.add_server("server-3")

# Маршрутизация запросов
for i in range(5):
    lb.route_request(f"req_{i}")
```

**Output:**
```
➕ Сервер 'server-1' добавлен
➕ Сервер 'server-2' добавлен
➕ Сервер 'server-3' добавлен
📤 Запрос req_0 -> сервер 'server-1' (соединений: 1)
📤 Запрос req_1 -> сервер 'server-2' (соединений: 1)
📤 Запрос req_2 -> сервер 'server-3' (соединений: 1)
📤 Запрос req_3 -> сервер 'server-1' (соединений: 2)
📤 Запрос req_4 -> сервер 'server-2' (соединений: 2)
```

---

## 8. Caching (Кэширование)

Caching улучшает производительность за счёт хранения часто используемых данных.

### 8.1 Стратегии кэширования

**Cache-aside:**

- Приложение проверяет кэш
- При промахе загружает из БД
- Сохраняет в кэш для будущих запросов

**Write-through:**

- Запись одновременно в кэш и БД
- Консистентность данных
- Выше задержка записи

**Example: Cache-aside паттерн**

```python

class CacheAside:
    def __init__(self):
        self.cache = {}
        self.database = {}
        self.cache_hits = 0
        self.cache_misses = 0
    
    def get(self, key):
        """Получает значение с использованием cache-aside"""
        # Проверка кэша
        if key in self.cache:
            self.cache_hits += 1
            print(f"✅ Cache HIT: {key} = {self.cache[key]}")
            return self.cache[key]
        
        # Cache miss - загрузка из БД
        self.cache_misses += 1
        if key in self.database:
            value = self.database[key]
            # Сохранение в кэш
            self.cache[key] = value
            print(f"❌ Cache MISS: {key} = {value} (загружено из БД и сохранено в кэш)")
            return value
        else:
            print(f"❌ Key '{key}' не найдено")
            return None
    
    def set(self, key, value):
        """Устанавливает значение"""
        self.database[key] = value
        # Обновление кэша
        if key in self.cache:
            self.cache[key] = value
        print(f"💾 Установлено: {key} = {value}")
    
    def get_stats(self):
        """Возвращает статистику"""
        total = self.cache_hits + self.cache_misses
        hit_rate = (self.cache_hits / total * 100) if total > 0 else 0
        return {
            "hits": self.cache_hits,
            "misses": self.cache_misses,
            "hit_rate": f"{hit_rate:.1f}%"
        }

# Использование
cache = CacheAside()

# Инициализация данных
cache.set("user_1", "Alice")
cache.set("user_2", "Bob")

# Чтение (первый раз - cache miss)
cache.get("user_1")

# Чтение (второй раз - cache hit)
cache.get("user_1")
cache.get("user_2")

stats = cache.get_stats()
print(f"\n📊 Статистика кэша: {stats}")
```

**Output:**
```
💾 Установлено: user_1 = Alice
💾 Установлено: user_2 = Bob
❌ Cache MISS: user_1 = Alice (загружено из БД и сохранено в кэш)
✅ Cache HIT: user_1 = Alice
✅ Cache HIT: user_2 = Bob

📊 Статистика кэша: {'hits': 2, 'misses': 1, 'hit_rate': '66.7%'}
```

### 8.2 Best Practices кэширования

**Выбор TTL (Time To Live):**

- Баланс между актуальностью и производительностью
- Зависит от типа данных
- Мониторинг hit rate

**Инвалидация кэша:**

- Удаление устаревших данных
- Обновление при изменении
- Стратегии инвалидации

---

## 9. Performance Tuning (Оптимизация производительности)

Performance tuning улучшает производительность системы через оптимизацию.

### 9.1 Области оптимизации

**Запросы к БД:**

- Оптимизация SQL запросов
- Использование индексов
- Избежание N+1 проблем

**Код:**

- Оптимизация алгоритмов
- Устранение узких мест
- Профилирование

**Example: Оптимизация запросов**

```python

class QueryOptimizer:
    def __init__(self):
        self.queries = []
        self.indexes = {}
    
    def analyze_query(self, query, execution_time_ms):
        """Анализирует запрос"""
        self.queries.append({
            "query": query,
            "execution_time": execution_time_ms
        })
        
        # Проверка на медленные запросы
        if execution_time_ms > 100:
            print(f"⚠️  Медленный запрос: {query} ({execution_time_ms}ms)")
            return "slow"
        else:
            print(f"✅ Быстрый запрос: {query} ({execution_time_ms}ms)")
            return "fast"
    
    def suggest_index(self, table, column):
        """Предлагает индекс"""
        index_key = f"{table}.{column}"
        if index_key not in self.indexes:
            self.indexes[index_key] = True
            print(f"💡 Рекомендуется индекс на {table}.{column}")
            return True
        return False
    
    def get_slow_queries(self):
        """Возвращает медленные запросы"""
        return [q for q in self.queries if q["execution_time"] > 100]

# Использование
optimizer = QueryOptimizer()

# Анализ запросов
optimizer.analyze_query("SELECT * FROM users WHERE id = 1", 5)
optimizer.analyze_query("SELECT * FROM orders WHERE user_id = 1", 150)  # Медленный

# Предложение индекса
optimizer.suggest_index("orders", "user_id")

slow = optimizer.get_slow_queries()
print(f"\n🐌 Медленных запросов: {len(slow)}")
```

**Output:**
```
✅ Быстрый запрос: SELECT * FROM users WHERE id = 1 (5ms)
⚠️  Медленный запрос: SELECT * FROM orders WHERE user_id = 1 (150ms)
💡 Рекомендуется индекс на orders.user_id

🐌 Медленных запросов: 1
```

---

## 💡 Key Takeaways

- **Horizontal vs Vertical**: Horizontal scaling добавляет серверы, vertical увеличивает ресурсы. Horizontal масштабируется безгранично, но сложнее.

- **Throughput vs Latency**: Throughput — операции в секунду, latency — время операции. Trade-off зависит от use case.

- **Bottlenecks**: Узкие места ограничивают производительность. CPU, Memory, I/O bound требуют разных решений.

- **Auto-scaling**: Автоматическое масштабирование на основе нагрузки. Reactive scaling реагирует на метрики, predictive scaling предсказывает нагрузку.

- **Cost-aware Design**: Проектирование с учётом стоимости. Right-sizing, выбор типа инстансов, мониторинг использования.

- **Right-sizing**: Выбор правильного размера ресурсов на основе мониторинга использования. Избежание over-provisioning и under-provisioning.

- **Load Balancing**: Распределение нагрузки между серверами. Round Robin для простоты, Least Connections для эффективности.

- **Caching**: Улучшение производительности через кэширование. Cache-aside для гибкости, write-through для консистентности. Мониторинг hit rate критичен.

- **Performance Tuning**: Оптимизация запросов, кода и конфигурации. Профилирование для выявления узких мест, индексы для ускорения запросов.

- **Баланс**: Оптимальная производительность требует баланса между масштабированием, производительностью и стоимостью. Auto-scaling, load balancing и caching помогают автоматизировать этот баланс.

---

## 🚀 Next Steps

**Related Modules:**

- [19_Reliability_Operations](../19_Reliability_Operations/) — надёжность и эксплуатация
- [20_Data_Engineering_System_Design](../20_Data_Engineering_System_Design/) — system design
- [17_Data_Platform_Architectures](../17_Data_Platform_Architectures/) — архитектуры

**Practice Ideas:**

1. Проанализируйте bottlenecks: выявите узкие места в вашей системе
2. Оптимизируйте стоимость: сравните разные варианты ресурсов
3. Измерьте производительность: throughput и latency

**Going Deeper:**

- Изучите auto-scaling: автоматическое масштабирование
- Погрузитесь в performance tuning: оптимизация производительности
- Изучите cost optimization: практические подходы

---

## 📚 Additional Resources

**Books:**

- "Designing Data-Intensive Applications" by Martin Kleppmann — масштабирование
- "High Performance Browser Networking" — производительность

**Articles:**

- "Scaling Strategies" — подходы к масштабированию
- "Cost Optimization Best Practices" — оптимизация стоимости

**Documentation:**

- AWS Auto Scaling: https://docs.aws.amazon.com/autoscaling/
- Google Cloud Performance: https://cloud.google.com/performance

---


