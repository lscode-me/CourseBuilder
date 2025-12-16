# OpenResty и Lua - Quiz

Проверьте свои знания по теме "OpenResty и программируемый веб-сервер на базе Nginx".

---

## Question 1: Что такое OpenResty?

Что представляет собой OpenResty?

A) Отдельный веб-сервер, написанный на Lua

B) Форк Apache HTTP Server

C) Плагин для Node.js

D) Nginx с встроенным LuaJIT и набором Lua-библиотек

---

## Question 2: LuaJIT

Почему в OpenResty используется LuaJIT, а не стандартный Lua?

A) LuaJIT поддерживает больше типов данных

B) LuaJIT работает только на Linux

C) LuaJIT обеспечивает производительность близкую к нативному коду

D) LuaJIT бесплатный, а стандартный Lua — платный

---

## Question 3: Индексация массивов в Lua

С какого числа начинается индексация массивов в Lua?

A) Зависит от настроек

B) 1

C) -1

D) 0

---

## Question 4: Универсальная структура данных

Какая единственная структура данных есть в Lua для массивов, словарей и объектов?

A) table

B) array

C) object

D) dict

---

## Question 5: Конкатенация строк

Какой оператор используется для конкатенации строк в Lua?

A) concat()

B) ..

C) &

D) +

---

## Question 6: Фаза access_by_lua

Для чего обычно используется фаза `access_by_lua`?

A) Для инициализации worker процесса

B) Для проверки авторизации и rate limiting

C) Для генерации HTML контента

D) Для логирования запросов

---

## Question 7: content_by_lua

Что делает директива `content_by_lua_block`?

A) Модифицирует заголовки ответа

B) Логирует запрос после отправки

C) Генерирует тело HTTP ответа

D) Переписывает URL запроса

---

## Question 8: ngx.say vs ngx.print

В чём разница между `ngx.say()` и `ngx.print()`?

A) ngx.say() добавляет перевод строки в конце

B) Разницы нет

C) ngx.print() быстрее

D) ngx.say() только для JSON

---

## Question 9: Чтение тела запроса

Что нужно сделать перед вызовом `ngx.req.get_body_data()`?

A) Проверить метод запроса

B) Ничего, body доступно сразу

C) Вызвать `ngx.req.read_body()`

D) Установить Content-Type

---

## Question 10: Cosockets

Что такое Cosockets в OpenResty?

A) Сокеты для WebSocket соединений

B) Сжатые сокеты

C) Неблокирующие сокеты с автоматическим yield корутин

D) Шифрованные сокеты

---

## Question 11: Connection pooling

Какой метод используется для возврата соединения в пул в lua-resty-redis?

A) release()

B) pool()

C) set_keepalive()

D) close()

---

## Question 12: lua_shared_dict

Для чего используется `lua_shared_dict`?

A) Для shared memory между worker процессами

B) Для хранения SSL сертификатов

C) Для конфигурации Nginx

D) Для хранения Lua модулей

---

## Question 13: Rate limiting

Какой тип хранилища используется для rate limiting в OpenResty?

A) Файловая система

B) SQLite

C) lua_shared_dict

D) Redis обязательно

---

## Question 14: Немедленное завершение

Как немедленно завершить обработку запроса с кодом 403?

A) ngx.return(403)

B) ngx.end(403)

C) ngx.stop(403)

D) ngx.exit(403)

---

## Question 15: Internal location

Что означает директива `internal` для location?

A) Location доступен только через subrequest

B) Location только для POST запросов

C) Location зашифрован

D) Location доступен только для localhost

---

## Question 16: Параллельные subrequests

Какая функция выполняет несколько subrequests параллельно?

A) ngx.location.parallel()

B) ngx.location.capture_multi()

C) ngx.location.all()

D) ngx.parallel.capture()

---

## Question 17: Логирование

Какой уровень логирования используется для обычных ошибок?

A) ngx.ERR

B) ngx.DEBUG

C) ngx.WARN

D) ngx.INFO

---

## Question 18: Kong

На какой технологии построен популярный API Gateway Kong?

A) Go

B) Node.js

C) Java

D) OpenResty

---

## Question 19: Локальные переменные

Почему в OpenResty рекомендуется ВСЕГДА использовать `local`?

A) Для экономии памяти

B) Это требование синтаксиса Lua

C) Локальные переменные быстрее и безопаснее между запросами

D) Глобальные переменные не поддерживаются

---

## Question 20: Falsy values

Какие значения в Lua являются "falsy" (ложными)?

A) nil и false

B) 0, "", nil, false

C) Только nil

D) Только false

---

## Question 21: JSON в OpenResty

Какая библиотека обычно используется для работы с JSON в OpenResty?

A) cjson

B) dkjson

C) rapidjson

D) json

---

## Question 22: Регулярные выражения

Какую функцию рекомендуется использовать для regex в OpenResty вместо string.match?

A) lua.regex()

B) ngx.re.match()

C) ngx.match()

D) ngx.regex()

---

## Question 23: HTTP клиент

Какая библиотека используется для HTTP запросов из OpenResty?

A) resty.http

B) lua-resty-curl

C) ngx.http

D) lua-http

---

## Question 24: Фаза rewrite

В какой фазе обычно выполняется изменение URI запроса?

A) init_by_lua

B) access_by_lua

C) content_by_lua

D) rewrite_by_lua

---

## Question 25: Переменные Nginx

Как получить значение переменной Nginx `$remote_addr` из Lua?

A) ngx.get("remote_addr")

B) ngx.var.remote_addr

C) ngx.remote_addr

D) ngx.req.remote_addr

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | D | OpenResty = Nginx + LuaJIT + набор lua-resty-* библиотек |
| 2 | C | LuaJIT — JIT компилятор для Lua, даёт производительность близкую к C |
| 3 | B | В Lua массивы индексируются с 1, не с 0 как в большинстве языков |
| 4 | A | table — единственная структура данных в Lua для всех коллекций |
| 5 | B | Оператор `..` используется для конкатенации строк в Lua |
| 6 | B | access_by_lua используется для авторизации, аутентификации, rate limiting |
| 7 | C | content_by_lua генерирует тело HTTP ответа |
| 8 | A | ngx.say() добавляет \n в конце, ngx.print() — нет |
| 9 | C | Нужно явно прочитать body вызовом ngx.req.read_body() |
| 10 | C | Cosockets — неблокирующие сокеты, автоматически yield при ожидании I/O |
| 11 | C | set_keepalive(timeout, pool_size) возвращает соединение в пул |
| 12 | A | lua_shared_dict — shared memory между всеми workers |
| 13 | C | lua_shared_dict используется для счётчиков rate limiting |
| 14 | D | ngx.exit(status_code) немедленно завершает обработку |
| 15 | A | internal location доступен только через ngx.location.capture |
| 16 | B | ngx.location.capture_multi() выполняет несколько subrequests параллельно |
| 17 | A | ngx.ERR — стандартный уровень для ошибок |
| 18 | D | Kong построен на OpenResty (Nginx + Lua) |
| 19 | C | Локальные переменные быстрее и не shared между запросами (безопасность) |
| 20 | A | В Lua только nil и false являются falsy; 0 и "" — truthy! |
| 21 | A | cjson (lua-cjson) — стандартная библиотека для JSON в OpenResty |
| 22 | B | ngx.re.match() использует PCRE и поддерживает JIT компиляцию regex |
| 23 | A | lua-resty-http (require "resty.http") — HTTP клиент для OpenResty |
| 24 | D | rewrite_by_lua предназначена для изменения URI и редиректов |
| 25 | B | ngx.var.имя_переменной — доступ к переменным Nginx |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **23-25 правильных (90-100%)** | 🏆 Отлично! | Вы отлично понимаете OpenResty и Lua. |
| **18-22 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Углубите знания по фазам и cosockets. |
| **13-17 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы о Lua и архитектуре OpenResty. |
| **Менее 13 правильных (<50%)** | 📚 Нужно повторить | Начните с основ Lua и простых примеров OpenResty. |

---


