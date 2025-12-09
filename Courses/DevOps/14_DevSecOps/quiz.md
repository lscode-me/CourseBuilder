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

## Question 11: Compliance as Code


Что такое Compliance as Code?

A) Ручная проверка compliance раз в год

B) Описание и автоматическая проверка compliance-требований в виде кода

C) Документация compliance в Word файлах

D) Проверка compliance только аудиторами

---

## Question 12: AWS Config


Для чего используется AWS Config?

A) Deployment приложений

B) Автоматический мониторинг compliance AWS ресурсов

C) CI/CD pipeline

D) Логирование приложений

---

## Question 13: Cloud Custodian


Что позволяет делать Cloud Custodian?

A) Только мониторинг облачных ресурсов

B) Определять policies и автоматически remediate non-compliant ресурсы

C) Только генерировать отчёты

D) Управлять DNS

---

## Question 14: Compliance Frameworks


Какой framework НЕ относится к compliance стандартам?

A) SOC 2

B) PCI DSS

C) DORA metrics

D) HIPAA

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
| 11 | B | Compliance as Code — автоматизация compliance требований |
| 12 | B | AWS Config мониторит compliance AWS ресурсов |
| 13 | B | Cloud Custodian — policy engine с auto-remediation |
| 14 | C | DORA metrics — метрики DevOps, не compliance framework |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **13-14 правильных (90-100%)** | 🏆 Отлично! | Переходите к Career. |
| **10-12 правильных (70-89%)** | ✅ Хорошо | Повторите Compliance as Code. |
| **7-9 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте типы тестирования. |
| **Менее 7 правильных (<50%)** | 📚 Нужно повторить | Изучите основы DevSecOps. |

---

