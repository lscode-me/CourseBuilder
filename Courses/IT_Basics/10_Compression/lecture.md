# Сжатие данных
## gzip, bzip2, xz и архивирование

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать форматы файлов (модуль 04_FileFormats)
- Иметь опыт работы в командной строке
- Знать основы работы с файлами

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Сжимать и распаковывать файлы с gzip, bzip2, xz
- Создавать и распаковывать tar архивы
- Выбирать подходящий алгоритм сжатия
- Работать со сжатыми данными в Python

---

## 1. Основы сжатия

### 1.1 Lossless vs Lossy

**Lossless (без потерь):**
- gzip, bzip2, xz, ZIP
- Полное восстановление данных
- Для текста, кода, данных

**Lossy (с потерями):**
- JPEG, MP3, H.264
- Меньший размер, потеря качества
- Для медиа

### 1.2 Соотношение размер/скорость

```
Скорость сжатия                    Степень сжатия
←─────────────────────────────────────────────────→
lz4   gzip   bzip2   xz/lzma
fast  ←──────────────────→  slow
```

---

## 2. gzip

### 2.1 Основы gzip

```bash
# Сжатие (заменяет оригинал!)
gzip file.txt
# Результат: file.txt.gz

# Распаковка
gunzip file.txt.gz
# или
gzip -d file.txt.gz

# Сохранить оригинал
gzip -k file.txt
# Результат: file.txt и file.txt.gz
```

### 2.2 Опции gzip

```bash
# Уровень сжатия (1-9, default=6)
gzip -9 file.txt    # Максимальное сжатие
gzip -1 file.txt    # Быстрое сжатие

# Рекурсивно
gzip -r directory/

# Просмотр информации
gzip -l file.txt.gz
```

### 2.3 Чтение сжатых файлов

```bash
# Просмотр без распаковки
zcat file.txt.gz
zless file.txt.gz
zgrep "pattern" file.txt.gz
```

---

## 3. bzip2

### 3.1 Использование

```bash
# Сжатие
bzip2 file.txt
# Результат: file.txt.bz2

# Распаковка
bunzip2 file.txt.bz2
bzip2 -d file.txt.bz2

# Сохранить оригинал
bzip2 -k file.txt
```

### 3.2 Сравнение с gzip

| Аспект | gzip | bzip2 |
|--------|------|-------|
| Сжатие | ~70% | ~60% |
| Скорость | Быстрее | Медленнее |
| Память | Меньше | Больше |
| Расширение | .gz | .bz2 |

---

## 4. xz (LZMA)

### 4.1 Использование

```bash
# Сжатие
xz file.txt
# Результат: file.txt.xz

# Распаковка
unxz file.txt.xz
xz -d file.txt.xz

# Сохранить оригинал
xz -k file.txt

# Просмотр
xzcat file.txt.xz
```

### 4.2 Преимущества xz

- Лучшее сжатие
- Используется для дистрибутивов Linux
- Медленнее, но результат меньше

---

## 5. tar (архивирование)

### 5.1 Что такое tar

**tar** (tape archive) — объединяет файлы в один архив БЕЗ сжатия.

```bash
# Создание архива
tar -cvf archive.tar file1.txt file2.txt directory/
# c = create, v = verbose, f = file

# Просмотр содержимого
tar -tvf archive.tar

# Распаковка
tar -xvf archive.tar
# x = extract

# В конкретную директорию
tar -xvf archive.tar -C /destination/
```

### 5.2 tar + сжатие

```bash
# tar.gz (gzip)
tar -czvf archive.tar.gz directory/
tar -xzvf archive.tar.gz

# tar.bz2 (bzip2)
tar -cjvf archive.tar.bz2 directory/
tar -xjvf archive.tar.bz2

# tar.xz (xz)
tar -cJvf archive.tar.xz directory/
tar -xJvf archive.tar.xz
```

**Флаги сжатия:**
- `-z` = gzip
- `-j` = bzip2
- `-J` = xz

---

## 6. ZIP

### 6.1 Использование

```bash
# Создание
zip archive.zip file1.txt file2.txt
zip -r archive.zip directory/  # Рекурсивно

# Распаковка
unzip archive.zip
unzip archive.zip -d /destination/

# Просмотр
unzip -l archive.zip
```

### 6.2 ZIP vs tar.gz

| ZIP | tar.gz |
|-----|--------|
| Один файл | tar + gzip отдельно |
| Случайный доступ | Последовательный |
| Windows стандарт | Unix стандарт |
| Встроенное сжатие | Отдельное сжатие |

---

## 7. Python и сжатие

### 7.1 gzip

```python
import gzip

# Запись
with gzip.open('file.txt.gz', 'wt', encoding='utf-8') as f:
    f.write('Hello, World!')

# Чтение
with gzip.open('file.txt.gz', 'rt', encoding='utf-8') as f:
    content = f.read()
```

### 7.2 tarfile

```python
import tarfile

# Создание tar.gz
with tarfile.open('archive.tar.gz', 'w:gz') as tar:
    tar.add('directory/')
    tar.add('file.txt')

# Распаковка
with tarfile.open('archive.tar.gz', 'r:gz') as tar:
    tar.extractall('destination/')

# Просмотр содержимого
with tarfile.open('archive.tar.gz', 'r:gz') as tar:
    for member in tar.getmembers():
        print(member.name)
```

### 7.3 zipfile

```python
import zipfile

# Создание
with zipfile.ZipFile('archive.zip', 'w') as zf:
    zf.write('file.txt')
    zf.write('directory/file.txt', arcname='renamed.txt')

# Чтение
with zipfile.ZipFile('archive.zip', 'r') as zf:
    print(zf.namelist())
    content = zf.read('file.txt')
```

---

## 8. Сравнение форматов

| Формат | Сжатие | Скорость | Использование |
|--------|--------|----------|---------------|
| gzip | Хорошее | Быстро | Веб, логи |
| bzip2 | Лучше | Средне | Архивы |
| xz | Лучшее | Медленно | Дистрибутивы |
| lz4 | Среднее | Очень быстро | Realtime |
| zstd | Отличное | Быстро | Современный стандарт |

---

## 💡 Key Takeaways

- **tar — архивирование, не сжатие**: tar объединяет файлы, gzip/bzip2/xz сжимают.

- **Выбор алгоритма**: gzip для скорости, xz для размера, zstd для баланса.

- **Флаги tar**: `-z` (gzip), `-j` (bzip2), `-J` (xz).

- **ZIP для кроссплатформенности**: Если нужна совместимость с Windows.

---

## 📚 Additional Resources

- [GNU gzip](https://www.gnu.org/software/gzip/)
- [XZ Utils](https://tukaani.org/xz/)
- [Zstandard](https://facebook.github.io/zstd/)

---

## 🚀 Next Steps

**Следующие модули:**
- [11_Checksums](../11_Checksums/) — Контрольные суммы и хеширование
- [12_DataTransfer](../12_DataTransfer/) — Передача данных и кодирование

**Практика:**
1. Сравните степень сжатия gzip, bzip2 и xz на разных типах файлов
2. Создайте архив tar.gz и распакуйте его
3. Измерьте время сжатия vs размер для разных алгоритмов


