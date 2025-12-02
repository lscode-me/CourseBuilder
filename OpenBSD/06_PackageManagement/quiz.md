# Package Management - Quiz

Проверьте свои знания по управлению пакетами в OpenBSD.

---

## Question 1: Файл зеркала

В каком файле указывается URL зеркала для pkg_add?

A) /etc/pkg.conf

B) /etc/installurl

C) /etc/apt/sources.list

D) /etc/mirrors.conf

---

## Question 2: Установка пакета

Какая команда устанавливает пакет в OpenBSD?

A) apt-get install

B) yum install

C) pkg_add

D) pkg install

---

## Question 3: Обновление пакетов

Какая команда обновляет все установленные пакеты?

A) pkg_update -a

B) pkg_add -u

C) pkg_upgrade

D) pkg_add --upgrade

---

## Question 4: Flavors

Что такое flavors в системе пакетов OpenBSD?

A) Разные версии пакета

B) Варианты пакета с разными опциями сборки

C) Цветовые схемы интерфейса

D) Типы лицензий

---

## Question 5: Список пакетов

Какая команда показывает список установленных пакетов?

A) pkg_list

B) pkg_info

C) dpkg -l

D) rpm -qa

---

## Question 6: Удаление пакета

Какая команда удаляет пакет?

A) pkg_remove

B) pkg_delete

C) pkg_del

D) pkg_uninstall

---

## Question 7: Поиск пакета

Какой флаг pkg_info используется для поиска пакетов в репозитории?

A) -s

B) -Q

C) -f

D) -l

---

## Question 8: Файлы пакета

Какой флаг pkg_info показывает файлы, установленные пакетом?

A) -f

B) -L

C) -l

D) -F

---

## Question 9: Ports

Где находится дерево портов в OpenBSD?

A) /opt/ports

B) /usr/ports

C) /var/ports

D) /ports

---

## Question 10: Сборка порта

Какая команда собирает и устанавливает порт?

A) make all

B) make build install

C) make install clean

D) ./configure && make && make install

---

## Question 11: pkg_add или ports

Когда следует использовать ports вместо pkg_add?

A) Всегда, ports быстрее

B) Когда нужны специфические опции сборки

C) Для системных утилит

D) Ports устарел, всегда используйте pkg_add

---

## Question 12: Зависимости

Какая команда показывает, от каких пакетов зависит указанный?

A) pkg_info -R

B) pkg_info -f

C) pkg_info -d

D) pkg_depends

---

## Question 13: Orphan пакеты

Какая команда удаляет пакеты без зависящих от них?

A) pkg_delete -o

B) pkg_delete -a

C) pkg_autoremove

D) pkg_clean

---

## Question 14: Поиск файла

Какая команда находит пакет по установленному файлу?

A) pkg_info -f /path

B) pkg_info -E /path

C) pkg_which /path

D) which -p /path

---

## Question 15: PKG_PATH

Для чего используется переменная PKG_PATH?

A) Путь к установленным пакетам

B) URL репозитория пакетов

C) Кэш загруженных пакетов

D) Логи установки

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | /etc/installurl — стандартный файл для указания зеркала в OpenBSD |
| 2 | C | pkg_add — команда установки пакетов в OpenBSD |
| 3 | B | pkg_add -u обновляет все установленные пакеты |
| 4 | B | Flavors — варианты пакета с разными опциями (например, с GUI или без) |
| 5 | B | pkg_info без аргументов показывает список установленных пакетов |
| 6 | B | pkg_delete удаляет установленные пакеты |
| 7 | B | pkg_info -Q ищет пакеты в репозитории |
| 8 | B | pkg_info -L показывает список файлов пакета |
| 9 | B | /usr/ports — стандартное расположение дерева портов |
| 10 | C | make install clean — компилирует, устанавливает и очищает |
| 11 | B | Ports используют для кастомных опций сборки или свежих версий |
| 12 | B | pkg_info -f показывает зависимости (dependencies) пакета |
| 13 | B | pkg_delete -a удаляет пакеты-сироты (orphans) |
| 14 | B | pkg_info -E находит пакет, которому принадлежит файл |
| 15 | B | PKG_PATH — альтернатива /etc/installurl для указания URL репозитория |

---

## Scoring Guide

Подсчитайте количество правильных ответов:

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **14-15 правильных (93-100%)** | 🏆 Отлично! | Вы хорошо знаете систему пакетов OpenBSD. |
| **11-13 правильных (73-87%)** | ✅ Хорошо | Повторите ports и flavors. |
| **8-10 правильных (53-67%)** | ⚠️ Удовлетворительно | Рекомендуется больше практики с pkg_info. |
| **Менее 8 правильных (<53%)** | 📚 Нужно повторить | Изучите man pkg_add и pkg_info. |

---

