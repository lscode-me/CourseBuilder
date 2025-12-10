# OpenResty и Lua
## Программируемый веб-сервер на базе Nginx

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать архитектуру и конфигурацию Nginx
- Иметь опыт работы с HTTP протоколом
- Знать основы любого скриптового языка (Python, JavaScript, etc.)

**Recommended prior modules:**
- [Web Servers](../03_WebServers/) — архитектура Nginx
- [HTTP Protocol](../01_HTTP/) — основы HTTP

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Понимать архитектуру OpenResty и её отличия от стандартного Nginx
- Писать базовые скрипты на Lua для обработки HTTP запросов
- Реализовывать динамическую логику прямо в веб-сервере
- Использовать lua-resty-* библиотеки для работы с Redis, MySQL, HTTP
- Понимать сценарии применения OpenResty (API Gateway, WAF, edge computing)

---

## 1. Введение в OpenResty

### 1.1 Что такое OpenResty

**OpenResty** — это расширенная версия Nginx, объединяющая стандартный Nginx с LuaJIT и набором Lua-библиотек. По сути, это полноценная платформа для создания высокопроизводительных веб-приложений.

```
┌────────────────────────────────────────────────────────────┐
│                      OpenResty                              │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  ┌────────────────────────────────────────────────────┐    │
│  │                     Nginx Core                      │    │
│  │  - Event-driven architecture                       │    │
│  │  - Non-blocking I/O                                │    │
│  │  - HTTP/HTTPS/HTTP2                                │    │
│  └────────────────────────────────────────────────────┘    │
│                          │                                 │
│                          ▼                                 │
│  ┌────────────────────────────────────────────────────┐    │
│  │                ngx_lua module                       │    │
│  │  - Встраивает LuaJIT в Nginx                       │    │
│  │  - Доступ к фазам обработки запроса                │    │
│  │  - Cosockets для async I/O                         │    │
│  └────────────────────────────────────────────────────┘    │
│                          │                                 │
│                          ▼                                 │
│  ┌────────────────────────────────────────────────────┐    │
│  │              lua-resty-* Libraries                  │    │
│  │  - lua-resty-redis                                 │    │
│  │  - lua-resty-mysql                                 │    │
│  │  - lua-resty-http                                  │    │
│  │  - lua-resty-jwt                                   │    │
│  │  - lua-resty-template                              │    │
│  │  - 100+ других библиотек                           │    │
│  └────────────────────────────────────────────────────┘    │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

### 1.2 История и мотивация

OpenResty был создан **Yichun Zhang (agentzh)** в 2009 году, когда он работал в Taobao (Alibaba). Проблема была в том, что:

- Стандартный Nginx не поддерживал динамическую логику
- Модули на C сложны в написании и поддержке
- Нужен был быстрый способ добавлять бизнес-логику в proxy

**Решение:** встроить LuaJIT в Nginx. Lua — минималистичный язык, созданный для встраивания, а LuaJIT даёт производительность близкую к нативному коду.

### 1.3 Кто использует OpenResty

| Компания | Применение |
|----------|------------|
| **Cloudflare** | WAF, Workers, весь edge computing |
| **Kong** | API Gateway (построен на OpenResty) |
| **APISIX** | API Gateway от Apache Foundation |
| **Shopify** | Edge routing |
| **Adobe** | API management |
| **Dropbox** | Traffic management |

---

## 2. Основы языка Lua

### 2.1 Краткий обзор синтаксиса

Lua — минималистичный язык, легко изучаемый за несколько часов.

```lua
-- Это комментарий

--[[
    Многострочный
    комментарий
]]

-- Переменные
local name = "OpenResty"
local count = 42
local pi = 3.14159
local is_active = true
local nothing = nil

-- Строки (можно использовать ' или ")
local s1 = "Hello"
local s2 = 'World'
local concat = s1 .. " " .. s2  -- конкатенация через ..

-- Вывод
print(concat)  -- Hello World
```

**Output:**
```
Hello World
```

### 2.2 Таблицы — универсальная структура данных

В Lua **таблицы** — единственная структура данных. Они могут быть массивами, словарями или объектами.

```lua
-- Массив (индексы начинаются с 1!)
local fruits = {"apple", "banana", "cherry"}
print(fruits[1])  -- apple

-- Словарь (ассоциативный массив)
local user = {
    name = "Alice",
    age = 30,
    email = "alice@example.com"
}
print(user.name)      -- Alice
print(user["email"])  -- alice@example.com

-- Смешанный
local mixed = {
    "first",
    "second",
    key1 = "value1",
    key2 = "value2"
}

-- Длина массива
print(#fruits)  -- 3

-- Итерация по таблице
for key, value in pairs(user) do
    print(key .. ": " .. tostring(value))
end
```

**Output:**
```
apple
Alice
alice@example.com
3
name: Alice
age: 30
email: alice@example.com
```

### 2.3 Управляющие конструкции

```lua
-- if/elseif/else
local status = 200

if status == 200 then
    print("OK")
elseif status == 404 then
    print("Not Found")
elseif status >= 500 then
    print("Server Error")
else
    print("Unknown status")
end

-- for loop (числовой)
for i = 1, 5 do
    print("Iteration: " .. i)
end

-- for с шагом
for i = 10, 1, -2 do
    print(i)  -- 10, 8, 6, 4, 2
end

-- while loop
local counter = 0
while counter < 3 do
    print("counter = " .. counter)
    counter = counter + 1
end

-- repeat/until (выполнится хотя бы раз)
local x = 10
repeat
    print("x = " .. x)
    x = x - 1
until x < 8
```

### 2.4 Функции

```lua
-- Обычная функция
local function greet(name)
    return "Hello, " .. name .. "!"
end

print(greet("World"))  -- Hello, World!

-- Функция с множественными возвращаемыми значениями
local function divide(a, b)
    if b == 0 then
        return nil, "division by zero"
    end
    return a / b, nil
end

local result, err = divide(10, 2)
if err then
    print("Error: " .. err)
else
    print("Result: " .. result)
end

-- Анонимная функция
local double = function(x)
    return x * 2
end

print(double(21))  -- 42

-- Variadic function
local function sum(...)
    local args = {...}
    local total = 0
    for _, v in ipairs(args) do
        total = total + v
    end
    return total
end

print(sum(1, 2, 3, 4, 5))  -- 15
```

**Output:**
```
Hello, World!
Result: 5.0
42
15
```

### 2.5 Особенности Lua

```lua
-- Локальные vs глобальные переменные
local safe_var = "локальная"
global_var = "ГЛОБАЛЬНАЯ (не делайте так!)"

-- В OpenResty ВСЕГДА используйте local!

-- nil и false — единственные "falsy" значения
local value = 0
if value then
    print("0 is truthy in Lua!")  -- выведется!
end

-- Сравнения
print(1 == "1")   -- false (нет type coercion)
print("~= это не равно")
print(1 ~= 2)     -- true

-- Логические операторы: and, or, not
local a = true and false  -- false
local b = true or false   -- true
local c = not true        -- false

-- Идиома "default value"
local name = nil
local display_name = name or "Anonymous"
print(display_name)  -- Anonymous
```

---

## 3. Архитектура OpenResty

### 3.1 Фазы обработки запроса

OpenResty позволяет выполнять Lua-код в разных фазах обработки HTTP-запроса:

```
┌────────────────────────────────────────────────────────────┐
│              Nginx Request Processing Phases                │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  1. init_by_lua*         ← Инициализация при старте        │
│  2. init_worker_by_lua*  ← Инициализация worker процесса   │
│         │                                                  │
│         ▼                                                  │
│  ┌─────────────── Per Request ───────────────┐             │
│  │                                           │             │
│  │  3. set_by_lua*        ← Установка переменных           │
│  │  4. rewrite_by_lua*    ← Переписывание URL              │
│  │  5. access_by_lua*     ← Проверка доступа               │
│  │  6. content_by_lua*    ← Генерация контента   ◄───┐     │
│  │  7. header_filter_by_lua*  ← Модификация headers  │     │
│  │  8. body_filter_by_lua*    ← Модификация body     │     │
│  │  9. log_by_lua*        ← Логирование          ◄───┘     │
│  │                                           │             │
│  └───────────────────────────────────────────┘             │
│                                                            │
│  * Также есть _block версии (inline в конфиге)             │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

| Фаза | Директива | Назначение |
|------|-----------|------------|
| **init** | `init_by_lua_block` | Инициализация при запуске master процесса |
| **init_worker** | `init_worker_by_lua_block` | Инициализация каждого worker |
| **set** | `set_by_lua_block` | Вычисление значения nginx переменной |
| **rewrite** | `rewrite_by_lua_block` | Переписывание URI, редиректы |
| **access** | `access_by_lua_block` | Авторизация, rate limiting |
| **content** | `content_by_lua_block` | Генерация ответа |
| **header_filter** | `header_filter_by_lua_block` | Модификация response headers |
| **body_filter** | `body_filter_by_lua_block` | Модификация response body |
| **log** | `log_by_lua_block` | Логирование после отправки ответа |

### 3.2 Первый пример: Hello World

```nginx
# /etc/openresty/nginx.conf

worker_processes auto;

events {
    worker_connections 1024;
}

http {
    server {
        listen 8080;
        
        location /hello {
            default_type text/plain;
            
            content_by_lua_block {
                ngx.say("Hello from OpenResty!")
            }
        }
    }
}
```

```bash
# Запуск
openresty

# Тестирование
curl http://localhost:8080/hello
```

**Output:**
```
Hello from OpenResty!
```

### 3.3 Доступ к данным запроса

```nginx
location /request-info {
    default_type application/json;
    
    content_by_lua_block {
        local cjson = require "cjson"
        
        local info = {
            method = ngx.req.get_method(),
            uri = ngx.var.uri,
            args = ngx.req.get_uri_args(),
            headers = ngx.req.get_headers(),
            remote_addr = ngx.var.remote_addr,
            http_version = ngx.req.http_version(),
        }
        
        ngx.say(cjson.encode(info))
    }
}
```

```bash
curl "http://localhost:8080/request-info?name=Alice&age=30" \
     -H "X-Custom: test"
```

**Output:**
```json
{
    "method": "GET",
    "uri": "/request-info",
    "args": {"name": "Alice", "age": "30"},
    "headers": {"host": "localhost:8080", "x-custom": "test", ...},
    "remote_addr": "127.0.0.1",
    "http_version": 1.1
}
```

### 3.4 Чтение тела запроса

```nginx
location /echo {
    default_type application/json;
    
    content_by_lua_block {
        -- Сначала нужно явно прочитать body
        ngx.req.read_body()
        
        local body = ngx.req.get_body_data()
        
        if not body then
            -- Body может быть в файле при больших запросах
            local file = ngx.req.get_body_file()
            if file then
                local f = io.open(file, "r")
                body = f:read("*a")
                f:close()
            end
        end
        
        ngx.say("Received: " .. (body or "empty"))
    }
}
```

```bash
curl -X POST http://localhost:8080/echo \
     -d '{"message": "Hello!"}'
```

**Output:**
```
Received: {"message": "Hello!"}
```

---

## 4. Работа с ответами

### 4.1 Установка статуса и заголовков

```nginx
location /custom-response {
    content_by_lua_block {
        -- Установка статуса
        ngx.status = 201
        
        -- Установка заголовков
        ngx.header["Content-Type"] = "application/json"
        ngx.header["X-Custom-Header"] = "custom-value"
        ngx.header["Cache-Control"] = "no-cache"
        
        -- Множественные значения одного заголовка
        ngx.header["Set-Cookie"] = {
            "session=abc123; Path=/",
            "user=Alice; Path=/"
        }
        
        local cjson = require "cjson"
        ngx.say(cjson.encode({
            status = "created",
            id = 12345
        }))
    }
}
```

### 4.2 Редиректы

```nginx
location /old-url {
    content_by_lua_block {
        -- Внешний редирект (302 по умолчанию)
        return ngx.redirect("/new-url")
        
        -- Или с кодом
        -- return ngx.redirect("/new-url", 301)
    }
}

location /internal-redirect {
    content_by_lua_block {
        -- Внутренний редирект (клиент не видит)
        return ngx.exec("/actual-handler")
    }
}
```

### 4.3 Немедленное завершение

```nginx
location /protected {
    access_by_lua_block {
        local token = ngx.req.get_headers()["Authorization"]
        
        if not token then
            ngx.status = 401
            ngx.header["WWW-Authenticate"] = 'Bearer realm="api"'
            ngx.say('{"error": "Unauthorized"}')
            return ngx.exit(401)
        end
        
        -- Если токен есть, продолжаем к content phase
    }
    
    content_by_lua_block {
        ngx.say('{"data": "secret information"}')
    }
}
```

---

## 5. Cosockets: неблокирующий I/O

### 5.1 Что такое Cosockets

**Cosockets** — это неблокирующие сокеты OpenResty, которые автоматически передают управление другим корутинам во время ожидания I/O.

```
┌────────────────────────────────────────────────────────────┐
│                    Cosocket Architecture                    │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  Worker Process                                            │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                  Event Loop                          │   │
│  │                                                     │   │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐          │   │
│  │  │Request 1 │  │Request 2 │  │Request 3 │          │   │
│  │  │Coroutine │  │Coroutine │  │Coroutine │          │   │
│  │  └────┬─────┘  └────┬─────┘  └────┬─────┘          │   │
│  │       │             │             │                │   │
│  │       ▼             ▼             ▼                │   │
│  │  ┌───────────────────────────────────────────┐     │   │
│  │  │          Cosocket Layer                   │     │   │
│  │  │  - TCP/UDP sockets                        │     │   │
│  │  │  - Yields on I/O wait                     │     │   │
│  │  │  - Resumes when data ready                │     │   │
│  │  └───────────────────────────────────────────┘     │   │
│  │                                                     │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                            │
│  Преимущество: 1 worker обрабатывает тысячи соединений     │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

### 5.2 TCP клиент

```nginx
location /tcp-example {
    content_by_lua_block {
        local sock = ngx.socket.tcp()
        sock:settimeout(1000)  -- 1 секунда
        
        -- Подключение
        local ok, err = sock:connect("127.0.0.1", 11211)  -- memcached
        if not ok then
            ngx.say("Connection failed: ", err)
            return
        end
        
        -- Отправка
        local bytes, err = sock:send("stats\r\n")
        if not bytes then
            ngx.say("Send failed: ", err)
            return
        end
        
        -- Чтение (до END\r\n)
        local data, err = sock:receive("*a")
        
        -- Важно: вернуть сокет в пул
        sock:setkeepalive(10000, 100)  -- timeout, pool size
        
        ngx.say(data)
    }
}
```

---

## 6. lua-resty-* библиотеки

### 6.1 lua-resty-redis

```nginx
location /redis-example {
    content_by_lua_block {
        local redis = require "resty.redis"
        local red = redis:new()
        
        red:set_timeout(1000)  -- 1 секунда
        
        local ok, err = red:connect("127.0.0.1", 6379)
        if not ok then
            ngx.status = 500
            ngx.say("Redis connection failed: ", err)
            return
        end
        
        -- SET
        local ok, err = red:set("mykey", "myvalue")
        if not ok then
            ngx.say("SET failed: ", err)
            return
        end
        
        -- GET
        local res, err = red:get("mykey")
        if not res then
            ngx.say("GET failed: ", err)
            return
        end
        
        if res == ngx.null then
            ngx.say("Key not found")
            return
        end
        
        -- Вернуть в пул
        red:set_keepalive(10000, 100)
        
        ngx.say("Value: ", res)
    }
}
```

**Output:**
```
Value: myvalue
```

### 6.2 lua-resty-http

```nginx
location /proxy-api {
    content_by_lua_block {
        local http = require "resty.http"
        local httpc = http.new()
        
        local res, err = httpc:request_uri("https://api.github.com/users/openresty", {
            method = "GET",
            headers = {
                ["User-Agent"] = "OpenResty",
                ["Accept"] = "application/json",
            },
            ssl_verify = false,  -- в продакшне = true!
        })
        
        if not res then
            ngx.status = 502
            ngx.say("Request failed: ", err)
            return
        end
        
        ngx.status = res.status
        ngx.header["Content-Type"] = res.headers["Content-Type"]
        ngx.say(res.body)
    }
}
```

### 6.3 lua-resty-mysql

```nginx
location /db-query {
    content_by_lua_block {
        local mysql = require "resty.mysql"
        local db = mysql:new()
        
        db:set_timeout(1000)
        
        local ok, err, errcode, sqlstate = db:connect{
            host = "127.0.0.1",
            port = 3306,
            database = "test",
            user = "root",
            password = "secret",
            charset = "utf8mb4",
            max_packet_size = 1024 * 1024,
        }
        
        if not ok then
            ngx.status = 500
            ngx.say("MySQL connection failed: ", err)
            return
        end
        
        local res, err = db:query("SELECT id, name FROM users LIMIT 10")
        if not res then
            ngx.say("Query failed: ", err)
            return
        end
        
        local cjson = require "cjson"
        ngx.header["Content-Type"] = "application/json"
        ngx.say(cjson.encode(res))
        
        db:set_keepalive(10000, 100)
    }
}
```

---

## 7. Практические паттерны

### 7.1 Rate Limiting

```nginx
http {
    # Shared memory для rate limiting
    lua_shared_dict rate_limit 10m;
    
    server {
        location /api/ {
            access_by_lua_block {
                local limit = require "resty.limit.req"
                
                -- 10 requests/second с burst 5
                local lim, err = limit.new("rate_limit", 10, 5)
                if not lim then
                    ngx.log(ngx.ERR, "failed to create limiter: ", err)
                    return ngx.exit(500)
                end
                
                local key = ngx.var.binary_remote_addr
                local delay, err = lim:incoming(key, true)
                
                if not delay then
                    if err == "rejected" then
                        ngx.header["Retry-After"] = "1"
                        return ngx.exit(429)
                    end
                    ngx.log(ngx.ERR, "rate limit error: ", err)
                    return ngx.exit(500)
                end
                
                if delay > 0 then
                    ngx.sleep(delay)
                end
            }
            
            proxy_pass http://backend;
        }
    }
}
```

### 7.2 JWT аутентификация

```nginx
http {
    lua_shared_dict jwt_cache 10m;
    
    server {
        location /api/ {
            access_by_lua_block {
                local jwt = require "resty.jwt"
                local cjson = require "cjson"
                
                local auth_header = ngx.req.get_headers()["Authorization"]
                if not auth_header then
                    ngx.status = 401
                    ngx.say('{"error": "Missing Authorization header"}')
                    return ngx.exit(401)
                end
                
                -- Извлечь токен из "Bearer <token>"
                local token = auth_header:match("Bearer%s+(.+)")
                if not token then
                    ngx.status = 401
                    ngx.say('{"error": "Invalid Authorization format"}')
                    return ngx.exit(401)
                end
                
                -- Валидация JWT
                local secret = "your-256-bit-secret"
                local jwt_obj = jwt:verify(secret, token)
                
                if not jwt_obj.verified then
                    ngx.status = 401
                    ngx.say(cjson.encode({
                        error = "Invalid token",
                        reason = jwt_obj.reason
                    }))
                    return ngx.exit(401)
                end
                
                -- Добавить user info в заголовки для backend
                ngx.req.set_header("X-User-ID", jwt_obj.payload.sub)
                ngx.req.set_header("X-User-Role", jwt_obj.payload.role or "user")
            }
            
            proxy_pass http://backend;
        }
    }
}
```

### 7.3 Кеширование ответов

```nginx
http {
    lua_shared_dict cache 100m;
    
    server {
        location /cached-api {
            content_by_lua_block {
                local cache = ngx.shared.cache
                local cjson = require "cjson"
                
                local cache_key = ngx.var.uri .. "?" .. (ngx.var.args or "")
                
                -- Проверить кеш
                local cached = cache:get(cache_key)
                if cached then
                    ngx.header["X-Cache"] = "HIT"
                    ngx.say(cached)
                    return
                end
                
                -- Cache miss — запрос к backend
                local http = require "resty.http"
                local httpc = http.new()
                
                local res, err = httpc:request_uri("http://backend:8080" .. ngx.var.uri, {
                    method = "GET",
                    query = ngx.var.args,
                })
                
                if not res then
                    ngx.status = 502
                    ngx.say('{"error": "Backend unavailable"}')
                    return
                end
                
                -- Сохранить в кеш на 60 секунд
                cache:set(cache_key, res.body, 60)
                
                ngx.header["X-Cache"] = "MISS"
                ngx.status = res.status
                ngx.say(res.body)
            }
        }
    }
}
```

### 7.4 A/B тестирование

```nginx
http {
    lua_shared_dict ab_stats 10m;
    
    server {
        location / {
            set $backend "";
            
            rewrite_by_lua_block {
                local ab_stats = ngx.shared.ab_stats
                
                -- Определить вариант по cookie или случайно
                local variant = ngx.var.cookie_ab_variant
                
                if not variant then
                    -- Новый пользователь — рандомное распределение
                    math.randomseed(ngx.now() * 1000)
                    if math.random() < 0.5 then
                        variant = "A"
                    else
                        variant = "B"
                    end
                    
                    -- Установить cookie
                    ngx.header["Set-Cookie"] = "ab_variant=" .. variant .. "; Path=/; Max-Age=86400"
                end
                
                -- Инкремент счётчика
                ab_stats:incr("variant_" .. variant .. "_hits", 1, 0)
                
                -- Выбрать backend
                if variant == "A" then
                    ngx.var.backend = "http://backend-a:8080"
                else
                    ngx.var.backend = "http://backend-b:8080"
                end
            }
            
            proxy_pass $backend;
        }
        
        location /ab-stats {
            content_by_lua_block {
                local ab_stats = ngx.shared.ab_stats
                local cjson = require "cjson"
                
                ngx.say(cjson.encode({
                    variant_A = ab_stats:get("variant_A_hits") or 0,
                    variant_B = ab_stats:get("variant_B_hits") or 0,
                }))
            }
        }
    }
}
```

---

## 8. Shared Memory (lua_shared_dict)

### 8.1 Основы работы с shared dict

```nginx
http {
    # Объявление shared memory зон
    lua_shared_dict my_cache 10m;    # 10 мегабайт
    lua_shared_dict stats 1m;
    lua_shared_dict locks 1m;
    
    server {
        location /shared-demo {
            content_by_lua_block {
                local cache = ngx.shared.my_cache
                
                -- SET с TTL
                cache:set("key1", "value1", 60)  -- 60 секунд
                
                -- SET без TTL (бессрочно)
                cache:set("key2", "value2")
                
                -- GET
                local val, flags = cache:get("key1")
                ngx.say("key1 = ", val or "nil")
                
                -- Атомарный инкремент
                local new_val, err = cache:incr("counter", 1, 0)  -- начальное значение = 0
                ngx.say("counter = ", new_val)
                
                -- Добавить только если не существует
                local success, err = cache:add("unique_key", "unique_value", 60)
                ngx.say("add success = ", tostring(success))
                
                -- Получить и установить (safe_set)
                local old_val = cache:get("key1")
                cache:set("key1", "new_value")
                ngx.say("old value was: ", old_val)
                
                -- Удаление
                cache:delete("key2")
                
                -- Получить все ключи (осторожно с производительностью!)
                local keys = cache:get_keys(100)  -- максимум 100 ключей
                ngx.say("keys count: ", #keys)
            }
        }
    }
}
```

### 8.2 Mutex/Lock паттерн

```nginx
http {
    lua_shared_dict locks 1m;
    lua_shared_dict cache 10m;
    
    server {
        location /cache-with-lock {
            content_by_lua_block {
                local lock = require "resty.lock"
                local cache = ngx.shared.cache
                
                local key = "expensive_data"
                
                -- Проверить кеш
                local data = cache:get(key)
                if data then
                    ngx.say("Cache hit: ", data)
                    return
                end
                
                -- Cache miss — нужно вычислить
                -- Берём lock чтобы только один worker делал работу
                local lock_obj, err = lock:new("locks")
                if not lock_obj then
                    ngx.log(ngx.ERR, "failed to create lock: ", err)
                    return ngx.exit(500)
                end
                
                local elapsed, err = lock_obj:lock(key)
                if not elapsed then
                    ngx.log(ngx.ERR, "failed to acquire lock: ", err)
                    return ngx.exit(500)
                end
                
                -- Double-check после получения lock
                data = cache:get(key)
                if data then
                    lock_obj:unlock()
                    ngx.say("Cache hit after lock: ", data)
                    return
                end
                
                -- Выполняем "дорогую" операцию
                ngx.sleep(1)  -- имитация
                data = "computed_value_" .. ngx.now()
                
                -- Сохраняем в кеш
                cache:set(key, data, 60)
                
                lock_obj:unlock()
                
                ngx.say("Computed: ", data)
            }
        }
    }
}
```

---

## 9. Subrequests и Location Capture

### 9.1 Захват внутренних location

```nginx
server {
    # Внутренний location для получения данных пользователя
    location = /internal/user {
        internal;  # Доступен только изнутри
        
        content_by_lua_block {
            local user_id = ngx.var.arg_id
            -- В реальности — запрос к БД или сервису
            local cjson = require "cjson"
            ngx.say(cjson.encode({
                id = user_id,
                name = "User " .. user_id,
                role = "admin"
            }))
        }
    }
    
    location /api/profile {
        content_by_lua_block {
            -- Выполнить subrequest
            local res = ngx.location.capture("/internal/user", {
                args = { id = "123" }
            })
            
            if res.status ~= 200 then
                ngx.status = res.status
                ngx.say("Error fetching user")
                return
            end
            
            local cjson = require "cjson"
            local user = cjson.decode(res.body)
            
            ngx.say("Welcome, ", user.name, "! Your role is ", user.role)
        }
    }
}
```

### 9.2 Параллельные subrequests

```nginx
location /dashboard {
    content_by_lua_block {
        -- Параллельные запросы к нескольким сервисам
        local res1, res2, res3 = ngx.location.capture_multi({
            { "/internal/user", { args = { id = "123" } } },
            { "/internal/orders", { args = { user_id = "123" } } },
            { "/internal/notifications", { args = { user_id = "123" } } },
        })
        
        local cjson = require "cjson"
        
        local dashboard = {
            user = res1.status == 200 and cjson.decode(res1.body) or nil,
            orders = res2.status == 200 and cjson.decode(res2.body) or nil,
            notifications = res3.status == 200 and cjson.decode(res3.body) or nil,
        }
        
        ngx.header["Content-Type"] = "application/json"
        ngx.say(cjson.encode(dashboard))
    }
}
```

---

## 10. Продакшн-системы на OpenResty

### 10.1 Kong — API Gateway

**Kong** — популярнейший API Gateway, построенный на OpenResty.

```
┌────────────────────────────────────────────────────────────┐
│                       Kong Architecture                     │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  Clients                                                   │
│     │                                                      │
│     ▼                                                      │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                    Kong (OpenResty)                  │   │
│  │  ┌─────────────────────────────────────────────┐    │   │
│  │  │                  Plugins                     │    │   │
│  │  │  ┌─────────┐ ┌─────────┐ ┌─────────┐       │    │   │
│  │  │  │ Auth    │ │  Rate   │ │  Log    │       │    │   │
│  │  │  │ (JWT,   │ │ Limit   │ │ (HTTP,  │       │    │   │
│  │  │  │  OAuth) │ │         │ │  File)  │       │    │   │
│  │  │  └─────────┘ └─────────┘ └─────────┘       │    │   │
│  │  │  ┌─────────┐ ┌─────────┐ ┌─────────┐       │    │   │
│  │  │  │Transform│ │  CORS   │ │  ACL    │       │    │   │
│  │  │  └─────────┘ └─────────┘ └─────────┘       │    │   │
│  │  └─────────────────────────────────────────────┘    │   │
│  └───────────────┬─────────────────────────────────────┘   │
│                  │                                         │
│                  ▼                                         │
│  ┌───────────────────────────────────────────────────┐     │
│  │               Upstream Services                    │     │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────┐           │     │
│  │  │Service A│  │Service B│  │Service C│           │     │
│  │  └─────────┘  └─────────┘  └─────────┘           │     │
│  └───────────────────────────────────────────────────┘     │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

### 10.2 Apache APISIX

**APISIX** — альтернатива Kong от Apache Foundation, также на OpenResty.

Преимущества APISIX:
- Полностью динамическая конфигурация (etcd)
- Dashboard из коробки
- Больше встроенных плагинов
- Активно развивается

### 10.3 Cloudflare Workers

Cloudflare использует модифицированный OpenResty для своей edge-платформы:

- **WAF** (Web Application Firewall)
- **DDoS защита**
- **Cloudflare Workers** (serverless на edge)
- **Маршрутизация**

---

## 11. Отладка и профилирование

### 11.1 Логирование

```nginx
location /debug-example {
    content_by_lua_block {
        -- Уровни логирования
        ngx.log(ngx.STDERR, "STDERR message")
        ngx.log(ngx.EMERG, "Emergency!")
        ngx.log(ngx.ALERT, "Alert!")
        ngx.log(ngx.CRIT, "Critical!")
        ngx.log(ngx.ERR, "Error!")
        ngx.log(ngx.WARN, "Warning!")
        ngx.log(ngx.NOTICE, "Notice")
        ngx.log(ngx.INFO, "Info")
        ngx.log(ngx.DEBUG, "Debug")  -- требует error_log ... debug;
        
        -- Форматированное логирование
        local user_id = 123
        local action = "login"
        ngx.log(ngx.INFO, string.format("User %d performed %s", user_id, action))
        
        ngx.say("Check error.log for messages")
    }
}
```

### 11.2 Таймеры и профилирование

```nginx
location /timed-operation {
    content_by_lua_block {
        local start_time = ngx.now()
        
        -- Операция
        ngx.sleep(0.1)  -- имитация работы
        
        local elapsed = ngx.now() - start_time
        ngx.log(ngx.INFO, "Operation took ", elapsed, " seconds")
        
        ngx.header["X-Response-Time"] = string.format("%.3f", elapsed)
        ngx.say("Completed in ", elapsed, " seconds")
    }
}
```

### 11.3 Рекомендации по отладке

```lua
-- 1. Используйте pcall для перехвата ошибок
local ok, result = pcall(function()
    -- потенциально опасный код
    error("Something went wrong!")
end)

if not ok then
    ngx.log(ngx.ERR, "Error: ", result)
end

-- 2. Проверяйте возвращаемые значения
local res, err = some_function()
if not res then
    ngx.log(ngx.ERR, "Function failed: ", err)
    return ngx.exit(500)
end

-- 3. Используйте ngx.var.request_id для трассировки
ngx.log(ngx.INFO, "[", ngx.var.request_id, "] Processing request")
```

---

## 12. Best Practices

### 12.1 Производительность

```lua
-- 1. ВСЕГДА используйте local
local ngx = ngx  -- кешировать ngx в локальной переменной
local cjson = require "cjson"

-- 2. Избегайте создания таблиц в hot paths
-- Плохо:
for i = 1, 1000 do
    local t = {}  -- создаётся каждую итерацию
end

-- Хорошо:
local t = {}
for i = 1, 1000 do
    -- переиспользуем t
end

-- 3. Используйте string.format вместо конкатенации для сложных строк
-- Плохо:
local msg = "User " .. user_id .. " from " .. ip .. " requested " .. uri

-- Хорошо:
local msg = string.format("User %s from %s requested %s", user_id, ip, uri)

-- 4. Используйте ngx.re.match вместо string.match для regex
local m = ngx.re.match(uri, [[^/api/v(\d+)/]], "jo")  -- "jo" = JIT + compile once
```

### 12.2 Безопасность

```lua
-- 1. Экранируйте пользовательский ввод
local user_input = ngx.var.arg_query
local safe_input = ngx.quote_sql_str(user_input)  -- для SQL
-- Или используйте prepared statements через lua-resty-mysql

-- 2. Валидируйте типы и форматы
local id = tonumber(ngx.var.arg_id)
if not id or id < 1 then
    return ngx.exit(400)
end

-- 3. Ограничивайте размер тела запроса
-- В nginx.conf:
-- client_max_body_size 1m;

-- 4. Не доверяйте заголовкам
local real_ip = ngx.var.remote_addr  -- не X-Forwarded-For!
-- X-Forwarded-For можно использовать только если настроен set_real_ip_from
```

### 12.3 Код организация

```lua
-- Выносите логику в отдельные файлы

-- /usr/local/openresty/lualib/myapp/auth.lua
local _M = {}

function _M.verify_token(token)
    -- логика верификации
    return true, { user_id = 123, role = "admin" }
end

return _M

-- В nginx.conf:
-- lua_package_path "/usr/local/openresty/lualib/?.lua;;";

-- В location:
content_by_lua_block {
    local auth = require "myapp.auth"
    local ok, user = auth.verify_token(token)
}
```

---

## 💡 Key Takeaways

- **OpenResty = Nginx + LuaJIT** — программируемый веб-сервер с производительностью близкой к C
- **Cosockets** — неблокирующий I/O позволяет обрабатывать тысячи соединений на один worker
- **Фазы обработки** — Lua-код выполняется в конкретных фазах (rewrite, access, content, log)
- **lua_shared_dict** — быстрая shared memory между workers для кеширования и rate limiting
- **lua-resty-*** — богатая экосистема библиотек для Redis, MySQL, HTTP, JWT и многого другого

---

## 🚀 Next Steps

**Related Modules:**
- [Web Servers](../03_WebServers/) — базовая конфигурация Nginx
- [Architecture](../08_Architecture/) — архитектура веб-приложений

**Practice Ideas:**
1. Реализуйте простой API Gateway с rate limiting и JWT аутентификацией
2. Настройте кеширующий прокси с OpenResty и Redis
3. Создайте A/B тестирование на edge
4. Реализуйте WAF с базовыми правилами безопасности

**Going Deeper:**
- Изучите Kong и APISIX для production API Gateway
- Попробуйте написать свой Kong plugin
- Изучите Lua coroutines и ngx.thread для параллелизма

---

## 📚 Additional Resources

**Documentation:**
- [OpenResty Documentation](https://openresty.org/en/docs.html) — официальная документация
- [lua-nginx-module](https://github.com/openresty/lua-nginx-module) — полный API reference
- [Lua 5.1 Reference Manual](https://www.lua.org/manual/5.1/) — справочник по Lua

**Books:**
- "Programming in Lua" by Roberto Ierusalimschy — библия Lua
- "OpenResty Best Practices" — сборник рецептов (на GitHub)

**Tools:**
- [OPM](https://opm.openresty.org/) — OpenResty Package Manager
- [resty-cli](https://github.com/openresty/resty-cli) — CLI для запуска Lua скриптов

**Projects:**
- [Kong](https://konghq.com/) — API Gateway
- [Apache APISIX](https://apisix.apache.org/) — динамический API Gateway
- [lua-resty-* libraries](https://github.com/openresty) — библиотеки OpenResty

---

