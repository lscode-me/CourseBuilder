# UNIX и его философия

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать основы операционных систем (процессы, файлы, системные вызовы)
- Знать концепцию time-sharing систем
- Иметь представление о командной строке

**Recommended prior modules:**

- [02_OperatingSystems](../02_OperatingSystems/) — появление операционных систем

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Объяснить происхождение UNIX и его влияние на современные ОС
- Понимать философию UNIX: "всё — файл", минимализм, композиция
- Описать работу процессов и pipes в UNIX
- Объяснить наследие UNIX в современных системах

---

## 1. Происхождение UNIX

### 1.1 Создание UNIX

**UNIX** был создан в Bell Labs (AT&T) в 1969-1970 годах Кеном Томпсоном и Деннисом Ритчи.

**Контекст:**

- Проект Multics был слишком сложным и дорогим
- Нужна была простая система для разработки
- Первая версия написана на ассемблере для PDP-7

**Ключевые решения:**

- Простота вместо сложности
- Малый размер системы
- Переносимость (переписан на C в 1973)

### 1.2 Распространение UNIX

**Лицензирование:**

- Изначально распространялся с исходным кодом
- Университеты получили лицензии за символическую плату
- Это способствовало быстрому распространению и развитию

**Влияние:**

- Стал основой для многих операционных систем
- Влиял на развитие программного обеспечения
- Создал культуру открытого исходного кода

---

## 2. Философия UNIX

### 2.1 "Всё — файл"

**Принцип:**
В UNIX почти всё представлено как файл:

- Обычные файлы
- Директории
- Устройства (/dev)
- Процессы (/proc)
- Сетевые соединения
- И многое другое

**Преимущества:**

- Единый интерфейс для работы с разными ресурсами
- Простота программирования
- Композиция: программы могут работать с любыми "файлами"

**Пример:**
```bash
# Чтение из устройства как из файла

cat /dev/random

# Чтение информации о процессе

cat /proc/1/status
```

### 2.2 Минимализм

**Принцип:**

- Каждая программа делает одну вещь хорошо
- Программы маленькие и сфокусированные
- Сложность достигается композицией простых программ

**Примеры:**

- `cat` — выводит содержимое файла
- `grep` — ищет текст
- `sort` — сортирует строки
- `wc` — считает слова/строки

**Композиция:**
```bash
# Композиция простых программ для сложной задачи

cat file.txt | grep "error" | sort | uniq | wc -l
```

### 2.3 Композиция через pipes

**Pipes (|)** — механизм передачи вывода одной программы на вход другой.

**Преимущества:**

- Программы не нужно модифицировать для работы вместе
- Гибкость: можно комбинировать программы разными способами
- Простота: каждая программа остаётся простой

**Пример:**
```bash
# Найти все файлы .txt, отсортировать, показать первые 10

find . -name "*.txt" | sort | head -10
```

---

## 3. Процессы в UNIX

### 3.1 Концепция процесса

**Процесс** — выполняющаяся программа с изолированными ресурсами.

**Характеристики:**

- Собственное адресное пространство
- Собственные файловые дескрипторы
- Собственный идентификатор (PID)

### 3.2 Создание процессов

**fork()** — системный вызов для создания нового процесса.

**Как работает:**

1. Текущий процесс клонируется
2. Создаётся точная копия (дочерний процесс)
3. Оба процесса продолжают выполнение с того же места
4. Различаются только возвращаемым значением fork()

**Пример: fork() в деталях**

```c
#include <unistd.h>
#include <stdio.h>
#include <sys/wait.h>

int main() {
    printf("Before fork: PID=%d\n", getpid());
    
    pid_t pid = fork();
    
    if (pid == 0) {
        // Дочерний процесс
        printf("Child: PID=%d, Parent PID=%d\n", 
               getpid(), getppid());
    } else if (pid > 0) {
        // Родительский процесс
        printf("Parent: PID=%d, Child PID=%d\n", 
               getpid(), pid);
        wait(NULL);  // Ждать завершения дочернего процесса
    } else {
        // Ошибка
        perror("fork failed");
        return 1;
    }
    
    return 0;
}
```

**exec()** — системный вызов для замены программы в процессе.

**Пример: exec() семейство**

```c
#include <unistd.h>

// exec() семейство функций
execl("/bin/ls", "ls", "-l", NULL);           // Список аргументов
execv("/bin/ls", argv);                        // Массив аргументов
execlp("ls", "ls", "-l", NULL);                // Поиск в PATH
execvp("ls", argv);                            // PATH + массив
execle("/bin/ls", "ls", NULL, envp);           // С переменными окружения
execve("/bin/ls", argv, envp);                 // Полный контроль
```

**Типичный паттерн:**
```c

pid_t pid = fork();
if (pid == 0) {
    // Дочерний процесс
    execl("/bin/ls", "ls", "-l", NULL);
    // Если exec() успешен, этот код не выполнится
    perror("exec failed");
    exit(1);
} else if (pid > 0) {
    // Родительский процесс
    int status;
    waitpid(pid, &status, 0);  // Ждать завершения
    if (WIFEXITED(status)) {
        printf("Child exited with code %d\n", WEXITSTATUS(status));
    }
} else {
    perror("fork failed");
}
```

### 3.3 Коммуникация процессов

**Механизмы:**

**1. Pipes** — однонаправленная коммуникация

**Пример: Anonymous pipe**

```c
#include <unistd.h>

int pipefd[2];
pipe(pipefd);  // pipefd[0] - read, pipefd[1] - write

pid_t pid = fork();
if (pid == 0) {
    // Дочерний процесс - пишет
    close(pipefd[0]);  // Закрыть read end
    write(pipefd[1], "Hello", 5);
    close(pipefd[1]);
} else {
    // Родительский процесс - читает
    close(pipefd[1]);  // Закрыть write end
    char buffer[100];
    read(pipefd[0], buffer, 100);
    printf("Received: %s\n", buffer);
    close(pipefd[0]);
}
```

**2. Named pipes (FIFO)** — именованные каналы

**Пример: FIFO**

```bash
# Создание FIFO
mkfifo mypipe

# Процесс 1 (пишет)
echo "Hello" > mypipe

# Процесс 2 (читает)
cat < mypipe
```

```c

// Программное создание FIFO
#include <sys/stat.h>
mkfifo("/tmp/mypipe", 0666);

// Открытие для записи
int fd = open("/tmp/mypipe", O_WRONLY);
write(fd, "Hello", 5);
close(fd);
```

**3. Signals** — асинхронные уведомления

**Пример: Обработка сигналов**

```c
#include <signal.h>
#include <stdio.h>

void signal_handler(int sig) {
    printf("Received signal %d\n", sig);
    if (sig == SIGINT) {
        printf("Interrupt signal, cleaning up...\n");
        exit(0);
    }
}

int main() {
    // Установка обработчика
    signal(SIGINT, signal_handler);
    
    // Игнорирование сигнала
    signal(SIGTERM, SIG_IGN);
    
    // Бесконечный цикл
    while (1) {
        sleep(1);
    }
    
    return 0;
}
```

**4. Shared memory** — общая память

**Пример: Shared memory**

```c
#include <sys/shm.h>
#include <sys/ipc.h>

// Создание shared memory
key_t key = ftok("/tmp", 'A');
int shmid = shmget(key, 1024, IPC_CREAT | 0666);

// Присоединение к shared memory
void *shm = shmat(shmid, NULL, 0);

// Использование
strcpy((char*)shm, "Hello from shared memory");

// Отсоединение
shmdt(shm);
```

**5. Sockets** — сетевые соединения

**Пример: Unix domain socket**

```c
#include <sys/socket.h>
#include <sys/un.h>

// Создание socket
int sockfd = socket(AF_UNIX, SOCK_STREAM, 0);

struct sockaddr_un addr;
addr.sun_family = AF_UNIX;
strcpy(addr.sun_path, "/tmp/mysocket");

bind(sockfd, (struct sockaddr*)&addr, sizeof(addr));
listen(sockfd, 5);

// Принятие соединения
int client = accept(sockfd, NULL, NULL);
```

---

## 4. Файловая система

### 4.1 Иерархическая структура

**Особенности:**

- Единое дерево файлов (начинается с `/`)
- Всё монтируется в одно дерево
- Логическая структура не зависит от физических устройств

**Структура:**
```

/
├── bin/      # Исполняемые программы
├── etc/      # Конфигурационные файлы
├── home/     # Домашние директории пользователей
├── tmp/      # Временные файлы
├── usr/      # Пользовательские программы
└── var/      # Переменные данные
```

### 4.2 Права доступа

**Модель прав:**

- Владелец (owner)
- Группа (group)
- Остальные (others)

**Права:**

- Чтение (r) = 4
- Запись (w) = 2
- Выполнение (x) = 1

**Пример:**
```bash

-rwxr-xr-- 1 user group 1024 file.txt
│││││││││
││││││││└── others: r-- (read only)
│││││││└─── others: r--
││││││└──── others: r--
│││││└───── group: r-x (read + execute)
││││└────── group: r-x
│││└─────── group: r-x
││└──────── owner: rwx (read + write + execute)
│└───────── owner: rwx
└────────── owner: rwx
```

**Числовое представление:**
```bash
# rwxr-xr-- = 754
# owner:  rwx = 4+2+1 = 7
# group:  r-x = 4+0+1 = 5
# others: r-- = 4+0+0 = 4

chmod 755 file.txt  # rwxr-xr-x
chmod 644 file.txt  # rw-r--r--
chmod 700 file.txt  # rwx------
```

**Пример: Изменение прав в C**

```c
#include <sys/stat.h>

// Установка прав
chmod("file.txt", S_IRUSR | S_IWUSR | S_IXUSR |  // owner: rwx
                  S_IRGRP | S_IXGRP |            // group: r-x
                  S_IROTH);                      // others: r--

// Или числовое
chmod("file.txt", 0754);  // rwxr-xr--
```

**Sticky bit, setuid, setgid:**
```bash
# Sticky bit (t) - только владелец может удалить файл в /tmp
chmod +t /tmp/file

# Setuid (s) - выполняется с правами владельца
chmod u+s /usr/bin/passwd

# Setgid (s) - выполняется с правами группы
chmod g+s /usr/bin/write
```

### 4.3 Символические и жёсткие ссылки

**Hard links:**
```bash
# Создание hard link
ln original.txt link.txt

# Оба файла указывают на одни данные
# Удаление одного не удаляет данные, пока есть другой
```

**Symbolic links:**
```bash
# Создание symbolic link
ln -s original.txt symlink.txt

# symlink.txt → указывает на original.txt
# Если original.txt удалён, symlink "сломается"
```

**Пример: Работа со ссылками в C**

```c
#include <unistd.h>

// Создание hard link
link("original.txt", "hardlink.txt");

// Создание symbolic link
symlink("original.txt", "symlink.txt");

// Чтение symbolic link
char target[256];
readlink("symlink.txt", target, sizeof(target));
```

---

---

## 5. Наследие UNIX

### 5.1 Потомки UNIX

**Прямые потомки:**

- **BSD** — Berkeley Software Distribution

- **Linux** — клон UNIX (не прямой потомок)

- **macOS** — основан на BSD

- **Solaris** — от Sun Microsystems

**Влияние:**

- Большинство современных ОС используют идеи UNIX
- Стандарты POSIX обеспечивают совместимость
- Командная строка стала стандартом

### 5.2 Философия в современных системах

**Применение:**

**Контейнеры (Docker):**
```bash
# Используют изоляцию процессов из UNIX
docker run ubuntu ls -l

# Композиция через pipes
docker ps | grep running | awk '{print $1}'
```

**Микросервисы:**

- Следуют принципу "одна программа — одна задача"
- Коммуникация через простые интерфейсы (как pipes)
- Легко комбинируются

**DevOps инструменты:**
```bash
# Композиция через pipes
kubectl get pods | grep running | awk '{print $1}' | xargs kubectl logs

# Каждая команда делает одну вещь
git log | grep "fix" | wc -l
```

**Функциональные ОС:**

- **NixOS / Guix** — операционные системы с декларативной конфигурацией
- Версионирование всей системы
- Воспроизводимые сборки
- Продолжают идеи UNIX о композиции и предсказуемости

**Пример: NixOS декларативная конфигурация**

```nix
# /etc/nixos/configuration.nix
{ config, pkgs, ... }:
{
  services.nginx.enable = true;
  services.nginx.virtualHosts."example.com" = {
    root = "/var/www";
  };
  
  # Вся система описана декларативно
  # Воспроизводимые сборки
}
```

**Актуальность:**
Философия UNIX остаётся актуальной спустя 50+ лет.

### 5.3 POSIX стандарт

**POSIX (Portable Operating System Interface):**

- Стандарт совместимости между UNIX-подобными системами
- Определяет API для системных вызовов
- Обеспечивает переносимость программ

**Пример: POSIX-совместимый код**

```c

// POSIX-совместимый код работает на Linux, macOS, BSD
#include <unistd.h>
#include <sys/types.h>

pid_t pid = fork();
if (pid == 0) {
    execl("/bin/ls", "ls", NULL);
}
```

---

## 💡 Key Takeaways

- **UNIX** создал философию простоты и композиции, которая влияет на современные системы

- **"Всё — файл"** — единый интерфейс упрощает программирование и позволяет композицию

- **Минимализм** — каждая программа делает одну вещь хорошо, сложность через композицию

- **Pipes** — мощный механизм композиции программ без их модификации

- **Наследие UNIX** видно во всех современных операционных системах и подходах к разработке

---

## 🚀 Next Steps

**Related Modules:**

- [11_DOSWindows](../11_DOSWindows/) — альтернативный подход к операционным системам
- [12_CorporateUNIX](../12_CorporateUNIX/) — развитие UNIX в корпоративном мире

**Practice Ideas:**

1. Используйте pipes для композиции команд в командной строке
2. Изучите структуру файловой системы вашей ОС
3. Попробуйте создать простой скрипт, использующий несколько программ

**Going Deeper:**

- Исходный код ранних версий UNIX
- Философия UNIX и её применение в современной разработке
- История развития различных вариантов UNIX

---

## 📚 Additional Resources

**Books:**

- "The UNIX Programming Environment" by Kernighan & Pike
- "Design of the UNIX Operating System" by Maurice Bach

**Articles & Tutorials:**

- Философия UNIX и её влияние
- История UNIX и его создателей

---



