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

B) rcctl autostart sshd

C) rcctl start sshd

D) rcctl enable sshd

---

## Question 3: Конфигурация служб


В каком файле хранятся локальные настройки служб?

A) /etc/init.conf

B) /etc/rc.conf.local

C) /etc/rc.conf

D) /etc/services.conf

---

## Question 4: Каталог rc.d


Где находятся скрипты управления службами?

A) /etc/services.d/

B) /etc/rc.d/

C) /usr/lib/systemd/

D) /etc/init.d/

---

## Question 5: Статус службы


Какая команда проверяет, запущена ли служба?

A) rcctl running sshd

B) rcctl check sshd

C) rcctl is-active sshd

D) rcctl status sshd

---

## Question 6: Список служб


Какая команда показывает все запущенные службы?

A) rcctl show active

B) rcctl list running

C) rcctl ls started

D) rcctl ps

---

## Question 7: Флаги службы


Как установить флаги запуска для службы?

A) rcctl config httpd flags="-f /etc/httpd.conf"

B) rcctl flags httpd "-f /etc/httpd.conf"

C) rcctl -f httpd "-f /etc/httpd.conf"

D) rcctl set httpd flags "-f /etc/httpd.conf"

---

## Question 8: Пакетные службы


Какая переменная определяет порядок запуска пакетных служб?

A) services_order

B) rc_packages

C) daemon_order

D) pkg_scripts

---

## Question 9: Перезапуск службы


Какая команда перезапускает службу?

A) rcctl reload sshd

B) rcctl reset sshd

C) rcctl reboot sshd

D) rcctl restart sshd

---

## Question 10: rc.d скрипт


Какая переменная указывает путь к исполняемому файлу в rc.d скрипте?

A) binary

B) executable

C) daemon

D) program

---

## Question 11: Пользователь службы


Какая переменная определяет пользователя для запуска службы?

A) run_as

B) daemon_user

C) service_user

D) user

---

## Question 12: Отключение службы


Как отключить службу (убрать из автозапуска)?

A) rcctl delete sshd

B) rcctl remove sshd

C) rcctl stop sshd

D) rcctl disable sshd

---

## Question 13: Перечитывание конфигурации


Какая команда перечитывает конфигурацию без перезапуска?

A) rcctl restart nginx

B) rcctl reconfig nginx

C) rcctl refresh nginx

D) rcctl reload nginx

---

## Question 14: Встроенный веб-сервер


Как называется встроенный веб-сервер OpenBSD?

A) lighttpd

B) apache

C) httpd

D) nginx

---

## Question 15: Логи служб


В каком файле искать общие логи демонов?

A) /var/log/services

B) /var/log/syslog

C) /var/log/rc.log

D) /var/log/daemon

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | rcctl — стандартная утилита управления службами в OpenBSD |
| 2 | D | rcctl enable добавляет службу в автозапуск |
| 3 | B | /etc/rc.conf.local — файл для локальных настроек (не редактируйте rc.conf!) |
| 4 | B | /etc/rc.d/ содержит скрипты управления службами |
| 5 | B | rcctl check проверяет, запущена ли служба |
| 6 | C | rcctl ls started показывает все запущенные службы |
| 7 | D | rcctl set service flags "..." устанавливает флаги |
| 8 | D | pkg_scripts определяет порядок запуска пакетных служб |
| 9 | D | rcctl restart перезапускает службу (stop + start) |
| 10 | C | daemon — путь к исполняемому файлу в rc.d скрипте |
| 11 | B | daemon_user — пользователь для запуска службы |
| 12 | D | rcctl disable убирает службу из автозапуска |
| 13 | D | rcctl reload отправляет SIGHUP для перечитывания конфигурации |
| 14 | C | httpd — простой встроенный веб-сервер OpenBSD |
| 15 | D | /var/log/daemon содержит логи демонов |

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

