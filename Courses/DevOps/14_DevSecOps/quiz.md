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

B) Использовать secrets management tools (Vault, AWS SM)

C) Хардкодить в коде

D) Хранить в .env файле в Git

---

## Question 6: Container Security





Какая практика НЕ является best practice для Docker security?

A) Использовать latest tag

B) Использовать non-root user

C) Минимизировать количество packages

D) Read-only filesystem

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

A) Логирование

B) CI/CD

C) Policy as Code — проверка соответствия политикам

D) Мониторинг

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

A) Ручная проверка compliance раз в год

B) Описание и автоматическая проверка compliance-требований в виде кода

C) Документация compliance в Word файлах

D) Проверка compliance только аудиторами

---

## Question 12: AWS Config





Для чего используется AWS Config?

A) CI/CD pipeline

B) Deployment приложений

C) Логирование приложений

D) Автоматический мониторинг compliance AWS ресурсов

---

## Question 13: Cloud Custodian





Что позволяет делать Cloud Custodian?

A) Определять policies и автоматически remediate non-compliant ресурсы

B) Только генерировать отчёты

C) Управлять DNS

D) Только мониторинг облачных ресурсов

---

## Question 14: Compliance Frameworks





Какой framework НЕ относится к compliance стандартам?

A) DORA metrics

B) SOC 2

C) HIPAA

D) PCI DSS

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

A) Доверять всему внутри сети

B) Не доверять по умолчанию, проверять каждый запрос

C) Отключить все проверки

D) Только для внешних пользователей

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
| 1 | B | Shift Left = security проверки максимально рано |
| 2 | A | SAST — статический анализ исходного кода |
| 3 | B | SCA проверяет уязвимости в зависимостях |
| 4 | D | DAST тестирует работающее приложение |
| 5 | B | Secrets management tools (Vault, AWS SM) |
| 6 | A | latest tag — плохая практика (нет воспроизводимости) |
| 7 | D | Trivy сканирует containers и IaC |
| 8 | B | GitLeaks ищет секреты в Git history |
| 9 | C | OPA — Policy as Code |
| 10 | B | В DevSecOps все отвечают за безопасность |
| 11 | B | Compliance as Code — автоматизация compliance требований |
| 12 | D | AWS Config мониторит compliance AWS ресурсов |
| 13 | A | Cloud Custodian — policy engine с auto-remediation |
| 14 | A | DORA metrics — метрики DevOps, не compliance framework |
| 15 | C | Runtime security: Falco, network policies, monitoring |
| 16 | B | Zero Trust: не доверять по умолчанию, проверять каждый запрос |
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

