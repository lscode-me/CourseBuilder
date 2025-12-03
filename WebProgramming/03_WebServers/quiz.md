# Web Servers - Quiz

Проверьте свои знания по теме "Веб-серверы: Apache, Nginx и другие".

---

## Question 1: История

Какой веб-сервер появился первым?

A) Apache

B) CERN httpd

C) Nginx

D) IIS

---

## Question 2: Apache MPM

Какой MPM в Apache создаёт новый процесс для каждого соединения?

A) event

B) worker

C) prefork

D) async

---

## Question 3: Nginx архитектура

Как Nginx обрабатывает множество соединений?

A) Создаёт новый поток для каждого соединения

B) Создаёт новый процесс для каждого соединения

C) Использует event-driven модель с epoll/kqueue

D) Использует только один поток для всех соединений

---

## Question 4: .htaccess

Какой веб-сервер поддерживает .htaccess файлы?

A) Nginx

B) Apache

C) OpenBSD httpd

D) H2O

---

## Question 5: Конфигурация Nginx

Как называется блок конфигурации виртуального хоста в Nginx?

A) VirtualHost

B) server

C) host

D) site

---

## Question 6: Reverse Proxy

Какая директива Nginx используется для проксирования запросов?

A) forward_pass

B) proxy_pass

C) backend_pass

D) upstream_pass

---

## Question 7: Apache модули

Какой модуль Apache используется для URL rewriting?

A) mod_redirect

B) mod_rewrite

C) mod_url

D) mod_route

---

## Question 8: Nginx worker_processes

Какое значение рекомендуется для `worker_processes` на сервере с 4 CPU?

A) 1

B) 2

C) 4 или auto

D) 8

---

## Question 9: Caddy

Какая главная особенность веб-сервера Caddy?

A) Самый быстрый в мире

B) Автоматический HTTPS с Let's Encrypt

C) Совместимость с Apache

D) Встроенная база данных

---

## Question 10: OpenBSD httpd

Что является главным приоритетом OpenBSD httpd?

A) Максимальная производительность

B) Совместимость с Apache

C) Безопасность и простота

D) Поддержка всех протоколов

---

## Question 11: SSL/TLS

Какой порт по умолчанию используется для HTTPS?

A) 80

B) 8080

C) 443

D) 8443

---

## Question 12: Nginx upstream

Для чего используется блок `upstream` в Nginx?

A) Для загрузки файлов

B) Для определения группы backend серверов

C) Для логирования

D) Для SSL настройки

---

## Question 13: Apache event MPM

Чем event MPM отличается от worker MPM?

A) Использует больше памяти

B) Эффективнее обрабатывает keep-alive соединения

C) Создаёт больше процессов

D) Не поддерживает потоки

---

## Question 14: Nginx статические файлы

Какая директива Nginx используется для кэширования статических файлов?

A) cache

B) expires

C) static_cache

D) file_cache

---

## Question 15: Lighttpd

Для каких сценариев лучше всего подходит Lighttpd?

A) Корпоративные приложения

B) Встраиваемые системы и высоконагруженные статические сайты

C) Только Windows серверы

D) Только базы данных

---

## Question 16: Nginx try_files

Что делает директива `try_files $uri $uri/ /index.html`?

A) Создаёт файл если не существует

B) Пробует найти файл, затем директорию, затем index.html

C) Удаляет файл

D) Переименовывает файл

---

## Question 17: HTTP/2

Какой веб-сервер был специально оптимизирован для HTTP/2?

A) Apache

B) Nginx

C) H2O

D) Lighttpd

---

## Question 18: Traefik

Для чего в основном используется Traefik?

A) Статические сайты

B) Reverse proxy для микросервисов (Docker/Kubernetes)

C) База данных

D) Email сервер

---

## Question 19: Nginx reload

Какая команда перезагружает конфигурацию Nginx без остановки сервера?

A) `nginx -s stop`

B) `nginx -s reload`

C) `nginx -restart`

D) `nginx -reconfig`

---

## Question 20: Выбор сервера

Какой сервер лучше использовать для shared hosting с .htaccess?

A) Nginx

B) Apache с LiteSpeed

C) OpenBSD httpd

D) H2O

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | CERN httpd был создан Tim Berners-Lee в 1990 году — первый веб-сервер |
| 2 | C | prefork создаёт отдельный процесс для каждого соединения |
| 3 | C | Nginx использует event loop с epoll (Linux) или kqueue (BSD) |
| 4 | B | Только Apache поддерживает .htaccess; Nginx использует централизованную конфигурацию |
| 5 | B | В Nginx виртуальные хосты настраиваются в блоках `server { }` |
| 6 | B | `proxy_pass` указывает URL backend сервера для проксирования |
| 7 | B | mod_rewrite — модуль для сложных URL преобразований |
| 8 | C | Рекомендуется устанавливать worker_processes равным числу CPU или auto |
| 9 | B | Caddy автоматически получает и обновляет сертификаты Let's Encrypt |
| 10 | C | OpenBSD httpd создан с приоритетом безопасности (privilege separation, chroot) |
| 11 | C | HTTPS использует порт 443 по умолчанию |
| 12 | B | upstream определяет группу серверов для load balancing |
| 13 | B | event MPM использует асинхронную обработку keep-alive соединений |
| 14 | B | Директива `expires` устанавливает время кэширования для браузера |
| 15 | B | Lighttpd отлично подходит для embedded систем и высоконагруженных статических сайтов |
| 16 | B | try_files последовательно проверяет существование файлов/директорий |
| 17 | C | H2O был создан специально с оптимизацией под HTTP/2 |
| 18 | B | Traefik — reverse proxy с автоматическим обнаружением сервисов в Docker/Kubernetes |
| 19 | B | `nginx -s reload` отправляет сигнал для перезагрузки конфигурации |
| 20 | B | Apache поддерживает .htaccess; LiteSpeed совместим с Apache и используется на хостингах |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы отлично разбираетесь в веб-серверах. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Углубите знания Nginx и Apache. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы о конфигурации серверов. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Попрактикуйтесь с настройкой Nginx и Apache на реальных примерах. |

---

