# Security & Privacy - Quiz

Проверьте свои знания по безопасности и конфиденциальности в healthcare: HIPAA, GDPR, PHI, encryption, access control.

---

## Question 1: HIPAA

HIPAA регулирует:

A) Обучение врачей

B) Защиту медицинских данных

C) Качество медицинской помощи

D) Цены на лекарства

---

## Question 2: PHI

Что такое PHI?

A) Protected Health Information

B) Public Health Information

C) Primary Health Indicator

D) Personal Health Insurance

---

## Question 3: De-identification

Сколько идентификаторов нужно удалить для Safe Harbor de-identification?

A) 18

B) Все персональные данные

C) 25

D) 10

---

## Question 4: GDPR Right to Erasure

GDPR "Right to Erasure" означает:

A) Право на удаление данных

B) Право на шифрование

C) Право на доступ к данным

D) Право на копию данных

---

## Question 5: TLS

TLS используется для:

A) Audit logging

B) Access control

C) Encryption in transit

D) Encryption at rest

---

## Question 6: RBAC

RBAC означает:

A) Role-Based Access Control

B) Remote Backup and Control

C) Record-Based Authentication Control

D) Risk-Based Audit Compliance

---

## Question 7: Audit Logging

Что НЕ нужно логировать при доступе к PHI?

A) Кто обращался (user_id)

B) Пароль пользователя

C) Когда (timestamp)

D) К чему обращались (resource_id)

---

## Question 8: MFA

Многофакторная аутентификация (MFA) требует:

A) Два или более факторов аутентификации

B) Только биометрию

C) Только смарт-карту

D) Только пароль

---

## Question 9: HIPAA Breach Notification

В течение какого времени нужно уведомить пациентов о breach (если затронуто >500 человек)?

A) 30 дней

B) 24 часа

C) 60 дней

D) 90 дней

---

## Question 10: SQL Injection

Как защититься от SQL Injection?

A) Шифровать базу данных

B) Использовать parameterized queries

C) Использовать firewall

D) Отключить интернет

---

## Question 11: Session Timeout

Рекомендуемый session timeout для healthcare приложений:

A) 15 минут

B) 8 часов

C) 1 час

D) 1 минута

---

## Question 12: GDPR Consent

Что требует GDPR для обработки персональных данных?

A) Явное согласие пациента

B) Только устное согласие

C) Письменное согласие на бумаге

D) Согласие не требуется

---

## Question 13: Business Associate Agreement

BAA (Business Associate Agreement) требуется:

A) С третьими сторонами, имеющими доступ к PHI

B) Только с страховыми компаниями

C) Только с пациентами

D) Между всеми сотрудниками

---

## Question 14: Encryption at Rest

Encryption at rest защищает данные:

A) При хранении на диске

B) При отображении пользователю

C) При передаче по сети

D) При обработке в памяти

---

## Question 15: Breach Response

Первый шаг при обнаружении breach:

A) Identify и Contain (выявить и остановить)

B) Удалить все данные

C) Уволить ответственных

D) Уведомить прессу

---

## Question 16: Least Privilege

Принцип "наименьших привилегий" означает:

A) Права только для администраторов

B) Давать только минимальные необходимые права

C) Дать максимальные права для удобства

D) Запретить весь доступ

---

## Question 17: GDPR DPO

Кто такой DPO в контексте GDPR?

A) Database Protection Officer

B) Data Protection Officer

C) Document Production Officer

D) Digital Processing Operator

---

## Question 18: XSS Prevention

Как защититься от XSS (Cross-Site Scripting)?

A) Использовать firewall

B) Увеличить timeout

C) Использовать VPN

D) Экранировать (escape) user input

---

## Question 19: Account Lockout

После скольких неудачных попыток входа рекомендуется блокировать аккаунт?

A) 20

B) 5

C) 2

D) 10

---

## Question 20: GDPR Right to Portability

GDPR "Right to Portability" означает:

A) Право на анонимность

B) Право удалить данные

C) Право на шифрование

D) Право перенести данные в другую систему

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | Защита медицинских данных (HIPAA) |
| 2 | A | Protected Health Information |
| 3 | A | 18 идентификаторов по правилу Safe Harbor |
| 4 | A | Право на удаление данных ("право быть забытым") |
| 5 | C | Encryption in transit (шифрование при передаче) |
| 6 | A | Role-Based Access Control |
| 7 | B | Пароли никогда не логируются, даже хэши |
| 8 | A | Два или более факторов (пароль + OTP, биометрия) |
| 9 | C | 60 дней для уведомления пациентов |
| 10 | B | Parameterized queries предотвращают SQL injection |
| 11 | A | 15 минут неактивности — стандартный таймаут |
| 12 | A | Явное (explicit) согласие пациента |
| 13 | A | С третьими сторонами, обрабатывающими PHI |
| 14 | A | При хранении на диске (at rest) |
| 15 | A | Identify и Contain — сначала выявить и остановить |
| 16 | B | Минимальные необходимые права |
| 17 | B | Data Protection Officer |
| 18 | D | Экранировать user input предотвращает XSS |
| 19 | B | 5 неудачных попыток — стандартная практика |
| 20 | D | Right to Portability — право перенести данные |

---

## Scoring Guide

Подсчитайте количество правильных ответов:

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы отлично усвоили материал. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Повторите темы с ошибками. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Рекомендуется перечитать лекцию. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Внимательно перечитайте лекцию. |

---

