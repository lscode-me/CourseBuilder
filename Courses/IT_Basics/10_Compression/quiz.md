# Compression - Quiz

Проверьте свои знания по теме "Сжатие данных".

---

## Question 1: Типы сжатия




Какой тип сжатия используется для текстовых файлов?

A) Partial

B) Lossy

C) Hybrid

D) Lossless

---

## Question 2: gzip команда




Какая команда сжимает файл с gzip?

A) gzip file.txt

B) `compress file.txt`

C) `pack file.txt`

D) `zip file.txt`

---

## Question 3: Распаковка gzip




Какая команда распаковывает .gz файл?

A) `unzip file.txt.gz`

B) `ungzip file.txt.gz`

C) `extract file.txt.gz`

D) gunzip file.txt.gz

---

## Question 4: tar назначение




Что делает tar?

A) Шифрует файлы

B) Объединяет файлы в один архив

C) Сжимает файлы

D) Удаляет дубликаты

---

## Question 5: tar + gzip




Какой флаг tar использует gzip сжатие?

A) `-c`

B) `-g`

C) -z

D) `-Z`

---

## Question 6: tar создание




Какая команда создаёт tar.gz архив?

A) tar -czvf archive.tar.gz dir/

B) `tar -xzvf archive.tar.gz dir/`

C) `tar -tzvf archive.tar.gz dir/`

D) `tar -azvf archive.tar.gz dir/`

---

## Question 7: tar распаковка




Какой флаг tar извлекает файлы?

A) `-t`

B) -x

C) `-c`

D) `-r`

---

## Question 8: bzip2 расширение




Какое расширение у файлов сжатых bzip2?

A) `.bz`

B) `.bzip`

C) .bz2

D) `.b2`

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

A) -j

B) `-2`

C) `-b`

D) `-B`

---

## Question 11: zcat




Что делает команда zcat?

A) Показывает содержимое .gz файла без распаковки

B) Проверяет целостность архива

C) Создаёт zip архив

D) Конкатенирует zip файлы

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

B) `gzip.read('file.gz')`

C) `open('file.gz', 'gz')`

D) gzip.open('file.gz', 'rt')

---

## Question 14: ZIP vs tar




Что верно о ZIP по сравнению с tar.gz?

A) ZIP позволяет извлекать отдельные файлы без полной распаковки

B) ZIP только для Windows

C) ZIP не поддерживает директории

D) ZIP не поддерживает сжатие

---

## Question 15: tar xz флаг




Какой флаг tar использует xz сжатие?

A) `-x`

B) `-X`

C) `-Z`

D) -J

---

## Question 16: zstd




Что характерно для формата zstd?

A) Отличное соотношение сжатие/скорость (современный стандарт)

B) Самое медленное сжатие

C) Только для Windows

D) Не поддерживает потоковое сжатие

---

## Question 17: Python tarfile




Как создать tar.gz архив в Python?

A) `tarfile.create('archive.tar.gz')`

B) `tar.gz('archive.tar.gz')`

C) tarfile.open('archive.tar.gz', 'w:gz')

D) `tarfile.write('archive.tar.gz')`

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
| 1 | D | Lossless (без потерь) используется для текста, кода, данных. Lossy — для медиа. |
| 2 | A | `gzip file.txt` сжимает файл, создаёт file.txt.gz. |
| 3 | D | `gunzip` или `gzip -d` распаковывает .gz файлы. |
| 4 | B | tar (tape archive) объединяет файлы без сжатия. |
| 5 | C | `-z` активирует gzip сжатие в tar. |
| 6 | A | `-c` создаёт, `-z` gzip, `-v` verbose, `-f` файл. |
| 7 | B | `-x` (extract) извлекает файлы из архива. |
| 8 | C | bzip2 создаёт файлы с расширением .bz2. |
| 9 | A | xz (LZMA2) обеспечивает лучшее сжатие, но медленнее. |
| 10 | A | `-j` активирует bzip2 в tar. |
| 11 | A | `zcat` выводит содержимое .gz без распаковки на диск. |
| 12 | B | `-k` (keep) сохраняет оригинальный файл после сжатия. |
| 13 | D | `'rt'` = read text, для текстовых файлов с кодировкой. |
| 14 | A | ZIP поддерживает random access — можно извлечь один файл. |
| 15 | D | `-J` (заглавная) активирует xz сжатие в tar. |
| 16 | A | zstd (Zstandard) — современный алгоритм с отличным балансом. |
| 17 | C | `tarfile.open('file.tar.gz', 'w:gz')` — создание tar.gz. |
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

