# Go (Golang)

Курс по языку программирования Go (Golang). Для разработчиков, которые хотят освоить язык для backend, CLI и cloud-native разработки.

## Модули курса

| # | Модуль | Описание |
|---|--------|----------|
| 01 | [Intro](./01_Intro/) | История Go, философия, где используется, установка, go toolchain |
| 02 | [Basics](./02_Basics/) | Переменные, типы, константы, операторы, форматирование |
| 03 | [FlowControl](./03_FlowControl/) | if, for, switch, defer — управление потоком выполнения |
| 04 | [Functions](./04_Functions/) | Функции, множественные возвращаемые значения, variadic |
| 05 | [DataStructures](./05_DataStructures/) | Массивы, слайсы, мапы, структуры |
| 06 | [Pointers](./06_Pointers/) | Указатели, значения vs ссылки, new vs make |
| 07 | [Methods](./07_Methods/) | Методы, интерфейсы, полиморфизм, embedding |
| 08 | [Errors](./08_Errors/) | Обработка ошибок, error interface, sentinel errors, wrapping |
| 09 | [Concurrency](./09_Concurrency/) | Горутины, каналы, select, sync примитивы |
| 10 | [Packages](./10_Packages/) | Организация кода, модули, go.mod, импорты |
| 11 | [Testing](./11_Testing/) | Тестирование в Go, table-driven tests, бенчмарки |
| 12 | [Stdlib](./12_Stdlib/) | net/http, encoding/json, io, os — стандартная библиотека |

## Требования

- Терминал
- Go toolchain (go 1.21+)
- Редактор с поддержкой Go (VS Code с Go extension, GoLand, Vim с vim-go)

## Установка Go

### macOS (Homebrew)

```bash

brew install go
```

### Linux

```bash

wget https://go.dev/dl/go1.22.0.linux-amd64.tar.gz
sudo tar -C /usr/local -xzf go1.22.0.linux-amd64.tar.gz
export PATH=$PATH:/usr/local/go/bin
```

### Проверка

```bash

go version
go env GOPATH
```

## Рекомендуемый порядок изучения

1. **Основы (модули 1-4)**: Синтаксис, типы, функции
2. **Структуры данных (модули 5-7)**: Коллекции, указатели, методы
3. **Продвинутые темы (модули 8-10)**: Ошибки, конкурентность, модули
4. **Практика (модули 11-12)**: Тестирование, стандартная библиотека

## Полезные ресурсы

- [A Tour of Go](https://go.dev/tour/) — интерактивное введение
- [Effective Go](https://go.dev/doc/effective_go) — лучшие практики
- [Go by Example](https://gobyexample.com/) — примеры кода
- [Go Playground](https://go.dev/play/) — онлайн редактор

---

**Язык курса:** Русский


