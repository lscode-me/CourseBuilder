# Testing - Quiz

Проверьте свои знания по теме "Тестирование в Go".

---

## Question 1: Файлы тестов

Какой суффикс должен быть у файлов с тестами?

A) _spec.go

B) _test.go

C) .test.go

D) _tests.go

---

## Question 2: Сигнатура теста

Какая сигнатура правильная для теста?

A) `func TestAdd()`

B) `func TestAdd(t *testing.T)`

C) `func Test_Add(t testing.T)`

D) `func testAdd(t *testing.T)`

---

## Question 3: Запуск тестов

Какая команда запускает все тесты?

A) `go run test`

B) `go test`

C) `go check`

D) `go verify`

---

## Question 4: Verbose output

Как запустить тесты с подробным выводом?

A) `go test --verbose`

B) `go test -v`

C) `go test -debug`

D) `go test -d`

---

## Question 5: Конкретный тест

Как запустить только TestAdd?

A) `go test TestAdd`

B) `go test -run TestAdd`

C) `go test -only TestAdd`

D) `go test -name TestAdd`

---

## Question 6: t.Error vs t.Fatal

В чём разница между t.Error и t.Fatal?

A) Error быстрее

B) Fatal останавливает тест, Error продолжает

C) Разницы нет

D) Error для warnings

---

## Question 7: Table-driven tests

Что такое table-driven tests?

A) Тесты для баз данных

B) Тесты с таблицей тестовых случаев

C) HTML тесты

D) Тесты Excel файлов

---

## Question 8: t.Run

Для чего используется t.Run?

A) Запуск программы

B) Создание подтестов

C) Запуск горутины

D) Выполнение скрипта

---

## Question 9: t.Parallel

Что делает t.Parallel()?

A) Запускает тест параллельно

B) Создаёт несколько копий теста

C) Ускоряет тест

D) Блокирует параллельное выполнение

---

## Question 10: t.Helper

Для чего используется t.Helper()?

A) Ускоряет тест

B) Показывает правильную строку в ошибках

C) Создаёт helper функцию

D) Пропускает тест

---

## Question 11: Бенчмарк

Какой префикс у бенчмарков?

A) Test

B) Benchmark

C) Perf

D) Speed

---

## Question 12: Сигнатура бенчмарка

Какая сигнатура правильная?

A) `func BenchmarkAdd(t *testing.T)`

B) `func BenchmarkAdd(b *testing.B)`

C) `func BenchmarkAdd()`

D) `func Benchmark_Add(b testing.B)`

---

## Question 13: b.N

Что такое b.N в бенчмарке?

A) Количество запусков, определённое фреймворком

B) Номер итерации

C) Размер данных

D) Количество CPU

---

## Question 14: Запуск бенчмарков

Как запустить бенчмарки?

A) `go bench`

B) `go test -bench=.`

C) `go test -benchmark`

D) `go test -perf`

---

## Question 15: b.ReportAllocs

Что делает b.ReportAllocs()?

A) Выделяет память

B) Показывает количество аллокаций

C) Освобождает память

D) Логирует ошибки

---

## Question 16: Coverage

Как получить coverage отчёт?

A) `go test -cover`

B) `go test -coverage`

C) `go cover`

D) `go test -report`

---

## Question 17: HTML coverage

Как сгенерировать HTML отчёт coverage?

A) `go test -html`

B) `go tool cover -html=coverage.out`

C) `go cover -html`

D) `go test -coverhtml`

---

## Question 18: TestMain

Для чего используется TestMain?

A) Как альтернативная точка входа

B) Для setup/teardown всего пакета

C) Для main тестов

D) Для запуска main функции

---

## Question 19: t.Cleanup

Когда выполняется t.Cleanup?

A) В начале теста

B) После завершения теста

C) При ошибке

D) Вручную

---

## Question 20: Example функции

Какой комментарий проверяет вывод?

A) `// Expected:`

B) `// Output:`

C) `// Result:`

D) `// Returns:`

---

## Question 21: Race detector

Как запустить с race detector?

A) `go test -race`

B) `go test -detect-race`

C) `go test -concurrent`

D) `go test -thread`

---

## Question 22: Skip test

Как пропустить тест?

A) `t.Skip("reason")`

B) `t.Ignore("reason")`

C) `return`

D) `t.Pass()`

---

## Question 23: Mock

Что рекомендуется для mocking в Go?

A) Специальные mock библиотеки

B) Интерфейсы и свои mock реализации

C) Reflection

D) Generics

---

## Question 24: Failing test

Как пометить тест как failed без остановки?

A) `t.Fail()`

B) `t.Failed()`

C) `t.SetFailed()`

D) `t.Mark()`

---

## Question 25: testdata

Для чего используется директория testdata/?

A) Кэш тестов

B) Тестовые данные (игнорируется go build)

C) Результаты тестов

D) Временные файлы

---

## Question 26: Покрытие функций

Как увидеть coverage по функциям?

A) `go tool cover -func=coverage.out`

B) `go test -func-coverage`

C) `go cover -functions`

D) `go test -show-funcs`

---

## Question 27: Параллельные тесты

Какая проблема с переменной цикла в параллельных тестах?

A) Нет проблем

B) Нужно копировать переменную

C) Нужен mutex

D) Нельзя использовать

---

## Question 28: Пакет тестов

В каком пакете пишутся тесты?

A) Отдельном test пакете

B) В том же пакете или *_test

C) Только в том же пакете

D) Только в отдельном

---

## Question 29: Black-box testing

Как писать black-box тесты?

A) Использовать пакет package_test

B) Невозможно в Go

C) Через reflection

D) Использовать internal

---

## Question 30: Test timeout

Как установить timeout для теста?

A) `go test -timeout 30s`

B) `go test -time 30s`

C) `go test -limit 30s`

D) `go test -max 30s`

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | Тестовые файлы должны иметь суффикс _test.go. |
| 2 | B | `func TestXxx(t *testing.T)` — правильная сигнатура. |
| 3 | B | `go test` запускает тесты. |
| 4 | B | `-v` для verbose output. |
| 5 | B | `-run TestAdd` запускает конкретный тест. |
| 6 | B | Fatal останавливает, Error продолжает тест. |
| 7 | B | Паттерн с таблицей тестовых случаев. |
| 8 | B | t.Run создаёт подтесты. |
| 9 | A | t.Parallel запускает тест параллельно. |
| 10 | B | Helper показывает caller в сообщениях об ошибках. |
| 11 | B | Benchmark* — префикс для бенчмарков. |
| 12 | B | `func BenchmarkXxx(b *testing.B)`. |
| 13 | A | b.N — количество итераций от фреймворка. |
| 14 | B | `go test -bench=.` запускает все бенчмарки. |
| 15 | B | ReportAllocs показывает количество аллокаций. |
| 16 | A | `go test -cover` показывает coverage. |
| 17 | B | `go tool cover -html=file` создаёт HTML. |
| 18 | B | TestMain для setup/teardown пакета. |
| 19 | B | Cleanup выполняется после теста. |
| 20 | B | `// Output:` проверяет вывод example. |
| 21 | A | `-race` включает race detector. |
| 22 | A | `t.Skip()` пропускает тест. |
| 23 | B | Интерфейсы — рекомендуемый способ. |
| 24 | A | `t.Fail()` помечает failed без остановки. |
| 25 | B | testdata/ для тестовых данных. |
| 26 | A | `go tool cover -func` показывает по функциям. |
| 27 | B | Нужно копировать: `tt := tt`. |
| 28 | B | В том же или с суффиксом _test. |
| 29 | A | `package_test` для black-box testing. |
| 30 | A | `-timeout 30s` устанавливает timeout. |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **27-30 правильных (90-100%)** | 🏆 Отлично! | Вы отлично понимаете тестирование. |
| **21-26 правильных (70-89%)** | ✅ Хорошо | Повторите бенчмарки и coverage. |
| **15-20 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте table-driven tests. |
| **Менее 15 правильных (<50%)** | 📚 Нужно повторить | Внимательно перечитайте лекцию. |

---

