# Socket Activation - Quiz

Проверьте свои знания по теме "Socket Activation и эмуляция веб-сервера".

---

## Question 1: Концепция Socket Activation


Что происходит при использовании socket activation в systemd?

A) Каждое соединение обрабатывается отдельным процессом systemd

B) Демон запускается при старте системы, но не слушает порт

C) Демон сам открывает сокет при старте системы

D) systemd открывает сокет, демон запускается при первом соединении

---

## Question 2: Переменные окружения


Какие переменные окружения устанавливает systemd при socket activation?

A) SD_SOCKET и SD_PID

B) LISTEN_FDS и LISTEN_PID

C) SYSTEMD_SOCKET и SYSTEMD_FDS

D) SOCKET_FD и SOCKET_PID

---

## Question 3: Файловый дескриптор


С какого номера начинаются файловые дескрипторы, переданные от systemd?

A) 1

B) 2

C) 0

D) 3

---

## Question 4: Accept=yes vs Accept=no


Что происходит при настройке `Accept=yes` в socket unit?

A) systemd принимает соединения и запускает новый процесс для каждого

B) systemd отклоняет все соединения кроме первого

C) Соединения ставятся в очередь до запуска демона

D) Один процесс демона обрабатывает все соединения

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

B) В stdout

C) В переменную окружения RESPONSE

D) В файл /tmp/response

---

## Question 7: Преимущества socket activation


Какое из преимуществ НЕ относится к socket activation?

A) Быстрая загрузка системы

B) Автоматическое шифрование трафика

C) Экономия памяти

D) Отсутствие потери соединений при перезапуске демона

---

## Question 8: Python socket.fromfd()


Для чего используется `socket.fromfd()` в контексте socket activation?

A) Для закрытия сокета

B) Для привязки сокета к порту

C) Для создания нового сокета

D) Для получения socket-объекта из существующего файлового дескриптора

---

## Question 9: systemd ListenStream


Что означает параметр `ListenStream=8080` в socket unit?

A) Максимум 8080 соединений

B) TCP порт 8080

C) Unix socket по пути 8080

D) UDP порт 8080

---

## Question 10: inetd


Что такое inetd?

A) Современный init-демон для Linux

B) Демон для шифрования соединений

C) Интернет-демон для DNS

D) "Супердемон", который слушает порты и запускает сервисы по требованию

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

A) `ss -systemd`

B) `systemctl list-sockets`

C) `netstat --systemd`

D) `systemctl list-units`

---

## Question 13: xinetd


Чем xinetd отличается от классического inetd?

A) Работает только на BSD системах

B) Поддерживает более детальную конфигурацию и контроль доступа

C) Работает только с UDP

D) Не поддерживает TCP

---

## Question 14: Безопасность


Какой параметр в service unit предотвращает получение новых привилегий процессом?

A) PrivilegeEscalation=no

B) NoNewPrivileges=yes

C) SecureBits=no-new

D) ProtectSystem=strict

---

## Question 15: MIME типы


Какой MIME тип следует использовать для JSON ответа?

A) application/json

B) text/json

C) text/javascript

D) application/javascript

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | D | Socket activation: systemd открывает сокет при загрузке, демон запускается при первом подключении |
| 2 | B | LISTEN_FDS — количество переданных FD, LISTEN_PID — PID процесса-получателя |
| 3 | D | Переданные FD начинаются с 3 (SD_LISTEN_FDS_START), т.к. 0-2 это stdin/stdout/stderr |
| 4 | A | Accept=yes — systemd сам делает accept() и запускает новый процесс для каждого соединения |
| 5 | B | Символ @ означает шаблонный (template) unit для создания экземпляров |
| 6 | B | В inetd-style сервере stdout напрямую подключён к клиентскому соединению |
| 7 | B | Шифрование не связано с socket activation; оно обеспечивается TLS отдельно |
| 8 | D | socket.fromfd() создаёт Python socket объект из существующего файлового дескриптора |
| 9 | B | ListenStream создаёт TCP сокет (stream), ListenDatagram — UDP |
| 10 | D | inetd — Internet super-server daemon, слушает порты и запускает сервисы при подключении |
| 11 | B | HTTP использует CRLF (\r\n) для разделения строк |
| 12 | B | `systemctl list-sockets` показывает все socket units и их состояние |
| 13 | B | xinetd (extended inetd) добавляет ACL, лимиты соединений, детальное логирование |
| 14 | B | NoNewPrivileges=yes предотвращает escalation через setuid/setgid/capabilities |
| 15 | A | application/json — правильный MIME тип для JSON данных |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **14-15 правильных (90-100%)** | 🏆 Отлично! | Вы отлично понимаете socket activation. Переходите к веб-серверам. |
| **11-13 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Повторите работу с systemd units. |
| **7-10 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы о systemd и переменных окружения. |
| **Менее 7 правильных (<50%)** | 📚 Нужно повторить | Попрактикуйтесь с созданием socket units на реальной системе. |

---

