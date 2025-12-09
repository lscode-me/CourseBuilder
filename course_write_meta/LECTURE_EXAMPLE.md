# Git Branching
## Создание, переключение и управление ветками

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:
- Знать базовые команды Git (`init`, `add`, `commit`, `status`)
- Понимать концепцию коммитов и истории
- Уметь работать с терминалом

**Recommended prior modules:**
- [01_Intro](../01_Intro/) — основы Git
- [02_Basics](../02_Basics/) — базовые команды

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:
- Создавать и удалять ветки в Git
- Переключаться между ветками с помощью `checkout` и `switch`
- Объяснять концепцию HEAD и detached state
- Применять ветки для организации параллельной работы

---

## 1. Что такое ветки в Git

Ветки — это один из ключевых механизмов Git, позволяющий вести параллельную разработку. В отличие от других систем контроля версий, ветки в Git невероятно легковесны — это просто указатели на коммиты.

### 1.1 Зачем нужны ветки

Ветки решают несколько важных задач:

- **Изоляция изменений**: работа над новой функцией не влияет на стабильный код
- **Параллельная разработка**: несколько разработчиков могут работать независимо
- **Эксперименты**: можно пробовать идеи без риска сломать проект
- **Релизы**: разные версии продукта могут существовать одновременно

### 1.2 Как устроены ветки

Ветка в Git — это просто файл, содержащий 40-символьный SHA-1 хеш коммита. Создание ветки не копирует файлы и не занимает много места.

```bash
# Посмотреть, что хранит ветка main
cat .git/refs/heads/main
```

**Output:**
```
a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0
```

Это просто указатель на последний коммит в ветке.

---

## 2. Создание веток

### 2.1 Команда git branch

Для создания новой ветки используется команда `git branch`:

```bash
# Создать новую ветку feature-login
git branch feature-login

# Посмотреть список всех веток
git branch
```

**Output:**
```
  feature-login
* main
```

Звездочка `*` показывает текущую ветку. Обратите внимание: мы создали ветку, но не переключились на неё.

### 2.2 Создание с переключением

Чтобы создать ветку и сразу переключиться на неё:

```bash
# Старый способ (всё ещё работает)
git checkout -b feature-signup

# Новый способ (Git 2.23+)
git switch -c feature-dashboard
```

**Output:**
```
Switched to a new branch 'feature-dashboard'
```

> **💡 Pro Tip:**  
> Команда `git switch` появилась в Git 2.23 и предназначена специально для работы с ветками. Она более интуитивна, чем `checkout`.

### 2.3 Именование веток

**Best practices для имён веток:**

| Тип | Формат | Пример |
|-----|--------|--------|
| Фича | `feature/описание` | `feature/user-auth` |
| Баг-фикс | `fix/описание` | `fix/login-crash` |
| Хотфикс | `hotfix/описание` | `hotfix/security-patch` |
| Релиз | `release/версия` | `release/v2.1.0` |

```bash
# Примеры хороших имён
git branch feature/payment-integration
git branch fix/header-alignment
git branch release/v1.2.0
```

---

## 3. Переключение между ветками

### 3.1 Команда git switch

Современный способ переключения между ветками:

```bash
# Переключиться на существующую ветку
git switch feature-login

# Вернуться на main
git switch main
```

**Output:**
```
Switched to branch 'feature-login'
```

### 3.2 Команда git checkout

Классический способ, работает во всех версиях Git:

```bash
# Переключиться на ветку
git checkout feature-login

# Переключиться на предыдущую ветку
git checkout -
```

**Output:**
```
Switched to branch 'feature-login'
```

> **⚠️ Warning:**  
> `git checkout` используется для многих целей (ветки, файлы, коммиты). Это может запутать новичков. Для работы с ветками рекомендуется `git switch`.

### 3.3 Что происходит при переключении

При переключении ветки Git:

1. Обновляет указатель HEAD
2. Заменяет файлы в рабочей директории
3. Обновляет индекс (staging area)

```bash
# Проверить текущую ветку
git branch --show-current
```

**Output:**
```
feature-login
```

---

## 4. HEAD и указатели

### 4.1 Что такое HEAD

HEAD — это специальный указатель на текущую позицию в репозитории. Обычно он указывает на ветку, а не напрямую на коммит.

```bash
# Посмотреть, куда указывает HEAD
cat .git/HEAD
```

**Output:**
```
ref: refs/heads/main
```

### 4.2 Визуализация HEAD

```
         HEAD
          ↓
        main
          ↓
    A --- B --- C --- D
                      ↑
                  feature
```

В этом примере:
- HEAD указывает на `main`
- `main` указывает на коммит D
- `feature` тоже указывает на коммит D

### 4.3 Detached HEAD

**Detached HEAD** — состояние, когда HEAD указывает напрямую на коммит, а не на ветку.

```bash
# Переключиться на конкретный коммит (вызовет detached HEAD)
git checkout a1b2c3d
```

**Output:**
```
Note: switching to 'a1b2c3d'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.
```

> **⚠️ Warning:**  
> В detached HEAD коммиты не принадлежат ни одной ветке. Если вы переключитесь на другую ветку, эти коммиты могут быть потеряны (пока не будут удалены сборщиком мусора).

### 4.4 Выход из detached HEAD

Чтобы сохранить изменения из detached HEAD:

```bash
# Создать новую ветку из текущей позиции
git switch -c saved-work

# Или вернуться на существующую ветку (изменения будут потеряны)
git switch main
```

---

## 5. Удаление веток

### 5.1 Удаление локальных веток

```bash
# Безопасное удаление (только если ветка слита)
git branch -d feature-login

# Принудительное удаление (даже если не слита)
git branch -D feature-experimental
```

**Output:**
```
Deleted branch feature-login (was a1b2c3d).
```

### 5.2 Почему -d vs -D

| Флаг | Поведение | Когда использовать |
|------|-----------|-------------------|
| `-d` | Удалит только слитую ветку | Обычное удаление |
| `-D` | Удалит любую ветку | Когда точно знаете, что делаете |

```bash
# Пример: попытка удалить неслитую ветку с -d
git branch -d unmerged-feature
```

**Output:**
```
error: The branch 'unmerged-feature' is not fully merged.
If you are sure you want to delete it, run 'git branch -D unmerged-feature'.
```

Git защищает вас от случайной потери работы.

### 5.3 Удаление удалённых веток

```bash
# Удалить ветку на удалённом сервере
git push origin --delete feature-login

# Или короткий синтаксис
git push origin :feature-login
```

**Output:**
```
To github.com:user/repo.git
 - [deleted]         feature-login
```

---

## 6. Просмотр информации о ветках

### 6.1 Список веток

```bash
# Локальные ветки
git branch

# Удалённые ветки
git branch -r

# Все ветки (локальные и удалённые)
git branch -a
```

**Output:**
```
* main
  feature-login
  feature-signup
  remotes/origin/main
  remotes/origin/feature-api
```

### 6.2 Подробная информация

```bash
# Показать последний коммит каждой ветки
git branch -v

# Показать ветки, слитые в текущую
git branch --merged

# Показать ветки, НЕ слитые в текущую
git branch --no-merged
```

**Output (git branch -v):**
```
  feature-login  a1b2c3d Add login form
  feature-signup b2c3d4e Add signup validation
* main           c3d4e5f Merge feature-api
```

---

## 7. Практические сценарии

### 7.1 Сценарий: Работа над новой фичей

```bash
# 1. Убедиться, что main актуален
git switch main
git pull origin main

# 2. Создать ветку для фичи
git switch -c feature/shopping-cart

# 3. Работать над фичей
# ... редактирование файлов ...
git add .
git commit -m "Add shopping cart component"

# 4. Ещё коммиты
git add .
git commit -m "Add cart item counter"

# 5. Когда готово — пушить для code review
git push -u origin feature/shopping-cart
```

### 7.2 Сценарий: Срочный баг-фикс

```bash
# 1. Сохранить текущую работу (если есть незакоммиченные изменения)
git stash

# 2. Переключиться на main
git switch main

# 3. Создать ветку для фикса
git switch -c hotfix/critical-bug

# 4. Исправить баг
# ... редактирование ...
git add .
git commit -m "Fix critical security vulnerability"

# 5. Запушить и создать PR
git push -u origin hotfix/critical-bug

# 6. Вернуться к своей работе
git switch feature/shopping-cart
git stash pop
```

### 7.3 Сценарий: Посмотреть старую версию кода

```bash
# Посмотреть код на момент тега v1.0.0
git checkout v1.0.0

# Вы в detached HEAD — можно смотреть, но не коммитить
# ... изучение кода ...

# Вернуться к работе
git switch main
```

---

## 8. Common Pitfalls

### 8.1 Pitfall: Переключение с незакоммиченными изменениями

❌ **Проблема:**
```bash
# Есть незакоммиченные изменения
git switch feature-login
```

**Output:**
```
error: Your local changes to the following files would be overwritten by checkout:
        index.html
Please commit your changes or stash them before you switch branches.
```

✅ **Решение:**
```bash
# Вариант 1: Закоммитить
git add .
git commit -m "WIP: work in progress"

# Вариант 2: Stash
git stash
git switch feature-login
# Потом: git stash pop

# Вариант 3: Принудительно (потеряете изменения!)
git switch -f feature-login
```

### 8.2 Pitfall: Удаление ветки, на которой находишься

❌ **Проблема:**
```bash
git branch -d main  # когда находишься на main
```

**Output:**
```
error: Cannot delete branch 'main' checked out at '/path/to/repo'
```

✅ **Решение:**
```bash
# Сначала переключиться на другую ветку
git switch feature-login
git branch -d main
```

### 8.3 Pitfall: Забыли, на какой ветке находитесь

✅ **Решение:**
```bash
# Быстрая проверка
git branch --show-current

# Или через status
git status
```

**Output:**
```
On branch feature-login
nothing to commit, working tree clean
```

---

## 💡 Key Takeaways

- **Ветки — легковесны**: это просто указатели на коммиты, создание ветки мгновенно
- **HEAD — текущая позиция**: обычно указывает на ветку, в detached state — на коммит
- **git switch vs checkout**: `switch` современнее и безопаснее для работы с ветками
- **Именование важно**: используйте конвенции (`feature/`, `fix/`, `release/`)
- **-d vs -D**: маленькая `d` защищает от потери неслитых изменений

---

## 🚀 Next Steps

**Related Modules:**
- [04_Merging](../04_Merging/) — слияние веток, разрешение конфликтов
- [06_Rebase](../06_Rebase/) — альтернатива merge, переписывание истории
- [07_Stash](../07_Stash/) — временное сохранение изменений

**Practice Ideas:**
1. Создайте репозиторий с несколькими ветками и попрактикуйтесь в переключении
2. Намеренно создайте detached HEAD и выйдите из него
3. Попробуйте удалить неслитую ветку и посмотрите на сообщение Git

**Going Deeper:**
- Git Internals: как хранятся ветки в `.git/refs/`
- Reflog: восстановление "потерянных" коммитов из detached HEAD
- Worktrees: работа с несколькими ветками одновременно

---

## 📚 Additional Resources

**Documentation:**
- [Git Branching - Official Docs](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell) — официальная документация

**Articles:**
- [A successful Git branching model](https://nvie.com/posts/a-successful-git-branching-model/) — классическая статья о GitFlow

---

<!--
===========================================
ЭТО ОБРАЗЦОВАЯ ЛЕКЦИЯ (LECTURE_EXAMPLE.md)
===========================================

Эта лекция демонстрирует все стандарты CourseBuilder:

✅ СТРУКТУРА:
- H1 + H2 заголовок
- Prerequisites с ссылками на предыдущие модули
- Learning Objectives (4 цели с глаголами действия)
- 8 основных секций с нумерацией
- Подсекции (1.1, 1.2, etc.)
- Key Takeaways (5 пунктов)
- Next Steps с ссылками и практикой

✅ МЕТРИКИ:
- ~650 строк
- 20+ блоков кода
- ~35 минут чтения
- Соотношение теория/практика ≈ 50/50

✅ СТИЛЬ:
- Дружелюбный, но профессиональный тон
- От простого к сложному
- Все примеры с Output
- Объяснение "зачем", а не только "как"

✅ ФОРМАТИРОВАНИЕ:
- Эмодзи только в заголовках секций
- Таблицы для сравнений
- Warning и Pro Tip блоки
- Код с комментариями

Используйте эту лекцию как референс при создании
новых модулей для любого курса.

===========================================
-->

