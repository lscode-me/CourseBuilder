# YAML
## Human-friendly формат данных для конфигураций

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:
- Знать JSON (модуль 05_JSON)
- Понимать структуры данных (объекты, массивы)
- Иметь опыт работы с конфигурационными файлами

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:
- Читать и писать корректный YAML
- Понимать особенности и "gotchas" YAML
- Сравнивать YAML и JSON, выбирать подходящий формат
- Использовать yq для обработки YAML
- Применять YAML в DevOps инструментах

---

## 1. Что такое YAML

### 1.1 Определение

**YAML** (YAML Ain't Markup Language) — человекочитаемый формат сериализации данных.

- Создан в 2001 году
- Надмножество JSON (валидный JSON = валидный YAML)
- Использует отступы вместо скобок
- Поддерживает комментарии

### 1.2 Где используется YAML

| Инструмент | Файл |
|------------|------|
| Docker Compose | `docker-compose.yml` |
| Kubernetes | `deployment.yaml`, `service.yaml` |
| GitHub Actions | `.github/workflows/*.yml` |
| Ansible | playbooks, inventory |
| CI/CD | `.gitlab-ci.yml`, `.travis.yml` |
| Helm | `Chart.yaml`, `values.yaml` |

### 1.3 Пример YAML

```yaml
# Конфигурация приложения
app:
  name: MyApp
  version: 1.0.0
  
server:
  host: localhost
  port: 8080
  debug: true
  
database:
  host: db.example.com
  port: 5432
  credentials:
    username: admin
    password: secret  # TODO: use secrets manager
    
features:
  - authentication
  - logging
  - caching
```

---

## 2. Синтаксис YAML

### 2.1 Базовые типы

```yaml
# Строки
string1: Hello World
string2: "Hello World"        # С кавычками
string3: 'Hello World'        # Одинарные кавычки
string4: "Line 1\nLine 2"     # С escape (только в двойных)

# Числа
integer: 42
negative: -17
float: 3.14159
scientific: 1.5e+10
hex: 0xFF        # ⚠️ Может интерпретироваться как строка!
octal: 0o755     # ⚠️ Зависит от версии YAML

# Boolean
bool1: true
bool2: false
bool3: yes       # ⚠️ Тоже boolean!
bool4: no        # ⚠️ Тоже boolean!
bool5: on        # ⚠️ Тоже boolean!
bool6: off       # ⚠️ Тоже boolean!

# Null
null1: null
null2: ~
null3:           # Пустое значение = null
```

### 2.2 Строки — детали

```yaml
# Без кавычек — обычная строка
simple: Hello World

# Двойные кавычки — поддержка escape
escaped: "Tab:\t Newline:\n Quote:\""

# Одинарные кавычки — всё буквально (кроме '')
literal: 'No escape: \n stays as \n'
apostrophe: 'It''s working'  # '' = одна '

# Многострочные — литеральный блок (сохраняет переносы)
description: |
  This is a long
  multi-line string.
  Newlines are preserved.

# Многострочные — свёрнутый блок (переносы → пробелы)
summary: >
  This is also multi-line
  but newlines become spaces.
  Only double newlines create paragraphs.
  
  New paragraph here.

# С отступом
indented: |2
    This text starts with 4 spaces
    because of |2 modifier.
```

### 2.3 Списки (Arrays)

```yaml
# Block style (рекомендуется)
fruits:
  - apple
  - banana
  - cherry

# Flow style (как JSON)
fruits: [apple, banana, cherry]

# Вложенные списки
matrix:
  - [1, 2, 3]
  - [4, 5, 6]
  - [7, 8, 9]

# Список объектов
users:
  - name: Alice
    age: 30
  - name: Bob
    age: 25
```

### 2.4 Объекты (Maps)

```yaml
# Block style
person:
  name: Alice
  age: 30
  email: alice@example.com

# Flow style
person: {name: Alice, age: 30}

# Вложенные объекты
config:
  server:
    host: localhost
    port: 8080
  database:
    host: db.local
    port: 5432

# Сложные ключи
? |-
  multi-line
  key
: value for complex key
```

### 2.5 Смешанные структуры

```yaml
# Объект со списками
server:
  name: web-1
  ports:
    - 80
    - 443
  tags:
    - production
    - frontend

# Список объектов со вложенностью
deployments:
  - name: app-deployment
    replicas: 3
    containers:
      - name: app
        image: myapp:latest
        ports:
          - containerPort: 8080
      - name: sidecar
        image: sidecar:latest
```

---

## 3. Продвинутые возможности

### 3.1 Якоря и алиасы (Anchors & Aliases)

```yaml
# Определяем якорь с &
defaults: &defaults
  adapter: postgres
  host: localhost
  pool: 5

# Используем алиас с *
development:
  <<: *defaults          # Вставить все ключи из defaults
  database: dev_db

production:
  <<: *defaults
  database: prod_db
  pool: 25               # Переопределяем pool

# Результат development:
# adapter: postgres
# host: localhost
# pool: 5
# database: dev_db
```

### 3.2 Множественные документы

```yaml
# Первый документ
---
name: Document 1
type: config
---
# Второй документ
name: Document 2
type: data
...
# Конец документов (опционально)
```

### 3.3 Теги (Tags)

```yaml
# Явное указание типа
not_a_bool: !!str yes
not_a_number: !!str 123
explicit_float: !!float 42

# Кастомные теги
date: !custom 2024-01-15
```

---

## 4. YAML "Gotchas" — подводные камни

### 4.1 Norway Problem

```yaml
# ⚠️ ОСТОРОЖНО! В YAML 1.1:
country: NO      # Интерпретируется как false!
answer: YES      # Интерпретируется как true!

# ✅ Решение — кавычки:
country: "NO"
answer: "YES"
```

### 4.2 Числа как строки

```yaml
# ⚠️ Может быть интерпретировано как число:
version: 1.0     # float 1.0, не строка "1.0"!
phone: 12345     # integer, не строка

# ✅ Решение:
version: "1.0"
phone: "12345"
```

### 4.3 Двоеточие в значениях

```yaml
# ⚠️ Ошибка:
message: Error: file not found

# ✅ Решение — кавычки:
message: "Error: file not found"

# Или (если нет пробела после двоеточия — OK):
url: http://example.com
```

### 4.4 Специальные значения

```yaml
# Эти значения интерпретируются специально:
empty:           # null
tilde: ~         # null  
yes: yes         # true (YAML 1.1)
no: no           # false (YAML 1.1)
on: on           # true (YAML 1.1)
off: off         # false (YAML 1.1)

# В YAML 1.2 только true/false — boolean
```

### 4.5 Отступы — только пробелы!

```yaml
# ⚠️ ТАБЫ ЗАПРЕЩЕНЫ!
# Используйте только пробелы (обычно 2)

server:
  host: localhost    # 2 пробела — OK
	port: 8080        # ТАБ — ОШИБКА!
```

---

## 5. YAML vs JSON

### 5.1 Сравнение синтаксиса

**JSON:**
```json
{
  "server": {
    "host": "localhost",
    "port": 8080,
    "features": ["auth", "logging"]
  }
}
```

**YAML:**
```yaml
server:
  host: localhost
  port: 8080
  features:
    - auth
    - logging
```

### 5.2 Когда использовать

| Критерий | JSON | YAML |
|----------|------|------|
| Комментарии | ❌ Нет | ✅ Да |
| Читаемость | Средняя | Высокая |
| Машинная генерация | ✅ Просто | ⚠️ Сложнее |
| Размер файла | Больше | Меньше |
| Безопасность | ✅ Безопаснее | ⚠️ Риски (теги) |
| API | ✅ Стандарт | ❌ Редко |
| Конфигурации | ⚠️ Неудобно | ✅ Идеально |

### 5.3 Рекомендации

- **JSON**: API, обмен данными, машинная генерация
- **YAML**: Конфигурации, DevOps, файлы редактируемые человеком

---

## 6. Инструменты для YAML

### 6.1 yq — YAML процессор

```bash
# Установка (macOS)
brew install yq

# Установка (Linux)
# https://github.com/mikefarah/yq/releases

# Форматирование
yq eval '.' config.yaml

# Извлечение значения
yq eval '.server.port' config.yaml

# Изменение значения
yq eval '.server.port = 9090' config.yaml

# Добавление элемента в список
yq eval '.features += ["new-feature"]' config.yaml

# Удаление поля
yq eval 'del(.server.debug)' config.yaml
```

### 6.2 Конвертация YAML ↔ JSON

```bash
# YAML → JSON (с yq)
yq eval -o=json config.yaml

# JSON → YAML (с yq)
yq eval -P config.json

# С Python
python3 -c "import yaml, json, sys; print(json.dumps(yaml.safe_load(open('config.yaml')), indent=2))"
```

### 6.3 Валидация YAML

```bash
# С yamllint
pip install yamllint
yamllint config.yaml

# С Python
python3 -c "import yaml; yaml.safe_load(open('config.yaml'))"

# Онлайн: yamllint.com
```

### 6.4 yamllint правила

```yaml
# .yamllint файл
---
rules:
  line-length:
    max: 120
  indentation:
    spaces: 2
  truthy:
    check-keys: true
  comments:
    require-starting-space: true
```

---

## 7. YAML в Python

### 7.1 Базовые операции

```python
import yaml

# YAML string → Python dict
yaml_string = """
server:
  host: localhost
  port: 8080
features:
  - auth
  - logging
"""

data = yaml.safe_load(yaml_string)
print(data)
# {'server': {'host': 'localhost', 'port': 8080}, 'features': ['auth', 'logging']}

# Python dict → YAML string
yaml_output = yaml.dump(data, default_flow_style=False)
print(yaml_output)
```

### 7.2 Работа с файлами

```python
import yaml

# Чтение
with open('config.yaml', 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

# Запись
with open('output.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(config, f, default_flow_style=False, allow_unicode=True)
```

### 7.3 safe_load vs load

```python
import yaml

# ✅ ВСЕГДА используйте safe_load
data = yaml.safe_load(yaml_string)

# ⚠️ НИКОГДА не используйте yaml.load без Loader!
# yaml.load(yaml_string)  # ОПАСНО! Может выполнить код!

# Если нужен полный load (редко):
data = yaml.load(yaml_string, Loader=yaml.SafeLoader)
```

### 7.4 Множественные документы

```python
import yaml

yaml_multi = """
---
name: doc1
---
name: doc2
---
name: doc3
"""

# Загрузка всех документов
docs = list(yaml.safe_load_all(yaml_multi))
print(len(docs))  # 3

# Запись множественных документов
yaml.dump_all(docs, stream, default_flow_style=False)
```

---

## 8. YAML в DevOps

### 8.1 Docker Compose

```yaml
# docker-compose.yml
version: '3.8'

services:
  web:
    image: nginx:latest
    ports:
      - "80:80"
    volumes:
      - ./html:/usr/share/nginx/html
    depends_on:
      - api
    environment:
      - NODE_ENV=production

  api:
    build: ./api
    ports:
      - "3000:3000"
    env_file:
      - .env
    
  db:
    image: postgres:15
    environment:
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - db_data:/var/lib/postgresql/data

volumes:
  db_data:
```

### 8.2 Kubernetes

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
  labels:
    app: myapp
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
        - name: myapp
          image: myapp:1.0.0
          ports:
            - containerPort: 8080
          resources:
            limits:
              memory: "128Mi"
              cpu: "500m"
          env:
            - name: DATABASE_URL
              valueFrom:
                secretKeyRef:
                  name: db-secret
                  key: url
```

### 8.3 GitHub Actions

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      
      - name: Run tests
        run: pytest --cov=app tests/
```

### 8.4 Ansible

```yaml
# playbook.yml
---
- name: Configure web servers
  hosts: webservers
  become: true
  
  vars:
    http_port: 80
    max_clients: 200
  
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
        update_cache: yes
    
    - name: Copy nginx config
      template:
        src: nginx.conf.j2
        dest: /etc/nginx/nginx.conf
      notify: Restart nginx
    
    - name: Ensure nginx is running
      service:
        name: nginx
        state: started
        enabled: yes
  
  handlers:
    - name: Restart nginx
      service:
        name: nginx
        state: restarted
```

---

## 9. Best Practices

### 9.1 Форматирование

```yaml
# ✅ Хорошо
server:
  host: localhost
  port: 8080

# ❌ Плохо — смешение стилей
server:
  host: localhost
  port: 8080
database: {host: db, port: 5432}  # Flow style внезапно
```

### 9.2 Кавычки

```yaml
# ✅ Используйте кавычки для:
version: "1.0"           # Версий (иначе float)
country: "NO"            # Строк похожих на boolean
port: "8080"             # Если нужна строка, не число
message: "Hello: World"  # Строк с двоеточием
```

### 9.3 Комментарии

```yaml
# ✅ Полезные комментарии
server:
  host: localhost
  port: 8080  # Default HTTP port
  
  # Connection pool settings
  pool:
    min: 5
    max: 20

# ❌ Бесполезные комментарии  
server:
  host: localhost  # The host
  port: 8080       # The port
```

### 9.4 Организация файлов

```yaml
# Группировка логически связанных настроек
# 1. Метаданные
app:
  name: MyApp
  version: 1.0.0

# 2. Серверные настройки
server:
  host: localhost
  port: 8080

# 3. База данных
database:
  host: db.example.com
  port: 5432

# 4. Фичи
features:
  auth: true
  logging: true
```

---

## 10. Common Pitfalls

### 10.1 Табы вместо пробелов

❌ **Ошибка:**

```yaml
server:
→host: localhost    # TAB — ошибка!
```

✅ **Решение:** Настройте редактор на spaces-only.

### 10.2 Unsafe load

❌ **Ошибка:**

```python
yaml.load(user_input)  # ОПАСНО!
```

✅ **Решение:**

```python
yaml.safe_load(user_input)  # Безопасно
```

### 10.3 Неожиданные типы

❌ **Проблема:**

```yaml
version: 1.0    # Это float 1.0, не "1.0"
enabled: yes    # Это boolean true
country: NO     # Это boolean false
```

✅ **Решение:**

```yaml
version: "1.0"
enabled: true    # Явный boolean
country: "NO"
```

### 10.4 Пустые значения

```yaml
# Все это null!
empty1:
empty2: 
empty3: ~
empty4: null

# Если нужна пустая строка:
empty_string: ""
```

---

## 💡 Key Takeaways

- **YAML — для людей**: Комментарии, чистый синтаксис, отступы вместо скобок.

- **Осторожно с типами**: `yes/no`, `on/off` — boolean. `1.0` — float. Используйте кавычки.

- **Только пробелы**: Табы запрещены! Обычно 2 пробела для отступа.

- **safe_load всегда**: Никогда не используйте `yaml.load()` без SafeLoader.

- **JSON — подмножество YAML**: Любой JSON — валидный YAML (начиная с YAML 1.2).

---

## 🚀 Next Steps

**Related Modules:**
- [Markup](../07_Markup/) — HTML, XML, Markdown
- [Config Files](../08_ConfigFiles/) — INI, TOML и другие форматы

**Practice Ideas:**
1. Напишите docker-compose.yml для своего проекта
2. Создайте GitHub Actions workflow для CI/CD
3. Конвертируйте JSON конфиг в YAML и обратно
4. Напишите yamllint конфигурацию для проекта

**Going Deeper:**
- YAML 1.1 vs 1.2 (различия в boolean)
- Kustomize для Kubernetes
- Ansible templating с Jinja2

---

## 📚 Additional Resources

**Documentation:**
- [YAML Specification](https://yaml.org/spec/)
- [yq Documentation](https://mikefarah.gitbook.io/yq/)
- [PyYAML Documentation](https://pyyaml.org/wiki/PyYAMLDocumentation)

**Tools:**
- [YAML Lint](https://www.yamllint.com/)
- [YAML Multiline](https://yaml-multiline.info/)
- [yq releases](https://github.com/mikefarah/yq/releases)

**Learning:**
- [Learn YAML in Y minutes](https://learnxinyminutes.com/docs/yaml/)
- [YAML Gotchas](https://www.arp242.net/yaml-config.html)

---


