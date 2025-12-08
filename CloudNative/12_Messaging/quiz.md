# Cloud Native Development - Quiz
## Messaging: SQS, SNS, EventBridge

---

## Question 1: SQS Queue Types

Какой тип SQS queue гарантирует FIFO ordering и exactly-once delivery?

A) Standard Queue
B) FIFO Queue
C) Priority Queue
D) Express Queue

---

## Question 2: SNS vs SQS

Какое ключевое отличие SNS от SQS?

A) SNS — pull-based, SQS — push-based
B) SNS — pub/sub (fan-out), SQS — point-to-point queue
C) SNS дешевле
D) SQS не поддерживает filtering

---

## Question 3: Visibility Timeout

Что такое Visibility Timeout в SQS?

A) Время жизни сообщения в очереди
B) Время, в течение которого сообщение невидимо для других consumers после получения
C) Максимальное время обработки
D) Время между отправками

---

## Question 4: Long Polling

Зачем использовать Long Polling в SQS?

A) Для увеличения скорости доставки
B) Для уменьшения количества пустых ответов и снижения стоимости
C) Для шифрования сообщений
D) Для увеличения размера сообщений

---

## Question 5: EventBridge vs SNS

Когда предпочтительнее EventBridge вместо SNS?

A) Для отправки email notifications
B) Для маршрутизации событий на основе их содержимого (content-based routing)
C) Для SMS уведомлений
D) Для простого fan-out

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | FIFO Queue гарантирует порядок сообщений и exactly-once processing. Standard — at-least-once, best-effort ordering. |
| 2 | B | SNS — pub/sub для fan-out к многим подписчикам. SQS — point-to-point queue между producer и consumer. |
| 3 | B | Visibility Timeout — период, когда сообщение "заблокировано" для обработки одним consumer. |
| 4 | B | Long Polling ждёт до появления сообщений, снижая количество пустых ответов и API calls. |
| 5 | B | EventBridge имеет мощные rules для content-based routing. SNS лучше для простого fan-out и notifications. |

---
