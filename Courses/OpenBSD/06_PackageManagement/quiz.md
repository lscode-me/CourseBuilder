# Package Management - Quiz

Проверьте свои знания по управлению пакетами в OpenBSD.

---

## Question 1: Файл зеркала


В каком файле указывается URL зеркала для pkg_add?

A) /etc/pkg.conf

B) /etc/apt/sources.list

C) /etc/installurl

D) /etc/mirrors.conf

---

## Question 2: Установка пакета


Какая команда устанавливает пакет в OpenBSD?

A) apt-get install

B) pkg install

C) pkg_add

D) yum install

---

## Question 3: Обновление пакетов


Какая команда обновляет все установленные пакеты?

A) pkg_add --upgrade

B) pkg_update -a

C) pkg_add -u

D) pkg_upgrade

---

## Question 4: Flavors


Что такое flavors в системе пакетов OpenBSD?

A) Цветовые схемы интерфейса

B) Типы лицензий

C) Варианты пакета с разными опциями сборки

D) Разные версии пакета

---

## Question 5: Список пакетов


Какая команда показывает список установленных пакетов?

A) pkg_list

B) rpm -qa

C) dpkg -l

D) pkg_info

---

## Question 6: Удаление пакета


Какая команда удаляет пакет?

A) pkg_uninstall

B) pkg_remove

C) pkg_delete

D) pkg_del

---

## Question 7: Поиск пакета


Какой флаг pkg_info используется для поиска пакетов в репозитории?

A) -s

B) -l

C) -Q

D) -f

---

## Question 8: Файлы пакета


Какой флаг pkg_info показывает файлы, установленные пакетом?

A) -f

B) -l

C) -L

D) -F

---

## Question 9: Ports


Где находится дерево портов в OpenBSD?

A) /usr/ports

B) /opt/ports

C) /var/ports

D) /ports

---

## Question 10: Сборка порта


Какая команда собирает и устанавливает порт?

A) ./configure && make && make install

B) make all

C) make install clean

D) make build install

---

## Question 11: pkg_add или ports


Когда следует использовать ports вместо pkg_add?

A) Когда нужны специфические опции сборки

B) Ports устарел, всегда используйте pkg_add

C) Всегда, ports быстрее

D) Для системных утилит

---

## Question 12: Зависимости


Какая команда показывает, от каких пакетов зависит указанный?

A) pkg_info -f

B) pkg_info -R

C) pkg_depends

D) pkg_info -d

---

## Question 13: Orphan пакеты


Какая команда удаляет пакеты без зависящих от них?

A) pkg_delete -a

B) pkg_autoremove

C) pkg_clean

D) pkg_delete -o

---

## Question 14: Поиск файла


Какая команда находит пакет по установленному файлу?

A) pkg_info -E /path

B) pkg_info -f /path

C) pkg_which /path

D) which -p /path

---

## Question 15: PKG_PATH


Для чего используется переменная PKG_PATH?

A) Логи установки

B) URL репозитория пакетов

C) Кэш загруженных пакетов

D) Путь к установленным пакетам

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | /etc/installurl — стандартный файл для указания зеркала в OpenBSD |
| 2 | C | pkg_add — команда установки пакетов в OpenBSD |
| 3 | C | pkg_add -u обновляет все установленные пакеты |
| 4 | C | Flavors — варианты пакета с разными опциями (например, с GUI или без) |
| 5 | D | pkg_info без аргументов показывает список установленных пакетов |
| 6 | C | pkg_delete удаляет установленные пакеты |
| 7 | C | pkg_info -Q ищет пакеты в репозитории |
| 8 | C | pkg_info -L показывает список файлов пакета |
| 9 | A | /usr/ports — стандартное расположение дерева портов |
| 10 | C | make install clean — компилирует, устанавливает и очищает |
| 11 | A | Ports используют для кастомных опций сборки или свежих версий |
| 12 | A | pkg_info -f показывает зависимости (dependencies) пакета |
| 13 | A | pkg_delete -a удаляет пакеты-сироты (orphans) |
| 14 | A | pkg_info -E находит пакет, которому принадлежит файл |
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

