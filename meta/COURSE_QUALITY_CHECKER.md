# Course Quality Checker - Объединенный инструмент проверки качества курсов

## Описание

`course_quality_checker.py` - это объединенный инструмент, который включает в себя все функции проверки и улучшения качества курсов из папки `course_validate_tools`. Предназначен для использования в процессе создания новых курсов.

## Основные функции

### 1. Анализ качества курсов
- Проверка длины лекций (600-1000 строк)
- Подсчет основных секций H2 (5-12)
- Анализ количества блоков кода (15-30)
- Проверка наличия Learning Objectives (3-5)
- Проверка наличия Key Takeaways (3-5)
- Анализ квизов (20-40 вопросов)

### 2. Проверка комплектности
- Наличие README.md в корне курса
- Наличие lecture.md и quiz.md в каждом модуле
- Соответствие между модулями в README и реальными папками
- Выявление и удаление лишних файлов/папок

### 3. Автоматическое исправление форматирования
- Пустые строки между bold-пунктами списков
- Пустые строки между **Bold:** и последующими списками
- Пустые строки до/после блоков кода
- Пустые строки после заголовков
- Удаление лишних пустых строк

### 4. Балансировка квизов
- Перемешивание вариантов ответов A/B/C/D
- Автоматическое обновление Answer Key
- Стремление к равномерному распределению (25% на каждый вариант)

## Использование

### Базовое использование

```bash
# Проверка всех курсов
python course_quality_checker.py

# Проверка конкретного курса
python course_quality_checker.py Courses/AI/

# Проверка с рекомендациями
python course_quality_checker.py --recommendations Courses/Python/

# Режим dry-run (только проверка, без изменений)
python course_quality_checker.py --dry-run Courses/IT_Basics/
```

### Режимы работы

```bash
# Только анализ качества
python course_quality_checker.py --mode quality Courses/AI/

# Только проверка комплектности
python course_quality_checker.py --mode completeness Courses/API/

# Только исправление форматирования
python course_quality_checker.py --mode format Courses/Python/

# Только работа с квизами
python course_quality_checker.py --mode quiz Courses/DevOps/

# Все проверки (по умолчанию)
python course_quality_checker.py --mode all Courses/
```

### Дополнительные параметры

```bash
# Без исправления форматирования
python course_quality_checker.py --no-format Courses/AI/

# Без перемешивания квизов
python course_quality_checker.py --no-shuffle Courses/Python/

# Показать рекомендации по улучшению
python course_quality_checker.py --recommendations Courses/
```

## Интеграция в процесс создания курсов

### 1. После создания нового модуля

```bash
# Проверить качество и исправить форматирование
python course_quality_checker.py --mode format Courses/NewCourse/01_Introduction/
```

### 2. После завершения курса

```bash
# Полная проверка с рекомендациями
python course_quality_checker.py --recommendations Courses/NewCourse/
```

### 3. Перед публикацией

```bash
# Финальная проверка и балансировка
python course_quality_checker.py Courses/NewCourse/
```

## Выходная информация

### Отчет по модулю
```
📖 Проверка модуля: 01_Introduction
--------------------------------------------------
  📝 Исправлено форматирование lecture.md: 3 проблем
  📊 Качество: ✅ Хорошо
     - Строк в лекции: 847 (✅ Норма)
     - H2 секций: 8 (✅ Норма)
     - Блоков кода: 22 (✅ Норма)
     - Quiz: 25 вопросов (✅ Норма)
  🎯 Квиз готов к перемешиванию
```

### Итоговый отчет по курсу
```
📋 ИТОГОВЫЙ ОТЧЕТ: AI
------------------------------------------------------------
Модулей: 14
Средняя длина лекции: 756 строк
Модулей с квизом: 14/14
Всего вопросов в квизах: 350

Качество модулей:
  ✅ Отлично: 8
  ✅ Хорошо: 4
  ⚠️ Требует улучшений: 2
  ❌ Серьёзные проблемы: 0
```

### Рекомендации по улучшению
```
💡 РЕКОМЕНДАЦИИ ПО УЛУЧШЕНИЮ
============================================================
📖 05_Prompt_Basics:
  - Добавить больше примеров кода
  - Добавить больше вопросов в квиз

📖 12_Market:
  - Расширить содержимое лекции (текущая длина: 543 строк)
  - Добавить секцию 💡 Key Takeaways
```

## Стандарты качества

### Лекции
- **Длина:** 600-1000 строк (оптимум: 700-900)
- **Основные секции:** 5-12 (оптимум: 7-10)
- **Блоки кода:** 15-30 (оптимум: 20-25)
- **Learning Objectives:** 3-5 пунктов
- **Key Takeaways:** 3-5 пунктов

### Квизы
- **Количество вопросов:** 20-40 (оптимум: 25-30)
- **Распределение ответов:** стремление к 25% на каждый вариант
- **Обязательные элементы:** Answer Key, объяснения

### Структура
- **Обязательные файлы:** README.md в корне курса
- **Обязательные файлы модуля:** lecture.md, quiz.md
- **Обязательные секции лекции:**
  - 📋 Prerequisites
  - 🎯 Learning Objectives
  - 💡 Key Takeaways
  - 🚀 Next Steps

## Автоматизация

Скрипт можно интегрировать в CI/CD или использовать в качестве pre-commit hook:

```bash
# В .git/hooks/pre-commit
#!/bin/bash
python course_write_meta/course_quality_checker.py --mode format --dry-run
if [ $? -ne 0 ]; then
    echo "❌ Проблемы с форматированием. Запустите course_quality_checker.py"
    exit 1
fi
```

## Расширение функциональности

Скрипт легко расширять новыми проверками:

1. Добавить новые методы в соответствующие классы
2. Обновить `ModuleMetrics` для новых метрик
3. Добавить новые режимы в CLI

## Примеры использования в workflow

### 1. Ежедневная проверка

```bash
# Cron job для ежедневной проверки всех курсов
0 9 * * * cd /path/to/CourseBuilder && python course_write_meta/course_quality_checker.py --mode quality > quality_report.txt
```

### 2. Проверка перед коммитом

```bash
# Проверка измененных курсов
git diff --name-only | grep "Courses/" | head -1 | xargs dirname | xargs python course_write_meta/course_quality_checker.py --mode format --dry-run
```

### 3. Создание нового модуля

```bash
# После создания lecture.md и quiz.md
python course_quality_checker.py --mode all --recommendations Courses/NewCourse/XX_NewModule/
```