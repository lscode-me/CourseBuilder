# Course Generation Pipeline - Полный процесс создания курсов

Данная папка содержит все инструменты и руководства для создания качественных курсов в формате CourseBuilder.

> 💡 **Быстрая навигация:** [INDEX.md](INDEX.md) - детальный индекс всех файлов | [quick_start_commands.sh](quick_start_commands.sh) - готовые команды

## 📁 Содержимое папки meta/

### 🛠️ Основные инструменты
- **`course_quality_checker.py`** - главный инструмент проверки и улучшения качества курсов (включает функции форматирования Markdown)

### 📚 Документация и стандарты
- **`README.md`** (этот файл) - полное руководство по созданию курсов
- **`STANDARDS_SUMMARY.md`** - сводка стандартов качества CourseBuilder
- **`COURSE_QUALITY_CHECKER.md`** - подробная документация по инструменту проверки

### 📝 Шаблоны и примеры
- **`LECTURE_TEMPLATE.md`** - шаблон для создания лекций
- **`LECTURE_EXAMPLE.md`** - пример качественной лекции
- **`QUIZ_TEMPLATE.md`** - шаблон для создания квизов
- **`LECTURE_CHECKLIST.md`** - чек-лист для самопроверки лекций

### 🤖 Промпты для ИИ
- **`GENERATION_GUIDE.md`** - промпты для генерации контента с помощью ИИ
- **`LECTURE_ENHANCEMENT_PROMPT.md`** - промпты для улучшения лекций
- **`QUIZ_DISTRACTOR_IMPROVEMENT_PROMPT.md`** - улучшение вариантов ответов в квизах

### 📋 Справочные материалы
- **`LECTURE_STANDARD.md`** - детальные стандарты для лекций
- **`QUICK_REFERENCE.md`** - быстрая справка по форматированию
- **`queries.txt`** - полезные поисковые запросы

### � Утилиты и скрипты
- **`quick_start_commands.sh`** - готовые bash-команды для создания курсов
- **`queries.txt`** - полезные поисковые запросы

### �🔗 Интеграционная документация
- **`INTEGRATION_SUMMARY.md`** - описание объединения инструментов
- **`README_QUALITY_CHECKER.md`** - краткое руководство по инструменту проверки

## 🎯 Обзор процесса

Создание курса проходит через несколько этапов, каждый из которых обеспечивает высокое качество итогового контента:

```
1. Планирование → 2. Структура → 3. Содержимое → 4. Проверка → 5. Финализация
```

---

## 📋 Этап 1: Планирование и описание курса

### 1.1 Создание описания курса

Первым шагом создается файл `Courses/{COURSENAME}/description.md` с полным описанием курса:

```bash
mkdir -p Courses/NewCourse/
touch Courses/NewCourse/description.md
```

**Структура description.md:**
- Название и краткое описание курса
- Цели курса (что изучит студент)
- Целевая аудитория
- Предварительные требования
- План курса (модули)
- Примерная длительность

**Пример description.md:**
```markdown
# Курс: Название курса

## Описание курса
Краткое описание курса, его применимость и важность.

## Цели курса
После прохождения курса слушатель:
- понимает основные концепции
- умеет применять знания на практике
- ориентируется в терминологии

## Целевая аудитория
- Разработчики начального уровня
- Студенты технических специальностей

## Предварительные требования
- Базовое понимание программирования
- Знакомство с терминалом

## План курса
1. Введение и основы
2. Практические примеры
3. Продвинутые темы
4. Заключение

Примерная длительность: 8-12 часов
```

### 1.2 Проверка уникальности названия

Убедитесь, что курс с таким названием не существует:
```bash
ls Courses/ | grep -i "coursename"
```

---

## 🏗️ Этап 2: Создание структуры курса

### 2.1 Генерация каркаса

Основываясь на description.md, создается структура папок и файлов:

```bash
# Создание папок для модулей
mkdir -p Courses/NewCourse/01_Introduction/
mkdir -p Courses/NewCourse/02_Basics/
mkdir -p Courses/NewCourse/03_Advanced/
mkdir -p Courses/NewCourse/04_Conclusion/

# Создание базовых файлов для каждого модуля
for module in Courses/NewCourse/*/; do
    touch "$module/lecture.md"
    touch "$module/quiz.md"
done

# Создание README курса
touch Courses/NewCourse/README.md
```

### 2.2 Создание README курса

Файл `Courses/{COURSENAME}/README.md` содержит навигацию по курсу:

**Шаблон README.md:**
```markdown
# Название курса

Краткое описание курса.

## Структура курса

1. [Введение](01_Introduction/)
2. [Основы](02_Basics/)
3. [Продвинутые темы](03_Advanced/)
4. [Заключение](04_Conclusion/)

## Как изучать

1. Читайте лекции последовательно
2. Выполняйте практические задания
3. Проходите квизы для закрепления
4. Используйте дополнительные материалы

## Ресурсы

- [Документация](https://example.com)
- [Практические примеры](https://github.com/example)
```

---

## ✍️ Этап 3: Создание содержимого

### 3.1 Написание лекций

Для каждого модуля создается `lecture.md` по стандартному шаблону:

**Используйте шаблон из [LECTURE_TEMPLATE.md](LECTURE_TEMPLATE.md):**
- 🎯 Learning Objectives (3-5 пунктов)
- 📋 Prerequisites
- Основной контент (5-12 секций)
- 💡 Key Takeaways (3-5 пунктов)
- 🚀 Next Steps

**Целевые метрики лекции:**
- Длина: 600-1000 строк
- Основных секций (H2): 5-12
- Блоков кода: 15-30
- Примеры должны быть рабочими

### 3.2 Создание квизов

Для каждого модуля создается `quiz.md` по шаблону:

**Используйте шаблон из [QUIZ_TEMPLATE.md](QUIZ_TEMPLATE.md):**
- 20-40 вопросов различных типов
- Multiple choice (A, B, C, D)
- Answer Key с объяснениями
- Scoring Guide

**Типы вопросов:**
- Определения и концепции
- Практическое применение  
- Анализ кода
- Troubleshooting

### 3.3 Инструменты для написания

**Полезные файлы в meta/:**
- `LECTURE_STANDARD.md` - стандарты качества лекций
- `LECTURE_EXAMPLE.md` - пример хорошей лекции
- `LECTURE_ENHANCEMENT_PROMPT.md` - промпты для улучшения
- `QUIZ_DISTRACTOR_IMPROVEMENT_PROMPT.md` - улучшение вариантов ответов
- `GENERATION_GUIDE.md` - детальное руководство по генерации
- `QUICK_REFERENCE.md` - быстрая справка

---

## 🔍 Этап 4: Проверка качества

### 4.1 Автоматическая проверка

Используйте объединенный инструмент проверки качества:

```bash
# Полная проверка курса в режиме dry-run
python meta/course_quality_checker.py --dry-run Courses/NewCourse/

# Проверка только качества контента
python meta/course_quality_checker.py --mode quality Courses/NewCourse/

# Получение рекомендаций по улучшению
python meta/course_quality_checker.py --recommendations Courses/NewCourse/
```

### 4.2 Проверяемые аспекты

**Качество контента:**
- ✅ Длина лекций соответствует стандартам
- ✅ Наличие всех обязательных секций
- ✅ Достаточное количество примеров кода
- ✅ Правильная структура квизов

**Структура файлов:**
- ✅ Все необходимые файлы присутствуют
- ✅ Соответствие README и файловой системы
- ✅ Отсутствие лишних файлов

**Форматирование:**
- ✅ Корректный Markdown
- ✅ Правильные пустые строки
- ✅ Оформление блоков кода и списков

**Квизы:**
- ✅ Достаточное количество вопросов
- ✅ Равномерное распределение правильных ответов
- ✅ Наличие объяснений

---

## 🎨 Этап 5: Улучшение и исправления

### 5.1 Автоматические исправления

```bash
# Исправление форматирования Markdown
python meta/course_quality_checker.py --mode format Courses/NewCourse/

# Балансировка ответов в квизах
python meta/course_quality_checker.py --mode quiz Courses/NewCourse/

# Применение всех исправлений
python meta/course_quality_checker.py --mode all Courses/NewCourse/
```

### 5.2 Ручные улучшения

**Анализ рекомендаций:**
1. Изучите отчет `--recommendations`
2. Исправьте критические проблемы (красные ❌)
3. Рассмотрите предупреждения (желтые ⚠️)

**Типичные улучшения:**
- Расширение слишком коротких лекций
- Добавление примеров кода
- Улучшение объяснений в квизах
- Добавление недостающих секций

### 5.3 Итеративная проверка

Повторяйте проверку после каждого крупного изменения:

```bash
# Быстрая проверка после изменений
python meta/course_quality_checker.py --mode quality --dry-run Courses/NewCourse/
```

---

## ✨ Этап 6: Финализация

### 6.1 Финальная проверка

```bash
# Полная проверка без dry-run (применит все исправления)
python meta/course_quality_checker.py Courses/NewCourse/

# Проверка что все модули достигли качества "Хорошо" или "Отлично"
python meta/course_quality_checker.py --mode quality Courses/NewCourse/
```

### 6.2 Генерация HTML (опционально)

```bash
# Если есть система сборки HTML
cd build_html/
./build_html.sh Courses/NewCourse/
```

### 6.3 Генерация TMA (опционально)

```bash
# Если требуется TMA формат
cd build_tma/
./build_tma.sh Courses/NewCourse/
```

---

## 📚 Этап 7: Регистрация курса

### 7.1 Добавление в каталог

Добавьте курс в `Courses/course_names.py`:

```python
# Найдите соответствующую категорию или создайте новую
course_names = {
    "Programming": [
        "Python",
        "Go", 
        "Rust",
        "NewCourse",  # ← Добавьте сюда
    ],
    # ...
}
```

### 7.2 Финальная проверка каталога

```bash
# Проверьте что файл корректен
python -c "from Courses.course_names import course_names; print('OK')"

# Проверьте что курс добавлен
python -c "from Courses.course_names import course_names; print([course for courses in course_names.values() for course in courses if 'NewCourse' in course])"
```

---

## 🧹 Этап 8: Очистка

### 8.1 Удаление временных файлов

```bash
# Удаление description.md (опционально)
rm Courses/NewCourse/description.md

# Удаление файлов сборки
rm -f Courses/NewCourse/*.html
rm -f Courses/NewCourse/**/*.html

# Удаление cache файлов (если есть)
find Courses/NewCourse/ -name "__pycache__" -type d -exec rm -rf {} +
find Courses/NewCourse/ -name "*.pyc" -delete
```

### 8.2 Финальная структура

После очистки в курсе должны остаться только:
```
Courses/NewCourse/
├── README.md
├── 01_ModuleName/
│   ├── lecture.md
│   └── quiz.md
├── 02_ModuleName/
│   ├── lecture.md
│   └── quiz.md
└── ...
```

---

## 🚀 Быстрый старт

Для создания нового курса выполните:

```bash
# 1. Планирование
mkdir -p Courses/NewCourse/
nano Courses/NewCourse/description.md

# 2. Создание структуры
# (создайте папки модулей и файлы lecture.md, quiz.md)

# 3. Написание контента
# (используйте шаблоны из meta/)

# 4. Проверка
python meta/course_quality_checker.py --recommendations Courses/NewCourse/

# 5. Исправления
python meta/course_quality_checker.py Courses/NewCourse/

# 6. Регистрация
# (добавьте в course_names.py)

# 7. Очистка
rm Courses/NewCourse/description.md
```

---

## 📖 Справочные материалы

### Основные стандарты
- [STANDARDS_SUMMARY.md](STANDARDS_SUMMARY.md) - сводка по стандартам качества
- [LECTURE_CHECKLIST.md](LECTURE_CHECKLIST.md) - чек-лист для лекций

### Шаблоны и примеры
- [LECTURE_TEMPLATE.md](LECTURE_TEMPLATE.md) - шаблон лекции
- [LECTURE_EXAMPLE.md](LECTURE_EXAMPLE.md) - пример качественной лекции
- [QUIZ_TEMPLATE.md](QUIZ_TEMPLATE.md) - шаблон квиза

### Инструменты
- [course_quality_checker.py](course_quality_checker.py) - основной инструмент проверки
- [COURSE_QUALITY_CHECKER.md](COURSE_QUALITY_CHECKER.md) - документация инструмента

### Промпты для ИИ
- [GENERATION_GUIDE.md](GENERATION_GUIDE.md) - промпты для генерации контента
- [LECTURE_ENHANCEMENT_PROMPT.md](LECTURE_ENHANCEMENT_PROMPT.md) - улучшение лекций
- [QUIZ_DISTRACTOR_IMPROVEMENT_PROMPT.md](QUIZ_DISTRACTOR_IMPROVEMENT_PROMPT.md) - улучшение квизов

---

## ⚠️ Важные замечания

### Качество важнее скорости
- Лучше потратить больше времени на планирование
- Используйте итеративный подход к улучшению
- Не переходите к следующему этапу пока текущий не завершен

### Автоматизация
- Используйте `course_quality_checker.py` на каждом этапе
- Настройте автоматические проверки в процессе разработки
- Следите за метриками качества

### Консистентность
- Следуйте установленным стандартам
- Используйте единую терминологию
- Проверяйте соответствие стилю существующих курсов

---

*Этот процесс разработан для обеспечения высокого качества и консистентности всех курсов в системе CourseBuilder.*