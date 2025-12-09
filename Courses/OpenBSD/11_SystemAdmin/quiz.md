# System Administration - Quiz

Проверьте свои знания по системному администрированию OpenBSD.

---

## Question 1: Мониторинг







Какая утилита предоставляет интерактивный мониторинг системы?

A) htop

B) monitor

C) watch

D) systat

---

## Question 2: Логи







В каком файле находятся общие системные сообщения?

A) /var/log/kern.log

B) /var/log/syslog

C) /var/log/messages

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

A) tar

B) rsync

C) backup

D) dump

---

## Question 6: cron формат







Что означает запись "0 3 * * *" в crontab?

A) Каждые 3 часа

B) В 3:00 каждый день

C) Каждую третью минуту

D) Третьего числа каждого месяца

---

## Question 7: Системные скрипты







Какой файл выполняется ежедневно?

A) /var/cron/daily

B) /etc/cron.daily

C) /etc/daily

D) /etc/daily.sh

---

## Question 8: Обновление системы







Какая утилита обновляет систему между релизами?

A) openbsd-upgrade

B) upgrade

C) sysupgrade

D) release-upgrade

---

## Question 9: Информация о системе







Какая команда показывает сообщения загрузки ядра?

A) syslog

B) bootlog

C) kernlog

D) dmesg

---

## Question 10: Дисковое пространство







Какая команда показывает использование дисков?

A) du -h

B) df -h

C) disk -h

D) space -h

---

## Question 11: Сетевая статистика







Какая команда показывает сетевые соединения?

A) netstat -an

B) ipstat

C) ss -an

D) connections

---

## Question 12: Периодические скрипты







Куда добавлять локальные ежедневные задачи?

A) /etc/daily/local

B) /etc/local.daily

C) /etc/daily.local

D) /etc/cron.d/daily

---

## Question 13: Датчики







Какая команда показывает температуру и другие датчики?

A) sensors

B) hwmon

C) temp

D) sysctl hw.sensors

---

## Question 14: Просмотр crontab







Какая команда показывает текущий crontab?

A) crontab -l

B) show cron

C) cron -l

D) cat /etc/crontab

---

## Question 15: Проверка файловой системы







Какая команда проверяет целостность файловой системы?

A) fscheck

B) diskcheck

C) fsck

D) checkfs

---

## Question 16: sysupgrade






Что делает sysupgrade?

A) Обновляет систему до новой версии

B) Обновляет только ядро

C) Обновляет пакеты

D) Обновляет порты

---

## Question 17: daily/weekly/monthly






Где настраиваются автоматические скрипты обслуживания?

A) /usr/local/etc/maintenance

B) /var/maintenance/

C) /etc/cron.d/

D) /etc/daily.local, /etc/weekly.local, /etc/monthly.local

---

## Question 18: newsyslog






Для чего используется newsyslog?

A) Для отправки логов

B) Для создания новых логов

C) Для ротации лог-файлов

D) Для чтения системных логов

---

## Question 19: sendbug






Для чего используется sendbug?

A) Для отладки

B) Для отправки отчётов об ошибках разработчикам OpenBSD

C) Для тестирования

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
| 1 | D | systat — интерактивная утилита мониторинга с различными представлениями |
| 2 | C | /var/log/messages — основной файл системных сообщений |
| 3 | A | syspatch устанавливает бинарные патчи безопасности |
| 4 | C | newsyslog — утилита ротации логов в BSD системах |
| 5 | D | dump создаёт полный бэкап файловой системы на уровне блоков |
| 6 | B | 0 минут, 3 часа, любой день = в 3:00 каждый день |
| 7 | C | /etc/daily выполняется ежедневно через cron |
| 8 | C | sysupgrade обновляет OpenBSD между релизами |
| 9 | D | dmesg показывает сообщения ядра, включая загрузку |
| 10 | B | df -h показывает использование дисков в читаемом формате |
| 11 | A | netstat -an показывает все соединения в числовом формате |
| 12 | C | /etc/daily.local — место для локальных ежедневных задач |
| 13 | D | sysctl hw.sensors показывает данные датчиков |
| 14 | A | crontab -l показывает crontab текущего пользователя |
| 15 | C | fsck проверяет и восстанавливает файловую систему |
| 16 | A | sysupgrade обновляет систему до новой версии OpenBSD |
| 17 | D | *.local файлы в /etc для локальных настроек обслуживания |
| 18 | C | newsyslog ротирует и сжимает лог-файлы |
| 19 | B | sendbug отправляет отчёты об ошибках разработчикам |
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

