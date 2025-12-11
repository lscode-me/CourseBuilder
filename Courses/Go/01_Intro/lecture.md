# Go (Golang)
## Введение: история, философия, установка и первые шаги

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Иметь базовый опыт программирования на любом языке
- Уметь работать с командной строкой (терминалом)
- Понимать базовые концепции: переменные, функции, циклы
- Иметь доступ к Linux, macOS или Windows

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Объяснить историю создания Go и его философию
- Установить и настроить Go на своей системе
- Использовать основные инструменты Go toolchain
- Создавать и запускать простые Go-программы
- Понимать структуру Go-проекта

---

## 1. Что такое Go

Go (или Golang) — это компилируемый статически типизированный язык программирования, созданный в Google. Первая стабильная версия вышла в 2012 году, хотя разработка началась ещё в 2007 году.

Go разрабатывался для решения проблем, с которыми сталкивались инженеры Google при работе с большими кодовыми базами: медленная компиляция, сложность языков (C++), проблемы с зависимостями.

### 1.1 Создатели языка

Go создан командой легендарных разработчиков:

- **Rob Pike** — разработчик Plan 9, UTF-8, редактора Acme

- **Ken Thompson** — создатель Unix, языка B, UTF-8

- **Robert Griesemer** — работал над V8 JavaScript engine, Java HotSpot

```go

// Первая программа на Go — традиционный Hello, World!
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}

```

**Output:**
```

Hello, World!

```

### 1.2 Почему "Go" и "Golang"

Официальное название языка — **Go**. Однако термин **Golang** (Go Language) используется повсеместно, потому что:

- "Go" слишком короткое слово для поисковых систем
- Домен golang.org легче запомнить
- Хэштеги #golang более уникальны, чем #go

> **💡 Pro Tip:**  
> Для поиска информации используйте "golang" вместо "go", чтобы получить релевантные результаты.

---

## 2. Философия Go

### 2.1 Простота превыше всего

Go сознательно ограничивает количество возможностей языка. Вместо десяти способов сделать что-то, Go предлагает один — очевидный и понятный.

```go

package main

import "fmt"

func main() {
    // В Go только один тип цикла — for
    for i := 0; i < 5; i++ {
        fmt.Println(i)
    }
    
    // while-стиль
    j := 0
    for j < 3 {
        fmt.Println("j:", j)
        j++
    }
    
    // бесконечный цикл
    // for {
    //     fmt.Println("forever")
    // }
}

```

**Output:**
```

0
1
2
3
4
j: 0
j: 1
j: 2

```

### 2.2 Явное лучше неявного

Go требует явного указания намерений. Нет неявных преобразований типов, нет скрытой магии.

```go

package main

import "fmt"

func main() {
    var x int = 42
    var y float64 = float64(x) // Явное преобразование обязательно!
    
    fmt.Printf("x (int): %d\n", x)
    fmt.Printf("y (float64): %f\n", y)
    
    // var z float64 = x  // Ошибка компиляции!
}

```

**Output:**
```

x (int): 42
y (float64): 42.000000

```

### 2.3 Минимализм

Go намеренно не включает многие "продвинутые" возможности:

| Чего нет в Go | Почему |
|---------------|--------|
| Классы | Композиция вместо наследования |
| Исключения | Явная обработка ошибок |
| Generics (до 1.18) | Добавлены в Go 1.18 |
| Перегрузка функций | Простота > удобство |
| Неявные преобразования | Предсказуемость |

### 2.4 Пословицы Go (Go Proverbs)

Rob Pike сформулировал "пословицы Go" — принципы философии языка:

- **Don't communicate by sharing memory, share memory by communicating**

- **Concurrency is not parallelism**

- **Channels orchestrate; mutexes serialize**

- **The bigger the interface, the weaker the abstraction**

- **Make the zero value useful**

- **A little copying is better than a little dependency**

- **Clear is better than clever**

- **Errors are values**

---

## 3. Где используется Go

### 3.1 Области применения

Go особенно силён в следующих областях:

**Cloud & Infrastructure:**

- Docker — контейнеризация
- Kubernetes — оркестрация контейнеров
- Terraform — Infrastructure as Code
- Prometheus — мониторинг
- etcd — распределённое хранилище

**Backend & Microservices:**

- gRPC — высокопроизводительный RPC
- API сервисы
- Веб-серверы

**CLI Tools:**

- Hugo — генератор статических сайтов
- gh — GitHub CLI
- cobra — создание CLI

```go

// Пример простого HTTP-сервера
package main

import (
    "fmt"
    "net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "Привет, %s!", r.URL.Path[1:])
}

func main() {
    http.HandleFunc("/", handler)
    fmt.Println("Сервер запущен на http://localhost:8080")
    http.ListenAndServe(":8080", nil)
}

```

### 3.2 Компании, использующие Go

| Компания | Применение |
|----------|------------|
| Google | Kubernetes, внутренние сервисы |
| Uber | Геолокация, высоконагруженные сервисы |
| Twitch | Чат, видео-инфраструктура |
| Dropbox | Миграция с Python для критичных сервисов |
| SoundCloud | Микросервисы |
| Cloudflare | Сетевые сервисы |

### 3.3 Преимущества Go для backend

```go

package main

import (
    "fmt"
    "runtime"
    "sync"
    "time"
)

func main() {
    // Go отлично использует многоядерность
    fmt.Printf("Доступно ядер CPU: %d\n", runtime.NumCPU())
    
    var wg sync.WaitGroup
    start := time.Now()
    
    // Запускаем 1000 горутин
    for i := 0; i < 1000; i++ {
        wg.Add(1)
        go func(n int) {
            defer wg.Done()
            time.Sleep(10 * time.Millisecond)
        }(i)
    }
    
    wg.Wait()
    fmt.Printf("1000 горутин выполнено за: %v\n", time.Since(start))
}

```

**Output:**
```

Доступно ядер CPU: 8
1000 горутин выполнено за: 12.345ms

```

---

## 4. Установка Go

### 4.1 Проверка установленной версии

```bash

go version

```

**Output:**
```

go version go1.22.0 darwin/arm64

```

### 4.2 Установка на macOS

**Через Homebrew (рекомендуется):**

```bash
# Установка
brew install go

# Проверка
go version

# Путь к установке
which go

```

**Output:**
```

go version go1.22.0 darwin/arm64
/opt/homebrew/bin/go

```

**Через официальный установщик:**

1. Скачайте установщик с https://go.dev/dl/
2. Запустите .pkg файл
3. Следуйте инструкциям

### 4.3 Установка на Linux

**Ubuntu/Debian:**

```bash
# Скачиваем последнюю версию
wget https://go.dev/dl/go1.22.0.linux-amd64.tar.gz

# Удаляем старую версию (если есть)
sudo rm -rf /usr/local/go

# Распаковываем в /usr/local
sudo tar -C /usr/local -xzf go1.22.0.linux-amd64.tar.gz

# Добавляем в PATH (в ~/.bashrc или ~/.zshrc)
echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bashrc
source ~/.bashrc

# Проверка
go version

```

### 4.4 Настройка переменных окружения

Go использует несколько важных переменных окружения:

```bash
# Посмотреть текущие настройки
go env

# Основные переменные
go env GOROOT   # Где установлен Go
go env GOPATH   # Рабочая директория (устарело с модулями)
go env GOBIN    # Куда устанавливаются бинарники
go env GOPROXY  # Прокси для загрузки модулей

```

**Output:**
```

GOROOT="/opt/homebrew/Cellar/go/1.22.0/libexec"
GOPATH="/Users/developer/go"
GOBIN=""
GOPROXY="https://proxy.golang.org,direct"

```

Рекомендуемая настройка `~/.bashrc` или `~/.zshrc`:

```bash
# Go environment
export GOPATH=$HOME/go
export PATH=$PATH:$GOPATH/bin

```

> **⚠️ Warning:**  
> С появлением Go Modules (Go 1.11+), GOPATH стал менее важен. Вы можете создавать проекты в любой директории.

---

## 5. Go Toolchain

Go поставляется с мощным набором инструментов. Все команды начинаются с `go`.

### 5.1 Основные команды

```bash
# Компиляция и запуск
go run main.go          # Скомпилировать и запустить
go build                # Скомпилировать в исполняемый файл
go install              # Скомпилировать и установить в GOBIN

# Управление модулями
go mod init myproject   # Инициализировать модуль
go mod tidy             # Обновить зависимости
go get package@version  # Добавить зависимость

# Качество кода
go fmt ./...            # Форматировать код
go vet ./...            # Статический анализ
go test ./...           # Запустить тесты

# Документация
go doc fmt              # Документация пакета
go doc fmt.Println      # Документация функции

```

### 5.2 go run — запуск без компиляции

```bash
# Создаём файл
cat > hello.go << 'EOF'
package main

import "fmt"

func main() {
    fmt.Println("Запущено через go run!")
}
EOF

# Запускаем
go run hello.go

```

**Output:**
```

Запущено через go run!

```

### 5.3 go build — компиляция

```bash
# Компиляция текущего модуля
go build

# Компиляция конкретного файла
go build -o myapp main.go

# Кросс-компиляция (для Linux из macOS)
GOOS=linux GOARCH=amd64 go build -o myapp-linux

# Уменьшение размера бинарника
go build -ldflags="-s -w" -o myapp-small

```

**Сравнение размеров:**

| Флаги | Размер (примерно) |
|-------|-------------------|
| По умолчанию | 2.5 MB |
| `-ldflags="-s -w"` | 1.8 MB |
| + UPX сжатие | 0.6 MB |

### 5.4 go fmt — форматирование

Go имеет единый стандарт форматирования. Все споры о стиле решены:

```go

// До форматирования
package main
import "fmt"
func main(){
fmt.Println("messy")
    fmt.Println("code")}

```

```bash

go fmt main.go

```

```go

// После форматирования
package main

import "fmt"

func main() {
    fmt.Println("messy")
    fmt.Println("code")
}

```

> **💡 Pro Tip:**  
> Настройте редактор на автоматический `go fmt` при сохранении файла.

### 5.5 go vet — статический анализ

`go vet` находит подозрительные конструкции, которые могут быть ошибками:

```go

package main

import "fmt"

func main() {
    // go vet найдёт эту ошибку
    fmt.Printf("Число: %s\n", 42) // %s для int!
}

```

```bash

go vet main.go

```

**Output:**
```

main.go:7:2: Printf format %s has arg 42 of wrong type int

```

---

## 6. Структура Go-проекта

### 6.1 Простейший проект

```

myproject/
├── go.mod          # Определение модуля
└── main.go         # Точка входа

```

**go.mod:**
```

module myproject

go 1.22

```

**main.go:**
```go

package main

import "fmt"

func main() {
    fmt.Println("Hello from myproject!")
}

```

### 6.2 Типичный проект

```

myproject/
├── cmd/
│   └── myapp/
│       └── main.go       # Точка входа приложения
├── internal/
│   ├── config/
│   │   └── config.go     # Внутренняя логика (не экспортируется)
│   └── handler/
│       └── handler.go
├── pkg/
│   └── utils/
│       └── utils.go      # Переиспользуемые пакеты
├── go.mod
├── go.sum                # Контрольные суммы зависимостей
└── README.md

```

### 6.3 Создание нового проекта

```bash
# Создаём директорию проекта
mkdir myproject && cd myproject

# Инициализируем модуль
go mod init github.com/username/myproject

# Создаём main.go
cat > main.go << 'EOF'
package main

import "fmt"

func main() {
    fmt.Println("Project initialized!")
}
EOF

# Запускаем
go run .

```

**Output:**
```

Project initialized!

```

---

## 7. Первая программа

### 7.1 Анатомия Go-программы

```go

// 1. Package declaration — каждый файл принадлежит пакету
package main

// 2. Import — подключаем нужные пакеты
import (
    "fmt"
    "time"
)

// 3. Функция main — точка входа для исполняемых программ
func main() {
    // 4. Код программы
    fmt.Println("Привет, Go!")
    fmt.Printf("Текущее время: %s\n", time.Now().Format("15:04:05"))
}

```

**Output:**
```

Привет, Go!
Текущее время: 14:30:45

```

### 7.2 package main

```go

// package main означает, что это исполняемая программа
// У библиотек будет другое имя пакета
package main

import "fmt"

// func main() — точка входа, обязательна для package main
func main() {
    fmt.Println("Это исполняемая программа")
}

```

Программа без `package main` и `func main()` — это библиотека, не исполняемый файл.

### 7.3 Import

```go

package main

// Одиночный импорт
import "fmt"

// Множественный импорт (предпочтительно)
import (
    "fmt"
    "os"
    "strings"
)

// Импорт с алиасом
import (
    f "fmt"                    // Теперь fmt доступен как f
    _ "image/png"              // Импорт только для side effects
    . "strings"                // Импортировать всё в текущий namespace (не рекомендуется)
)

func main() {
    f.Println("Using alias")
}

```

> **⚠️ Warning:**  
> Неиспользуемые импорты — ошибка компиляции в Go. Удаляйте лишние или используйте `goimports`.

### 7.4 Программа с аргументами

```go

package main

import (
    "fmt"
    "os"
)

func main() {
    // os.Args содержит аргументы командной строки
    // os.Args[0] — имя программы
    args := os.Args
    
    fmt.Printf("Программа: %s\n", args[0])
    fmt.Printf("Количество аргументов: %d\n", len(args))
    
    if len(args) > 1 {
        fmt.Println("Аргументы:")
        for i, arg := range args[1:] {
            fmt.Printf("  %d: %s\n", i+1, arg)
        }
    }
}

```

```bash

go run main.go hello world 123

```

**Output:**
```

Программа: /tmp/go-build123/main
Количество аргументов: 4
Аргументы:
  1: hello
  2: world
  3: 123

```

---

## 8. Форматирование вывода

### 8.1 fmt.Println и fmt.Print

```go

package main

import "fmt"

func main() {
    // Print — без переноса строки
    fmt.Print("Hello")
    fmt.Print(" ")
    fmt.Print("World")
    fmt.Println() // Добавляем перенос
    
    // Println — с переносом строки, пробелы между аргументами
    fmt.Println("Hello", "World", 2024)
    
    // Println автоматически добавляет пробелы
    name := "Go"
    version := 1.22
    fmt.Println("Language:", name, "Version:", version)
}

```

**Output:**
```

Hello World
Hello World 2024
Language: Go Version: 1.22

```

### 8.2 fmt.Printf — форматированный вывод

```go

package main

import "fmt"

func main() {
    // Базовые форматы
    name := "Gopher"
    age := 10
    height := 1.75
    active := true
    
    fmt.Printf("Имя: %s\n", name)           // строка
    fmt.Printf("Возраст: %d лет\n", age)    // целое число
    fmt.Printf("Рост: %.2f м\n", height)    // дробное число
    fmt.Printf("Активен: %t\n", active)     // boolean
    fmt.Printf("Тип: %T\n", name)           // тип переменной
    fmt.Printf("Значение: %v\n", name)      // универсальный формат
    fmt.Printf("Детально: %+v\n", name)     // с именами полей (для структур)
    fmt.Printf("Go-синтаксис: %#v\n", name) // Go-представление
}

```

**Output:**
```

Имя: Gopher
Возраст: 10 лет
Рост: 1.75 м
Активен: true
Тип: string
Значение: Gopher
Детально: Gopher
Go-синтаксис: "Gopher"

```

### 8.3 Все форматы Printf

| Формат | Описание | Пример |
|--------|----------|--------|
| `%v` | Значение в формате по умолчанию | `{field: value}` |
| `%+v` | С именами полей | `{field:value}` |
| `%#v` | Go-синтаксис | `main.Type{field:"value"}` |
| `%T` | Тип значения | `int`, `string` |
| `%d` | Целое число (десятичное) | `42` |
| `%b` | Целое (двоичное) | `101010` |
| `%x` | Целое (hex, lowercase) | `2a` |
| `%X` | Целое (hex, uppercase) | `2A` |
| `%f` | Дробное число | `3.141593` |
| `%e` | Научная нотация | `3.141593e+00` |
| `%s` | Строка | `hello` |
| `%q` | Строка в кавычках | `"hello"` |
| `%t` | Boolean | `true` |
| `%p` | Указатель | `0xc0000a6010` |
| `%%` | Символ процента | `%` |

```go

package main

import "fmt"

func main() {
    // Ширина и выравнивание
    fmt.Printf("|%10s|\n", "right")    // Выравнивание вправо
    fmt.Printf("|%-10s|\n", "left")    // Выравнивание влево
    fmt.Printf("|%10d|\n", 42)         // Число вправо
    fmt.Printf("|%-10d|\n", 42)        // Число влево
    fmt.Printf("|%010d|\n", 42)        // С ведущими нулями
    
    // Точность для чисел
    pi := 3.14159265359
    fmt.Printf("%.2f\n", pi)           // 2 знака после запятой
    fmt.Printf("%.5f\n", pi)           // 5 знаков
    fmt.Printf("%8.2f\n", pi)          // Ширина 8, 2 знака
}

```

**Output:**
```

|     right|
|left      |
|        42|
|42        |
|0000000042|
3.14
3.14159
    3.14

```

---

## 9. Редакторы и IDE

### 9.1 Visual Studio Code

VS Code с расширением Go — наиболее популярный выбор:

```bash
# Установите расширение "Go" от Go Team at Google
# Extensions → Search "Go" → Install
```

**Настройка settings.json:**
```json

{
    "go.formatTool": "goimports",
    "go.lintTool": "golangci-lint",
    "go.useLanguageServer": true,
    "[go]": {
        "editor.formatOnSave": true,
        "editor.codeActionsOnSave": {
            "source.organizeImports": "explicit"
        }
    }
}

```

### 9.2 GoLand

JetBrains GoLand — профессиональная IDE для Go:

- Мощный рефакторинг
- Встроенный дебаггер
- Интеграция с тестами
- Платная (бесплатна для студентов и open source)

### 9.3 Vim/Neovim

Для любителей Vim:

```bash
# Установите vim-go плагин
# В vimrc:
Plug 'fatih/vim-go', { 'do': ':GoUpdateBinaries' }

```

### 9.4 Полезные инструменты

```bash
# Установка дополнительных инструментов
go install golang.org/x/tools/gopls@latest          # Language server
go install github.com/golangci/golangci-lint/cmd/golangci-lint@latest  # Linter
go install golang.org/x/tools/cmd/goimports@latest  # Форматирование + imports
go install github.com/go-delve/delve/cmd/dlv@latest # Debugger

```

---

## 10. Common Pitfalls

### 10.1 Неиспользуемые переменные

❌ **Ошибка компиляции:**
```go

package main

func main() {
    x := 42    // Объявлено, но не использовано!
    // main.go:4:2: x declared but not used
}

```

✅ **Решение:**
```go

package main

import "fmt"

func main() {
    x := 42
    fmt.Println(x)  // Используем переменную
    
    // Или используем _ для игнорирования
    _ = 42
}

```

### 10.2 Неиспользуемые импорты

❌ **Ошибка:**
```go

package main

import (
    "fmt"
    "os"  // imported and not used
)

func main() {
    fmt.Println("Hello")
}

```

✅ **Решение:**
```go

package main

import "fmt"

func main() {
    fmt.Println("Hello")
}

```

> **💡 Pro Tip:**  
> Используйте `goimports` вместо `go fmt` — он автоматически добавляет и удаляет импорты.

### 10.3 GOPATH vs Go Modules

❌ **Устаревший подход (GOPATH):**
```bash
# Старый способ — проекты должны быть в $GOPATH/src
cd $GOPATH/src/github.com/user/project

```

✅ **Современный подход (Go Modules):**
```bash
# Создавайте проекты в любой директории
mkdir ~/projects/myapp
cd ~/projects/myapp
go mod init github.com/user/myapp

```

### 10.4 Забыли инициализировать модуль

```bash
# При попытке сборки без go.mod
go: go.mod file not found in current directory or any parent directory

# Решение
go mod init myproject

```

---

## 💡 Key Takeaways

- **Go — простой и эффективный**: Создан для решения реальных проблем больших команд. Компилируется быстро, исполняется быстро.

- **Единый стиль кода**: `go fmt` исключает споры о форматировании. Весь Go-код выглядит одинаково.

- **Мощный toolchain**: Все инструменты встроены — сборка, тестирование, форматирование, документация.

- **Go Modules**: Современный способ управления зависимостями. Забудьте про GOPATH.

- **Статическая компиляция**: Go создаёт единый бинарный файл без внешних зависимостей. Идеально для контейнеров и деплоя.

---

## 🚀 Next Steps

**Related Modules:**

- [02_Basics](../02_Basics/) — переменные, типы, константы, операторы
- [03_FlowControl](../03_FlowControl/) — условия, циклы, defer

**Practice Ideas:**

1. Установите Go и настройте редактор
2. Создайте проект с `go mod init` и напишите Hello World
3. Поэкспериментируйте с `go run`, `go build`, `go fmt`
4. Напишите программу, которая принимает аргументы командной строки

**Going Deeper:**

- Прочитайте [Effective Go](https://go.dev/doc/effective_go)
- Изучите [Go Proverbs](https://go-proverbs.github.io/)
- Посмотрите [Go at Google](https://go.dev/talks/2012/splash.article)

---

## 📚 Additional Resources

**Documentation:**

- [go.dev](https://go.dev/) — официальный сайт
- [Go Documentation](https://go.dev/doc/) — документация
- [Go Tour](https://go.dev/tour/) — интерактивный тур

**Books:**

- "The Go Programming Language" by Donovan & Kernighan
- "Go in Action" by Kennedy, Ketelsen & St. Martin
- "Learning Go" by Jon Bodner

**Videos:**

- [GopherCon](https://www.youtube.com/c/GopherAcademy) — конференция по Go
- [justforfunc](https://www.youtube.com/c/JustForFunc) — Go видео-уроки

---




