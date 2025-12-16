# System Administration - Quiz

Проверьте свои знания по системному администрированию OpenBSD.

---

## Question 1: Мониторинг

Какая утилита предоставляет интерактивный мониторинг системы?

A) systat

B) htop

C) monitor

D) watch

---

## Question 2: Логи

В каком файле находятся общие системные сообщения?

A) /var/log/messages

B) /var/log/syslog

C) /var/log/kern.log

D) /var/log/system

---

## Question 3: Патчи безопасности

Какая команда устанавливает патчи безопасности?

A) syspatch

B) pkg_add -u

C) openbsd-update

D) security-update

---

## Question 4: Ротация логов

Какая утилита управляет ротацией логов в OpenBSD?

A) rotatelog

B) syslog-rotate

C) newsyslog

D) logrotate

---

## Question 5: Резервное копирование

Какая команда создаёт полный бэкап файловой системы?

A) dump

B) backup

C) rsync

D) tar

---

## Question 6: cron формат

Что означает запись "0 3 * * *" в crontab?

A) В 3:00 каждый день

B) Каждые 3 часа

C) Каждую третью минуту

D) Третьего числа каждого месяца

---

## Question 7: Системные скрипты

Какой файл выполняется ежедневно?

A) /etc/cron.daily

B) /var/cron/daily

C) /etc/daily.sh

D) /etc/daily

---

## Question 8: Обновление системы

Какая утилита обновляет систему между релизами?

A) sysupgrade

B) openbsd-upgrade

C) release-upgrade

D) upgrade

---

## Question 9: Информация о системе

Какая команда показывает сообщения загрузки ядра?

A) kernlog

B) syslog

C) dmesg

D) bootlog

---

## Question 10: Дисковое пространство

Какая команда показывает использование дисков?

A) disk -h

B) du -h

C) space -h

D) df -h

---

## Question 11: Сетевая статистика

Какая команда показывает сетевые соединения?

A) ss -an

B) netstat -an

C) ipstat

D) connections

---

## Question 12: Периодические скрипты

Куда добавлять локальные ежедневные задачи?

A) /etc/daily.local

B) /etc/daily/local

C) /etc/local.daily

D) /etc/cron.d/daily

---

## Question 13: Датчики

Какая команда показывает температуру и другие датчики?

A) hwmon

B) sensors

C) temp

D) sysctl hw.sensors

---

## Question 14: Просмотр crontab

Какая команда показывает текущий crontab?

A) crontab -l

B) cron -l

C) cat /etc/crontab

D) show cron

---

## Question 15: Проверка файловой системы

Какая команда проверяет целостность файловой системы?

A) fsck

B) checkfs

C) fscheck

D) diskcheck

---

## Question 16: sysupgrade

Что делает sysupgrade?

A) Обновляет только ядро

B) Обновляет систему до новой версии

C) Обновляет пакеты

D) Обновляет порты

---

## Question 17: daily/weekly/monthly

Где настраиваются автоматические скрипты обслуживания?

A) /etc/daily.local, /etc/weekly.local, /etc/monthly.local

B) /var/maintenance/

C) /usr/local/etc/maintenance

D) /etc/cron.d/

---

## Question 18: newsyslog

Для чего используется newsyslog?

A) Для ротации лог-файлов

B) Для чтения системных логов

C) Для отправки логов

D) Для создания новых логов

---

## Question 19: sendbug

Для чего используется sendbug?

A) Для отладки

B) Для тестирования

C) Для отправки отчётов об ошибках разработчикам OpenBSD

D) Для поиска багов

---

## Question 20: fw_update

Что делает команда fw_update?

A) Обновляет Wi-Fi драйвер

B) Загружает и устанавливает firmware для устройств

C) Обновляет firewall правила

D) Обновляет прошивку BIOS

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | systat — интерактивная утилита мониторинга с различными представлениями |
| 2 | A | /var/log/messages — основной файл системных сообщений |
| 3 | A | syspatch устанавливает бинарные патчи безопасности |
| 4 | C | newsyslog — утилита ротации логов в BSD системах |
| 5 | A | dump создаёт полный бэкап файловой системы на уровне блоков |
| 6 | A | 0 минут, 3 часа, любой день = в 3:00 каждый день |
| 7 | D | /etc/daily выполняется ежедневно через cron |
| 8 | A | sysupgrade обновляет OpenBSD между релизами |
| 9 | C | dmesg показывает сообщения ядра, включая загрузку |
| 10 | D | df -h показывает использование дисков в читаемом формате |
| 11 | B | netstat -an показывает все соединения в числовом формате |
| 12 | A | /etc/daily.local — место для локальных ежедневных задач |
| 13 | D | sysctl hw.sensors показывает данные датчиков |
| 14 | A | crontab -l показывает crontab текущего пользователя |
| 15 | A | fsck проверяет и восстанавливает файловую систему |
| 16 | B | sysupgrade обновляет систему до новой версии OpenBSD |
| 17 | A | *.local файлы в /etc для локальных настроек обслуживания |
| 18 | A | newsyslog ротирует и сжимает лог-файлы |
| 19 | C | sendbug отправляет отчёты об ошибках разработчикам |
| 20 | B | fw_update загружает firmware для устройств (Wi-Fi, GPU и т.д.) |

---

## Scoring Guide

Подсчитайте количество правильных ответов:

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **14-15 правильных (93-100%)** | 🏆 Отлично! | Вы готовы администрировать OpenBSD. |
| **11-13 правильных (73-87%)** | ✅ Хорошо | Повторите cron и резервное копирование. |
| **8-10 правильных (53-67%)** | ⚠️ Удовлетворительно | Рекомендуется больше практики с systat и логами. |
| **Менее 8 правильных (<53%)** | 📚 Нужно повторить | Изучите man syspatch и man cron. |

---

