# DevSecOps - Quiz

Проверьте свои знания по безопасности в DevOps.

---

## Question 1: Shift Left







Что означает "Shift Left" в DevSecOps?

A) Игнорировать security на начальных этапах

B) Перенести security в отдельную команду

C) Внедрить security проверки максимально рано в pipeline

D) Сдвинуть security проверки в конец pipeline

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

A) User permissions

B) Уязвимости в зависимостях (dependencies)

C) Код приложения

D) Network traffic

---

## Question 4: DAST







Когда выполняется DAST?

A) При code review

B) При запущенном приложении (runtime)

C) При компиляции кода

D) При написании кода

---

## Question 5: Secrets







Как правильно управлять секретами?

A) Передавать через email

B) Использовать secrets management tools (Vault, AWS SM)

C) Хардкодить в коде

D) Хранить в .env файле в Git

---

## Question 6: Container Security







Какая практика НЕ является best practice для Docker security?

A) Использовать non-root user

B) Использовать latest tag

C) Read-only filesystem

D) Минимизировать количество packages

---

## Question 7: Trivy







Для чего используется Trivy?

A) Для логирования

B) Для мониторинга

C) Для CI/CD

D) Для сканирования containers и IaC на уязвимости

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

A) CI/CD

B) Мониторинг

C) Policy as Code — проверка соответствия политикам

D) Логирование

---

## Question 10: Security Responsibility







Кто отвечает за безопасность в DevSecOps?

A) Только security team

B) Все участники (developers, ops, security)

C) Только developers

D) Только management

---

## Question 11: Compliance as Code







Что такое Compliance as Code?

A) Проверка compliance только аудиторами

B) Описание и автоматическая проверка compliance-требований в виде кода

C) Ручная проверка compliance раз в год

D) Документация compliance в Word файлах

---

## Question 12: AWS Config







Для чего используется AWS Config?

A) Автоматический мониторинг compliance AWS ресурсов

B) Логирование приложений

C) Deployment приложений

D) CI/CD pipeline

---

## Question 13: Cloud Custodian







Что позволяет делать Cloud Custodian?

A) Управлять DNS

B) Только мониторинг облачных ресурсов

C) Определять policies и автоматически remediate non-compliant ресурсы

D) Только генерировать отчёты

---

## Question 14: Compliance Frameworks







Какой framework НЕ относится к compliance стандартам?

A) PCI DSS

B) HIPAA

C) SOC 2

D) DORA metrics

---

## Question 15: Runtime Security






Что включает runtime security для контейнеров?

A) Только антивирус

B) Только firewall

C) Falco, network policies, runtime monitoring

D) Только сканирование образов

---

## Question 16: Zero Trust






Что такое Zero Trust в DevSecOps?

A) Только для внешних пользователей

B) Доверять всему внутри сети

C) Отключить все проверки

D) Не доверять по умолчанию, проверять каждый запрос

---

## Question 17: Security Champions






Кто такие Security Champions?

A) Внешние аудиторы

B) Менеджеры

C) Разработчики, продвигающие security в своих командах

D) Специалисты по безопасности

---

## Question 18: Threat Modeling






Когда проводить threat modeling?

A) Только при инцидентах

B) На ранних этапах дизайна системы

C) После production deployment

D) Раз в год

---

## Question 19: SBOM






Что такое SBOM?

A) Software Budget of Materials

B) Security Best Of Methods

C) Software Bill of Materials — список компонентов приложения

D) System Build Operation Mode

---

## Question 20: Security Gates






Что такое security gates в pipeline?

A) Ручные approvals

B) Автоматические проверки безопасности, блокирующие deployment

C) Физические барьеры

D) Firewall rules

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | Shift Left = security проверки максимально рано |
| 2 | A | SAST — статический анализ исходного кода |
| 3 | B | SCA проверяет уязвимости в зависимостях |
| 4 | B | DAST тестирует работающее приложение |
| 5 | B | Secrets management tools (Vault, AWS SM) |
| 6 | B | latest tag — плохая практика (нет воспроизводимости) |
| 7 | D | Trivy сканирует containers и IaC |
| 8 | B | GitLeaks ищет секреты в Git history |
| 9 | C | OPA — Policy as Code |
| 10 | B | В DevSecOps все отвечают за безопасность |
| 11 | B | Compliance as Code — автоматизация compliance требований |
| 12 | A | AWS Config мониторит compliance AWS ресурсов |
| 13 | C | Cloud Custodian — policy engine с auto-remediation |
| 14 | D | DORA metrics — метрики DevOps, не compliance framework |
| 15 | C | Runtime security: Falco, network policies, monitoring |
| 16 | D | Zero Trust: не доверять по умолчанию, проверять каждый запрос |
| 17 | C | Security Champions — разработчики продвигающие security |
| 18 | B | Threat modeling на ранних этапах дизайна |
| 19 | C | SBOM — Software Bill of Materials |
| 20 | B | Security gates — автоматические проверки в pipeline |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **13-14 правильных (90-100%)** | 🏆 Отлично! | Переходите к Career. |
| **10-12 правильных (70-89%)** | ✅ Хорошо | Повторите Compliance as Code. |
| **7-9 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте типы тестирования. |
| **Менее 7 правильных (<50%)** | 📚 Нужно повторить | Изучите основы DevSecOps. |

---

