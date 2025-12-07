# CLI Tools - Тест

---

## Вопрос 1: samtools view

Команда `samtools view -F 4` выводит:

A) Unmapped reads  
B) Mapped reads  
C) Первые 4 рида  
D) Риды с качеством >4  

---

## Вопрос 2: bcftools

Какой инструмент используется для работы с VCF файлами?

A) samtools  
B) bcftools  
C) bedtools  
D) seqtk  

---

## Вопрос 3: bedtools intersect

`bedtools intersect -a A.bed -b B.bed -v` выводит:

A) Пересечения A и B  
B) Регионы из A, которые НЕ пересекаются с B  
C) Регионы из B  
D) Объединение A и B  

---

## Вопрос 4: Индексация

Какая команда создаёт индекс для BAM файла?

A) samtools index  
B) samtools sort  
C) samtools view  
D) samtools faidx  

---

## Вопрос 5: Фильтрация VCF

Как оставить только PASS варианты?

A) bcftools view -f PASS  
B) bcftools filter PASS  
C) bcftools view -p PASS  
D) bcftools select PASS  

---

## Вопрос 6: Coverage

Какой инструмент подсчитывает покрытие BAM по BED регионам?

A) samtools coverage  
B) bedtools coverage  
C) bcftools coverage  
D) Все вышеперечисленные  

---

## Вопрос 7: seqtk

seqtk используется для:

A) Выравнивания ридов  
B) Обработки FASTA/FASTQ файлов  
C) Вызова вариантов  
D) Аннотации  

---

## Вопрос 8: Pipe

Что делает `|` (pipe) в bash?

A) Сохраняет вывод в файл  
B) Передаёт вывод одной команды на вход другой  
C) Комментирует строку  
D) Объединяет файлы  

---

## Вопрос 9: Сортировка BAM

Почему важно сортировать BAM файл?

A) Для уменьшения размера  
B) Для индексации и быстрого доступа к регионам  
C) Для улучшения качества  
D) Для удаления дубликатов  

---

## Вопрос 10: bgzip

В чём отличие bgzip от обычного gzip?

A) bgzip быстрее  
B) bgzip позволяет индексацию (block-compressed)  
C) bgzip лучше сжимает  
D) Нет различий  

---

## Ключ к Ответам

1. **B** - `-F 4` исключает unmapped, т.е. выводит mapped
2. **B** - bcftools для VCF/BCF файлов
3. **B** - `-v` выводит регионы из A без пересечений с B
4. **A** - `samtools index` создаёт .bai индекс
5. **A** - `bcftools view -f PASS` фильтрует по PASS
6. **B** - bedtools coverage
7. **B** - seqtk для FASTA/FASTQ
8. **B** - pipe передаёт stdout → stdin
9. **B** - для индексации и random access
10. **B** - bgzip block-compressed, позволяет индексацию

---

## Шкала Оценивания

- **8-10**: Отлично!
- **6-7**: Хорошо!
- **4-5**: Удовлетворительно
- **<4**: Повторите материал

Happy learning! 🧬

