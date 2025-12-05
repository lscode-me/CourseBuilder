# Continuous Integration - Quiz

Проверьте свои знания по CI, автоматизации сборки и тестированию.

---

## Question 1: Определение CI

Что является ключевой практикой Continuous Integration?

A) Деплой в production каждый час

B) Частая интеграция кода с автоматической проверкой каждого изменения

C) Написание документации для каждого commit

D) Ручное тестирование после каждого merge

---

## Question 2: Branching Strategy

Какая branching стратегия лучше всего подходит для CI/CD с частыми деплоями?

A) GitFlow с долгоживущими ветками

B) Trunk-based development

C) Feature branches живущие месяцами

D) Отдельная ветка для каждого разработчика

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

B) < 30 минут

C) < 10-15 минут

D) < 5 минут для всех тестов включая E2E

---

## Question 5: Flaky Tests

Что такое flaky test?

A) Тест, который всегда падает

B) Тест, который иногда проходит, иногда нет без изменений в коде

C) Тест без assertions

D) Тест, написанный на устаревшем фреймворке

---

## Question 6: Broken Build

Какой должен быть приоритет при обнаружении сломанного build?

A) Запланировать исправление на следующий спринт

B) Исправить в течение рабочего дня

C) Исправить немедленно (максимум 10 минут) или revert

D) Подождать, пока автор заметит

---

## Question 7: Caching

Что из перечисленного обычно кэшируется в CI pipeline?

A) Исходный код

B) Зависимости (pip packages, npm modules)

C) Test results

D) Git history

---

## Question 8: GitHub Flow

Какой порядок шагов в GitHub Flow?

A) Deploy → PR → Review → Merge

B) Branch → Changes → PR → CI + Review → Merge → Deploy

C) Merge → Branch → PR → Deploy

D) Review → Branch → Merge → CI

---

## Question 9: Build Once Deploy Many

Что означает принцип "Build once, deploy many"?

A) Собирать заново для каждого environment

B) Собрать artifact один раз и использовать для всех environments

C) Деплоить только один раз

D) Использовать только один сервер

---

## Question 10: Test Types

Какой тип тестов обычно запускается последним в CI pipeline?

A) Unit tests

B) Lint checks

C) E2E tests

D) Type checking

---

## Question 11: Branch Protection

Что обеспечивает Branch Protection в GitHub?

A) Шифрование веток

B) Обязательные проверки и reviews перед merge

C) Автоматическое удаление веток

D) Backup веток

---

## Question 12: Parallelization

Как параллелизация улучшает CI pipeline?

A) Уменьшает количество тестов

B) Выполняет независимые задачи одновременно, сокращая общее время

C) Увеличивает надёжность

D) Упрощает код тестов

---

## Question 13: CODEOWNERS

Для чего используется файл CODEOWNERS?

A) Для хранения паролей

B) Для определения, кто должен review изменения в определённых файлах

C) Для логирования изменений

D) Для автоматического форматирования

---

## Question 14: CI Metrics

Какая метрика показывает процент успешных builds?

A) Pipeline duration

B) Success rate

C) Queue time

D) Test coverage

---

## Question 15: Trunk-based Development

Сколько максимум должна жить feature branch в trunk-based development?

A) 1 месяц

B) 1 неделя

C) 1-2 дня

D) Пока фича не готова полностью

---

## Question 16: Security in CI

Какой инструмент используется для сканирования Docker images на уязвимости?

A) pytest

B) Trivy

C) ruff

D) mypy

---

## Question 17: Test Sharding

Что такое test sharding в CI?

A) Удаление ненужных тестов

B) Разбиение тестов на части для параллельного выполнения

C) Шифрование результатов тестов

D) Группировка тестов по категориям

---

## Question 18: Quality Gates

Что из перечисленного является типичным quality gate?

A) Минимальное количество комментариев в коде

B) Code coverage > 80%

C) Максимальное количество файлов в PR

D) Время написания кода

---

## Question 19: Self-hosted Runners

Когда имеет смысл использовать self-hosted runners?

A) Всегда, для экономии

B) Когда нужен доступ к internal resources или специфическое hardware

C) Только для open source проектов

D) Когда нет интернета

---

## Question 20: Environment Variables

Как правильно хранить секреты в CI pipeline?

A) В исходном коде

B) В переменных окружения, захардкоженных в workflow файле

C) В защищённых secrets хранилище CI системы (GitHub Secrets и т.д.)

D) В README файле

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | CI — частая интеграция с автоматической проверкой каждого изменения |
| 2 | B | Trunk-based: короткие ветки, частые merge, идеально для CI/CD |
| 3 | C | Test pyramid: много unit tests (быстрые), меньше integration, мало E2E |
| 4 | C | 10-15 минут — оптимальное время для быстрой обратной связи |
| 5 | B | Flaky test проходит/падает случайно без изменений в коде |
| 6 | C | Сломанный build — приоритет #1, максимум 10 минут на фикс или revert |
| 7 | B | Кэширование зависимостей значительно ускоряет pipeline |
| 8 | B | GitHub Flow: branch → changes → PR → CI + review → merge → deploy |
| 9 | B | Build once: один artifact используется во всех environments |
| 10 | C | E2E тесты медленные, запускаются после быстрых проверок |
| 11 | B | Branch protection обеспечивает обязательные checks и reviews |
| 12 | B | Параллельные независимые jobs сокращают общее время |
| 13 | B | CODEOWNERS определяет required reviewers для файлов |
| 14 | B | Success rate = successful builds / total builds |
| 15 | C | Trunk-based: branches живут 1-2 дня максимум |
| 16 | B | Trivy — популярный scanner для контейнеров и кода |
| 17 | B | Sharding — разбиение тестов для параллельного выполнения |
| 18 | B | Coverage > 80% — типичный quality gate |
| 19 | B | Self-hosted нужны для internal resources или спец. hardware |
| 20 | C | Секреты хранятся в защищённом secrets хранилище CI системы |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы отлично понимаете CI. Переходите к CD. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Повторите branching strategies и test pyramid. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы о pipeline оптимизации. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Внимательно изучите основы CI и примеры. |

---

