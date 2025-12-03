# Socket Activation - Quiz

Проверьте свои знания по теме "Socket Activation и эмуляция веб-сервера".

---

## Question 1: Концепция Socket Activation

Что происходит при использовании socket activation в systemd?

A) Демон сам открывает сокет при старте системы

B) systemd открывает сокет, демон запускается при первом соединении

C) Демон запускается при старте системы, но не слушает порт

D) Каждое соединение обрабатывается отдельным процессом systemd

---

## Question 2: Переменные окружения

Какие переменные окружения устанавливает systemd при socket activation?

A) SOCKET_FD и SOCKET_PID

B) LISTEN_FDS и LISTEN_PID

C) SD_SOCKET и SD_PID

D) SYSTEMD_SOCKET и SYSTEMD_FDS

---

## Question 3: Файловый дескриптор

С какого номера начинаются файловые дескрипторы, переданные от systemd?

A) 0

B) 1

C) 2

D) 3

---

## Question 4: Accept=yes vs Accept=no

Что происходит при настройке `Accept=yes` в socket unit?

A) systemd принимает соединения и запускает новый процесс для каждого

B) Один процесс демона обрабатывает все соединения

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

A) В stderr

B) В файл /tmp/response

C) В stdout

D) В переменную окружения RESPONSE

---

## Question 7: Преимущества socket activation

Какое из преимуществ НЕ относится к socket activation?

A) Быстрая загрузка системы

B) Экономия памяти

C) Автоматическое шифрование трафика

D) Отсутствие потери соединений при перезапуске демона

---

## Question 8: Python socket.fromfd()

Для чего используется `socket.fromfd()` в контексте socket activation?

A) Для создания нового сокета

B) Для получения socket-объекта из существующего файлового дескриптора

C) Для закрытия сокета

D) Для привязки сокета к порту

---

## Question 9: systemd ListenStream

Что означает параметр `ListenStream=8080` в socket unit?

A) UDP порт 8080

B) TCP порт 8080

C) Unix socket по пути 8080

D) Максимум 8080 соединений

---

## Question 10: inetd

Что такое inetd?

A) Современный init-демон для Linux

B) "Супердемон", который слушает порты и запускает сервисы по требованию

C) Интернет-демон для DNS

D) Демон для шифрования соединений

---

## Question 11: HTTP в shell

Какой символ используется для обозначения конца строки в HTTP протоколе?

A) `\n` (LF)

B) `\r\n` (CRLF)

C) `\r` (CR)

D) `\0` (NULL)

---

## Question 12: Отладка

Какая команда показывает все сокеты, управляемые systemd?

A) `systemctl list-units`

B) `systemctl list-sockets`

C) `ss -systemd`

D) `netstat --systemd`

---

## Question 13: xinetd

Чем xinetd отличается от классического inetd?

A) Работает только с UDP

B) Поддерживает более детальную конфигурацию и контроль доступа

C) Не поддерживает TCP

D) Работает только на BSD системах

---

## Question 14: Безопасность

Какой параметр в service unit предотвращает получение новых привилегий процессом?

A) ProtectSystem=strict

B) NoNewPrivileges=yes

C) PrivilegeEscalation=no

D) SecureBits=no-new

---

## Question 15: MIME типы

Какой MIME тип следует использовать для JSON ответа?

A) text/json

B) application/json

C) text/javascript

D) application/javascript

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | Socket activation: systemd открывает сокет при загрузке, демон запускается при первом подключении |
| 2 | B | LISTEN_FDS — количество переданных FD, LISTEN_PID — PID процесса-получателя |
| 3 | D | Переданные FD начинаются с 3 (SD_LISTEN_FDS_START), т.к. 0-2 это stdin/stdout/stderr |
| 4 | A | Accept=yes — systemd сам делает accept() и запускает новый процесс для каждого соединения |
| 5 | B | Символ @ означает шаблонный (template) unit для создания экземпляров |
| 6 | C | В inetd-style сервере stdout напрямую подключён к клиентскому соединению |
| 7 | C | Шифрование не связано с socket activation; оно обеспечивается TLS отдельно |
| 8 | B | socket.fromfd() создаёт Python socket объект из существующего файлового дескриптора |
| 9 | B | ListenStream создаёт TCP сокет (stream), ListenDatagram — UDP |
| 10 | B | inetd — Internet super-server daemon, слушает порты и запускает сервисы при подключении |
| 11 | B | HTTP использует CRLF (\r\n) для разделения строк |
| 12 | B | `systemctl list-sockets` показывает все socket units и их состояние |
| 13 | B | xinetd (extended inetd) добавляет ACL, лимиты соединений, детальное логирование |
| 14 | B | NoNewPrivileges=yes предотвращает escalation через setuid/setgid/capabilities |
| 15 | B | application/json — правильный MIME тип для JSON данных |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **14-15 правильных (90-100%)** | 🏆 Отлично! | Вы отлично понимаете socket activation. Переходите к веб-серверам. |
| **11-13 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Повторите работу с systemd units. |
| **7-10 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы о systemd и переменных окружения. |
| **Менее 7 правильных (<50%)** | 📚 Нужно повторить | Попрактикуйтесь с созданием socket units на реальной системе. |

---

