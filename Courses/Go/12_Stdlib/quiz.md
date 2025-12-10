# Standard Library - Quiz

Проверьте свои знания по теме "Стандартная библиотека Go".

---

## Question 1: HTTP сервер

Какая функция запускает HTTP сервер?

A) `http.Start()`

B) `http.ListenAndServe()`

C) `http.Run()`

D) `http.Server()`

---

## Question 2: HTTP handler

Какая сигнатура у HTTP handler функции?

A) `func(w http.Writer, r *http.Request)`

B) `func(w http.ResponseWriter, r *http.Request)`

C) `func(r *http.Request) http.Response`

D) `func(w http.Response, r http.Request)`

---

## Question 3: HTTP клиент

Как сделать простой GET запрос?

A) `http.Get(url)`

B) `http.Request(url)`

C) `http.Fetch(url)`

D) `http.Download(url)`

---

## Question 4: JSON маршалинг

Какой тег игнорирует поле при JSON?

A) `json:"ignore"`

B) `json:"-"`

C) `json:"omit"`

D) `json:"skip"`

---

## Question 5: omitempty

Что делает тег `json:"name,omitempty"`?

A) Делает поле обязательным

B) Пропускает zero value при сериализации

C) Игнорирует поле

D) Устанавливает default

---

## Question 6: json.Marshal

Что возвращает json.Marshal?

A) string

B) []byte, error

C) io.Reader

D) *json.Result

---

## Question 7: json.Decoder

Для чего используется json.Decoder?

A) Декодирование строки

B) Потоковое декодирование из Reader

C) Шифрование JSON

D) Валидация JSON

---

## Question 8: io.Reader

Какой метод определяет io.Reader?

A) `Read(p []byte) (n int, err error)`

B) `ReadAll() []byte`

C) `GetBytes() []byte`

D) `Data() []byte`

---

## Question 9: io.EOF

Что означает io.EOF?

A) Ошибка чтения

B) Конец данных

C) Файл не найден

D) Timeout

---

## Question 10: io.Copy

Что делает io.Copy?

A) Копирует файлы

B) Копирует данные из Reader в Writer

C) Клонирует объект

D) Создаёт бэкап

---

## Question 11: os.ReadFile

Что возвращает os.ReadFile?

A) *os.File

B) []byte, error

C) string

D) io.Reader

---

## Question 12: os.Create

Какие права у файла по умолчанию?

A) 0644

B) 0755

C) 0777

D) 0666

---

## Question 13: os.Getenv

Что возвращает os.Getenv для несуществующей переменной?

A) nil

B) Пустую строку

C) Ошибку

D) panic

---

## Question 14: os.Args

Что содержит os.Args[0]?

A) Первый аргумент

B) Имя программы

C) Рабочую директорию

D) Версию Go

---

## Question 15: strings.Contains

Что возвращает strings.Contains?

A) int

B) bool

C) string

D) error

---

## Question 16: strings.Builder

Для чего используется strings.Builder?

A) Парсинг строк

B) Эффективная конкатенация строк

C) Поиск в строках

D) Форматирование

---

## Question 17: time.Now

Что возвращает time.Now()?

A) int64

B) string

C) time.Time

D) *time.Time

---

## Question 18: time.Format

Какое референсное время используется?

A) 1970-01-01 00:00:00

B) 2000-01-01 00:00:00

C) 2006-01-02 15:04:05

D) Текущее время

---

## Question 19: time.Duration

Как создать duration в 5 секунд?

A) `time.Duration(5)`

B) `5 * time.Second`

C) `time.Seconds(5)`

D) `time.NewDuration(5)`

---

## Question 20: log.Fatal

Что делает log.Fatal?

A) Только логирует

B) Логирует и вызывает os.Exit(1)

C) Вызывает panic

D) Возвращает ошибку

---

## Question 21: fmt.Sprintf

Что возвращает fmt.Sprintf?

A) error

B) int

C) string

D) []byte

---

## Question 22: fmt.Errorf

Что возвращает fmt.Errorf?

A) string

B) error

C) panic

D) nil

---

## Question 23: filepath.Join

Для чего используется filepath.Join?

A) Объединение строк

B) Кроссплатформенное объединение путей

C) Только для Unix

D) Только для Windows

---

## Question 24: http.ResponseWriter

Какой метод устанавливает статус код?

A) `w.Status(code)`

B) `w.WriteHeader(code)`

C) `w.SetStatus(code)`

D) `w.StatusCode = code`

---

## Question 25: http.NewRequest

Когда использовать http.NewRequest вместо http.Get?

A) Для GET запросов

B) Для кастомных headers и методов

C) Для быстрых запросов

D) Для синхронных запросов

---

## Question 26: json.NewEncoder

Куда пишет json.NewEncoder?

A) В файл

B) В io.Writer

C) В строку

D) В массив

---

## Question 27: os.MkdirAll

В чём отличие от os.Mkdir?

A) Создаёт только один уровень

B) Создаёт все промежуточные директории

C) Работает быстрее

D) Требует права root

---

## Question 28: io.ReadAll

Когда использовать io.ReadAll?

A) Для больших файлов

B) Для маленьких данных целиком

C) Для потоков

D) Для записи

---

## Question 29: http.Client Timeout

Как установить timeout для HTTP клиента?

A) `client.Timeout = time.Second`

B) `client.SetTimeout(time.Second)`

C) `client.Config.Timeout = time.Second`

D) Через context

---

## Question 30: defer file.Close()

Зачем defer для file.Close()?

A) Для скорости

B) Гарантированное закрытие при выходе

C) Для логирования

D) Не обязательно

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | `http.ListenAndServe(":8080", handler)` запускает сервер. |
| 2 | B | `func(w http.ResponseWriter, r *http.Request)`. |
| 3 | A | `http.Get(url)` для простого GET. |
| 4 | B | `json:"-"` игнорирует поле. |
| 5 | B | omitempty пропускает zero values. |
| 6 | B | Возвращает `[]byte, error`. |
| 7 | B | Decoder для потокового чтения из Reader. |
| 8 | A | `Read(p []byte) (n int, err error)`. |
| 9 | B | EOF — конец данных, не ошибка. |
| 10 | B | Копирует из Reader в Writer. |
| 11 | B | Возвращает `[]byte, error`. |
| 12 | A | 0644 (rw-r--r--) по умолчанию для Create. |
| 13 | B | Пустую строку для несуществующей. |
| 14 | B | Args[0] — имя программы. |
| 15 | B | Возвращает bool. |
| 16 | B | Для эффективной конкатенации. |
| 17 | C | Возвращает time.Time. |
| 18 | C | 2006-01-02 15:04:05 — референсное время Go. |
| 19 | B | `5 * time.Second`. |
| 20 | B | Логирует и вызывает os.Exit(1). |
| 21 | C | Возвращает string. |
| 22 | B | Возвращает error. |
| 23 | B | Кроссплатформенное объединение путей. |
| 24 | B | `WriteHeader(code)` устанавливает статус. |
| 25 | B | Для кастомных headers и методов. |
| 26 | B | Пишет в io.Writer. |
| 27 | B | Создаёт все промежуточные директории. |
| 28 | B | Для чтения маленьких данных целиком. |
| 29 | A | `client.Timeout = duration`. |
| 30 | B | Гарантированное закрытие файла. |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **27-30 правильных (90-100%)** | 🏆 Отлично! | Вы отлично знаете stdlib. |
| **21-26 правильных (70-89%)** | ✅ Хорошо | Повторите io и json. |
| **15-20 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте net/http. |
| **Менее 15 правильных (<50%)** | 📚 Нужно повторить | Внимательно перечитайте лекцию. |

---

