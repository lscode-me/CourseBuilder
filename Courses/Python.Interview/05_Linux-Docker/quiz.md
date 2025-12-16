# Linux и Docker — Quiz

Проверьте знание базовых команд Linux и Docker.

---

## Question 1: Права доступа

Что означает `chmod 755 file`?

A) rwxr-xr-x — владелец всё, остальные читать и выполнять

B) Все могут всё

C) Только владелец может читать

D) Файл удаляется

---

## Question 2: Systemctl

Какая команда включит автозапуск сервиса при загрузке системы?

A) `systemctl restart nginx`

B) `systemctl enable nginx`

C) `systemctl start nginx`

D) `systemctl autostart nginx`

---

## Question 3: Docker кэширование

Почему рекомендуется копировать requirements.txt перед копированием всего кода?

A) requirements.txt должен быть первым файлом

B) Для использования кэша слоёв — зависимости не пересобираются при изменении кода

C) Иначе pip не найдёт файл

D) Это обязательное требование Docker

---

## Question 4: Размер директории

Какая команда покажет размер директории /var/log?

A) `df -h /var/log`

B) `ls -l /var/log`

C) `du -sh /var/log`

D) `size /var/log`

---

## Question 5: Docker exec

Как войти в работающий контейнер с bash?

A) `docker connect container bash`

B) `docker ssh container`

C) `docker exec -it container bash`

D) `docker run container bash`

---

## Question 6: Минимизация слоёв

Как уменьшить количество слоёв в Docker образе?

A) Удалить все комментарии

B) Объединять RUN команды через &&

C) Использовать только COPY

D) Использовать больше FROM

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | 755 = rwx(7) r-x(5) r-x(5) — владелец всё, остальные читать/выполнять |
| 2 | B | `enable` добавляет в автозапуск, `start` только запускает |
| 3 | B | Docker кэширует слои; если requirements.txt не изменился, pip install пропускается |
| 4 | C | `du -sh` — disk usage, `-s` summary, `-h` human-readable |
| 5 | C | `exec -it` запускает команду в работающем контейнере с tty |
| 6 | B | Каждый RUN создаёт слой; объединение через && уменьшает их количество |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **5-6 правильных (83-100%)** | 🏆 Отлично! | Готовы к вопросам по Linux/Docker |
| **3-4 правильных (50-66%)** | ✅ Хорошо | Попрактикуйтесь с Docker |
| **Менее 3 правильных (<50%)** | 📚 Нужно повторить | Изучите базовые команды |

---

