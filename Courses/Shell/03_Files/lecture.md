# Работа с файлами
## Команды cp, mv, rm, mkdir, touch и расширения shell

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Уметь навигировать по файловой системе (модуль [02_Navigation](../02_Navigation/))
- Понимать абсолютные и относительные пути
- Знать базовые команды `pwd`, `ls`, `cd`

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Использовать команды `cp`, `mv`, `rm` для управления файлами
- Создавать директории с помощью `mkdir` и файлы с помощью `touch`
- Применять glob-шаблоны для работы с множеством файлов
- Использовать brace expansion и tilde expansion для эффективной работы
- Понимать различия между различными способами расширения имён файлов

---

## 1. Копирование файлов — команда cp

Команда `cp` (copy) используется для копирования файлов и директорий.

### 1.1 Базовое копирование файла

**Example: Копирование одного файла**

```bash
# Создать тестовый файл
$ echo "Hello, World!" > source.txt

# Скопировать файл
$ cp source.txt destination.txt

# Проверить результат
$ ls -l *.txt
```

**Output:**
```

-rw-r--r-- 1 user user 14 Jan 15 10:00 destination.txt
-rw-r--r-- 1 user user 14 Jan 15 10:00 source.txt
```

Оба файла имеют одинаковое содержимое и размер.

**Example: Копирование в директорию**

```bash
# Создать директорию
$ mkdir backup

# Скопировать файл в директорию
$ cp source.txt backup/

# Проверить
$ ls backup/
```

**Output:**
```

source.txt
```

Когда вы указываете директорию как назначение, файл копируется с тем же именем.

### 1.2 Копирование нескольких файлов

**Example: Копирование нескольких файлов**

```bash
# Создать несколько файлов
$ touch file1.txt file2.txt file3.txt

# Скопировать все в директорию
$ cp file1.txt file2.txt file3.txt backup/

# Проверить
$ ls backup/
```

**Output:**
```

file1.txt  file2.txt  file3.txt  source.txt
```

Можно указать несколько исходных файлов, последний аргумент должен быть директорией назначения.

### 1.3 Рекурсивное копирование директорий

**Example: Копирование директории с содержимым**

```bash
# Создать структуру директорий
$ mkdir -p project/src project/tests
$ touch project/src/main.sh project/tests/test.sh

# Копировать всю директорию
$ cp -r project project_backup

# Проверить структуру
$ find project_backup -type f
```

**Output:**
```

project_backup/src/main.sh
project_backup/tests/test.sh
```

Опция `-r` (recursive) копирует директорию со всем содержимым рекурсивно.

**Example: Сохранение атрибутов**

```bash
# Копировать с сохранением прав доступа и времени модификации
$ cp -p source.txt backup/source.txt

# Или более полное сохранение всех атрибутов
$ cp -a project project_backup
```

Опция `-a` (archive) эквивалентна `-dR --preserve=all` и сохраняет все атрибуты файлов.

### 1.4 Интерактивный режим

**Example: Запрос подтверждения перед перезаписью**

```bash
# Если файл уже существует, cp спросит подтверждение
$ cp -i source.txt existing.txt
cp: overwrite 'existing.txt'? (y/n)
```

Опция `-i` (interactive) запрашивает подтверждение перед перезаписью существующих файлов.

> **⚠️ Warning:**  
> По умолчанию `cp` перезаписывает существующие файлы без предупреждения. Используйте `-i` для безопасности или `-n` (no-clobber) чтобы не перезаписывать.

---

## 2. Перемещение и переименование — команда mv

Команда `mv` (move) используется для перемещения файлов и директорий, а также для их переименования.

### 2.1 Переименование файла

**Example: Переименование файла**

```bash
# Создать файл
$ touch oldname.txt

# Переименовать
$ mv oldname.txt newname.txt

# Проверить
$ ls newname.txt
```

**Output:**
```

newname.txt
```

Файл `oldname.txt` больше не существует, он был переименован в `newname.txt`.

### 2.2 Перемещение файла

**Example: Перемещение файла в другую директорию**

```bash
# Создать файл и директорию
$ touch file.txt
$ mkdir target

# Переместить файл
$ mv file.txt target/

# Проверить
$ ls target/
```

**Output:**
```

file.txt
```

```bash
# Файл больше не в текущей директории
$ ls file.txt
ls: cannot access 'file.txt': No such file or directory
```

### 2.3 Перемещение нескольких файлов

**Example: Перемещение нескольких файлов**

```bash
# Создать несколько файлов
$ touch file1.txt file2.txt file3.txt
$ mkdir archive

# Переместить все файлы
$ mv file1.txt file2.txt file3.txt archive/

# Проверить
$ ls archive/
```

**Output:**
```

file1.txt  file2.txt  file3.txt
```

Как и с `cp`, можно указать несколько исходных файлов, последний аргумент — директория назначения.

### 2.4 Перемещение директорий

**Example: Перемещение директории**

```bash
# Создать директорию с содержимым
$ mkdir -p olddir/subdir
$ touch olddir/file.txt olddir/subdir/nested.txt

# Переместить директорию
$ mv olddir newdir

# Проверить структуру
$ find newdir -type f
```

**Output:**
```

newdir/file.txt
newdir/subdir/nested.txt
```

При перемещении директории всё её содержимое перемещается вместе с ней.

> **💡 Pro Tip:**  
> `mv` работает быстрее, чем `cp` + `rm`, так как при перемещении в пределах одной файловой системы только изменяется запись в каталоге, а не копируются данные.

---

## 3. Удаление — команда rm

Команда `rm` (remove) используется для удаления файлов и директорий.

### 3.1 Удаление файлов

**Example: Удаление одного файла**

```bash
# Создать файл
$ touch file.txt

# Удалить файл
$ rm file.txt

# Проверить
$ ls file.txt
ls: cannot access 'file.txt': No such file or directory
```

Файл был удалён безвозвратно.

**Example: Удаление нескольких файлов**

```bash
# Создать несколько файлов
$ touch file1.txt file2.txt file3.txt

# Удалить все
$ rm file1.txt file2.txt file3.txt

# Или использовать шаблон
$ touch file1.txt file2.txt file3.txt
$ rm file*.txt
```

### 3.2 Рекурсивное удаление директорий

**Example: Удаление директории с содержимым**

```bash
# Создать директорию с файлами
$ mkdir -p dir/subdir
$ touch dir/file1.txt dir/subdir/file2.txt

# Удалить директорию рекурсивно
$ rm -r dir

# Проверить
$ ls dir
ls: cannot access 'dir': No such file or directory
```

Опция `-r` (recursive) удаляет директорию и всё её содержимое.

**Example: Принудительное удаление**

```bash
# Удалить без запросов подтверждения
$ rm -rf directory/
```

Опция `-f` (force) принудительно удаляет файлы без запросов подтверждения, даже если файлы защищены от записи.

> **⚠️ Warning:**  
> `rm -rf` очень опасная команда! Она удаляет файлы безвозвратно без возможности восстановления. Будьте осторожны, особенно с путями вроде `rm -rf /` или `rm -rf ~`, которые могут удалить всю систему или домашний каталог.

### 3.3 Интерактивное удаление

**Example: Запрос подтверждения**

```bash
# Удалить с подтверждением
$ rm -i file.txt
rm: remove regular file 'file.txt'? y
```

Опция `-i` (interactive) запрашивает подтверждение перед удалением каждого файла.

### 3.4 Удаление пустых директорий

**Example: Удаление пустой директории**

```bash
# Создать пустую директорию
$ mkdir emptydir

# Удалить пустую директорию
$ rmdir emptydir

# Или использовать rm
$ mkdir emptydir
$ rm -d emptydir
```

Команда `rmdir` удаляет только пустые директории. Если директория не пуста, команда выдаст ошибку.

---

## 4. Создание директорий — команда mkdir

Команда `mkdir` (make directory) создаёт новые директории.

### 4.1 Создание одной директории

**Example: Создание директории**

```bash
# Создать директорию
$ mkdir newdir

# Проверить
$ ls -d newdir
```

**Output:**
```

newdir
```

### 4.2 Создание нескольких директорий

**Example: Создание нескольких директорий**

```bash
# Создать несколько директорий одновременно
$ mkdir dir1 dir2 dir3

# Проверить
$ ls -d dir*
```

**Output:**
```

dir1  dir2  dir3
```

### 4.3 Создание вложенных директорий

**Example: Создание структуры директорий**

```bash
# Создать директорию с родительскими директориями
$ mkdir -p path/to/newdir

# Проверить структуру
$ find path -type d
```

**Output:**
```

path
path/to
path/to/newdir
```

Опция `-p` (parents) создаёт все необходимые родительские директории, если они не существуют.

**Example: Создание сложной структуры**

```bash
# Создать структуру проекта
$ mkdir -p project/{src,tests,docs}/{main,utils}

# Проверить
$ tree project/ 2>/dev/null || find project -type d | sort
```

**Output:**
```

project/
project/docs
project/docs/main
project/docs/utils
project/src
project/src/main
project/src/utils
project/tests
project/tests/main
project/tests/utils
```

Здесь используется brace expansion (будет рассмотрено позже).

### 4.4 Установка прав при создании

**Example: Создание директории с определёнными правами**

```bash
# Создать директорию с правами 700 (только владелец)
$ mkdir -m 700 privatedir

# Проверить права
$ ls -ld privatedir
```

**Output:**
```

drwx------ 2 user user 4096 Jan 15 10:00 privatedir
```

Опция `-m` (mode) устанавливает права доступа при создании директории.

---

## 5. Создание файлов — команда touch

Команда `touch` создаёт пустые файлы или обновляет время модификации существующих файлов.

### 5.1 Создание пустого файла

**Example: Создание нового файла**

```bash
# Создать пустой файл
$ touch newfile.txt

# Проверить
$ ls -l newfile.txt
```

**Output:**
```

-rw-r--r-- 1 user user 0 Jan 15 10:00 newfile.txt
```

Файл создан с размером 0 байт.

### 5.2 Создание нескольких файлов

**Example: Создание нескольких файлов**

```bash
# Создать несколько файлов
$ touch file1.txt file2.txt file3.txt

# Проверить
$ ls -l file*.txt
```

**Output:**
```

-rw-r--r-- 1 user user 0 Jan 15 10:00 file1.txt
-rw-r--r-- 1 user user 0 Jan 15 10:00 file2.txt
-rw-r--r-- 1 user user 0 Jan 15 10:00 file3.txt
```

### 5.3 Обновление времени модификации

**Example: Обновление времени существующего файла**

```bash
# Создать файл
$ touch oldfile.txt
$ sleep 2

# Обновить время модификации
$ touch oldfile.txt

# Проверить время (должно быть обновлено)
$ stat oldfile.txt | grep Modify
```

**Output:**
```

Modify: 2024-01-15 10:00:02.000000000 +0000
```

Если файл уже существует, `touch` обновляет его время модификации и доступа до текущего времени.

### 5.4 Установка конкретного времени

**Example: Установка времени модификации**

```bash
# Создать файл с определённым временем
$ touch -t 202401011200 file.txt

# Проверить
$ ls -l file.txt
```

**Output:**
```

-rw-r--r-- 1 user user 0 Jan  1 12:00 file.txt
```

Опция `-t` позволяет установить конкретное время в формате `[[CC]YY]MMDDhhmm[.ss]`.

---

## 6. Glob-шаблоны (Globbing)

**Globbing** — это механизм shell для сопоставления имён файлов с шаблонами. Это не регулярные выражения, а более простой паттерн-матчинг.

### 6.1 Базовые шаблоны

**Example: Звёздочка (*)**

```bash
# Создать файлы
$ touch file1.txt file2.txt file3.log file4.txt

# Найти все .txt файлы
$ ls *.txt
```

**Output:**
```

file1.txt  file2.txt  file4.txt
```

Символ `*` соответствует любому количеству любых символов (кроме начальной точки в скрытых файлах).

**Example: Вопросительный знак (?)**

```bash
# Создать файлы
$ touch file1.txt file2.txt file10.txt

# Найти файлы с одним символом перед .txt
$ ls file?.txt
```

**Output:**
```

file1.txt  file2.txt
```

Символ `?` соответствует ровно одному символу.

### 6.2 Классы символов

**Example: Квадратные скобки []**

```bash
# Создать файлы
$ touch file1.txt file2.txt file3.txt filea.txt

# Найти файлы, где цифра от 1 до 3
$ ls file[1-3].txt
```

**Output:**
```

file1.txt  file2.txt  file3.txt
```

`[1-3]` соответствует одному символу из диапазона от 1 до 3.

**Example: Несколько диапазонов**

```bash
# Создать файлы
$ touch file1.txt file2.txt filea.txt fileb.txt

# Найти файлы с цифрой или буквой
$ ls file[1-9a-z].txt
```

**Output:**
```

file1.txt  file2.txt  filea.txt  fileb.txt
```

### 6.3 Отрицание в классах

**Example: Исключение символов**

```bash
# Создать файлы
$ touch file1.txt file2.txt filea.txt

# Найти файлы, где НЕ цифра
$ ls file[!0-9].txt
```

**Output:**
```

filea.txt
```

`[!0-9]` соответствует любому символу, кроме цифр от 0 до 9.

### 6.4 Вложенные директории

**Example: Glob в поддиректориях**

```bash
# Создать структуру
$ mkdir -p dir1 dir2
$ touch dir1/file.txt dir2/file.txt

# Найти все .txt файлы рекурсивно
$ ls */file.txt
```

**Output:**
```

dir1/file.txt  dir2/file.txt
```

Glob работает и с путями к файлам в поддиректориях.

> **💡 Pro Tip:**  
> Для рекурсивного поиска используйте `find` или включите опцию `globstar` в bash: `shopt -s globstar` и используйте `**/*.txt`.

---

## 7. Brace Expansion

**Brace expansion** — это механизм bash для генерации строк. Это происходит до других расширений.

### 7.1 Базовое использование

**Example: Простое расширение**

```bash
# Расширение создаёт несколько вариантов
$ echo file{1,2,3}.txt
```

**Output:**
```

file1.txt file2.txt file3.txt
```

Brace expansion генерирует все возможные комбинации.

**Example: Создание файлов через brace expansion**

```bash
# Создать несколько файлов одной командой
$ touch file{1,2,3}.txt

# Проверить
$ ls file*.txt
```

**Output:**
```

file1.txt  file2.txt  file3.txt
```

### 7.2 Диапазоны

**Example: Числовые диапазоны**

```bash
# Создать файлы от 1 до 5
$ touch file{1..5}.txt

# Проверить
$ ls file*.txt
```

**Output:**
```

file1.txt  file2.txt  file3.txt  file4.txt  file5.txt
```

`{1..5}` генерирует последовательность от 1 до 5.

**Example: Буквенные диапазоны**

```bash
# Создать файлы от a до c
$ touch file{a..c}.txt

# Проверить
$ ls file*.txt
```

**Output:**
```

filea.txt  fileb.txt  filec.txt
```

### 7.3 Вложенные расширения

**Example: Вложенные brace expansion**

```bash
# Создать комбинации
$ echo {a,b}{1,2}
```

**Output:**
```

a1 a2 b1 b2
```

Каждый элемент первого набора комбинируется с каждым элементом второго.

**Example: Создание структуры проекта**

```bash
# Создать структуру директорий
$ mkdir -p project/{src,tests}/{main,utils}

# Проверить
$ find project -type d | sort
```

**Output:**
```

project
project/src
project/src/main
project/src/utils
project/tests
project/tests/main
project/tests/utils
```

### 7.4 С шагом

**Example: Диапазон с шагом**

```bash
# Создать файлы с шагом 2
$ touch file{1..10..2}.txt

# Проверить
$ ls file*.txt
```

**Output:**
```

file1.txt  file3.txt  file5.txt  file7.txt  file9.txt
```

`{1..10..2}` генерирует числа от 1 до 10 с шагом 2.

---

## 8. Tilde Expansion

**Tilde expansion** — это расширение символа `~` до пути к домашнему каталогу.

### 8.1 Базовое использование

**Example: Домашний каталог**

```bash
# ~ расширяется до домашнего каталога
$ echo ~
```

**Output:**
```

/home/user
```

### 8.2 Домашний каталог другого пользователя

**Example: Домашний каталог другого пользователя**

```bash
# Домашний каталог пользователя john
$ echo ~john
```

**Output:**
```

/home/john
```

`~username` расширяется до домашнего каталога указанного пользователя.

### 8.3 В путях

**Example: Использование в путях**

```bash
# Перейти в поддиректорию домашнего каталога
$ cd ~/Documents

# Или создать файл
$ touch ~/myfile.txt

# Проверить
$ ls ~/myfile.txt
```

**Output:**
```

/home/user/myfile.txt
```

Tilde expansion работает в любом месте пути.

### 8.4 Текущий и предыдущий каталог

**Example: Специальные значения**

```bash
# ~+ расширяется до текущего каталога (как $PWD)
$ echo ~+
```

**Output:**
```

/home/user/Documents
```

```bash
# ~- расширяется до предыдущего каталога (как $OLDPWD)
$ cd /tmp
$ echo ~-
```

**Output:**
```

/home/user/Documents
```

---

## 9. Комбинация расширений

Различные типы расширений можно комбинировать для создания мощных конструкций.

### 9.1 Glob с brace expansion

**Example: Комбинация glob и brace**

```bash
# Создать файлы
$ touch file{1,2,3}.txt data{1,2}.log

# Найти все .txt файлы, созданные через brace expansion
$ ls file{1,2,3}.txt
```

**Output:**
```

file1.txt  file2.txt  file3.txt
```

### 9.2 Brace expansion в путях

**Example: Работа с несколькими директориями**

```bash
# Создать структуру
$ mkdir -p ~/projects/{web,api,mobile}

# Создать файлы в каждой директории
$ touch ~/projects/{web,api,mobile}/README.md

# Проверить
$ ls ~/projects/*/README.md
```

**Output:**
```

/home/user/projects/api/README.md
/home/user/projects/mobile/README.md
/home/user/projects/web/README.md
```

---

## 10. Практические примеры

Рассмотрим несколько реальных сценариев использования.

### 10.1 Example: Резервное копирование

```bash
# Создать резервную копию проекта
$ mkdir -p ~/backups/$(date +%Y%m%d)
$ cp -r ~/projects/myproject ~/backups/$(date +%Y%m%d)/
```

### 10.2 Example: Организация файлов

```bash
# Создать структуру для проекта
$ mkdir -p project/{src/{main,utils},tests,docs}
$ touch project/src/{main,utils}/*.sh project/tests/*.sh
```

### 10.3 Example: Массовое переименование

```bash
# Переименовать файлы с помощью цикла (будет рассмотрено позже)
$ for file in file{1..5}.txt; do
    mv "$file" "backup_$file"
  done
```

---

## 💡 Key Takeaways

- **cp** копирует файлы и директории, поддерживает рекурсивное копирование (`-r`) и сохранение атрибутов (`-a`)

- **mv** перемещает или переименовывает файлы и директории, работает быстрее чем cp+rm в пределах одной файловой системы

- **rm** удаляет файлы и директории, требует осторожности, особенно с опцией `-rf`

- **mkdir** создаёт директории, опция `-p` создаёт родительские директории при необходимости

- **touch** создаёт пустые файлы или обновляет время модификации существующих

- **Glob-шаблоны** (`*`, `?`, `[]`) позволяют работать с множеством файлов по паттернам

- **Brace expansion** (`{}`) генерирует комбинации строк, полезен для создания структуры

- **Tilde expansion** (`~`) расширяется до домашнего каталога, упрощает работу с путями

---

## 🚀 Next Steps

**Related Modules:**

- [04_Streams_Pipes](../04_Streams_Pipes/) — перенаправление потоков и pipes
- [05_Bash_Language](../05_Bash_Language/) — bash как язык программирования

**Practice Ideas:**

1. Создайте структуру проекта используя brace expansion: `mkdir -p project/{src,tests,docs}`
2. Попрактикуйтесь в копировании и перемещении файлов между директориями
3. Используйте glob-шаблоны для поиска и работы с группами файлов
4. Создайте резервную копию важных файлов используя изученные команды

**Going Deeper:**

- Изучите права доступа к файлам (chmod, chown)
- Узнайте о символических и жёстких ссылках (ln)
- Изучите команду `find` для более сложного поиска файлов

---

## 📚 Additional Resources

**Documentation:**

- [GNU Coreutils: cp](https://www.gnu.org/software/coreutils/manual/html_node/cp-invocation.html)
- [GNU Coreutils: mv](https://www.gnu.org/software/coreutils/manual/html_node/mv-invocation.html)
- [Bash Manual: Brace Expansion](https://www.gnu.org/software/bash/manual/html_node/Brace-Expansion.html)

**Articles & Tutorials:**

- [File Operations in Linux](https://tldp.org/LDP/intro-linux/html/sect_03_03.html) — работа с файлами в Linux
- [Bash Globbing Tutorial](https://www.linuxjournal.com/content/bash-extended-globbing) — расширенное globbing


