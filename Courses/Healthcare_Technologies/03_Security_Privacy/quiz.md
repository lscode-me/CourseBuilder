# Security & Privacy - Quiz

Проверьте свои знания по безопасности и конфиденциальности в healthcare: HIPAA, GDPR, PHI, encryption, access control.

---

## Question 1: HIPAA

HIPAA регулирует:

A) Цены на лекарства

B) Защиту медицинских данных

C) Качество медицинской помощи

D) Обучение врачей

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

A) 10

B) 18

C) 25

D) Все персональные данные

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

B) Когда (timestamp)

C) Пароль пользователя

D) К чему обращались (resource_id)

---

## Question 8: MFA

Многофакторная аутентификация (MFA) требует:

A) Только пароль

B) Два или более факторов аутентификации

C) Только биометрию

D) Только смарт-карту

---

## Question 9: HIPAA Breach Notification

В течение какого времени нужно уведомить пациентов о breach (если затронуто >500 человек)?

A) 24 часа

B) 30 дней

C) 60 дней

D) 90 дней

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

A) 1 минута

B) 15 минут

C) 1 час

D) 8 часов

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

A) Между всеми сотрудниками

B) С третьими сторонами, имеющими доступ к PHI

C) Только с пациентами

D) Только с страховыми компаниями

---

## Question 14: Encryption at Rest

Encryption at rest защищает данные:

A) При передаче по сети

B) При хранении на диске

C) При обработке в памяти

D) При отображении пользователю

---

## Question 15: Breach Response

Первый шаг при обнаружении breach:

A) Уведомить прессу

B) Identify и Contain (выявить и остановить)

C) Удалить все данные

D) Уволить ответственных

---

## Answers

1. **B** - Защита медицинских данных (Health Insurance Portability and Accountability Act)
2. **B** - Protected Health Information (защищённая медицинская информация)
3. **B** - 18 идентификаторов по правилу Safe Harbor
4. **B** - Право на удаление данных ("право быть забытым")
5. **B** - Encryption in transit (шифрование при передаче)
6. **A** - Role-Based Access Control (управление доступом на основе ролей)
7. **C** - Пароли никогда не логируются, даже хэши
8. **B** - Два или более факторов (пароль + OTP, биометрия и т.д.)
9. **C** - 60 дней для уведомления пациентов
10. **A** - Parameterized queries предотвращают SQL injection
11. **B** - 15 минут неактивности — стандартный таймаут
12. **B** - Явное (explicit) согласие пациента
13. **B** - С третьими сторонами, обрабатывающими PHI
14. **B** - При хранении на диске (at rest)
15. **B** - Identify и Contain — сначала выявить и остановить утечку
