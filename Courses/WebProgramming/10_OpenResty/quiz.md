# OpenResty и Lua - Quiz

Проверьте свои знания по теме "OpenResty и программируемый веб-сервер на базе Nginx".

---

## Question 1: Что такое OpenResty?






Что представляет собой OpenResty?

A) Форк Apache HTTP Server

B) Nginx с встроенным LuaJIT и набором Lua-библиотек

C) Отдельный веб-сервер, написанный на Lua

D) Плагин для Node.js

---

## Question 2: LuaJIT






Почему в OpenResty используется LuaJIT, а не стандартный Lua?

A) LuaJIT бесплатный, а стандартный Lua — платный

B) LuaJIT обеспечивает производительность близкую к нативному коду

C) LuaJIT поддерживает больше типов данных

D) LuaJIT работает только на Linux

---

## Question 3: Индексация массивов в Lua






С какого числа начинается индексация массивов в Lua?

A) 0

B) 1

C) -1

D) Зависит от настроек

---

## Question 4: Универсальная структура данных






Какая единственная структура данных есть в Lua для массивов, словарей и объектов?

A) array

B) dict

C) table

D) object

---

## Question 5: Конкатенация строк






Какой оператор используется для конкатенации строк в Lua?

A) +

B) &

C) ..

D) concat()

---

## Question 6: Фаза access_by_lua






Для чего обычно используется фаза `access_by_lua`?

A) Для генерации HTML контента

B) Для проверки авторизации и rate limiting

C) Для логирования запросов

D) Для инициализации worker процесса

---

## Question 7: content_by_lua






Что делает директива `content_by_lua_block`?

A) Модифицирует заголовки ответа

B) Генерирует тело HTTP ответа

C) Переписывает URL запроса

D) Логирует запрос после отправки

---

## Question 8: ngx.say vs ngx.print






В чём разница между `ngx.say()` и `ngx.print()`?

A) ngx.say() добавляет перевод строки в конце

B) ngx.print() быстрее

C) ngx.say() только для JSON

D) Разницы нет

---

## Question 9: Чтение тела запроса






Что нужно сделать перед вызовом `ngx.req.get_body_data()`?

A) Установить Content-Type

B) Вызвать `ngx.req.read_body()`

C) Проверить метод запроса

D) Ничего, body доступно сразу

---

## Question 10: Cosockets






Что такое Cosockets в OpenResty?

A) Шифрованные сокеты

B) Неблокирующие сокеты с автоматическим yield корутин

C) Сокеты для WebSocket соединений

D) Сжатые сокеты

---

## Question 11: Connection pooling






Какой метод используется для возврата соединения в пул в lua-resty-redis?

A) close()

B) release()

C) set_keepalive()

D) pool()

---

## Question 12: lua_shared_dict






Для чего используется `lua_shared_dict`?

A) Для хранения Lua модулей

B) Для shared memory между worker процессами

C) Для хранения SSL сертификатов

D) Для конфигурации Nginx

---

## Question 13: Rate limiting






Какой тип хранилища используется для rate limiting в OpenResty?

A) Redis обязательно

B) Файловая система

C) lua_shared_dict

D) SQLite

---

## Question 14: Немедленное завершение






Как немедленно завершить обработку запроса с кодом 403?

A) ngx.stop(403)

B) ngx.exit(403)

C) ngx.return(403)

D) ngx.end(403)

---

## Question 15: Internal location






Что означает директива `internal` для location?

A) Location доступен только для localhost

B) Location доступен только через subrequest

C) Location зашифрован

D) Location только для POST запросов

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

A) ngx.WARN

B) ngx.ERR

C) ngx.INFO

D) ngx.DEBUG

---

## Question 18: Kong






На какой технологии построен популярный API Gateway Kong?

A) Node.js

B) OpenResty

C) Go

D) Java

---

## Question 19: Локальные переменные






Почему в OpenResty рекомендуется ВСЕГДА использовать `local`?

A) Глобальные переменные не поддерживаются

B) Локальные переменные быстрее и безопаснее между запросами

C) Это требование синтаксиса Lua

D) Для экономии памяти

---

## Question 20: Falsy values






Какие значения в Lua являются "falsy" (ложными)?

A) 0, "", nil, false

B) nil и false

C) Только nil

D) Только false

---

## Question 21: JSON в OpenResty






Какая библиотека обычно используется для работы с JSON в OpenResty?

A) json

B) cjson

C) rapidjson

D) dkjson

---

## Question 22: Регулярные выражения






Какую функцию рекомендуется использовать для regex в OpenResty вместо string.match?

A) ngx.regex()

B) ngx.re.match()

C) ngx.match()

D) lua.regex()

---

## Question 23: HTTP клиент






Какая библиотека используется для HTTP запросов из OpenResty?

A) lua-http

B) resty.http

C) ngx.http

D) lua-resty-curl

---

## Question 24: Фаза rewrite






В какой фазе обычно выполняется изменение URI запроса?

A) init_by_lua

B) access_by_lua

C) rewrite_by_lua

D) content_by_lua

---

## Question 25: Переменные Nginx






Как получить значение переменной Nginx `$remote_addr` из Lua?

A) ngx.remote_addr

B) ngx.var.remote_addr

C) ngx.req.remote_addr

D) ngx.get("remote_addr")

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | OpenResty = Nginx + LuaJIT + набор lua-resty-* библиотек |
| 2 | B | LuaJIT — JIT компилятор для Lua, даёт производительность близкую к C |
| 3 | B | В Lua массивы индексируются с 1, не с 0 как в большинстве языков |
| 4 | C | table — единственная структура данных в Lua для всех коллекций |
| 5 | C | Оператор `..` используется для конкатенации строк в Lua |
| 6 | B | access_by_lua используется для авторизации, аутентификации, rate limiting |
| 7 | B | content_by_lua генерирует тело HTTP ответа |
| 8 | A | ngx.say() добавляет \n в конце, ngx.print() — нет |
| 9 | B | Нужно явно прочитать body вызовом ngx.req.read_body() |
| 10 | B | Cosockets — неблокирующие сокеты, автоматически yield при ожидании I/O |
| 11 | C | set_keepalive(timeout, pool_size) возвращает соединение в пул |
| 12 | B | lua_shared_dict — shared memory между всеми workers |
| 13 | C | lua_shared_dict используется для счётчиков rate limiting |
| 14 | B | ngx.exit(status_code) немедленно завершает обработку |
| 15 | B | internal location доступен только через ngx.location.capture |
| 16 | B | ngx.location.capture_multi() выполняет несколько subrequests параллельно |
| 17 | B | ngx.ERR — стандартный уровень для ошибок |
| 18 | B | Kong построен на OpenResty (Nginx + Lua) |
| 19 | B | Локальные переменные быстрее и не shared между запросами (безопасность) |
| 20 | B | В Lua только nil и false являются falsy; 0 и "" — truthy! |
| 21 | B | cjson (lua-cjson) — стандартная библиотека для JSON в OpenResty |
| 22 | B | ngx.re.match() использует PCRE и поддерживает JIT компиляцию regex |
| 23 | B | lua-resty-http (require "resty.http") — HTTP клиент для OpenResty |
| 24 | C | rewrite_by_lua предназначена для изменения URI и редиректов |
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

