# Потоки и pipes
## Перенаправление ввода/вывода и объединение команд

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Уметь работать с файлами (модуль [03_Files](../03_Files/))
- Понимать базовые команды shell
- Знать концепцию стандартных потоков

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Понимать три стандартных потока: stdin, stdout, stderr
- Использовать перенаправление вывода (`>`, `>>`) и ввода (`<`)
- Объединять команды с помощью pipes (`|`)
- Управлять процессами в фоне (job control)
- Использовать coprocesses для параллельной обработки

---

## 1. Стандартные потоки

В Unix-подобных системах каждая программа имеет три стандартных потока данных.

### 1.1 Три потока

**stdin** (standard input) — поток ввода, по умолчанию клавиатура  
**stdout** (standard output) — поток вывода, по умолчанию экран  
**stderr** (standard error) — поток ошибок, по умолчанию экран

**Example: Базовые потоки**

```bash
# Команда читает из stdin и пишет в stdout
$ echo "Hello"
Hello
```

**Output:**
```

Hello
```

Команда `echo` выводит текст в stdout, который по умолчанию отображается на экране.

**Example: Разделение stdout и stderr**

```bash
# Создать файл
$ touch test.txt

# Успешная команда (stdout)
$ ls test.txt
test.txt

# Ошибка (stderr)
$ ls nonexistent.txt
ls: cannot access 'nonexistent.txt': No such file or directory
```

Оба потока по умолчанию идут на экран, но их можно перенаправлять отдельно.

### 1.2 Дескрипторы файлов

В Unix каждый поток имеет числовой дескриптор:

- `0` — stdin
- `1` — stdout  
- `2` — stderr

**Example: Использование дескрипторов**

```bash
# Явное указание stdout (эквивалентно просто >)
$ echo "Hello" 1> output.txt

# Перенаправление stderr
$ ls nonexistent.txt 2> error.txt
$ cat error.txt
```

**Output:**
```

ls: cannot access 'nonexistent.txt': No such file or directory
```

---

## 2. Перенаправление вывода

Перенаправление позволяет отправлять вывод команд в файлы вместо экрана.

### 2.1 Перезапись (>)

**Example: Перенаправление в файл**

```bash
# Создать файл с содержимым
$ echo "Hello, World!" > output.txt

# Проверить содержимое
$ cat output.txt
```

**Output:**
```

Hello, World!
```

Символ `>` перенаправляет stdout в файл. Если файл существует, он перезаписывается.

**Example: Перезапись существующего файла**

```bash
# Создать файл
$ echo "First line" > file.txt

# Перезаписать
$ echo "Second line" > file.txt

# Проверить
$ cat file.txt
```

**Output:**
```

Second line
```

Старое содержимое файла было потеряно.

### 2.2 Добавление (>>)

**Example: Добавление в конец файла**

```bash
# Создать файл
$ echo "First line" > file.txt

# Добавить строку
$ echo "Second line" >> file.txt

# Проверить
$ cat file.txt
```

**Output:**
```

First line
Second line
```

Символ `>>` добавляет вывод в конец файла, не перезаписывая его.

**Example: Построчное добавление**

```bash
# Добавить несколько строк
$ echo "Line 1" > log.txt
$ echo "Line 2" >> log.txt
$ echo "Line 3" >> log.txt

# Проверить
$ cat log.txt
```

**Output:**
```

Line 1
Line 2
Line 3
```

### 2.3 Перенаправление stderr

**Example: Отдельное перенаправление ошибок**

```bash
# Перенаправить только stderr
$ ls nonexistent.txt 2> error.log

# Проверить файл ошибок
$ cat error.log
```

**Output:**
```

ls: cannot access 'nonexistent.txt': No such file or directory
```

Дескриптор `2` указывает на stderr.

**Example: Перенаправление обоих потоков**

```bash
# Перенаправить stdout и stderr в разные файлы
$ ls existing.txt nonexistent.txt > output.log 2> error.log

# Или оба в один файл
$ ls existing.txt nonexistent.txt > all.log 2>&1
```

`2>&1` означает "перенаправить stderr туда же, куда и stdout".

---

## 3. Перенаправление ввода

Перенаправление ввода позволяет читать данные из файла вместо клавиатуры.

### 3.1 Базовое перенаправление ввода (<)

**Example: Чтение из файла**

```bash
# Создать файл
$ echo "Hello, World!" > input.txt

# Передать файл в команду
$ cat < input.txt
```

**Output:**
```

Hello, World!
```

Символ `<` перенаправляет stdin из файла.

**Example: Использование с командами**

```bash
# Создать файл с числами
$ echo -e "1\n2\n3" > numbers.txt

# Подсчитать строки
$ wc -l < numbers.txt
```

**Output:**
```

3
```

Команда `wc -l` считает строки из stdin.

### 3.2 Here Documents (<<)

**Here document** позволяет передать многострочный текст в команду.

**Example: Here document**

```bash
# Передать текст в команду
$ cat << EOF
Line 1
Line 2
Line 3
EOF
```

**Output:**
```

Line 1
Line 2
Line 3
```

Текст между `<< EOF` и `EOF` передаётся в stdin команды.

**Example: Использование в скриптах**

```bash
# Создать файл через here document
$ cat > script.sh << 'SCRIPT'
#!/bin/bash
echo "Hello from script"
SCRIPT

# Проверить
$ cat script.sh
```

**Output:**
```
#!/bin/bash
echo "Hello from script"
```

### 3.3 Here Strings (<<<)

**Here string** — короткая версия here document для одной строки.

**Example: Here string**

```bash
# Передать строку в команду
$ cat <<< "Hello, World!"
```

**Output:**
```

Hello, World!
```

`<<<` передаёт строку в stdin команды.

---

## 4. Pipes (|)

**Pipe** (конвейер) позволяет передать stdout одной команды в stdin другой.

### 4.1 Базовое использование pipe

**Example: Простой pipe**

```bash
# Передать вывод ls в grep
$ ls /usr/bin | grep bash
```

**Output:**
```

bash
bashbug
```

Вывод `ls` передаётся в `grep`, который фильтрует строки, содержащие "bash".

**Example: Цепочка команд**

```bash
# Создать файл с данными
$ echo -e "apple\nbanana\ncherry\ndate" > fruits.txt

# Подсчитать строки, содержащие 'a'
$ cat fruits.txt | grep a | wc -l
```

**Output:**
```

3
```

Цепочка: `cat` → `grep` → `wc`.

### 4.2 Комбинация с перенаправлением

**Example: Pipe с перенаправлением**

```bash
# Передать через pipe и сохранить результат
$ ls /usr/bin | grep bash > bash_files.txt

# Проверить
$ cat bash_files.txt
```

**Output:**
```

bash
bashbug
```

Можно комбинировать pipes с перенаправлением в файлы.

**Example: Сложная цепочка**

```bash
# Создать файл
$ echo -e "1\n2\n3\n4\n5" > numbers.txt

# Фильтровать, сортировать, сохранить
$ cat numbers.txt | grep "[2-4]" | sort -r > filtered.txt

# Проверить
$ cat filtered.txt
```

**Output:**
```

4
3
2
```

---

## 5. Job Control

**Job control** позволяет управлять процессами: запускать в фоне, переводить между передним и задним планом.

### 5.1 Запуск в фоне (&)

**Example: Запуск процесса в фоне**

```bash
# Запустить команду в фоне
$ sleep 10 &

# Проверить фоновые процессы
$ jobs
```

**Output:**
```

[1]+  Running                 sleep 10 &
```

Символ `&` запускает команду в фоновом режиме.

**Example: Запуск с перенаправлением**

```bash
# Запустить в фоне с перенаправлением
$ find /usr -name "*.txt" > results.txt 2> errors.txt &

# Проверить статус
$ jobs
```

### 5.2 Управление задачами

**Example: Команды job control**

```bash
# Запустить процесс в фоне
$ sleep 30 &

# Показать задачи
$ jobs
[1]+  Running                 sleep 30 &

# Перевести в передний план
$ fg

# Или по номеру задачи
$ fg %1
```

**Example: Переключение между задачами**

```bash
# Запустить два процесса
$ sleep 20 &
$ sleep 30 &

# Показать задачи
$ jobs
[1]-  Running                 sleep 20 &
[2]+  Running                 sleep 30 &

# Перевести задачу 1 в передний план
$ fg %1
# Нажмите Ctrl+Z для приостановки

# Вернуть в фон
$ bg %1
```

### 5.3 nohup

**nohup** позволяет запустить команду, которая продолжит работу после закрытия терминала.

**Example: Использование nohup**

```bash
# Запустить долгую команду
$ nohup find / -name "*.log" > results.log 2>&1 &

# Проверить
$ jobs
```

Процесс продолжит работу даже после закрытия терминала.

---

## 6. Coprocesses (coproc)

**Coprocesses** позволяют запустить команду как фоновый процесс и обмениваться с ней данными через pipes.

### 6.1 Базовое использование coproc

**Example: Простой coprocess**

```bash
# Запустить coprocess
$ coproc MYPROC { cat; }

# Отправить данные
$ echo "Hello" >&${MYPROC[1]}

# Прочитать результат
$ read -u ${MYPROC[0]} result
$ echo "$result"
```

**Output:**
```

Hello
```

Coprocess позволяет двустороннюю коммуникацию с процессом.

---

## 7. Расширенное перенаправление

Bash поддерживает более сложные формы перенаправления.

### 7.1 Перенаправление обоих потоков

**Example: &> и >&**

```bash
# Перенаправить stdout и stderr в один файл
$ ls existing.txt nonexistent.txt &> all.log

# Эквивалентно
$ ls existing.txt nonexistent.txt > all.log 2>&1
```

`&>` — сокращение для перенаправления обоих потоков.

### 7.2 Process Substitution

**Process substitution** позволяет использовать вывод команды как файл.

**Example: <() и >()**

```bash
# Сравнить вывод двух команд
$ diff <(ls /bin) <(ls /usr/bin)
```

`<(command)` создаёт именованный pipe с выводом команды.

---

## 💡 Key Takeaways

- **Три стандартных потока**: stdin (0), stdout (1), stderr (2) — основа работы с данными в shell

- **Перенаправление вывода**: `>` перезаписывает файл, `>>` добавляет в конец

- **Перенаправление ввода**: `<` читает из файла, `<<` (here document) передаёт многострочный текст

- **Pipes (`|`)**: Объединяют команды, передавая stdout одной в stdin другой

- **Job control**: Управление процессами через `&`, `fg`, `bg`, `jobs`, `nohup`

- **Coprocesses**: Двусторонняя коммуникация с фоновыми процессами

---

## 🚀 Next Steps

**Related Modules:**

- [05_Bash_Language](../05_Bash_Language/) — bash как язык программирования
- [09_Text_Processing](../09_Text_Processing/) — работа с текстом (grep, sed, awk)

**Practice Ideas:**

1. Создайте цепочку команд с pipes для обработки данных
2. Попрактикуйтесь в перенаправлении stdout и stderr в разные файлы
3. Запустите процессы в фоне и управляйте ими через job control
4. Используйте here documents для создания конфигурационных файлов

**Going Deeper:**

- Изучите именованные pipes (FIFO)
- Узнайте о process substitution подробнее
- Изучите сигналы и их обработку в процессах

---

## 📚 Additional Resources

**Documentation:**

- [Bash Manual: Redirections](https://www.gnu.org/software/bash/manual/html_node/Redirections.html)
- [Bash Manual: Pipelines](https://www.gnu.org/software/bash/manual/html_node/Pipelines.html)

**Articles & Tutorials:**

- [I/O Redirection](https://tldp.org/LDP/abs/html/io-redirection.html) — подробное руководство по перенаправлению
- [Pipes and Filters](https://swcarpentry.github.io/shell-novice/04-pipefilter/) — работа с pipes


