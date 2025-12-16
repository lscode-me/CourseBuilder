# Standard Library - Quiz

Проверьте свои знания по теме "Стандартная библиотека Go".

---

## Question 1: HTTP сервер

Какая функция запускает HTTP сервер?

A) `http.Start()`

B) `http.Run()`

C) `http.Server()`

D) `http.ListenAndServe()`

---

## Question 2: HTTP handler

Какая сигнатура у HTTP handler функции?

A) `func(r *http.Request) http.Response`

B) `func(w http.Writer, r *http.Request)`

C) `func(w http.ResponseWriter, r *http.Request)`

D) `func(w http.Response, r http.Request)`

---

## Question 3: HTTP клиент

Как сделать простой GET запрос?

A) `http.Fetch(url)`

B) `http.Get(url)`

C) `http.Request(url)`

D) `http.Download(url)`

---

## Question 4: JSON маршалинг

Какой тег игнорирует поле при JSON?

A) `json:"skip"`

B) `json:"omit"`

C) `json:"-"`

D) `json:"ignore"`

---

## Question 5: omitempty

Что делает тег `json:"name,omitempty"`?

A) Делает поле обязательным

B) Пропускает zero value при сериализации

C) Устанавливает default

D) Игнорирует поле

---

## Question 6: json.Marshal

Что возвращает json.Marshal?

A) string

B) *json.Result

C) []byte, error

D) io.Reader

---

## Question 7: json.Decoder

Для чего используется json.Decoder?

A) Декодирование строки

B) Шифрование JSON

C) Валидация JSON

D) Потоковое декодирование из Reader

---

## Question 8: io.Reader

Какой метод определяет io.Reader?

A) `GetBytes() []byte`

B) `ReadAll() []byte`

C) `Data() []byte`

D) `Read(p []byte) (n int, err error)`

---

## Question 9: io.EOF

Что означает io.EOF?

A) Ошибка чтения

B) Конец данных

C) Timeout

D) Файл не найден

---

## Question 10: io.Copy

Что делает io.Copy?

A) Создаёт бэкап

B) Копирует данные из Reader в Writer

C) Копирует файлы

D) Клонирует объект

---

## Question 11: os.ReadFile

Что возвращает os.ReadFile?

A) []byte, error

B) io.Reader

C) *os.File

D) string

---

## Question 12: os.Create

Какие права у файла по умолчанию?

A) 0777

B) 0644

C) 0755

D) 0666

---

## Question 13: os.Getenv

Что возвращает os.Getenv для несуществующей переменной?

A) Пустую строку

B) panic

C) nil

D) Ошибку

---

## Question 14: os.Args

Что содержит os.Args[0]?

A) Имя программы

B) Первый аргумент

C) Версию Go

D) Рабочую директорию

---

## Question 15: strings.Contains

Что возвращает strings.Contains?

A) bool

B) error

C) string

D) int

---

## Question 16: strings.Builder

Для чего используется strings.Builder?

A) Форматирование

B) Парсинг строк

C) Эффективная конкатенация строк

D) Поиск в строках

---

## Question 17: time.Now

Что возвращает time.Now()?

A) string

B) int64

C) *time.Time

D) time.Time

---

## Question 18: time.Format

Какое референсное время используется?

A) Текущее время

B) 2006-01-02 15:04:05

C) 2000-01-01 00:00:00

D) 1970-01-01 00:00:00

---

## Question 19: time.Duration

Как создать duration в 5 секунд?

A) `5 * time.Second`

B) `time.Seconds(5)`

C) `time.Duration(5)`

D) `time.NewDuration(5)`

---

## Question 20: log.Fatal

Что делает log.Fatal?

A) Только логирует

B) Возвращает ошибку

C) Вызывает panic

D) Логирует и вызывает os.Exit(1)

---

## Question 21: fmt.Sprintf

Что возвращает fmt.Sprintf?

A) []byte

B) int

C) error

D) string

---

## Question 22: fmt.Errorf

Что возвращает fmt.Errorf?

A) string

B) panic

C) error

D) nil

---

## Question 23: filepath.Join

Для чего используется filepath.Join?

A) Только для Unix

B) Только для Windows

C) Кроссплатформенное объединение путей

D) Объединение строк

---

## Question 24: http.ResponseWriter

Какой метод устанавливает статус код?

A) `w.SetStatus(code)`

B) `w.StatusCode = code`

C) `w.Status(code)`

D) `w.WriteHeader(code)`

---

## Question 25: http.NewRequest

Когда использовать http.NewRequest вместо http.Get?

A) Для синхронных запросов

B) Для кастомных headers и методов

C) Для GET запросов

D) Для быстрых запросов

---

## Question 26: json.NewEncoder

Куда пишет json.NewEncoder?

A) В строку

B) В массив

C) В io.Writer

D) В файл

---

## Question 27: os.MkdirAll

В чём отличие от os.Mkdir?

A) Создаёт только один уровень

B) Работает быстрее

C) Создаёт все промежуточные директории

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

A) `client.SetTimeout(time.Second)`

B) Через context

C) `client.Config.Timeout = time.Second`

D) `client.Timeout = time.Second`

---

## Question 30: defer file.Close()

Зачем defer для file.Close()?

A) Для логирования

B) Гарантированное закрытие при выходе

C) Для скорости

D) Не обязательно

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | D | `http.ListenAndServe(":8080", handler)` запускает сервер. |
| 2 | C | `func(w http.ResponseWriter, r *http.Request)`. |
| 3 | B | `http.Get(url)` для простого GET. |
| 4 | C | `json:"-"` игнорирует поле. |
| 5 | B | omitempty пропускает zero values. |
| 6 | C | Возвращает `[]byte, error`. |
| 7 | D | Decoder для потокового чтения из Reader. |
| 8 | D | `Read(p []byte) (n int, err error)`. |
| 9 | B | EOF — конец данных, не ошибка. |
| 10 | B | Копирует из Reader в Writer. |
| 11 | A | Возвращает `[]byte, error`. |
| 12 | B | 0644 (rw-r--r--) по умолчанию для Create. |
| 13 | A | Пустую строку для несуществующей. |
| 14 | A | Args[0] — имя программы. |
| 15 | A | Возвращает bool. |
| 16 | C | Для эффективной конкатенации. |
| 17 | D | Возвращает time.Time. |
| 18 | B | 2006-01-02 15:04:05 — референсное время Go. |
| 19 | A | `5 * time.Second`. |
| 20 | D | Логирует и вызывает os.Exit(1). |
| 21 | D | Возвращает string. |
| 22 | C | Возвращает error. |
| 23 | C | Кроссплатформенное объединение путей. |
| 24 | D | `WriteHeader(code)` устанавливает статус. |
| 25 | B | Для кастомных headers и методов. |
| 26 | C | Пишет в io.Writer. |
| 27 | C | Создаёт все промежуточные директории. |
| 28 | B | Для чтения маленьких данных целиком. |
| 29 | D | `client.Timeout = duration`. |
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

