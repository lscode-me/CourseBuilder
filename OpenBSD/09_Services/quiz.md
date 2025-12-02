# Services - Quiz

Проверьте свои знания по системным службам OpenBSD.

---

## Question 1: Управление службами

Какая команда используется для управления службами в OpenBSD?

A) systemctl

B) service

C) rcctl

D) initctl

---

## Question 2: Включение службы

Какая команда включает автозапуск службы?

A) rcctl start sshd

B) rcctl enable sshd

C) rcctl autostart sshd

D) rcctl add sshd

---

## Question 3: Конфигурация служб

В каком файле хранятся локальные настройки служб?

A) /etc/rc.conf

B) /etc/rc.conf.local

C) /etc/services.conf

D) /etc/init.conf

---

## Question 4: Каталог rc.d

Где находятся скрипты управления службами?

A) /etc/init.d/

B) /etc/rc.d/

C) /usr/lib/systemd/

D) /etc/services.d/

---

## Question 5: Статус службы

Какая команда проверяет, запущена ли служба?

A) rcctl status sshd

B) rcctl check sshd

C) rcctl running sshd

D) rcctl is-active sshd

---

## Question 6: Список служб

Какая команда показывает все запущенные службы?

A) rcctl list running

B) rcctl ls started

C) rcctl show active

D) rcctl ps

---

## Question 7: Флаги службы

Как установить флаги запуска для службы?

A) rcctl flags httpd "-f /etc/httpd.conf"

B) rcctl set httpd flags "-f /etc/httpd.conf"

C) rcctl config httpd flags="-f /etc/httpd.conf"

D) rcctl -f httpd "-f /etc/httpd.conf"

---

## Question 8: Пакетные службы

Какая переменная определяет порядок запуска пакетных служб?

A) services_order

B) pkg_scripts

C) daemon_order

D) rc_packages

---

## Question 9: Перезапуск службы

Какая команда перезапускает службу?

A) rcctl reload sshd

B) rcctl restart sshd

C) rcctl reboot sshd

D) rcctl reset sshd

---

## Question 10: rc.d скрипт

Какая переменная указывает путь к исполняемому файлу в rc.d скрипте?

A) executable

B) binary

C) daemon

D) program

---

## Question 11: Пользователь службы

Какая переменная определяет пользователя для запуска службы?

A) run_as

B) user

C) daemon_user

D) service_user

---

## Question 12: Отключение службы

Как отключить службу (убрать из автозапуска)?

A) rcctl stop sshd

B) rcctl disable sshd

C) rcctl remove sshd

D) rcctl delete sshd

---

## Question 13: Перечитывание конфигурации

Какая команда перечитывает конфигурацию без перезапуска?

A) rcctl restart nginx

B) rcctl reload nginx

C) rcctl refresh nginx

D) rcctl reconfig nginx

---

## Question 14: Встроенный веб-сервер

Как называется встроенный веб-сервер OpenBSD?

A) apache

B) nginx

C) httpd

D) lighttpd

---

## Question 15: Логи служб

В каком файле искать общие логи демонов?

A) /var/log/syslog

B) /var/log/daemon

C) /var/log/services

D) /var/log/rc.log

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | rcctl — стандартная утилита управления службами в OpenBSD |
| 2 | B | rcctl enable добавляет службу в автозапуск |
| 3 | B | /etc/rc.conf.local — файл для локальных настроек (не редактируйте rc.conf!) |
| 4 | B | /etc/rc.d/ содержит скрипты управления службами |
| 5 | B | rcctl check проверяет, запущена ли служба |
| 6 | B | rcctl ls started показывает все запущенные службы |
| 7 | B | rcctl set service flags "..." устанавливает флаги |
| 8 | B | pkg_scripts определяет порядок запуска пакетных служб |
| 9 | B | rcctl restart перезапускает службу (stop + start) |
| 10 | C | daemon — путь к исполняемому файлу в rc.d скрипте |
| 11 | C | daemon_user — пользователь для запуска службы |
| 12 | B | rcctl disable убирает службу из автозапуска |
| 13 | B | rcctl reload отправляет SIGHUP для перечитывания конфигурации |
| 14 | C | httpd — простой встроенный веб-сервер OpenBSD |
| 15 | B | /var/log/daemon содержит логи демонов |

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

