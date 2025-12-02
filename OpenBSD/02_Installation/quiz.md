# Installation - Quiz

Проверьте свои знания по установке OpenBSD.

---

## Question 1: Типы образов

Какой образ следует использовать для установки OpenBSD на USB-накопитель?

A) install74.iso

B) install74.img

C) miniroot74.img

D) cd74.iso

---

## Question 2: Проверка образа

Какой файл содержит контрольные суммы для проверки целостности образов?

A) MD5SUMS

B) SHA256

C) CHECKSUMS

D) VERIFY

---

## Question 3: Выбор при загрузке

Какую опцию нужно выбрать для новой установки OpenBSD?

A) (U)pgrade

B) (I)nstall

C) (A)utoinstall

D) (S)hell

---

## Question 4: Разметка диска

Какой тип разметки рекомендуется для UEFI систем и дисков более 2TB?

A) MBR

B) GPT

C) OpenBSD area

D) Raw

---

## Question 5: Наборы файлов

Какой набор файлов содержит базовую систему OpenBSD?

A) bsd.tgz

B) base74.tgz

C) system74.tgz

D) core74.tgz

---

## Question 6: X Window System

Какие наборы нужно установить для графического интерфейса?

A) Только xbase74.tgz

B) xbase74.tgz, xfont74.tgz, xserv74.tgz, xshare74.tgz

C) Только xserv74.tgz

D) desktop74.tgz

---

## Question 7: Безопасность SSH

Какое значение PermitRootLogin рекомендуется для безопасности?

A) yes

B) no

C) without-password

D) forced-commands-only

---

## Question 8: doas

Какой файл нужно создать для настройки doas?

A) /etc/sudoers

B) /etc/doas.conf

C) /etc/doas/doas.conf

D) /usr/local/etc/doas.conf

---

## Question 9: Патчи безопасности

Какая команда устанавливает патчи безопасности в OpenBSD?

A) pkg_update

B) apt update

C) syspatch

D) openbsd-update

---

## Question 10: Зеркало пакетов

В каком файле указывается URL зеркала для pkg_add?

A) /etc/pkg.conf

B) /etc/installurl

C) /etc/apt/sources.list

D) /etc/mirrors.conf

---

## Question 11: Точки монтирования

Какой раздел содержит логи системы в стандартной схеме разметки?

A) /usr

B) /home

C) /var

D) /tmp

---

## Question 12: После установки

Какой man-page рекомендуется прочитать сразу после установки?

A) man intro

B) man afterboot

C) man install

D) man firstboot

---

## Question 13: Восстановление пароля root

Что нужно сделать, если забыт пароль root?

A) Переустановить систему

B) Загрузиться с установочного носителя и использовать shell

C) Отправить email разработчикам

D) Восстановить невозможно

---

## Question 14: Многопроцессорное ядро

Какой файл ядра используется для многопроцессорных систем?

A) bsd

B) bsd.mp

C) bsd.smp

D) bsd.multi

---

## Question 15: Группа wheel

Зачем добавлять пользователя в группу wheel?

A) Для доступа к графическому интерфейсу

B) Для возможности использовать doas/sudo

C) Для доступа к сети

D) Для монтирования USB устройств

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | install74.img — образ для записи на USB, install74.iso — для CD/виртуализации |
| 2 | B | SHA256 — файл с контрольными суммами SHA-256 для всех файлов |
| 3 | B | (I)nstall используется для новой установки системы |
| 4 | B | GPT (GUID Partition Table) рекомендуется для UEFI и больших дисков |
| 5 | B | base74.tgz содержит базовую систему OpenBSD |
| 6 | B | Для полноценного X Window нужны все четыре набора: xbase, xfont, xserv, xshare |
| 7 | B | PermitRootLogin no — запрещает прямой вход root, повышая безопасность |
| 8 | B | /etc/doas.conf — конфигурационный файл doas |
| 9 | C | syspatch — утилита для установки бинарных патчей безопасности |
| 10 | B | /etc/installurl содержит URL зеркала для pkg_add |
| 11 | C | /var содержит изменяемые данные: логи, почту, базы данных |
| 12 | B | man afterboot описывает все действия после установки |
| 13 | B | Загрузиться с установочного носителя, выбрать Shell, chroot и изменить пароль |
| 14 | B | bsd.mp — многопроцессорное ядро (multiprocessor) |
| 15 | B | Группа wheel позволяет использовать doas для выполнения команд от root |

---

## Scoring Guide

Подсчитайте количество правильных ответов:

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **14-15 правильных (93-100%)** | 🏆 Отлично! | Вы готовы к установке OpenBSD. |
| **11-13 правильных (73-87%)** | ✅ Хорошо | Повторите разделы о разметке диска и безопасности. |
| **8-10 правильных (53-67%)** | ⚠️ Удовлетворительно | Рекомендуется перечитать лекцию перед установкой. |
| **Менее 8 правильных (<53%)** | 📚 Нужно повторить | Внимательно изучите материал и попробуйте ещё раз. |

---

