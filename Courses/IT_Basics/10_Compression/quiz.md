# Compression - Quiz

Проверьте свои знания по теме "Сжатие данных".

---

## Question 1: Типы сжатия

Какой тип сжатия используется для текстовых файлов?

A) Hybrid

B) Lossless

C) Partial

D) Lossy

---

## Question 2: gzip команда

Какая команда сжимает файл с gzip?

A) `pack file.txt`

B) gzip file.txt

C) `compress file.txt`

D) `zip file.txt`

---

## Question 3: Распаковка gzip

Какая команда распаковывает .gz файл?

A) `ungzip file.txt.gz`

B) `extract file.txt.gz`

C) `unzip file.txt.gz`

D) gunzip file.txt.gz

---

## Question 4: tar назначение

Что делает tar?

A) Сжимает файлы

B) Удаляет дубликаты

C) Шифрует файлы

D) Объединяет файлы в один архив

---

## Question 5: tar + gzip

Какой флаг tar использует gzip сжатие?

A) -z

B) `-Z`

C) `-c`

D) `-g`

---

## Question 6: tar создание

Какая команда создаёт tar.gz архив?

A) `tar -azvf archive.tar.gz dir/`

B) tar -czvf archive.tar.gz dir/

C) `tar -tzvf archive.tar.gz dir/`

D) `tar -xzvf archive.tar.gz dir/`

---

## Question 7: tar распаковка

Какой флаг tar извлекает файлы?

A) `-r`

B) `-t`

C) `-c`

D) -x

---

## Question 8: bzip2 расширение

Какое расширение у файлов сжатых bzip2?

A) `.b2`

B) `.bz`

C) .bz2

D) `.bzip`

---

## Question 9: xz сжатие

Какой алгоритм обеспечивает лучшее сжатие?

A) xz

B) bzip2

C) lz4

D) gzip

---

## Question 10: tar bzip2 флаг

Какой флаг tar использует bzip2?

A) `-B`

B) -j

C) `-b`

D) `-2`

---

## Question 11: zcat

Что делает команда zcat?

A) Показывает содержимое .gz файла без распаковки

B) Создаёт zip архив

C) Конкатенирует zip файлы

D) Проверяет целостность архива

---

## Question 12: gzip -k

Что делает флаг `-k` в gzip?

A) Использует максимальное сжатие

B) Сохраняет оригинальный файл

C) Показывает прогресс

D) Рекурсивно сжимает директорию

---

## Question 13: Python gzip

Как открыть gzip файл для чтения текста в Python?

A) `gzip.open('file.gz', 'r')`

B) `open('file.gz', 'gz')`

C) gzip.open('file.gz', 'rt')

D) `gzip.read('file.gz')`

---

## Question 14: ZIP vs tar

Что верно о ZIP по сравнению с tar.gz?

A) ZIP не поддерживает сжатие

B) ZIP не поддерживает директории

C) ZIP только для Windows

D) ZIP позволяет извлекать отдельные файлы без полной распаковки

---

## Question 15: tar xz флаг

Какой флаг tar использует xz сжатие?

A) `-Z`

B) `-X`

C) -J

D) `-x`

---

## Question 16: zstd

Что характерно для формата zstd?

A) Самое медленное сжатие

B) Только для Windows

C) Отличное соотношение сжатие/скорость (современный стандарт)

D) Не поддерживает потоковое сжатие

---

## Question 17: Python tarfile

Как создать tar.gz архив в Python?

A) tarfile.open('archive.tar.gz', 'w:gz')

B) `tarfile.write('archive.tar.gz')`

C) `tarfile.create('archive.tar.gz')`

D) `tar.gz('archive.tar.gz')`

---

## Question 18: unzip просмотр

Какая команда показывает содержимое ZIP без распаковки?

A) unzip -l archive.zip

B) `unzip -t archive.zip`

C) `unzip -p archive.zip`

D) `unzip -v archive.zip`

---

## Question 19: gzip уровень

Какой диапазон уровней сжатия поддерживает gzip?

A) 1-9

B) 0-100

C) 1-10

D) 0-5

---

## Question 20: tar -C

Что делает флаг `-C` в tar?

A) Указывает директорию для распаковки

B) Создаёт архив

C) Проверяет целостность

D) Сжимает с gzip

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | Lossless (без потерь) используется для текста, кода, данных. Lossy — для медиа. |
| 2 | B | `gzip file.txt` сжимает файл, создаёт file.txt.gz. |
| 3 | D | `gunzip` или `gzip -d` распаковывает .gz файлы. |
| 4 | D | tar (tape archive) объединяет файлы без сжатия. |
| 5 | A | `-z` активирует gzip сжатие в tar. |
| 6 | B | `-c` создаёт, `-z` gzip, `-v` verbose, `-f` файл. |
| 7 | D | `-x` (extract) извлекает файлы из архива. |
| 8 | C | bzip2 создаёт файлы с расширением .bz2. |
| 9 | A | xz (LZMA2) обеспечивает лучшее сжатие, но медленнее. |
| 10 | B | `-j` активирует bzip2 в tar. |
| 11 | A | `zcat` выводит содержимое .gz без распаковки на диск. |
| 12 | B | `-k` (keep) сохраняет оригинальный файл после сжатия. |
| 13 | C | `'rt'` = read text, для текстовых файлов с кодировкой. |
| 14 | D | ZIP поддерживает random access — можно извлечь один файл. |
| 15 | C | `-J` (заглавная) активирует xz сжатие в tar. |
| 16 | C | zstd (Zstandard) — современный алгоритм с отличным балансом. |
| 17 | A | `tarfile.open('file.tar.gz', 'w:gz')` — создание tar.gz. |
| 18 | A | `unzip -l` показывает список файлов в архиве. |
| 19 | A | gzip поддерживает уровни 1-9 (1=быстро, 9=максимум). |
| 20 | A | `-C directory` указывает целевую директорию для распаковки. |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **13-15 правильных (87-100%)** | 🏆 Отлично! | Вы отлично знаете сжатие! |
| **10-12 правильных (67-86%)** | ✅ Хорошо | Повторите флаги tar. |
| **7-9 правильных (47-66%)** | ⚠️ Удовлетворительно | Перечитайте раздел о tar. |
| **Менее 7 правильных (<47%)** | 📚 Нужно повторить | Рекомендуется перечитать лекцию. |

---


