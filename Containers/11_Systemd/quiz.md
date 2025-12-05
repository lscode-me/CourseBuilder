# systemd-nspawn - Quiz

Проверьте свои знания по теме "systemd-контейнеры и машины".

---

## Question 1: Определение systemd-nspawn


Какой тип контейнеров создаёт systemd-nspawn?

A) Application containers — один процесс, без init системы

B) System containers — полная ОС с init системой

C) Виртуальные машины с полной эмуляцией hardware

D) Serverless функции

---

## Question 2: Сравнение с Docker


Какое главное отличие systemd-nspawn от Docker в плане образов?

A) systemd-nspawn работает с директориями, tar-архивами и raw образами вместо layered images

B) systemd-nspawn использует OverlayFS слои как Docker

C) systemd-nspawn использует OCI-совместимые образы

D) systemd-nspawn скачивает образы из Docker Hub

---

## Question 3: Запуск контейнера


Что делает флаг `-b` в команде `systemd-nspawn -b -D /var/lib/machines/debian`?

A) Включает bridge networking

B) Запускает контейнер в background

C) Создаёт bind mount

D) Запускает boot sequence — init систему контейнера

---

## Question 4: Директория машин


Какая директория является стандартным местом для хранения машин systemd-nspawn?

A) /etc/systemd/machines/

B) /var/lib/machines/

C) /home/machines/

D) /var/containers/

---

## Question 5: machinectl


Какая команда используется для просмотра списка запущенных машин?

A) `machinectl list`

B) `systemd-nspawn --list`

C) `nspawn-ctl ps`

D) `systemctl list-machines`

---

## Question 6: Сетевые режимы


Какой флаг создаёт virtual ethernet pair между хостом и контейнером?

A) `--private-network`

B) `--network-host`

C) `--network-veth`

D) `--network-bridge`

---

## Question 7: Конфигурационные файлы


Где должен располагаться файл конфигурации `.nspawn` для машины с именем "webserver"?

A) ~/.config/nspawn/webserver.nspawn

B) /etc/systemd/nspawn/webserver.nspawn

C) /etc/machines/webserver.conf

D) /var/lib/machines/webserver.nspawn

---

## Question 8: Capabilities


Какая команда запустит контейнер с дополнительной capability CAP_NET_ADMIN?

A) `systemd-nspawn --capability=CAP_NET_ADMIN -D /path`

B) `systemd-nspawn --grant=CAP_NET_ADMIN -D /path`

C) `systemd-nspawn --cap-add=NET_ADMIN -D /path`

D) `systemd-nspawn --add-cap=NET_ADMIN -D /path`

---

## Question 9: Bind mounts


Какой флаг используется для монтирования директории хоста в контейнер в режиме только для чтения?

A) `--mount-ro`

B) `--bind-readonly`

C) `--read-bind`

D) `--bind-ro`

---

## Question 10: Boot mode


Что произойдёт, если запустить `systemd-nspawn -D /var/lib/machines/debian` без флага `-b`?

A) Будет выдана ошибка "Boot flag required"

B) Запустится интерактивный shell вместо init системы

C) Контейнер не запустится

D) Контейнер запустится в background

---

## Question 11: Private network


Что делает флаг `--private-network`?

A) Отключает сеть полностью

B) Создаёт полностью изолированную сеть (только loopback)

C) Подключает контейнер к bridge

D) Создаёт veth pair к хосту

---

## Question 12: machinectl shell


Какая команда позволяет выполнить команду внутри запущенной машины "debian"?

A) `systemctl shell debian /bin/ls`

B) `machinectl run debian /bin/ls`

C) `machinectl shell debian /bin/ls`

D) `machinectl exec debian /bin/ls`

---

## Question 13: Volatile режим


Что означает опция `--volatile=yes`?

A) Root filesystem будет overlay — изменения не сохраняются

B) Контейнер будет автоматически удалён после остановки

C) Контейнер запустится в режиме высокой производительности

D) Логи будут храниться в памяти

---

## Question 14: Экспорт образа


Какая команда экспортирует машину "debian" в tar-архив?

A) `systemd-nspawn --export debian.tar.gz`

B) `machinectl export-tar debian debian.tar.gz`

C) `machinectl tar-export debian debian.tar.gz`

D) `nspawn export debian > debian.tar.gz`

---

## Question 15: systemd интеграция


Какой systemd unit отвечает за автозапуск машины "myserver"?

A) `systemd-nspawn-myserver.service`

B) `machine-myserver.service`

C) `systemd-nspawn@myserver.service`

D) `nspawn-myserver.service`

---

## Question 16: Journald


Какая команда показывает логи контейнера "debian" через journald?

A) `machinectl logs debian`

B) `journalctl -u debian`

C) `journalctl --container=debian`

D) `journalctl -M debian`

---

## Question 17: User namespaces


Какой флаг включает user namespace с автоматическим выбором UID/GID mapping?

A) `--map-users=auto`

B) `--userns=random`

C) `--user-namespace=auto`

D) `--private-users=pick`

---

## Question 18: .nspawn секции


Какая секция в .nspawn файле отвечает за настройку сети?

```ini
[???]
VirtualEthernet=yes
Bridge=br0
```

A) [Exec]

B) [Network]

C) [Networking]

D) [Files]

---

## Question 19: Клонирование машины


Какая команда создаст копию машины "debian" с именем "debian-test"?

A) `cp -r /var/lib/machines/debian /var/lib/machines/debian-test`

B) `machinectl clone debian debian-test`

C) `machinectl copy debian debian-test`

D) `machinectl duplicate debian debian-test`

---

## Question 20: Сравнение подходов


Для какого сценария systemd-nspawn подходит лучше, чем Docker?

A) Развёртывание в Kubernetes кластере

B) Запуск stateless приложений из Docker Hub

C) Микросервисная архитектура с сотнями контейнеров

D) Тестирование systemd unit-файлов и системного ПО

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | systemd-nspawn создаёт system containers с полной ОС и init системой (systemd), в отличие от application containers |
| 2 | A | systemd-nspawn работает напрямую с директориями, tar-архивами или raw disk images, без OCI layers и registry |
| 3 | D | Флаг `-b` (boot) запускает init систему контейнера, а не просто shell |
| 4 | B | `/var/lib/machines/` — стандартная директория для systemd-machined и systemd-nspawn |
| 5 | A | `machinectl list` показывает запущенные машины |
| 6 | C | `--network-veth` создаёт virtual ethernet pair: host0 в контейнере и ve-<name> на хосте |
| 7 | B | Файлы `.nspawn` располагаются в `/etc/systemd/nspawn/` |
| 8 | A | Правильный синтаксис: `--capability=CAP_NET_ADMIN` |
| 9 | D | `--bind-ro` создаёт read-only bind mount |
| 10 | B | Без `-b` запускается интерактивный shell (по умолчанию /bin/bash или /bin/sh) |
| 11 | B | `--private-network` создаёт изолированную сеть только с loopback интерфейсом |
| 12 | C | `machinectl shell <machine> <command>` выполняет команду в машине |
| 13 | A | `--volatile=yes` создаёт overlay над root filesystem, изменения не сохраняются после остановки |
| 14 | B | `machinectl export-tar` экспортирует машину в tar-архив |
| 15 | C | systemd использует template unit `systemd-nspawn@.service`, имя машины указывается после @ |
| 16 | D | `journalctl -M <machine>` показывает логи конкретной машины |
| 17 | D | `--private-users=pick` включает user namespace с автоматическим выбором свободного диапазона |
| 18 | B | Секция `[Network]` отвечает за сетевые настройки в .nspawn файлах |
| 19 | B | `machinectl clone` создаёт копию машины (образа) |
| 20 | D | systemd-nspawn идеален для тестирования systemd и системного ПО благодаря полной поддержке init системы |

---

## Scoring Guide

Подсчитайте количество правильных ответов:

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы отлично освоили systemd-nspawn. Готовы использовать его в production! |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Повторите разделы о сети и конфигурации. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Рекомендуется перечитать разделы о machinectl и .nspawn файлах. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Внимательно перечитайте лекцию, особенно базовые команды и концепции. |

---

