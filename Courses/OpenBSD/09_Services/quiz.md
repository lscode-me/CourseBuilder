# Services - Quiz

Проверьте свои знания по системным службам OpenBSD.

---

## Question 1: Управление службами

Какая команда используется для управления службами в OpenBSD?

A) systemctl

B) initctl

C) rcctl

D) service

---

## Question 2: Включение службы

Какая команда включает автозапуск службы?

A) rcctl add sshd

B) rcctl autostart sshd

C) rcctl enable sshd

D) rcctl start sshd

---

## Question 3: Конфигурация служб

В каком файле хранятся локальные настройки служб?

A) /etc/rc.conf.local

B) /etc/services.conf

C) /etc/init.conf

D) /etc/rc.conf

---

## Question 4: Каталог rc.d

Где находятся скрипты управления службами?

A) /etc/services.d/

B) /usr/lib/systemd/

C) /etc/init.d/

D) /etc/rc.d/

---

## Question 5: Статус службы

Какая команда проверяет, запущена ли служба?

A) rcctl status sshd

B) rcctl running sshd

C) rcctl is-active sshd

D) rcctl check sshd

---

## Question 6: Список служб

Какая команда показывает все запущенные службы?

A) rcctl ps

B) rcctl ls started

C) rcctl list running

D) rcctl show active

---

## Question 7: Флаги службы

Как установить флаги запуска для службы?

A) rcctl config httpd flags="-f /etc/httpd.conf"

B) rcctl flags httpd "-f /etc/httpd.conf"

C) rcctl set httpd flags "-f /etc/httpd.conf"

D) rcctl -f httpd "-f /etc/httpd.conf"

---

## Question 8: Пакетные службы

Какая переменная определяет порядок запуска пакетных служб?

A) rc_packages

B) pkg_scripts

C) daemon_order

D) services_order

---

## Question 9: Перезапуск службы

Какая команда перезапускает службу?

A) rcctl reset sshd

B) rcctl restart sshd

C) rcctl reboot sshd

D) rcctl reload sshd

---

## Question 10: rc.d скрипт

Какая переменная указывает путь к исполняемому файлу в rc.d скрипте?

A) binary

B) daemon

C) program

D) executable

---

## Question 11: Пользователь службы

Какая переменная определяет пользователя для запуска службы?

A) run_as

B) user

C) service_user

D) daemon_user

---

## Question 12: Отключение службы

Как отключить службу (убрать из автозапуска)?

A) rcctl delete sshd

B) rcctl remove sshd

C) rcctl disable sshd

D) rcctl stop sshd

---

## Question 13: Перечитывание конфигурации

Какая команда перечитывает конфигурацию без перезапуска?

A) rcctl restart nginx

B) rcctl refresh nginx

C) rcctl reconfig nginx

D) rcctl reload nginx

---

## Question 14: Встроенный веб-сервер

Как называется встроенный веб-сервер OpenBSD?

A) nginx

B) lighttpd

C) httpd

D) apache

---

## Question 15: Логи служб

В каком файле искать общие логи демонов?

A) /var/log/daemon

B) /var/log/services

C) /var/log/syslog

D) /var/log/rc.log

---

## Question 16: inetd

Для чего используется inetd?

A) Для DNS

B) Для запуска сетевых служб по требованию

C) Для инициализации сети

D) Для мониторинга интернета

---

## Question 17: unbound

Что такое unbound в OpenBSD?

A) Почтовый сервер

B) Кэширующий DNS резолвер

C) Веб-сервер

D) SSH сервер

---

## Question 18: smtpd

Какой почтовый сервер встроен в OpenBSD?

A) postfix

B) OpenSMTPD

C) exim

D) sendmail

---

## Question 19: rcctl restart

Что делает rcctl restart sshd?

A) Обновляет конфигурацию

B) Перезапускает службу sshd

C) Удаляет службу

D) Перезагружает систему

---

## Question 20: /etc/rc.conf.local

Для чего используется /etc/rc.conf.local?

A) Для локальных пользователей

B) Для настройки локальной сети

C) Для локальных настроек служб (переопределение rc.conf)

D) Для локализации системы

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | rcctl — стандартная утилита управления службами в OpenBSD |
| 2 | C | rcctl enable добавляет службу в автозапуск |
| 3 | A | /etc/rc.conf.local — файл для локальных настроек (не редактируйте rc.conf!) |
| 4 | D | /etc/rc.d/ содержит скрипты управления службами |
| 5 | D | rcctl check проверяет, запущена ли служба |
| 6 | B | rcctl ls started показывает все запущенные службы |
| 7 | C | rcctl set service flags "..." устанавливает флаги |
| 8 | B | pkg_scripts определяет порядок запуска пакетных служб |
| 9 | B | rcctl restart перезапускает службу (stop + start) |
| 10 | B | daemon — путь к исполняемому файлу в rc.d скрипте |
| 11 | D | daemon_user — пользователь для запуска службы |
| 12 | C | rcctl disable убирает службу из автозапуска |
| 13 | D | rcctl reload отправляет SIGHUP для перечитывания конфигурации |
| 14 | C | httpd — простой встроенный веб-сервер OpenBSD |
| 15 | A | /var/log/daemon содержит логи демонов |
| 16 | B | inetd запускает сетевые службы по запросу (on-demand) |
| 17 | B | unbound — встроенный кэширующий DNS резолвер |
| 18 | B | OpenSMTPD — почтовый сервер, разработанный проектом OpenBSD |
| 19 | B | rcctl restart останавливает и запускает службу заново |
| 20 | C | rc.conf.local содержит локальные настройки, переопределяющие rc.conf |

---

## Scoring Guide

Подсчитайте количество правильных ответов:

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **14-15 правильных (93-100%)** | 🏆 Отлично! | Вы хорошо знаете систему служб OpenBSD. |
| **11-13 правильных (73-87%)** | ✅ Хорошо | Повторите rc.d скрипты и pkg_scripts. |
| **8-10 правильных (53-67%)** | ⚠️ Удовлетворительно | Больше практики с rcctl. |
| **Менее 8 правильных (<53%)** | 📚 Нужно повторить | Изучите man rcctl и man rc.d. |

---

