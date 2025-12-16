# DevSecOps - Quiz

Проверьте свои знания по безопасности в DevOps.

---

## Question 1: Shift Left

Что означает "Shift Left" в DevSecOps?

A) Сдвинуть security проверки в конец pipeline

B) Внедрить security проверки максимально рано в pipeline

C) Игнорировать security на начальных этапах

D) Перенести security в отдельную команду

---

## Question 2: SAST

Что такое SAST?

A) Security API Scanning Tool

B) Static Application Security Testing — анализ исходного кода

C) Dynamic security testing

D) Software Audit System Test

---

## Question 3: SCA

Что проверяет SCA (Software Composition Analysis)?

A) Код приложения

B) User permissions

C) Уязвимости в зависимостях (dependencies)

D) Network traffic

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

B) Хранить в .env файле в Git

C) Передавать через email

D) Использовать secrets management tools (Vault, AWS SM)

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

B) Для сканирования containers и IaC на уязвимости

C) Для логирования

D) Для CI/CD

---

## Question 8: GitLeaks

Что проверяет GitLeaks?

A) Memory leaks в коде

B) Network leaks

C) Performance issues

D) Секреты и credentials в Git history

---

## Question 9: OPA

Для чего используется OPA (Open Policy Agent)?

A) Policy as Code — проверка соответствия политикам

B) Мониторинг

C) Логирование

D) CI/CD

---

## Question 10: Security Responsibility

Кто отвечает за безопасность в DevSecOps?

A) Все участники (developers, ops, security)

B) Только management

C) Только developers

D) Только security team

---

## Question 11: Compliance as Code

Что такое Compliance as Code?

A) Проверка compliance только аудиторами

B) Ручная проверка compliance раз в год

C) Документация compliance в Word файлах

D) Описание и автоматическая проверка compliance-требований в виде кода

---

## Question 12: AWS Config

Для чего используется AWS Config?

A) CI/CD pipeline

B) Логирование приложений

C) Deployment приложений

D) Автоматический мониторинг compliance AWS ресурсов

---

## Question 13: Cloud Custodian

Что позволяет делать Cloud Custodian?

A) Управлять DNS

B) Только генерировать отчёты

C) Определять policies и автоматически remediate non-compliant ресурсы

D) Только мониторинг облачных ресурсов

---

## Question 14: Compliance Frameworks

Какой framework НЕ относится к compliance стандартам?

A) DORA metrics

B) PCI DSS

C) SOC 2

D) HIPAA

---

## Question 15: Runtime Security

Что включает runtime security для контейнеров?

A) Только firewall

B) Только сканирование образов

C) Только антивирус

D) Falco, network policies, runtime monitoring

---

## Question 16: Zero Trust

Что такое Zero Trust в DevSecOps?

A) Отключить все проверки

B) Только для внешних пользователей

C) Доверять всему внутри сети

D) Не доверять по умолчанию, проверять каждый запрос

---

## Question 17: Security Champions

Кто такие Security Champions?

A) Внешние аудиторы

B) Разработчики, продвигающие security в своих командах

C) Менеджеры

D) Специалисты по безопасности

---

## Question 18: Threat Modeling

Когда проводить threat modeling?

A) После production deployment

B) Раз в год

C) На ранних этапах дизайна системы

D) Только при инцидентах

---

## Question 19: SBOM

Что такое SBOM?

A) Security Best Of Methods

B) System Build Operation Mode

C) Software Budget of Materials

D) Software Bill of Materials — список компонентов приложения

---

## Question 20: Security Gates

Что такое security gates в pipeline?

A) Автоматические проверки безопасности, блокирующие deployment

B) Firewall rules

C) Ручные approvals

D) Физические барьеры

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | Shift Left = security проверки максимально рано |
| 2 | B | SAST — статический анализ исходного кода |
| 3 | C | SCA проверяет уязвимости в зависимостях |
| 4 | B | DAST тестирует работающее приложение |
| 5 | D | Secrets management tools (Vault, AWS SM) |
| 6 | C | latest tag — плохая практика (нет воспроизводимости) |
| 7 | B | Trivy сканирует containers и IaC |
| 8 | D | GitLeaks ищет секреты в Git history |
| 9 | A | OPA — Policy as Code |
| 10 | A | В DevSecOps все отвечают за безопасность |
| 11 | D | Compliance as Code — автоматизация compliance требований |
| 12 | D | AWS Config мониторит compliance AWS ресурсов |
| 13 | C | Cloud Custodian — policy engine с auto-remediation |
| 14 | A | DORA metrics — метрики DevOps, не compliance framework |
| 15 | D | Runtime security: Falco, network policies, monitoring |
| 16 | D | Zero Trust: не доверять по умолчанию, проверять каждый запрос |
| 17 | B | Security Champions — разработчики продвигающие security |
| 18 | C | Threat modeling на ранних этапах дизайна |
| 19 | D | SBOM — Software Bill of Materials |
| 20 | A | Security gates — автоматические проверки в pipeline |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **13-14 правильных (90-100%)** | 🏆 Отлично! | Переходите к Career. |
| **10-12 правильных (70-89%)** | ✅ Хорошо | Повторите Compliance as Code. |
| **7-9 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте типы тестирования. |
| **Менее 7 правильных (<50%)** | 📚 Нужно повторить | Изучите основы DevSecOps. |

---

