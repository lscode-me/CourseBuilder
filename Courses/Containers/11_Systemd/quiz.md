# systemd-nspawn - Quiz

Проверьте свои знания по теме "systemd-контейнеры и машины".

---

## Question 1: Определение systemd-nspawn







Какой тип контейнеров создаёт systemd-nspawn?

A) System containers — полная ОС с init системой

B) Serverless функции

C) Виртуальные машины с полной эмуляцией hardware

D) Application containers — один процесс, без init системы

---

## Question 2: Сравнение с Docker







Какое главное отличие systemd-nspawn от Docker в плане образов?

A) systemd-nspawn использует OCI-совместимые образы

B) systemd-nspawn скачивает образы из Docker Hub

C) systemd-nspawn использует OverlayFS слои как Docker

D) systemd-nspawn работает с директориями, tar-архивами и raw образами вместо layered images

---

## Question 3: Запуск контейнера







Что делает флаг `-b` в команде `systemd-nspawn -b -D /var/lib/machines/debian`?

A) Запускает контейнер в background

B) Включает bridge networking

C) Создаёт bind mount

D) Запускает boot sequence — init систему контейнера

---

## Question 4: Директория машин







Какая директория является стандартным местом для хранения машин systemd-nspawn?

A) /etc/systemd/machines/

B) /home/machines/

C) /var/lib/machines/

D) /var/containers/

---

## Question 5: machinectl







Какая команда используется для просмотра списка запущенных машин?

A) `systemd-nspawn --list`

B) `nspawn-ctl ps`

C) `systemctl list-machines`

D) `machinectl list`

---

## Question 6: Сетевые режимы







Какой флаг создаёт virtual ethernet pair между хостом и контейнером?

A) `--private-network`

B) `--network-veth`

C) `--network-bridge`

D) `--network-host`

---

## Question 7: Конфигурационные файлы







Где должен располагаться файл конфигурации `.nspawn` для машины с именем "webserver"?

A) /etc/systemd/nspawn/webserver.nspawn

B) /var/lib/machines/webserver.nspawn

C) ~/.config/nspawn/webserver.nspawn

D) /etc/machines/webserver.conf

---

## Question 8: Capabilities







Какая команда запустит контейнер с дополнительной capability CAP_NET_ADMIN?

A) `systemd-nspawn --add-cap=NET_ADMIN -D /path`

B) `systemd-nspawn --grant=CAP_NET_ADMIN -D /path`

C) `systemd-nspawn --capability=CAP_NET_ADMIN -D /path`

D) `systemd-nspawn --cap-add=NET_ADMIN -D /path`

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

A) Запустится интерактивный shell вместо init системы

B) Контейнер не запустится

C) Контейнер запустится в background

D) Будет выдана ошибка "Boot flag required"

---

## Question 11: Private network







Что делает флаг `--private-network`?

A) Создаёт полностью изолированную сеть (только loopback)

B) Отключает сеть полностью

C) Создаёт veth pair к хосту

D) Подключает контейнер к bridge

---

## Question 12: machinectl shell







Какая команда позволяет выполнить команду внутри запущенной машины "debian"?

A) `machinectl exec debian /bin/ls`

B) `systemctl shell debian /bin/ls`

C) `machinectl run debian /bin/ls`

D) `machinectl shell debian /bin/ls`

---

## Question 13: Volatile режим







Что означает опция `--volatile=yes`?

A) Root filesystem будет overlay — изменения не сохраняются

B) Контейнер запустится в режиме высокой производительности

C) Логи будут храниться в памяти

D) Контейнер будет автоматически удалён после остановки

---

## Question 14: Экспорт образа







Какая команда экспортирует машину "debian" в tar-архив?

A) `nspawn export debian > debian.tar.gz`

B) `systemd-nspawn --export debian.tar.gz`

C) `machinectl tar-export debian debian.tar.gz`

D) `machinectl export-tar debian debian.tar.gz`

---

## Question 15: systemd интеграция







Какой systemd unit отвечает за автозапуск машины "myserver"?

A) `systemd-nspawn-myserver.service`

B) `nspawn-myserver.service`

C) `systemd-nspawn@myserver.service`

D) `machine-myserver.service`

---

## Question 16: Journald







Какая команда показывает логи контейнера "debian" через journald?

A) `journalctl --container=debian`

B) `journalctl -M debian`

C) `machinectl logs debian`

D) `journalctl -u debian`

---

## Question 17: User namespaces







Какой флаг включает user namespace с автоматическим выбором UID/GID mapping?

A) `--map-users=auto`

B) `--user-namespace=auto`

C) `--private-users=pick`

D) `--userns=random`

---

## Question 18: .nspawn секции







Какая секция в .nspawn файле отвечает за настройку сети?

```ini

[???]
VirtualEthernet=yes
Bridge=br0

```

A) [Files]

B) [Networking]

C) [Exec]

D) [Network]

---

## Question 19: Клонирование машины







Какая команда создаст копию машины "debian" с именем "debian-test"?

A) `cp -r /var/lib/machines/debian /var/lib/machines/debian-test`

B) `machinectl copy debian debian-test`

C) `machinectl clone debian debian-test`

D) `machinectl duplicate debian debian-test`

---

## Question 20: Сравнение подходов







Для какого сценария systemd-nspawn подходит лучше, чем Docker?

A) Тестирование systemd unit-файлов и системного ПО

B) Развёртывание в Kubernetes кластере

C) Запуск stateless приложений из Docker Hub

D) Микросервисная архитектура с сотнями контейнеров

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | systemd-nspawn создаёт system containers с полной ОС и init системой (systemd), в отличие от application containers |
| 2 | D | systemd-nspawn работает напрямую с директориями, tar-архивами или raw disk images, без OCI layers и registry |
| 3 | D | Флаг `-b` (boot) запускает init систему контейнера, а не просто shell |
| 4 | C | `/var/lib/machines/` — стандартная директория для systemd-machined и systemd-nspawn |
| 5 | D | `machinectl list` показывает запущенные машины |
| 6 | B | `--network-veth` создаёт virtual ethernet pair: host0 в контейнере и ve-<name> на хосте |
| 7 | A | Файлы `.nspawn` располагаются в `/etc/systemd/nspawn/` |
| 8 | C | Правильный синтаксис: `--capability=CAP_NET_ADMIN` |
| 9 | D | `--bind-ro` создаёт read-only bind mount |
| 10 | A | Без `-b` запускается интерактивный shell (по умолчанию /bin/bash или /bin/sh) |
| 11 | A | `--private-network` создаёт изолированную сеть только с loopback интерфейсом |
| 12 | D | `machinectl shell <machine> <command>` выполняет команду в машине |
| 13 | A | `--volatile=yes` создаёт overlay над root filesystem, изменения не сохраняются после остановки |
| 14 | D | `machinectl export-tar` экспортирует машину в tar-архив |
| 15 | C | systemd использует template unit `systemd-nspawn@.service`, имя машины указывается после @ |
| 16 | B | `journalctl -M <machine>` показывает логи конкретной машины |
| 17 | C | `--private-users=pick` включает user namespace с автоматическим выбором свободного диапазона |
| 18 | D | Секция `[Network]` отвечает за сетевые настройки в .nspawn файлах |
| 19 | C | `machinectl clone` создаёт копию машины (образа) |
| 20 | A | systemd-nspawn идеален для тестирования systemd и системного ПО благодаря полной поддержке init системы |

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



