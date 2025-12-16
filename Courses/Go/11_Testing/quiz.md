# Testing - Quiz

Проверьте свои знания по теме "Тестирование в Go".

---

## Question 1: Файлы тестов

Какой суффикс должен быть у файлов с тестами?

A) _spec.go

B) .test.go

C) _test.go

D) _tests.go

---

## Question 2: Сигнатура теста

Какая сигнатура правильная для теста?

A) `func testAdd(t *testing.T)`

B) `func Test_Add(t testing.T)`

C) `func TestAdd(t *testing.T)`

D) `func TestAdd()`

---

## Question 3: Запуск тестов

Какая команда запускает все тесты?

A) `go check`

B) `go test`

C) `go run test`

D) `go verify`

---

## Question 4: Verbose output

Как запустить тесты с подробным выводом?

A) `go test --verbose`

B) `go test -debug`

C) `go test -v`

D) `go test -d`

---

## Question 5: Конкретный тест

Как запустить только TestAdd?

A) `go test TestAdd`

B) `go test -only TestAdd`

C) `go test -run TestAdd`

D) `go test -name TestAdd`

---

## Question 6: t.Error vs t.Fatal

В чём разница между t.Error и t.Fatal?

A) Error для warnings

B) Error быстрее

C) Разницы нет

D) Fatal останавливает тест, Error продолжает

---

## Question 7: Table-driven tests

Что такое table-driven tests?

A) HTML тесты

B) Тесты с таблицей тестовых случаев

C) Тесты для баз данных

D) Тесты Excel файлов

---

## Question 8: t.Run

Для чего используется t.Run?

A) Выполнение скрипта

B) Запуск горутины

C) Создание подтестов

D) Запуск программы

---

## Question 9: t.Parallel

Что делает t.Parallel()?

A) Ускоряет тест

B) Запускает тест параллельно

C) Создаёт несколько копий теста

D) Блокирует параллельное выполнение

---

## Question 10: t.Helper

Для чего используется t.Helper()?

A) Показывает правильную строку в ошибках

B) Создаёт helper функцию

C) Ускоряет тест

D) Пропускает тест

---

## Question 11: Бенчмарк

Какой префикс у бенчмарков?

A) Speed

B) Benchmark

C) Test

D) Perf

---

## Question 12: Сигнатура бенчмарка

Какая сигнатура правильная?

A) `func Benchmark_Add(b testing.B)`

B) `func BenchmarkAdd(b *testing.B)`

C) `func BenchmarkAdd()`

D) `func BenchmarkAdd(t *testing.T)`

---

## Question 13: b.N

Что такое b.N в бенчмарке?

A) Номер итерации

B) Количество CPU

C) Размер данных

D) Количество запусков, определённое фреймворком

---

## Question 14: Запуск бенчмарков

Как запустить бенчмарки?

A) `go test -bench=.`

B) `go bench`

C) `go test -benchmark`

D) `go test -perf`

---

## Question 15: b.ReportAllocs

Что делает b.ReportAllocs()?

A) Логирует ошибки

B) Освобождает память

C) Показывает количество аллокаций

D) Выделяет память

---

## Question 16: Coverage

Как получить coverage отчёт?

A) `go test -cover`

B) `go test -coverage`

C) `go test -report`

D) `go cover`

---

## Question 17: HTML coverage

Как сгенерировать HTML отчёт coverage?

A) `go test -coverhtml`

B) `go cover -html`

C) `go tool cover -html=coverage.out`

D) `go test -html`

---

## Question 18: TestMain

Для чего используется TestMain?

A) Как альтернативная точка входа

B) Для setup/teardown всего пакета

C) Для запуска main функции

D) Для main тестов

---

## Question 19: t.Cleanup

Когда выполняется t.Cleanup?

A) После завершения теста

B) Вручную

C) При ошибке

D) В начале теста

---

## Question 20: Example функции

Какой комментарий проверяет вывод?

A) `// Expected:`

B) `// Returns:`

C) `// Result:`

D) `// Output:`

---

## Question 21: Race detector

Как запустить с race detector?

A) `go test -thread`

B) `go test -race`

C) `go test -concurrent`

D) `go test -detect-race`

---

## Question 22: Skip test

Как пропустить тест?

A) `t.Ignore("reason")`

B) `return`

C) `t.Skip("reason")`

D) `t.Pass()`

---

## Question 23: Mock

Что рекомендуется для mocking в Go?

A) Reflection

B) Интерфейсы и свои mock реализации

C) Специальные mock библиотеки

D) Generics

---

## Question 24: Failing test

Как пометить тест как failed без остановки?

A) `t.SetFailed()`

B) `t.Failed()`

C) `t.Mark()`

D) `t.Fail()`

---

## Question 25: testdata

Для чего используется директория testdata/?

A) Временные файлы

B) Результаты тестов

C) Тестовые данные (игнорируется go build)

D) Кэш тестов

---

## Question 26: Покрытие функций

Как увидеть coverage по функциям?

A) `go test -show-funcs`

B) `go tool cover -func=coverage.out`

C) `go test -func-coverage`

D) `go cover -functions`

---

## Question 27: Параллельные тесты

Какая проблема с переменной цикла в параллельных тестах?

A) Нет проблем

B) Нельзя использовать

C) Нужен mutex

D) Нужно копировать переменную

---

## Question 28: Пакет тестов

В каком пакете пишутся тесты?

A) Только в отдельном

B) Только в том же пакете

C) Отдельном test пакете

D) В том же пакете или *_test

---

## Question 29: Black-box testing

Как писать black-box тесты?

A) Использовать internal

B) Невозможно в Go

C) Через reflection

D) Использовать пакет package_test

---

## Question 30: Test timeout

Как установить timeout для теста?

A) `go test -limit 30s`

B) `go test -timeout 30s`

C) `go test -max 30s`

D) `go test -time 30s`

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | Тестовые файлы должны иметь суффикс _test.go. |
| 2 | C | `func TestXxx(t *testing.T)` — правильная сигнатура. |
| 3 | B | `go test` запускает тесты. |
| 4 | C | `-v` для verbose output. |
| 5 | C | `-run TestAdd` запускает конкретный тест. |
| 6 | D | Fatal останавливает, Error продолжает тест. |
| 7 | B | Паттерн с таблицей тестовых случаев. |
| 8 | C | t.Run создаёт подтесты. |
| 9 | B | t.Parallel запускает тест параллельно. |
| 10 | A | Helper показывает caller в сообщениях об ошибках. |
| 11 | B | Benchmark* — префикс для бенчмарков. |
| 12 | B | `func BenchmarkXxx(b *testing.B)`. |
| 13 | D | b.N — количество итераций от фреймворка. |
| 14 | A | `go test -bench=.` запускает все бенчмарки. |
| 15 | C | ReportAllocs показывает количество аллокаций. |
| 16 | A | `go test -cover` показывает coverage. |
| 17 | C | `go tool cover -html=file` создаёт HTML. |
| 18 | B | TestMain для setup/teardown пакета. |
| 19 | A | Cleanup выполняется после теста. |
| 20 | D | `// Output:` проверяет вывод example. |
| 21 | B | `-race` включает race detector. |
| 22 | C | `t.Skip()` пропускает тест. |
| 23 | B | Интерфейсы — рекомендуемый способ. |
| 24 | D | `t.Fail()` помечает failed без остановки. |
| 25 | C | testdata/ для тестовых данных. |
| 26 | B | `go tool cover -func` показывает по функциям. |
| 27 | D | Нужно копировать: `tt := tt`. |
| 28 | D | В том же или с суффиксом _test. |
| 29 | D | `package_test` для black-box testing. |
| 30 | B | `-timeout 30s` устанавливает timeout. |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **27-30 правильных (90-100%)** | 🏆 Отлично! | Вы отлично понимаете тестирование. |
| **21-26 правильных (70-89%)** | ✅ Хорошо | Повторите бенчмарки и coverage. |
| **15-20 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте table-driven tests. |
| **Менее 15 правильных (<50%)** | 📚 Нужно повторить | Внимательно перечитайте лекцию. |

---

