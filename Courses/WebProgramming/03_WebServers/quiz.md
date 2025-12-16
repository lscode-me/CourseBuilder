# Web Servers - Quiz

Проверьте свои знания по теме "Веб-серверы: Apache, Nginx и другие".

---

## Question 1: История

Какой веб-сервер появился первым?

A) Nginx

B) IIS

C) CERN httpd

D) Apache

---

## Question 2: Apache MPM

Какой MPM в Apache создаёт новый процесс для каждого соединения?

A) event

B) worker

C) async

D) prefork

---

## Question 3: Nginx архитектура

Как Nginx обрабатывает множество соединений?

A) Создаёт новый процесс для каждого соединения

B) Создаёт новый поток для каждого соединения

C) Использует только один поток для всех соединений

D) Использует event-driven модель с epoll/kqueue

---

## Question 4: .htaccess

Какой веб-сервер поддерживает .htaccess файлы?

A) Apache

B) Nginx

C) H2O

D) OpenBSD httpd

---

## Question 5: Конфигурация Nginx

Как называется блок конфигурации виртуального хоста в Nginx?

A) site

B) server

C) VirtualHost

D) host

---

## Question 6: Reverse Proxy

Какая директива Nginx используется для проксирования запросов?

A) backend_pass

B) proxy_pass

C) upstream_pass

D) forward_pass

---

## Question 7: Apache модули

Какой модуль Apache используется для URL rewriting?

A) mod_redirect

B) mod_route

C) mod_rewrite

D) mod_url

---

## Question 8: Nginx worker_processes

Какое значение рекомендуется для `worker_processes` на сервере с 4 CPU?

A) 8

B) 4 или auto

C) 2

D) 1

---

## Question 9: Caddy

Какая главная особенность веб-сервера Caddy?

A) Встроенная база данных

B) Совместимость с Apache

C) Автоматический HTTPS с Let's Encrypt

D) Самый быстрый в мире

---

## Question 10: OpenBSD httpd

Что является главным приоритетом OpenBSD httpd?

A) Максимальная производительность

B) Поддержка всех протоколов

C) Безопасность и простота

D) Совместимость с Apache

---

## Question 11: SSL/TLS

Какой порт по умолчанию используется для HTTPS?

A) 80

B) 443

C) 8443

D) 8080

---

## Question 12: Nginx upstream

Для чего используется блок `upstream` в Nginx?

A) Для загрузки файлов

B) Для SSL настройки

C) Для логирования

D) Для определения группы backend серверов

---

## Question 13: Apache event MPM

Чем event MPM отличается от worker MPM?

A) Не поддерживает потоки

B) Использует больше памяти

C) Создаёт больше процессов

D) Эффективнее обрабатывает keep-alive соединения

---

## Question 14: Nginx статические файлы

Какая директива Nginx используется для кэширования статических файлов?

A) static_cache

B) expires

C) file_cache

D) cache

---

## Question 15: Lighttpd

Для каких сценариев лучше всего подходит Lighttpd?

A) Корпоративные приложения

B) Только Windows серверы

C) Только базы данных

D) Встраиваемые системы и высоконагруженные статические сайты

---

## Question 16: Nginx try_files

Что делает директива `try_files $uri $uri/ /index.html`?

A) Пробует найти файл, затем директорию, затем index.html

B) Удаляет файл

C) Переименовывает файл

D) Создаёт файл если не существует

---

## Question 17: HTTP/2

Какой веб-сервер был специально оптимизирован для HTTP/2?

A) H2O

B) Nginx

C) Lighttpd

D) Apache

---

## Question 18: Traefik

Для чего в основном используется Traefik?

A) Reverse proxy для микросервисов (Docker/Kubernetes)

B) Статические сайты

C) Email сервер

D) База данных

---

## Question 19: Nginx reload

Какая команда перезагружает конфигурацию Nginx без остановки сервера?

A) `nginx -restart`

B) `nginx -s stop`

C) `nginx -reconfig`

D) `nginx -s reload`

---

## Question 20: Выбор сервера

Какой сервер лучше использовать для shared hosting с .htaccess?

A) Nginx

B) H2O

C) Apache с LiteSpeed

D) OpenBSD httpd

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | CERN httpd был создан Tim Berners-Lee в 1990 году — первый веб-сервер |
| 2 | D | prefork создаёт отдельный процесс для каждого соединения |
| 3 | D | Nginx использует event loop с epoll (Linux) или kqueue (BSD) |
| 4 | A | Только Apache поддерживает .htaccess; Nginx использует централизованную конфигурацию |
| 5 | B | В Nginx виртуальные хосты настраиваются в блоках `server { }` |
| 6 | B | `proxy_pass` указывает URL backend сервера для проксирования |
| 7 | C | mod_rewrite — модуль для сложных URL преобразований |
| 8 | B | Рекомендуется устанавливать worker_processes равным числу CPU или auto |
| 9 | C | Caddy автоматически получает и обновляет сертификаты Let's Encrypt |
| 10 | C | OpenBSD httpd создан с приоритетом безопасности (privilege separation, chroot) |
| 11 | B | HTTPS использует порт 443 по умолчанию |
| 12 | D | upstream определяет группу серверов для load balancing |
| 13 | D | event MPM использует асинхронную обработку keep-alive соединений |
| 14 | B | Директива `expires` устанавливает время кэширования для браузера |
| 15 | D | Lighttpd отлично подходит для embedded систем и высоконагруженных статических сайтов |
| 16 | A | try_files последовательно проверяет существование файлов/директорий |
| 17 | A | H2O был создан специально с оптимизацией под HTTP/2 |
| 18 | A | Traefik — reverse proxy с автоматическим обнаружением сервисов в Docker/Kubernetes |
| 19 | D | `nginx -s reload` отправляет сигнал для перезагрузки конфигурации |
| 20 | C | Apache поддерживает .htaccess; LiteSpeed совместим с Apache и используется на хостингах |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы отлично разбираетесь в веб-серверах. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Углубите знания Nginx и Apache. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы о конфигурации серверов. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Попрактикуйтесь с настройкой Nginx и Apache на реальных примерах. |

---

