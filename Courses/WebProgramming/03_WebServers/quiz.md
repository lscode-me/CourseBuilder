# Web Servers - Quiz

Проверьте свои знания по теме "Веб-серверы: Apache, Nginx и другие".

---

## Question 1: История





Какой веб-сервер появился первым?

A) CERN httpd

B) IIS

C) Apache

D) Nginx

---

## Question 2: Apache MPM





Какой MPM в Apache создаёт новый процесс для каждого соединения?

A) async

B) worker

C) event

D) prefork

---

## Question 3: Nginx архитектура





Как Nginx обрабатывает множество соединений?

A) Использует event-driven модель с epoll/kqueue

B) Создаёт новый поток для каждого соединения

C) Использует только один поток для всех соединений

D) Создаёт новый процесс для каждого соединения

---

## Question 4: .htaccess





Какой веб-сервер поддерживает .htaccess файлы?

A) H2O

B) Apache

C) Nginx

D) OpenBSD httpd

---

## Question 5: Конфигурация Nginx





Как называется блок конфигурации виртуального хоста в Nginx?

A) site

B) host

C) server

D) VirtualHost

---

## Question 6: Reverse Proxy





Какая директива Nginx используется для проксирования запросов?

A) proxy_pass

B) forward_pass

C) backend_pass

D) upstream_pass

---

## Question 7: Apache модули





Какой модуль Apache используется для URL rewriting?

A) mod_route

B) mod_url

C) mod_redirect

D) mod_rewrite

---

## Question 8: Nginx worker_processes





Какое значение рекомендуется для `worker_processes` на сервере с 4 CPU?

A) 2

B) 8

C) 4 или auto

D) 1

---

## Question 9: Caddy





Какая главная особенность веб-сервера Caddy?

A) Автоматический HTTPS с Let's Encrypt

B) Встроенная база данных

C) Самый быстрый в мире

D) Совместимость с Apache

---

## Question 10: OpenBSD httpd





Что является главным приоритетом OpenBSD httpd?

A) Безопасность и простота

B) Совместимость с Apache

C) Поддержка всех протоколов

D) Максимальная производительность

---

## Question 11: SSL/TLS





Какой порт по умолчанию используется для HTTPS?

A) 443

B) 8080

C) 80

D) 8443

---

## Question 12: Nginx upstream





Для чего используется блок `upstream` в Nginx?

A) Для определения группы backend серверов

B) Для загрузки файлов

C) Для логирования

D) Для SSL настройки

---

## Question 13: Apache event MPM





Чем event MPM отличается от worker MPM?

A) Не поддерживает потоки

B) Эффективнее обрабатывает keep-alive соединения

C) Создаёт больше процессов

D) Использует больше памяти

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

A) Только базы данных

B) Встраиваемые системы и высоконагруженные статические сайты

C) Корпоративные приложения

D) Только Windows серверы

---

## Question 16: Nginx try_files





Что делает директива `try_files $uri $uri/ /index.html`?

A) Пробует найти файл, затем директорию, затем index.html

B) Переименовывает файл

C) Создаёт файл если не существует

D) Удаляет файл

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

A) Статические сайты

B) База данных

C) Reverse proxy для микросервисов (Docker/Kubernetes)

D) Email сервер

---

## Question 19: Nginx reload





Какая команда перезагружает конфигурацию Nginx без остановки сервера?

A) `nginx -s reload`

B) `nginx -reconfig`

C) `nginx -restart`

D) `nginx -s stop`

---

## Question 20: Выбор сервера





Какой сервер лучше использовать для shared hosting с .htaccess?

A) Nginx

B) OpenBSD httpd

C) H2O

D) Apache с LiteSpeed

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | CERN httpd был создан Tim Berners-Lee в 1990 году — первый веб-сервер |
| 2 | D | prefork создаёт отдельный процесс для каждого соединения |
| 3 | A | Nginx использует event loop с epoll (Linux) или kqueue (BSD) |
| 4 | B | Только Apache поддерживает .htaccess; Nginx использует централизованную конфигурацию |
| 5 | C | В Nginx виртуальные хосты настраиваются в блоках `server { }` |
| 6 | A | `proxy_pass` указывает URL backend сервера для проксирования |
| 7 | D | mod_rewrite — модуль для сложных URL преобразований |
| 8 | C | Рекомендуется устанавливать worker_processes равным числу CPU или auto |
| 9 | A | Caddy автоматически получает и обновляет сертификаты Let's Encrypt |
| 10 | A | OpenBSD httpd создан с приоритетом безопасности (privilege separation, chroot) |
| 11 | A | HTTPS использует порт 443 по умолчанию |
| 12 | A | upstream определяет группу серверов для load balancing |
| 13 | B | event MPM использует асинхронную обработку keep-alive соединений |
| 14 | C | Директива `expires` устанавливает время кэширования для браузера |
| 15 | B | Lighttpd отлично подходит для embedded систем и высоконагруженных статических сайтов |
| 16 | A | try_files последовательно проверяет существование файлов/директорий |
| 17 | A | H2O был создан специально с оптимизацией под HTTP/2 |
| 18 | C | Traefik — reverse proxy с автоматическим обнаружением сервисов в Docker/Kubernetes |
| 19 | A | `nginx -s reload` отправляет сигнал для перезагрузки конфигурации |
| 20 | D | Apache поддерживает .htaccess; LiteSpeed совместим с Apache и используется на хостингах |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы отлично разбираетесь в веб-серверах. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Углубите знания Nginx и Apache. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы о конфигурации серверов. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Попрактикуйтесь с настройкой Nginx и Apache на реальных примерах. |

---

