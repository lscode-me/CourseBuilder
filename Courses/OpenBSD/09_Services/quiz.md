# Services - Quiz

Проверьте свои знания по системным службам OpenBSD.

---

## Question 1: Управление службами





Какая команда используется для управления службами в OpenBSD?

A) service

B) rcctl

C) systemctl

D) initctl

---

## Question 2: Включение службы





Какая команда включает автозапуск службы?

A) rcctl add sshd

B) rcctl enable sshd

C) rcctl start sshd

D) rcctl autostart sshd

---

## Question 3: Конфигурация служб





В каком файле хранятся локальные настройки служб?

A) /etc/services.conf

B) /etc/init.conf

C) /etc/rc.conf.local

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

A) rcctl check sshd

B) rcctl status sshd

C) rcctl running sshd

D) rcctl is-active sshd

---

## Question 6: Список служб





Какая команда показывает все запущенные службы?

A) rcctl ps

B) rcctl show active

C) rcctl ls started

D) rcctl list running

---

## Question 7: Флаги службы





Как установить флаги запуска для службы?

A) rcctl -f httpd "-f /etc/httpd.conf"

B) rcctl set httpd flags "-f /etc/httpd.conf"

C) rcctl flags httpd "-f /etc/httpd.conf"

D) rcctl config httpd flags="-f /etc/httpd.conf"

---

## Question 8: Пакетные службы





Какая переменная определяет порядок запуска пакетных служб?

A) rc_packages

B) daemon_order

C) pkg_scripts

D) services_order

---

## Question 9: Перезапуск службы





Какая команда перезапускает службу?

A) rcctl reset sshd

B) rcctl reload sshd

C) rcctl reboot sshd

D) rcctl restart sshd

---

## Question 10: rc.d скрипт





Какая переменная указывает путь к исполняемому файлу в rc.d скрипте?

A) program

B) binary

C) daemon

D) executable

---

## Question 11: Пользователь службы





Какая переменная определяет пользователя для запуска службы?

A) user

B) run_as

C) daemon_user

D) service_user

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

A) rcctl reload nginx

B) rcctl reconfig nginx

C) rcctl restart nginx

D) rcctl refresh nginx

---

## Question 14: Встроенный веб-сервер





Как называется встроенный веб-сервер OpenBSD?

A) apache

B) lighttpd

C) nginx

D) httpd

---

## Question 15: Логи служб





В каком файле искать общие логи демонов?

A) /var/log/services

B) /var/log/rc.log

C) /var/log/syslog

D) /var/log/daemon

---

## Question 16: inetd




Для чего используется inetd?

A) Для инициализации сети

B) Для запуска сетевых служб по требованию

C) Для DNS

D) Для мониторинга интернета

---

## Question 17: unbound




Что такое unbound в OpenBSD?

A) SSH сервер

B) Кэширующий DNS резолвер

C) Веб-сервер

D) Почтовый сервер

---

## Question 18: smtpd




Какой почтовый сервер встроен в OpenBSD?

A) OpenSMTPD

B) exim

C) sendmail

D) postfix

---

## Question 19: rcctl restart




Что делает rcctl restart sshd?

A) Обновляет конфигурацию

B) Перезапускает службу sshd

C) Перезагружает систему

D) Удаляет службу

---

## Question 20: /etc/rc.conf.local




Для чего используется /etc/rc.conf.local?

A) Для локальных пользователей

B) Для локализации системы

C) Для локальных настроек служб (переопределение rc.conf)

D) Для настройки локальной сети

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | rcctl — стандартная утилита управления службами в OpenBSD |
| 2 | B | rcctl enable добавляет службу в автозапуск |
| 3 | C | /etc/rc.conf.local — файл для локальных настроек (не редактируйте rc.conf!) |
| 4 | D | /etc/rc.d/ содержит скрипты управления службами |
| 5 | A | rcctl check проверяет, запущена ли служба |
| 6 | C | rcctl ls started показывает все запущенные службы |
| 7 | B | rcctl set service flags "..." устанавливает флаги |
| 8 | C | pkg_scripts определяет порядок запуска пакетных служб |
| 9 | D | rcctl restart перезапускает службу (stop + start) |
| 10 | C | daemon — путь к исполняемому файлу в rc.d скрипте |
| 11 | C | daemon_user — пользователь для запуска службы |
| 12 | C | rcctl disable убирает службу из автозапуска |
| 13 | A | rcctl reload отправляет SIGHUP для перечитывания конфигурации |
| 14 | D | httpd — простой встроенный веб-сервер OpenBSD |
| 15 | D | /var/log/daemon содержит логи демонов |
| 16 | B | inetd запускает сетевые службы по запросу (on-demand) |
| 17 | B | unbound — встроенный кэширующий DNS резолвер |
| 18 | A | OpenSMTPD — почтовый сервер, разработанный проектом OpenBSD |
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

