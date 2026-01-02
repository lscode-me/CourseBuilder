# Course Quality Checker - Быстрый старт

Объединенный инструмент для проверки и улучшения качества курсов.

## Основные команды

### Быстрая проверка курса
```bash
python course_quality_checker.py Courses/AI/
```

### Проверка с рекомендациями по улучшению
```bash
python course_quality_checker.py --recommendations Courses/Python/
```

### Только исправление форматирования (безопасно)
```bash
python course_quality_checker.py --mode format Courses/NewCourse/
```

### Режим dry-run (только проверка, без изменений)
```bash
python course_quality_checker.py --dry-run Courses/
```

## Что проверяет инструмент

✅ **Качество контента:**
- Длина лекций (600-1000 строк)
- Количество секций и примеров кода
- Наличие Learning Objectives и Key Takeaways
- Размер квизов (20-40 вопросов)

✅ **Структура файлов:**
- README.md в корне курса
- lecture.md и quiz.md в каждом модуле
- Отсутствие лишних файлов

✅ **Форматирование Markdown:**
- Пустые строки между элементами
- Корректное оформление списков
- Правильное размещение блоков кода

✅ **Балансировка квизов:**
- Равномерное распределение ответов A/B/C/D
- Обновление Answer Key при перемешивании

## Пример использования при создании курса

1. **После создания нового модуля:**
   ```bash
   python course_quality_checker.py --mode format Courses/NewCourse/01_Introduction/
   ```

2. **Проверка качества после написания контента:**
   ```bash
   python course_quality_checker.py --mode quality --recommendations Courses/NewCourse/
   ```

3. **Финальная проверка перед публикацией:**
   ```bash
   python course_quality_checker.py Courses/NewCourse/
   ```

## Результат работы

Скрипт выдает детальный отчет с оценкой качества каждого модуля и общей статистикой по курсу, а также конкретные рекомендации по улучшению.

Подробная документация: [COURSE_QUALITY_CHECKER.md](COURSE_QUALITY_CHECKER.md)