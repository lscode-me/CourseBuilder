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

A) Право на копию данных

B) Право на шифрование

C) Право на удаление данных

D) Право на доступ к данным

---

## Question 5: TLS





TLS используется для:

A) Encryption at rest

B) Audit logging

C) Encryption in transit

D) Access control

---

## Question 6: RBAC





RBAC означает:

A) Remote Backup and Control

B) Risk-Based Audit Compliance

C) Role-Based Access Control

D) Record-Based Authentication Control

---

## Question 7: Audit Logging





Что НЕ нужно логировать при доступе к PHI?

A) К чему обращались (resource_id)

B) Пароль пользователя

C) Когда (timestamp)

D) Кто обращался (user_id)

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

A) 24 часа

B) 90 дней

C) 30 дней

D) 60 дней

---

## Question 10: SQL Injection





Как защититься от SQL Injection?

A) Отключить интернет

B) Использовать firewall

C) Шифровать базу данных

D) Использовать parameterized queries

---

## Question 11: Session Timeout





Рекомендуемый session timeout для healthcare приложений:

A) 1 минута

B) 15 минут

C) 1 час

D) 8 часов

---

## Question 12: GDPR Consent





Что требует GDPR для обработки персональных данных?

A) Явное согласие пациента

B) Согласие не требуется

C) Только устное согласие

D) Письменное согласие на бумаге

---

## Question 13: Business Associate Agreement





BAA (Business Associate Agreement) требуется:

A) Только с страховыми компаниями

B) С третьими сторонами, имеющими доступ к PHI

C) Между всеми сотрудниками

D) Только с пациентами

---

## Question 14: Encryption at Rest





Encryption at rest защищает данные:

A) При хранении на диске

B) При передаче по сети

C) При отображении пользователю

D) При обработке в памяти

---

## Question 15: Breach Response





Первый шаг при обнаружении breach:

A) Уведомить прессу

B) Identify и Contain (выявить и остановить)

C) Удалить все данные

D) Уволить ответственных

---

## Question 16: Least Privilege





Принцип "наименьших привилегий" означает:

A) Запретить весь доступ

B) Дать максимальные права для удобства

C) Давать только минимальные необходимые права

D) Права только для администраторов

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

A) Экранировать (escape) user input

B) Использовать firewall

C) Использовать VPN

D) Увеличить timeout

---

## Question 19: Account Lockout





После скольких неудачных попыток входа рекомендуется блокировать аккаунт?

A) 5

B) 20

C) 10

D) 2

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
| 4 | C | Право на удаление данных ("право быть забытым") |
| 5 | C | Encryption in transit (шифрование при передаче) |
| 6 | C | Role-Based Access Control |
| 7 | B | Пароли никогда не логируются, даже хэши |
| 8 | C | Два или более факторов (пароль + OTP, биометрия) |
| 9 | D | 60 дней для уведомления пациентов |
| 10 | D | Parameterized queries предотвращают SQL injection |
| 11 | B | 15 минут неактивности — стандартный таймаут |
| 12 | A | Явное (explicit) согласие пациента |
| 13 | B | С третьими сторонами, обрабатывающими PHI |
| 14 | A | При хранении на диске (at rest) |
| 15 | B | Identify и Contain — сначала выявить и остановить |
| 16 | C | Минимальные необходимые права |
| 17 | B | Data Protection Officer |
| 18 | A | Экранировать user input предотвращает XSS |
| 19 | A | 5 неудачных попыток — стандартная практика |
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

