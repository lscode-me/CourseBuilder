# DevSecOps - Quiz

Проверьте свои знания по безопасности в DevOps.

---

## Question 1: Shift Left

Что означает "Shift Left" в DevSecOps?

A) Сдвинуть security проверки в конец pipeline

B) Внедрить security проверки максимально рано в pipeline

C) Перенести security в отдельную команду

D) Игнорировать security на начальных этапах

---

## Question 2: SAST

Что такое SAST?

A) Dynamic security testing

B) Static Application Security Testing — анализ исходного кода

C) Software Audit System Test

D) Security API Scanning Tool

---

## Question 3: SCA

Что проверяет SCA (Software Composition Analysis)?

A) Код приложения

B) Уязвимости в зависимостях (dependencies)

C) Network traffic

D) User permissions

---

## Question 4: DAST

Когда выполняется DAST?

A) При компиляции кода

B) При запущенном приложении (runtime)

C) При написании кода

D) При code review

---

## Question 5: Secrets

Как правильно управлять секретами?

A) Хардкодить в коде

B) Использовать secrets management tools (Vault, AWS SM)

C) Хранить в .env файле в Git

D) Передавать через email

---

## Question 6: Container Security

Какая практика НЕ является best practice для Docker security?

A) Использовать non-root user

B) Использовать latest tag

C) Минимизировать количество packages

D) Read-only filesystem

---

## Question 7: Trivy

Для чего используется Trivy?

A) Для CI/CD

B) Для сканирования containers и IaC на уязвимости

C) Для мониторинга

D) Для логирования

---

## Question 8: GitLeaks

Что проверяет GitLeaks?

A) Memory leaks в коде

B) Секреты и credentials в Git history

C) Network leaks

D) Performance issues

---

## Question 9: OPA

Для чего используется OPA (Open Policy Agent)?

A) Мониторинг

B) Policy as Code — проверка соответствия политикам

C) Логирование

D) CI/CD

---

## Question 10: Security Responsibility

Кто отвечает за безопасность в DevSecOps?

A) Только security team

B) Все участники (developers, ops, security)

C) Только developers

D) Только management

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | Shift Left = security проверки максимально рано |
| 2 | B | SAST — статический анализ исходного кода |
| 3 | B | SCA проверяет уязвимости в зависимостях |
| 4 | B | DAST тестирует работающее приложение |
| 5 | B | Secrets management tools (Vault, AWS SM) |
| 6 | B | latest tag — плохая практика (нет воспроизводимости) |
| 7 | B | Trivy сканирует containers и IaC |
| 8 | B | GitLeaks ищет секреты в Git history |
| 9 | B | OPA — Policy as Code |
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

