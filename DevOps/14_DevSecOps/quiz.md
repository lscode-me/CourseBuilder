# DevSecOps - Quiz

Проверьте свои знания по безопасности в DevOps.

---

## Question 1: Shift Left


Что означает "Shift Left" в DevSecOps?

A) Внедрить security проверки максимально рано в pipeline

B) Игнорировать security на начальных этапах

C) Сдвинуть security проверки в конец pipeline

D) Перенести security в отдельную команду

---

## Question 2: SAST


Что такое SAST?

A) Static Application Security Testing — анализ исходного кода

B) Dynamic security testing

C) Software Audit System Test

D) Security API Scanning Tool

---

## Question 3: SCA


Что проверяет SCA (Software Composition Analysis)?

A) Network traffic

B) Уязвимости в зависимостях (dependencies)

C) User permissions

D) Код приложения

---

## Question 4: DAST


Когда выполняется DAST?

A) При написании кода

B) При code review

C) При компиляции кода

D) При запущенном приложении (runtime)

---

## Question 5: Secrets


Как правильно управлять секретами?

A) Передавать через email

B) Хардкодить в коде

C) Использовать secrets management tools (Vault, AWS SM)

D) Хранить в .env файле в Git

---

## Question 6: Container Security


Какая практика НЕ является best practice для Docker security?

A) Read-only filesystem

B) Минимизировать количество packages

C) Использовать latest tag

D) Использовать non-root user

---

## Question 7: Trivy


Для чего используется Trivy?

A) Для мониторинга

B) Для логирования

C) Для CI/CD

D) Для сканирования containers и IaC на уязвимости

---

## Question 8: GitLeaks


Что проверяет GitLeaks?

A) Memory leaks в коде

B) Performance issues

C) Network leaks

D) Секреты и credentials в Git history

---

## Question 9: OPA


Для чего используется OPA (Open Policy Agent)?

A) Логирование

B) CI/CD

C) Policy as Code — проверка соответствия политикам

D) Мониторинг

---

## Question 10: Security Responsibility


Кто отвечает за безопасность в DevSecOps?

A) Только developers

B) Все участники (developers, ops, security)

C) Только security team

D) Только management

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | Shift Left = security проверки максимально рано |
| 2 | A | SAST — статический анализ исходного кода |
| 3 | B | SCA проверяет уязвимости в зависимостях |
| 4 | D | DAST тестирует работающее приложение |
| 5 | C | Secrets management tools (Vault, AWS SM) |
| 6 | C | latest tag — плохая практика (нет воспроизводимости) |
| 7 | D | Trivy сканирует containers и IaC |
| 8 | D | GitLeaks ищет секреты в Git history |
| 9 | C | OPA — Policy as Code |
| 10 | B | В DevSecOps все отвечают за безопасность |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **9-10 правильных (90-100%)** | 🏆 Отлично! | Переходите к Career. |
| **7-8 правильных (70-89%)** | ✅ Хорошо | Повторите container security. |
| **5-6 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте типы тестирования. |
| **Менее 5 правильных (<50%)** | 📚 Нужно повторить | Изучите основы DevSecOps. |

---

