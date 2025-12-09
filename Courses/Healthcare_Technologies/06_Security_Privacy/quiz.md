# Security & Privacy - Quiz

Проверьте свои знания по безопасности и конфиденциальности в healthcare: HIPAA, GDPR, PHI, encryption, access control.

---

## Question 1: HIPAA



HIPAA регулирует:

A) Качество медицинской помощи

B) Обучение врачей

C) Цены на лекарства

D) Защиту медицинских данных

---

## Question 2: PHI



Что такое PHI?

A) Public Health Information

B) Protected Health Information

C) Personal Health Insurance

D) Primary Health Indicator

---

## Question 3: De-identification



Сколько идентификаторов нужно удалить для Safe Harbor de-identification?

A) 18

B) 10

C) Все персональные данные

D) 25

---

## Question 4: GDPR Right to Erasure



GDPR "Right to Erasure" означает:

A) Право на доступ к данным

B) Право на удаление данных

C) Право на шифрование

D) Право на копию данных

---

## Question 5: TLS



TLS используется для:

A) Encryption at rest

B) Encryption in transit

C) Access control

D) Audit logging

---

## Question 6: RBAC



RBAC означает:

A) Role-Based Access Control

B) Record-Based Authentication Control

C) Remote Backup and Control

D) Risk-Based Audit Compliance

---

## Question 7: Audit Logging



Что НЕ нужно логировать при доступе к PHI?

A) Кто обращался (user_id)

B) К чему обращались (resource_id)

C) Когда (timestamp)

D) Пароль пользователя

---

## Question 8: MFA



Многофакторная аутентификация (MFA) требует:

A) Только биометрию

B) Только пароль

C) Два или более факторов аутентификации

D) Только смарт-карту

---

## Question 9: HIPAA Breach Notification



В течение какого времени нужно уведомить пациентов о breach (если затронуто >500 человек)?

A) 60 дней

B) 30 дней

C) 90 дней

D) 24 часа

---

## Question 10: SQL Injection



Как защититься от SQL Injection?

A) Использовать parameterized queries

B) Шифровать базу данных

C) Использовать firewall

D) Отключить интернет

---

## Question 11: Session Timeout



Рекомендуемый session timeout для healthcare приложений:

A) 1 час

B) 15 минут

C) 8 часов

D) 1 минута

---

## Question 12: GDPR Consent



Что требует GDPR для обработки персональных данных?

A) Письменное согласие на бумаге

B) Явное согласие пациента

C) Только устное согласие

D) Согласие не требуется

---

## Question 13: Business Associate Agreement



BAA (Business Associate Agreement) требуется:

A) Только с страховыми компаниями

B) Только с пациентами

C) С третьими сторонами, имеющими доступ к PHI

D) Между всеми сотрудниками

---

## Question 14: Encryption at Rest



Encryption at rest защищает данные:

A) При хранении на диске

B) При обработке в памяти

C) При передаче по сети

D) При отображении пользователю

---

## Question 15: Breach Response



Первый шаг при обнаружении breach:

A) Identify и Contain (выявить и остановить)

B) Уведомить прессу

C) Уволить ответственных

D) Удалить все данные

---

## Question 16: Least Privilege



Принцип "наименьших привилегий" означает:

A) Дать максимальные права для удобства

B) Запретить весь доступ

C) Права только для администраторов

D) Давать только минимальные необходимые права

---

## Question 17: GDPR DPO



Кто такой DPO в контексте GDPR?

A) Document Production Officer

B) Data Protection Officer

C) Database Protection Officer

D) Digital Processing Operator

---

## Question 18: XSS Prevention



Как защититься от XSS (Cross-Site Scripting)?

A) Использовать firewall

B) Экранировать (escape) user input

C) Увеличить timeout

D) Использовать VPN

---

## Question 19: Account Lockout



После скольких неудачных попыток входа рекомендуется блокировать аккаунт?

A) 2

B) 20

C) 5

D) 10

---

## Question 20: GDPR Right to Portability



GDPR "Right to Portability" означает:

A) Право перенести данные в другую систему

B) Право удалить данные

C) Право на анонимность

D) Право на шифрование

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | D | Защита медицинских данных (HIPAA) |
| 2 | B | Protected Health Information |
| 3 | A | 18 идентификаторов по правилу Safe Harbor |
| 4 | B | Право на удаление данных ("право быть забытым") |
| 5 | B | Encryption in transit (шифрование при передаче) |
| 6 | A | Role-Based Access Control |
| 7 | D | Пароли никогда не логируются, даже хэши |
| 8 | C | Два или более факторов (пароль + OTP, биометрия) |
| 9 | A | 60 дней для уведомления пациентов |
| 10 | A | Parameterized queries предотвращают SQL injection |
| 11 | B | 15 минут неактивности — стандартный таймаут |
| 12 | B | Явное (explicit) согласие пациента |
| 13 | C | С третьими сторонами, обрабатывающими PHI |
| 14 | A | При хранении на диске (at rest) |
| 15 | A | Identify и Contain — сначала выявить и остановить |
| 16 | D | Минимальные необходимые права |
| 17 | B | Data Protection Officer |
| 18 | B | Экранировать user input предотвращает XSS |
| 19 | C | 5 неудачных попыток — стандартная практика |
| 20 | A | Right to Portability — право перенести данные |

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

