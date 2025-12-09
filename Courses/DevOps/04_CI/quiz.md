# Continuous Integration - Quiz

Проверьте свои знания по CI, автоматизации сборки и тестированию.

---

## Question 1: Определение CI







Что является ключевой практикой Continuous Integration?

A) Написание документации для каждого commit

B) Ручное тестирование после каждого merge

C) Деплой в production каждый час

D) Частая интеграция кода с автоматической проверкой каждого изменения

---

## Question 2: Branching Strategy







Какая branching стратегия лучше всего подходит для CI/CD с частыми деплоями?

A) Feature branches живущие месяцами

B) Trunk-based development

C) GitFlow с долгоживущими ветками

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

B) < 10-15 минут

C) < 5 минут для всех тестов включая E2E

D) < 30 минут

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

A) Test results

B) Git history

C) Зависимости (pip packages, npm modules)

D) Исходный код

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

A) Шифрование веток

B) Обязательные проверки и reviews перед merge

C) Автоматическое удаление веток

D) Backup веток

---

## Question 12: Parallelization







Как параллелизация улучшает CI pipeline?

A) Выполняет независимые задачи одновременно, сокращая общее время

B) Уменьшает количество тестов

C) Упрощает код тестов

D) Увеличивает надёжность

---

## Question 13: CODEOWNERS







Для чего используется файл CODEOWNERS?

A) Для автоматического форматирования

B) Для логирования изменений

C) Для хранения паролей

D) Для определения, кто должен review изменения в определённых файлах

---

## Question 14: CI Metrics







Какая метрика показывает процент успешных builds?

A) Pipeline duration

B) Queue time

C) Test coverage

D) Success rate

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

A) Минимальное количество комментариев в коде

B) Максимальное количество файлов в PR

C) Время написания кода

D) Code coverage > 80%

---

## Question 19: Self-hosted Runners







Когда имеет смысл использовать self-hosted runners?

A) Когда нет интернета

B) Только для open source проектов

C) Когда нужен доступ к internal resources или специфическое hardware

D) Всегда, для экономии

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
| 2 | B | Trunk-based: короткие ветки, частые merge, идеально для CI/CD |
| 3 | B | Test pyramid: много unit tests (быстрые), меньше integration, мало E2E |
| 4 | B | 10-15 минут — оптимальное время для быстрой обратной связи |
| 5 | A | Flaky test проходит/падает случайно без изменений в коде |
| 6 | B | Сломанный build — приоритет #1, максимум 10 минут на фикс или revert |
| 7 | C | Кэширование зависимостей значительно ускоряет pipeline |
| 8 | D | GitHub Flow: branch → changes → PR → CI + review → merge → deploy |
| 9 | C | Build once: один artifact используется во всех environments |
| 10 | B | E2E тесты медленные, запускаются после быстрых проверок |
| 11 | B | Branch protection обеспечивает обязательные checks и reviews |
| 12 | A | Параллельные независимые jobs сокращают общее время |
| 13 | D | CODEOWNERS определяет required reviewers для файлов |
| 14 | D | Success rate = successful builds / total builds |
| 15 | B | Trunk-based: branches живут 1-2 дня максимум |
| 16 | A | Trivy — популярный scanner для контейнеров и кода |
| 17 | C | Sharding — разбиение тестов для параллельного выполнения |
| 18 | D | Coverage > 80% — типичный quality gate |
| 19 | C | Self-hosted нужны для internal resources или спец. hardware |
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

