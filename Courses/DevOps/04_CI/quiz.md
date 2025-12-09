# Continuous Integration - Quiz

Проверьте свои знания по CI, автоматизации сборки и тестированию.

---

## Question 1: Определение CI





Что является ключевой практикой Continuous Integration?

A) Деплой в production каждый час

B) Написание документации для каждого commit

C) Ручное тестирование после каждого merge

D) Частая интеграция кода с автоматической проверкой каждого изменения

---

## Question 2: Branching Strategy





Какая branching стратегия лучше всего подходит для CI/CD с частыми деплоями?

A) GitFlow с долгоживущими ветками

B) Feature branches живущие месяцами

C) Trunk-based development

D) Отдельная ветка для каждого разработчика

---

## Question 3: Test Pyramid





Согласно Test Pyramid, каких тестов должно быть больше всего?

A) Manual тестов

B) Unit тестов

C) Integration тестов

D) E2E тестов

---

## Question 4: Pipeline Time





Какое целевое время выполнения CI pipeline считается оптимальным?

A) < 1 час

B) < 5 минут для всех тестов включая E2E

C) < 30 минут

D) < 10-15 минут

---

## Question 5: Flaky Tests





Что такое flaky test?

A) Тест, который иногда проходит, иногда нет без изменений в коде

B) Тест, который всегда падает

C) Тест без assertions

D) Тест, написанный на устаревшем фреймворке

---

## Question 6: Broken Build





Какой должен быть приоритет при обнаружении сломанного build?

A) Запланировать исправление на следующий спринт

B) Исправить немедленно (максимум 10 минут) или revert

C) Исправить в течение рабочего дня

D) Подождать, пока автор заметит

---

## Question 7: Caching





Что из перечисленного обычно кэшируется в CI pipeline?

A) Исходный код

B) Git history

C) Test results

D) Зависимости (pip packages, npm modules)

---

## Question 8: GitHub Flow





Какой порядок шагов в GitHub Flow?

A) Merge → Branch → PR → Deploy

B) Review → Branch → Merge → CI

C) Deploy → PR → Review → Merge

D) Branch → Changes → PR → CI + Review → Merge → Deploy

---

## Question 9: Build Once Deploy Many





Что означает принцип "Build once, deploy many"?

A) Деплоить только один раз

B) Использовать только один сервер

C) Собрать artifact один раз и использовать для всех environments

D) Собирать заново для каждого environment

---

## Question 10: Test Types





Какой тип тестов обычно запускается последним в CI pipeline?

A) Unit tests

B) E2E tests

C) Type checking

D) Lint checks

---

## Question 11: Branch Protection





Что обеспечивает Branch Protection в GitHub?

A) Обязательные проверки и reviews перед merge

B) Автоматическое удаление веток

C) Шифрование веток

D) Backup веток

---

## Question 12: Parallelization





Как параллелизация улучшает CI pipeline?

A) Упрощает код тестов

B) Уменьшает количество тестов

C) Увеличивает надёжность

D) Выполняет независимые задачи одновременно, сокращая общее время

---

## Question 13: CODEOWNERS





Для чего используется файл CODEOWNERS?

A) Для логирования изменений

B) Для автоматического форматирования

C) Для определения, кто должен review изменения в определённых файлах

D) Для хранения паролей

---

## Question 14: CI Metrics





Какая метрика показывает процент успешных builds?

A) Success rate

B) Queue time

C) Pipeline duration

D) Test coverage

---

## Question 15: Trunk-based Development





Сколько максимум должна жить feature branch в trunk-based development?

A) Пока фича не готова полностью

B) 1-2 дня

C) 1 неделя

D) 1 месяц

---

## Question 16: Security in CI





Какой инструмент используется для сканирования Docker images на уязвимости?

A) Trivy

B) mypy

C) ruff

D) pytest

---

## Question 17: Test Sharding





Что такое test sharding в CI?

A) Шифрование результатов тестов

B) Группировка тестов по категориям

C) Разбиение тестов на части для параллельного выполнения

D) Удаление ненужных тестов

---

## Question 18: Quality Gates





Что из перечисленного является типичным quality gate?

A) Code coverage > 80%

B) Время написания кода

C) Максимальное количество файлов в PR

D) Минимальное количество комментариев в коде

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

A) В защищённых secrets хранилище CI системы (GitHub Secrets и т.д.)

B) В исходном коде

C) В README файле

D) В переменных окружения, захардкоженных в workflow файле

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | D | CI — частая интеграция с автоматической проверкой каждого изменения |
| 2 | C | Trunk-based: короткие ветки, частые merge, идеально для CI/CD |
| 3 | B | Test pyramid: много unit tests (быстрые), меньше integration, мало E2E |
| 4 | D | 10-15 минут — оптимальное время для быстрой обратной связи |
| 5 | A | Flaky test проходит/падает случайно без изменений в коде |
| 6 | B | Сломанный build — приоритет #1, максимум 10 минут на фикс или revert |
| 7 | D | Кэширование зависимостей значительно ускоряет pipeline |
| 8 | D | GitHub Flow: branch → changes → PR → CI + review → merge → deploy |
| 9 | C | Build once: один artifact используется во всех environments |
| 10 | B | E2E тесты медленные, запускаются после быстрых проверок |
| 11 | A | Branch protection обеспечивает обязательные checks и reviews |
| 12 | D | Параллельные независимые jobs сокращают общее время |
| 13 | C | CODEOWNERS определяет required reviewers для файлов |
| 14 | A | Success rate = successful builds / total builds |
| 15 | B | Trunk-based: branches живут 1-2 дня максимум |
| 16 | A | Trivy — популярный scanner для контейнеров и кода |
| 17 | C | Sharding — разбиение тестов для параллельного выполнения |
| 18 | A | Coverage > 80% — типичный quality gate |
| 19 | B | Self-hosted нужны для internal resources или спец. hardware |
| 20 | A | Секреты хранятся в защищённом secrets хранилище CI системы |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы отлично понимаете CI. Переходите к CD. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Повторите branching strategies и test pyramid. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте разделы о pipeline оптимизации. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Внимательно изучите основы CI и примеры. |

---

