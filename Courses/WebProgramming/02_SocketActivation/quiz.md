# Socket Activation - Quiz

Проверьте свои знания по теме "Socket Activation и эмуляция веб-сервера".

---

## Question 1: Концепция Socket Activation







Что происходит при использовании socket activation в systemd?

A) Каждое соединение обрабатывается отдельным процессом systemd

B) Демон запускается при старте системы, но не слушает порт

C) systemd открывает сокет, демон запускается при первом соединении

D) Демон сам открывает сокет при старте системы

---

## Question 2: Переменные окружения







Какие переменные окружения устанавливает systemd при socket activation?

A) LISTEN_FDS и LISTEN_PID

B) SOCKET_FD и SOCKET_PID

C) SYSTEMD_SOCKET и SYSTEMD_FDS

D) SD_SOCKET и SD_PID

---

## Question 3: Файловый дескриптор







С какого номера начинаются файловые дескрипторы, переданные от systemd?

A) 1

B) 0

C) 2

D) 3

---

## Question 4: Accept=yes vs Accept=no







Что происходит при настройке `Accept=yes` в socket unit?

A) Один процесс демона обрабатывает все соединения

B) systemd принимает соединения и запускает новый процесс для каждого

C) Соединения ставятся в очередь до запуска демона

D) systemd отклоняет все соединения кроме первого

---

## Question 5: Имя service unit







Как должен называться service unit для socket с Accept=yes?

A) myservice.service

B) myservice@.service

C) myservice-instance.service

D) myservice.socket.service

---

## Question 6: Shell HTTP сервер







В shell-скрипте для inetd-style сервера, куда нужно писать HTTP ответ?

A) В файл /tmp/response

B) В переменную окружения RESPONSE

C) В stdout

D) В stderr

---

## Question 7: Преимущества socket activation







Какое из преимуществ НЕ относится к socket activation?

A) Экономия памяти

B) Быстрая загрузка системы

C) Автоматическое шифрование трафика

D) Отсутствие потери соединений при перезапуске демона

---

## Question 8: Python socket.fromfd()







Для чего используется `socket.fromfd()` в контексте socket activation?

A) Для закрытия сокета

B) Для создания нового сокета

C) Для привязки сокета к порту

D) Для получения socket-объекта из существующего файлового дескриптора

---

## Question 9: systemd ListenStream







Что означает параметр `ListenStream=8080` в socket unit?

A) TCP порт 8080

B) Максимум 8080 соединений

C) UDP порт 8080

D) Unix socket по пути 8080

---

## Question 10: inetd







Что такое inetd?

A) Демон для шифрования соединений

B) "Супердемон", который слушает порты и запускает сервисы по требованию

C) Современный init-демон для Linux

D) Интернет-демон для DNS

---

## Question 11: HTTP в shell







Какой символ используется для обозначения конца строки в HTTP протоколе?

A) `\r` (CR)

B) `\n` (LF)

C) `\r\n` (CRLF)

D) `\0` (NULL)

---

## Question 12: Отладка







Какая команда показывает все сокеты, управляемые systemd?

A) `systemctl list-sockets`

B) `ss -systemd`

C) `netstat --systemd`

D) `systemctl list-units`

---

## Question 13: xinetd







Чем xinetd отличается от классического inetd?

A) Не поддерживает TCP

B) Поддерживает более детальную конфигурацию и контроль доступа

C) Работает только на BSD системах

D) Работает только с UDP

---

## Question 14: Безопасность







Какой параметр в service unit предотвращает получение новых привилегий процессом?

A) ProtectSystem=strict

B) PrivilegeEscalation=no

C) NoNewPrivileges=yes

D) SecureBits=no-new

---

## Question 15: MIME типы







Какой MIME тип следует использовать для JSON ответа?

A) text/json

B) application/json

C) application/javascript

D) text/javascript

---

## Question 16: ListenDatagram






Что создаёт параметр `ListenDatagram=8080` в socket unit?

A) Raw socket

B) UDP сокет

C) Unix socket

D) TCP сокет

---

## Question 17: SD_LISTEN_FDS_START






Чему равна константа SD_LISTEN_FDS_START?

A) 0

B) 2

C) 3

D) 1

---

## Question 18: ProtectSystem






Что делает параметр `ProtectSystem=strict` в service unit?

A) Запрещает сетевой доступ

B) Шифрует файловую систему

C) Делает /usr и /etc доступными только для чтения

D) Ограничивает CPU

---

## Question 19: Connection: close






Что означает заголовок `Connection: close` в HTTP ответе?

A) Соединение заблокировано

B) Соединение будет закрыто после ответа

C) Соединение шифруется

D) Ошибка соединения

---

## Question 20: netcat -e






Что делает флаг `-e` в `nc -l -p 8080 -e ./script.sh`?

A) Устанавливает таймаут

B) Логирует ошибки

C) Выполняет скрипт для каждого соединения

D) Шифрует соединение

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | Socket activation: systemd открывает сокет при загрузке, демон запускается при первом подключении |
| 2 | A | LISTEN_FDS — количество переданных FD, LISTEN_PID — PID процесса-получателя |
| 3 | D | Переданные FD начинаются с 3 (SD_LISTEN_FDS_START), т.к. 0-2 это stdin/stdout/stderr |
| 4 | B | Accept=yes — systemd сам делает accept() и запускает новый процесс для каждого соединения |
| 5 | B | Символ @ означает шаблонный (template) unit для создания экземпляров |
| 6 | C | В inetd-style сервере stdout напрямую подключён к клиентскому соединению |
| 7 | C | Шифрование не связано с socket activation; оно обеспечивается TLS отдельно |
| 8 | D | socket.fromfd() создаёт Python socket объект из существующего файлового дескриптора |
| 9 | A | ListenStream создаёт TCP сокет (stream), ListenDatagram — UDP |
| 10 | B | inetd — Internet super-server daemon, слушает порты и запускает сервисы при подключении |
| 11 | C | HTTP использует CRLF (\r\n) для разделения строк |
| 12 | A | `systemctl list-sockets` показывает все socket units и их состояние |
| 13 | B | xinetd (extended inetd) добавляет ACL, лимиты соединений, детальное логирование |
| 14 | C | NoNewPrivileges=yes предотвращает escalation через setuid/setgid/capabilities |
| 15 | B | application/json — правильный MIME тип для JSON данных |
| 16 | B | ListenDatagram создаёт UDP сокет, ListenStream — TCP |
| 17 | C | SD_LISTEN_FDS_START = 3, т.к. 0-2 зарезервированы для stdin/stdout/stderr |
| 18 | C | ProtectSystem=strict делает /usr, /boot, /etc read-only |
| 19 | B | Connection: close означает закрытие соединения после передачи ответа |
| 20 | C | -e (execute) запускает указанную программу для обработки соединения |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **14-15 правильных (90-100%)** | 🏆 Отлично! | Вы отлично понимаете socket activation. Переходите к веб-серверам. |
| **11-13 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Повторите работу с systemd units. |
| **7-10 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы о systemd и переменных окружения. |
| **Менее 7 правильных (<50%)** | 📚 Нужно повторить | Попрактикуйтесь с созданием socket units на реальной системе. |

---

