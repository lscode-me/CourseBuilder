# Continuous Integration - Quiz

Проверьте свои знания по CI, автоматизации сборки и тестированию.

---

## Question 1: Определение CI

Что является ключевой практикой Continuous Integration?

A) Частая интеграция кода с автоматической проверкой каждого изменения

B) Деплой в production каждый час

C) Ручное тестирование после каждого merge

D) Написание документации для каждого commit

---

## Question 2: Branching Strategy

Какая branching стратегия лучше всего подходит для CI/CD с частыми деплоями?

A) Feature branches живущие месяцами

B) Trunk-based development

C) Отдельная ветка для каждого разработчика

D) GitFlow с долгоживущими ветками

---

## Question 3: Test Pyramid

Согласно Test Pyramid, каких тестов должно быть больше всего?

A) E2E тестов

B) Integration тестов

C) Unit тестов

D) Manual тестов

---

## Question 4: Pipeline Time

Какое целевое время выполнения CI pipeline считается оптимальным?

A) < 1 час

B) < 10-15 минут

C) < 30 минут

D) < 5 минут для всех тестов включая E2E

---

## Question 5: Flaky Tests

Что такое flaky test?

A) Тест, который всегда падает

B) Тест, написанный на устаревшем фреймворке

C) Тест без assertions

D) Тест, который иногда проходит, иногда нет без изменений в коде

---

## Question 6: Broken Build

Какой должен быть приоритет при обнаружении сломанного build?

A) Запланировать исправление на следующий спринт

B) Подождать, пока автор заметит

C) Исправить в течение рабочего дня

D) Исправить немедленно (максимум 10 минут) или revert

---

## Question 7: Caching

Что из перечисленного обычно кэшируется в CI pipeline?

A) Исходный код

B) Test results

C) Зависимости (pip packages, npm modules)

D) Git history

---

## Question 8: GitHub Flow

Какой порядок шагов в GitHub Flow?

A) Review → Branch → Merge → CI

B) Deploy → PR → Review → Merge

C) Merge → Branch → PR → Deploy

D) Branch → Changes → PR → CI + Review → Merge → Deploy

---

## Question 9: Build Once Deploy Many

Что означает принцип "Build once, deploy many"?

A) Собрать artifact один раз и использовать для всех environments

B) Использовать только один сервер

C) Деплоить только один раз

D) Собирать заново для каждого environment

---

## Question 10: Test Types

Какой тип тестов обычно запускается последним в CI pipeline?

A) Type checking

B) E2E tests

C) Lint checks

D) Unit tests

---

## Question 11: Branch Protection

Что обеспечивает Branch Protection в GitHub?

A) Backup веток

B) Автоматическое удаление веток

C) Обязательные проверки и reviews перед merge

D) Шифрование веток

---

## Question 12: Parallelization

Как параллелизация улучшает CI pipeline?

A) Увеличивает надёжность

B) Выполняет независимые задачи одновременно, сокращая общее время

C) Уменьшает количество тестов

D) Упрощает код тестов

---

## Question 13: CODEOWNERS

Для чего используется файл CODEOWNERS?

A) Для автоматического форматирования

B) Для определения, кто должен review изменения в определённых файлах

C) Для хранения паролей

D) Для логирования изменений

---

## Question 14: CI Metrics

Какая метрика показывает процент успешных builds?

A) Success rate

B) Test coverage

C) Pipeline duration

D) Queue time

---

## Question 15: Trunk-based Development

Сколько максимум должна жить feature branch в trunk-based development?

A) 1 месяц

B) 1-2 дня

C) 1 неделя

D) Пока фича не готова полностью

---

## Question 16: Security in CI

Какой инструмент используется для сканирования Docker images на уязвимости?

A) ruff

B) Trivy

C) pytest

D) mypy

---

## Question 17: Test Sharding

Что такое test sharding в CI?

A) Шифрование результатов тестов

B) Разбиение тестов на части для параллельного выполнения

C) Удаление ненужных тестов

D) Группировка тестов по категориям

---

## Question 18: Quality Gates

Что из перечисленного является типичным quality gate?

A) Время написания кода

B) Минимальное количество комментариев в коде

C) Максимальное количество файлов в PR

D) Code coverage > 80%

---

## Question 19: Self-hosted Runners

Когда имеет смысл использовать self-hosted runners?

A) Когда нужен доступ к internal resources или специфическое hardware

B) Когда нет интернета

C) Только для open source проектов

D) Всегда, для экономии

---

## Question 20: Environment Variables

Как правильно хранить секреты в CI pipeline?

A) В переменных окружения, захардкоженных в workflow файле

B) В README файле

C) В исходном коде

D) В защищённых secrets хранилище CI системы (GitHub Secrets и т.д.)

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | CI — частая интеграция с автоматической проверкой каждого изменения |
| 2 | B | Trunk-based: короткие ветки, частые merge, идеально для CI/CD |
| 3 | C | Test pyramid: много unit tests (быстрые), меньше integration, мало E2E |
| 4 | B | 10-15 минут — оптимальное время для быстрой обратной связи |
| 5 | D | Flaky test проходит/падает случайно без изменений в коде |
| 6 | D | Сломанный build — приоритет #1, максимум 10 минут на фикс или revert |
| 7 | C | Кэширование зависимостей значительно ускоряет pipeline |
| 8 | D | GitHub Flow: branch → changes → PR → CI + review → merge → deploy |
| 9 | A | Build once: один artifact используется во всех environments |
| 10 | B | E2E тесты медленные, запускаются после быстрых проверок |
| 11 | C | Branch protection обеспечивает обязательные checks и reviews |
| 12 | B | Параллельные независимые jobs сокращают общее время |
| 13 | B | CODEOWNERS определяет required reviewers для файлов |
| 14 | A | Success rate = successful builds / total builds |
| 15 | B | Trunk-based: branches живут 1-2 дня максимум |
| 16 | B | Trivy — популярный scanner для контейнеров и кода |
| 17 | B | Sharding — разбиение тестов для параллельного выполнения |
| 18 | D | Coverage > 80% — типичный quality gate |
| 19 | A | Self-hosted нужны для internal resources или спец. hardware |
| 20 | D | Секреты хранятся в защищённом secrets хранилище CI системы |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы отлично понимаете CI. Переходите к CD. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Повторите branching strategies и test pyramid. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы о pipeline оптимизации. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Внимательно изучите основы CI и примеры. |

---

