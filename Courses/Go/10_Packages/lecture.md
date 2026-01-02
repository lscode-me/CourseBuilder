# Packages and Modules
## Организация кода, модули, go.mod и импорты

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Уметь создавать и запускать Go-программы
- Понимать функции и типы
- Знать экспорт через заглавные буквы

**Recommended prior modules:**

- [01_Intro](../01_Intro/) — установка Go
- [04_Functions](../04_Functions/) — функции

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Создавать и организовывать пакеты
- Работать с Go modules
- Управлять зависимостями
- Понимать правила видимости
- Использовать internal пакеты

---

## 1. Пакеты (Packages)

### 1.1 Концепция пакетов

```go
// mathutil/math.go
package mathutil  // Имя пакета

import "fmt"

// Экспортируемая функция (заглавная буква)
func Add(a, b int) int {
    return a + b
}

// Приватная функция (маленькая буква)
func subtract(a, b int) int {
    return a - b
}

// Экспортируемая константа
const Pi = 3.14159

// Приватная переменная
var internalState int
```

### 1.2 package main

```go
// main.go
package main  // Специальный пакет для исполняемых программ

import (
    "fmt"
    "myproject/mathutil"
)

func main() {
    result := mathutil.Add(3, 5)
    fmt.Println("3 + 5 =", result)
    fmt.Println("Pi =", mathutil.Pi)
    
    // mathutil.subtract(5, 3)  // Ошибка! subtract не экспортирован
}
```

**Output:**
```
3 + 5 = 8
Pi = 3.14159
```

### 1.3 Правила именования пакетов

```go
// ХОРОШО
package http
package json
package mathutil
package userservice

// ПЛОХО
package httpPackage      // Избыточно
package user_service     // Подчёркивания
package myHTTPServer     // Смешанный регистр
package Util             // Заглавная буква
```

**Рекомендации:**

- Короткие, понятные имена
- Lowercase, без подчёркиваний
- Единственное число (user, не users)
- Избегать generic имён (util, common, misc)

---

## 2. Go Modules

### 2.1 Инициализация модуля

```bash
# Создаём директорию проекта

mkdir myproject
cd myproject

# Инициализируем модуль

go mod init github.com/username/myproject

# Структура после инициализации

ls -la
# go.mod
```

**go.mod:**
```
module github.com/username/myproject

go 1.22
```

### 2.2 Структура go.mod

```
module github.com/username/myproject

go 1.22

require (
    github.com/gin-gonic/gin v1.9.1
    github.com/go-sql-driver/mysql v1.7.1
)

require (
    // Indirect dependencies (транзитивные)
    github.com/json-iterator/go v1.1.12 // indirect
)
```

### 2.3 Управление зависимостями

```bash
# Добавить зависимость

go get github.com/gin-gonic/gin

# Добавить конкретную версию

go get github.com/gin-gonic/gin@v1.9.1

# Добавить последнюю версию

go get github.com/gin-gonic/gin@latest

# Обновить зависимость

go get -u github.com/gin-gonic/gin

# Обновить все зависимости

go get -u ./...

# Удалить неиспользуемые зависимости

go mod tidy

# Скачать все зависимости

go mod download

# Показать дерево зависимостей

go mod graph
```

### 2.4 go.sum

```
github.com/gin-gonic/gin v1.9.1 h1:4idEAncQnU5cB7BeOkPtxjfCSye0AAm1R0RVIqJ+Jmg=
github.com/gin-gonic/gin v1.9.1/go.mod h1:hPrL7YrpYKXt5YId3A/Tn+7SEVvEpTQ0iW...
```

Контрольные суммы для обеспечения целостности зависимостей.

---

## 3. Структура проекта

### 3.1 Простой проект

```
myproject/
├── go.mod
├── go.sum
├── main.go
└── utils.go
```

### 3.2 Стандартная структура

```
myproject/
├── cmd/
│   ├── myapp/
│   │   └── main.go         # Точка входа приложения
│   └── cli/
│       └── main.go         # CLI инструмент
├── internal/
│   ├── config/
│   │   └── config.go       # Внутренняя конфигурация
│   └── service/
│       └── user.go
├── pkg/
│   └── utils/
│       └── utils.go        # Переиспользуемые утилиты
├── api/
│   └── handlers.go         # HTTP handlers
├── go.mod
├── go.sum
└── README.md
```

### 3.3 Пример с несколькими пакетами

```go
// cmd/myapp/main.go
package main

import (
    "fmt"
    "github.com/username/myproject/internal/config"
    "github.com/username/myproject/pkg/utils"
)

func main() {
    cfg := config.Load()
    fmt.Println("Config:", cfg)
    
    result := utils.FormatString("hello")
    fmt.Println("Result:", result)
}
```

```go
// internal/config/config.go
package config

type Config struct {
    Host string
    Port int
}

func Load() *Config {
    return &Config{
        Host: "localhost",
        Port: 8080,
    }
}
```

```go
// pkg/utils/utils.go
package utils

import "strings"

func FormatString(s string) string {
    return strings.ToUpper(s)
}
```

---

## 4. Импорты

### 4.1 Синтаксис импортов

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
    "fmt"
    myjson "encoding/json"  // Алиас
)

// Dot import (не рекомендуется)
import (
    . "fmt"  // Можно использовать Println вместо fmt.Println
)

// Blank import (для side effects)
import (
    _ "image/png"  // Регистрирует PNG decoder
)
```

### 4.2 Группировка импортов

```go
import (
    // Стандартная библиотека
    "context"
    "fmt"
    "net/http"
    
    // Внешние зависимости
    "github.com/gin-gonic/gin"
    "github.com/go-redis/redis"
    
    // Локальные пакеты
    "github.com/username/myproject/internal/config"
    "github.com/username/myproject/pkg/utils"
)
```

### 4.3 Циклические импорты

```go
// ОШИБКА: import cycle not allowed

// package a
import "myproject/b"

// package b  
import "myproject/a"  // Цикл!
```

**Решение:**

- Выделить общий код в третий пакет
- Использовать интерфейсы
- Пересмотреть архитектуру

---

## 5. Internal пакеты

### 5.1 Ограничение видимости

```
myproject/
├── cmd/
│   └── myapp/
│       └── main.go
├── internal/           # Виден только в myproject
│   └── secret/
│       └── secret.go
└── pkg/
    └── public/
        └── public.go   # Виден всем
```

```go
// internal/secret/secret.go
package secret

var APIKey = "super-secret"

func Decrypt(data []byte) []byte {
    // ...
    return data
}
```

```go
// cmd/myapp/main.go — МОЖНО использовать internal
import "github.com/username/myproject/internal/secret"

// Внешний проект — НЕЛЬЗЯ использовать internal
// import "github.com/username/myproject/internal/secret"
// Error: use of internal package not allowed
```

---

## 6. Экспорт и видимость

### 6.1 Правила экспорта

```go
package mypackage

// Экспортируемые (public) — с заглавной буквы
type User struct {      // Экспортирован
    Name  string        // Экспортировано поле
    email string        // Приватное поле!
}

func NewUser() *User {  // Экспортирована
    return &User{}
}

// Приватные (private) — с маленькой буквы
type internalData struct {}  // Не экспортирован

func helper() {}  // Не экспортирована

const maxSize = 100  // Не экспортирована
const MaxRetries = 3  // Экспортирована
```

### 6.2 Доступ к приватным полям

```go
package user

type User struct {
    Name  string
    email string  // Приватное
}

// Getter для приватного поля
func (u *User) Email() string {
    return u.email
}

// Setter для приватного поля
func (u *User) SetEmail(email string) error {
    if email == "" {
        return errors.New("email cannot be empty")
    }
    u.email = email
    return nil
}
```

---

## 7. init() функция

### 7.1 Порядок инициализации

```go
package main

import "fmt"

var a = initVar("a")  // 1. Переменные пакета

func initVar(name string) string {
    fmt.Println("Init var:", name)
    return name
}

func init() {  // 2. init функции
    fmt.Println("Init 1")
}

func init() {  // Можно несколько init
    fmt.Println("Init 2")
}

func main() {  // 3. main
    fmt.Println("Main")
}
```

**Output:**
```
Init var: a
Init 1
Init 2
Main
```

### 7.2 Использование init

```go
package database

import (
    "database/sql"
    _ "github.com/lib/pq"  // Регистрация драйвера в init()
)

var DB *sql.DB

func init() {
    var err error
    DB, err = sql.Open("postgres", "...")
    if err != nil {
        panic(err)
    }
}
```

---

## 8. Версионирование

### 8.1 Semantic Versioning

```
v1.2.3
│ │ │
│ │ └── Patch: исправления багов
│ └──── Minor: новые функции, обратно совместимые
└────── Major: breaking changes
```

### 8.2 Версии в Go modules

```bash
# Конкретная версия

go get github.com/pkg/errors@v0.9.1

# Последняя версия

go get github.com/pkg/errors@latest

# Конкретный коммит

go get github.com/pkg/errors@a1b2c3d

# Ветка

go get github.com/pkg/errors@master
```

### 8.3 Major версии

```go
// v1.x.x
import "github.com/user/pkg"

// v2.x.x и выше — путь включает версию
import "github.com/user/pkg/v2"
```

---

## 9. Локальные модули

### 9.1 replace директива

```
// go.mod
module myproject

go 1.22

require github.com/myorg/mylib v1.0.0

// Использовать локальную версию
replace github.com/myorg/mylib => ../mylib
```

### 9.2 Workspace (Go 1.18+)

```bash
# Создание workspace

go work init ./myapp ./mylib

# go.work

go 1.22

use (
    ./myapp
    ./mylib
)
```

---

## 10. Best Practices

### 10.1 Организация пакетов

```go
// ХОРОШО: пакет по функциональности
package user
package order
package payment

// ПЛОХО: пакет по типу
package models
package controllers
package utils
```

### 10.2 Минимизация API

```go
// ХОРОШО: минимальный экспортируемый API
package auth

func Login(email, password string) (*Token, error)
func Logout(token *Token) error

// ПЛОХО: всё экспортируется
func ValidateEmail(email string) bool  // Внутренняя функция
func HashPassword(pwd string) string   // Внутренняя функция
```

### 10.3 Документация

```go
// Package mathutil provides mathematical utilities.
package mathutil

// Add returns the sum of two integers.
// It handles overflow by returning math.MaxInt in such cases.
func Add(a, b int) int {
    // Implementation
}
```

---

## 💡 Key Takeaways

- **Пакеты группируют код**: Каждый файл принадлежит одному пакету.

- **Заглавная буква = экспорт**: Public API определяется именованием.

- **go.mod управляет зависимостями**: Используйте `go mod tidy` регулярно.

- **internal ограничивает доступ**: Для внутренних пакетов проекта.

- **Избегайте циклических импортов**: Используйте интерфейсы и рефакторинг.

---

## 🚀 Next Steps

**Related Modules:**

- [11_Testing](../11_Testing/) — тестирование пакетов
- [12_Stdlib](../12_Stdlib/) — стандартная библиотека

**Practice Ideas:**

1. Создайте многомодульный проект
2. Опубликуйте пакет на GitHub
3. Используйте replace для локальной разработки

---





