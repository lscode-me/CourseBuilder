# Services - Quiz

Проверьте свои знания по системным службам OpenBSD.

---

## Question 1: Управление службами







Какая команда используется для управления службами в OpenBSD?

A) initctl

B) systemctl

C) rcctl

D) service

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

A) /usr/lib/systemd/

B) /etc/rc.d/

C) /etc/init.d/

D) /etc/services.d/

---

## Question 5: Статус службы







Какая команда проверяет, запущена ли служба?

A) rcctl check sshd

B) rcctl running sshd

C) rcctl is-active sshd

D) rcctl status sshd

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

B) services_order

C) daemon_order

D) pkg_scripts

---

## Question 9: Перезапуск службы







Какая команда перезапускает службу?

A) rcctl restart sshd

B) rcctl reload sshd

C) rcctl reset sshd

D) rcctl reboot sshd

---

## Question 10: rc.d скрипт







Какая переменная указывает путь к исполняемому файлу в rc.d скрипте?

A) daemon

B) program

C) binary

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

A) Для DNS

B) Для инициализации сети

C) Для запуска сетевых служб по требованию

D) Для мониторинга интернета

---

## Question 17: unbound






Что такое unbound в OpenBSD?

A) SSH сервер

B) Почтовый сервер

C) Кэширующий DNS резолвер

D) Веб-сервер

---

## Question 18: smtpd






Какой почтовый сервер встроен в OpenBSD?

A) exim

B) postfix

C) sendmail

D) OpenSMTPD

---

## Question 19: rcctl restart






Что делает rcctl restart sshd?

A) Обновляет конфигурацию

B) Удаляет службу

C) Перезапускает службу sshd

D) Перезагружает систему

---

## Question 20: /etc/rc.conf.local






Для чего используется /etc/rc.conf.local?

A) Для настройки локальной сети

B) Для локальных пользователей

C) Для локальных настроек служб (переопределение rc.conf)

D) Для локализации системы

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | rcctl — стандартная утилита управления службами в OpenBSD |
| 2 | B | rcctl enable добавляет службу в автозапуск |
| 3 | C | /etc/rc.conf.local — файл для локальных настроек (не редактируйте rc.conf!) |
| 4 | B | /etc/rc.d/ содержит скрипты управления службами |
| 5 | A | rcctl check проверяет, запущена ли служба |
| 6 | C | rcctl ls started показывает все запущенные службы |
| 7 | B | rcctl set service flags "..." устанавливает флаги |
| 8 | D | pkg_scripts определяет порядок запуска пакетных служб |
| 9 | A | rcctl restart перезапускает службу (stop + start) |
| 10 | A | daemon — путь к исполняемому файлу в rc.d скрипте |
| 11 | D | daemon_user — пользователь для запуска службы |
| 12 | C | rcctl disable убирает службу из автозапуска |
| 13 | A | rcctl reload отправляет SIGHUP для перечитывания конфигурации |
| 14 | D | httpd — простой встроенный веб-сервер OpenBSD |
| 15 | D | /var/log/daemon содержит логи демонов |
| 16 | C | inetd запускает сетевые службы по запросу (on-demand) |
| 17 | C | unbound — встроенный кэширующий DNS резолвер |
| 18 | D | OpenSMTPD — почтовый сервер, разработанный проектом OpenBSD |
| 19 | C | rcctl restart останавливает и запускает службу заново |
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

