# Installation - Quiz

Проверьте свои знания по установке OpenBSD.

---

## Question 1: Типы образов


Какой образ следует использовать для установки OpenBSD на USB-накопитель?

A) miniroot74.img

B) cd74.iso

C) install74.img

D) install74.iso

---

## Question 2: Проверка образа


Какой файл содержит контрольные суммы для проверки целостности образов?

A) MD5SUMS

B) CHECKSUMS

C) SHA256

D) VERIFY

---

## Question 3: Выбор при загрузке


Какую опцию нужно выбрать для новой установки OpenBSD?

A) (A)utoinstall

B) (S)hell

C) (U)pgrade

D) (I)nstall

---

## Question 4: Разметка диска


Какой тип разметки рекомендуется для UEFI систем и дисков более 2TB?

A) Raw

B) OpenBSD area

C) GPT

D) MBR

---

## Question 5: Наборы файлов


Какой набор файлов содержит базовую систему OpenBSD?

A) core74.tgz

B) system74.tgz

C) bsd.tgz

D) base74.tgz

---

## Question 6: X Window System


Какие наборы нужно установить для графического интерфейса?

A) xbase74.tgz, xfont74.tgz, xserv74.tgz, xshare74.tgz

B) Только xbase74.tgz

C) desktop74.tgz

D) Только xserv74.tgz

---

## Question 7: Безопасность SSH


Какое значение PermitRootLogin рекомендуется для безопасности?

A) yes

B) forced-commands-only

C) no

D) without-password

---

## Question 8: doas


Какой файл нужно создать для настройки doas?

A) /usr/local/etc/doas.conf

B) /etc/doas.conf

C) /etc/doas/doas.conf

D) /etc/sudoers

---

## Question 9: Патчи безопасности


Какая команда устанавливает патчи безопасности в OpenBSD?

A) openbsd-update

B) syspatch

C) pkg_update

D) apt update

---

## Question 10: Зеркало пакетов


В каком файле указывается URL зеркала для pkg_add?

A) /etc/pkg.conf

B) /etc/apt/sources.list

C) /etc/mirrors.conf

D) /etc/installurl

---

## Question 11: Точки монтирования


Какой раздел содержит логи системы в стандартной схеме разметки?

A) /var

B) /tmp

C) /home

D) /usr

---

## Question 12: После установки


Какой man-page рекомендуется прочитать сразу после установки?

A) man intro

B) man firstboot

C) man install

D) man afterboot

---

## Question 13: Восстановление пароля root


Что нужно сделать, если забыт пароль root?

A) Переустановить систему

B) Восстановить невозможно

C) Загрузиться с установочного носителя и использовать shell

D) Отправить email разработчикам

---

## Question 14: Многопроцессорное ядро


Какой файл ядра используется для многопроцессорных систем?

A) bsd

B) bsd.multi

C) bsd.smp

D) bsd.mp

---

## Question 15: Группа wheel


Зачем добавлять пользователя в группу wheel?

A) Для доступа к сети

B) Для возможности использовать doas/sudo

C) Для монтирования USB устройств

D) Для доступа к графическому интерфейсу

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | install74.img — образ для записи на USB, install74.iso — для CD/виртуализации |
| 2 | C | SHA256 — файл с контрольными суммами SHA-256 для всех файлов |
| 3 | D | (I)nstall используется для новой установки системы |
| 4 | C | GPT (GUID Partition Table) рекомендуется для UEFI и больших дисков |
| 5 | D | base74.tgz содержит базовую систему OpenBSD |
| 6 | A | Для полноценного X Window нужны все четыре набора: xbase, xfont, xserv, xshare |
| 7 | C | PermitRootLogin no — запрещает прямой вход root, повышая безопасность |
| 8 | B | /etc/doas.conf — конфигурационный файл doas |
| 9 | B | syspatch — утилита для установки бинарных патчей безопасности |
| 10 | D | /etc/installurl содержит URL зеркала для pkg_add |
| 11 | A | /var содержит изменяемые данные: логи, почту, базы данных |
| 12 | D | man afterboot описывает все действия после установки |
| 13 | C | Загрузиться с установочного носителя, выбрать Shell, chroot и изменить пароль |
| 14 | D | bsd.mp — многопроцессорное ядро (multiprocessor) |
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

