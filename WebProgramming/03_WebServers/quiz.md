# Web Servers - Quiz

Проверьте свои знания по теме "Веб-серверы: Apache, Nginx и другие".

---

## Question 1: История


Какой веб-сервер появился первым?

A) Nginx

B) CERN httpd

C) IIS

D) Apache

---

## Question 2: Apache MPM


Какой MPM в Apache создаёт новый процесс для каждого соединения?

A) async

B) worker

C) prefork

D) event

---

## Question 3: Nginx архитектура


Как Nginx обрабатывает множество соединений?

A) Использует event-driven модель с epoll/kqueue

B) Использует только один поток для всех соединений

C) Создаёт новый процесс для каждого соединения

D) Создаёт новый поток для каждого соединения

---

## Question 4: .htaccess


Какой веб-сервер поддерживает .htaccess файлы?

A) Nginx

B) OpenBSD httpd

C) Apache

D) H2O

---

## Question 5: Конфигурация Nginx


Как называется блок конфигурации виртуального хоста в Nginx?

A) VirtualHost

B) site

C) server

D) host

---

## Question 6: Reverse Proxy


Какая директива Nginx используется для проксирования запросов?

A) upstream_pass

B) forward_pass

C) proxy_pass

D) backend_pass

---

## Question 7: Apache модули


Какой модуль Apache используется для URL rewriting?

A) mod_route

B) mod_rewrite

C) mod_url

D) mod_redirect

---

## Question 8: Nginx worker_processes


Какое значение рекомендуется для `worker_processes` на сервере с 4 CPU?

A) 8

B) 2

C) 1

D) 4 или auto

---

## Question 9: Caddy


Какая главная особенность веб-сервера Caddy?

A) Встроенная база данных

B) Самый быстрый в мире

C) Совместимость с Apache

D) Автоматический HTTPS с Let's Encrypt

---

## Question 10: OpenBSD httpd


Что является главным приоритетом OpenBSD httpd?

A) Совместимость с Apache

B) Максимальная производительность

C) Поддержка всех протоколов

D) Безопасность и простота

---

## Question 11: SSL/TLS


Какой порт по умолчанию используется для HTTPS?

A) 8443

B) 80

C) 8080

D) 443

---

## Question 12: Nginx upstream


Для чего используется блок `upstream` в Nginx?

A) Для SSL настройки

B) Для загрузки файлов

C) Для логирования

D) Для определения группы backend серверов

---

## Question 13: Apache event MPM


Чем event MPM отличается от worker MPM?

A) Не поддерживает потоки

B) Использует больше памяти

C) Эффективнее обрабатывает keep-alive соединения

D) Создаёт больше процессов

---

## Question 14: Nginx статические файлы


Какая директива Nginx используется для кэширования статических файлов?

A) cache

B) file_cache

C) expires

D) static_cache

---

## Question 15: Lighttpd


Для каких сценариев лучше всего подходит Lighttpd?

A) Встраиваемые системы и высоконагруженные статические сайты

B) Только базы данных

C) Только Windows серверы

D) Корпоративные приложения

---

## Question 16: Nginx try_files


Что делает директива `try_files $uri $uri/ /index.html`?

A) Переименовывает файл

B) Создаёт файл если не существует

C) Удаляет файл

D) Пробует найти файл, затем директорию, затем index.html

---

## Question 17: HTTP/2


Какой веб-сервер был специально оптимизирован для HTTP/2?

A) H2O

B) Apache

C) Nginx

D) Lighttpd

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

A) `nginx -s reload`

B) `nginx -restart`

C) `nginx -s stop`

D) `nginx -reconfig`

---

## Question 20: Выбор сервера


Какой сервер лучше использовать для shared hosting с .htaccess?

A) Apache с LiteSpeed

B) H2O

C) Nginx

D) OpenBSD httpd

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | CERN httpd был создан Tim Berners-Lee в 1990 году — первый веб-сервер |
| 2 | C | prefork создаёт отдельный процесс для каждого соединения |
| 3 | A | Nginx использует event loop с epoll (Linux) или kqueue (BSD) |
| 4 | C | Только Apache поддерживает .htaccess; Nginx использует централизованную конфигурацию |
| 5 | C | В Nginx виртуальные хосты настраиваются в блоках `server { }` |
| 6 | C | `proxy_pass` указывает URL backend сервера для проксирования |
| 7 | B | mod_rewrite — модуль для сложных URL преобразований |
| 8 | D | Рекомендуется устанавливать worker_processes равным числу CPU или auto |
| 9 | D | Caddy автоматически получает и обновляет сертификаты Let's Encrypt |
| 10 | D | OpenBSD httpd создан с приоритетом безопасности (privilege separation, chroot) |
| 11 | D | HTTPS использует порт 443 по умолчанию |
| 12 | D | upstream определяет группу серверов для load balancing |
| 13 | C | event MPM использует асинхронную обработку keep-alive соединений |
| 14 | C | Директива `expires` устанавливает время кэширования для браузера |
| 15 | A | Lighttpd отлично подходит для embedded систем и высоконагруженных статических сайтов |
| 16 | D | try_files последовательно проверяет существование файлов/директорий |
| 17 | A | H2O был создан специально с оптимизацией под HTTP/2 |
| 18 | A | Traefik — reverse proxy с автоматическим обнаружением сервисов в Docker/Kubernetes |
| 19 | A | `nginx -s reload` отправляет сигнал для перезагрузки конфигурации |
| 20 | A | Apache поддерживает .htaccess; LiteSpeed совместим с Apache и используется на хостингах |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы отлично разбираетесь в веб-серверах. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Углубите знания Nginx и Apache. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы о конфигурации серверов. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Попрактикуйтесь с настройкой Nginx и Apache на реальных примерах. |

---

