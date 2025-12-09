# Cloud Native Development - Quiz
## Messaging: SQS, SNS, EventBridge

---

## Question 1: SQS Queue Types







Какой тип SQS queue гарантирует FIFO ordering и exactly-once delivery?

A) Express Queue

B) FIFO Queue

C) Priority Queue

D) Standard Queue

---

## Question 2: SNS vs SQS







Какое ключевое отличие SNS от SQS?

A) SNS дешевле

B) SQS не поддерживает filtering

C) SNS — pull-based, SQS — push-based

D) SNS — pub/sub (fan-out), SQS — point-to-point queue

---

## Question 3: Visibility Timeout







Что такое Visibility Timeout в SQS?

A) Время жизни сообщения в очереди

B) Время между отправками

C) Максимальное время обработки

D) Время, в течение которого сообщение невидимо для других consumers после получения

---

## Question 4: Long Polling







Зачем использовать Long Polling в SQS?

A) Для увеличения размера сообщений

B) Для шифрования сообщений

C) Для уменьшения количества пустых ответов и снижения стоимости

D) Для увеличения скорости доставки

---

## Question 5: EventBridge vs SNS







Когда предпочтительнее EventBridge вместо SNS?

A) Для маршрутизации событий на основе их содержимого (content-based routing)

B) Для отправки email notifications

C) Для SMS уведомлений

D) Для простого fan-out

---

## Question 6: SQS Message Size






Какой максимальный размер сообщения SQS?

A) 64 KB

B) 10 MB

C) 1 MB

D) 256 KB

---

## Question 7: DLQ






Для чего используется Dead Letter Queue?

A) Для логирования

B) Для сообщений, которые не удалось обработать

C) Для шифрования

D) Для архивации

---

## Question 8: SNS Filter Policy






Что делает SNS Filter Policy?

A) Фильтрует спам

B) Шифрует сообщения

C) Доставляет сообщения только matching subscribers

D) Ограничивает rate

---

## Question 9: FIFO Throughput






Какой throughput у SQS FIFO queue?

A) 10 TPS

B) 1000 TPS

C) 300 TPS (3000 с batching, High Throughput до 70K)

D) Unlimited

---

## Question 10: Message Groups






Для чего используются Message Group IDs?

A) Для routing

B) Для billing

C) Для шифрования

D) Для ordering внутри группы в FIFO queue

---

## Question 11: EventBridge Rules






Какие типы rules в EventBridge?

A) Только event patterns

B) Event patterns и scheduled

C) Только manual

D) Только scheduled

---

## Question 12: EventBridge Archive






Для чего используется Archive в EventBridge?

A) Для шифрования

B) Для logging

C) Для replay events для testing/recovery

D) Для backup

---

## Question 13: Step Functions






Для чего используется Step Functions?

A) Только для Lambda

B) Только для SQS

C) Orchestration workflows из AWS services

D) Только для messaging

---

## Question 14: SQS Batching






Какой максимум messages в batch для SQS?

A) 5

B) 10

C) 25

D) 100

---

## Question 15: SNS FIFO






Что такое SNS FIFO Topic?

A) Только для SMS

B) Нет такого

C) Только для email

D) Topic с ordering и deduplication (для SQS FIFO)

---

## Question 16: Kinesis vs SQS






Когда использовать Kinesis вместо SQS?

A) Для email notifications

B) Для real-time streaming, analytics, ordering

C) Для simple queue

D) Всегда

---

## Question 17: Amazon MQ






Когда использовать Amazon MQ?

A) Для migration от on-premises message brokers (ActiveMQ/RabbitMQ)

B) Никогда

C) Для analytics

D) Для новых приложений

---

## Question 18: EventBridge Pipes






Что делает EventBridge Pipes?

A) Networking

B) Point-to-point integrations с filtering и enrichment

C) Logging

D) Security

---

## Question 19: SQS Delay Queue






Что делает Delay Queue?

A) Шифрует сообщения

B) Ускоряет доставку

C) Задерживает доставку сообщений на указанное время

D) Фильтрует сообщения

---

## Question 20: SNS Mobile Push






Куда может отправлять SNS push notifications?

A) Только HTTP

B) iOS (APNS), Android (FCM), и другие платформы

C) Только email

D) Только SMS

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | FIFO Queue гарантирует порядок сообщений и exactly-once processing. Standard — at-least-once, best-effort ordering. |
| 2 | D | SNS — pub/sub для fan-out к многим подписчикам. SQS — point-to-point queue между producer и consumer. |
| 3 | D | Visibility Timeout — период, когда сообщение "заблокировано" для обработки одним consumer. |
| 4 | C | Long Polling ждёт до появления сообщений, снижая количество пустых ответов и API calls. |
| 5 | A | EventBridge имеет мощные rules для content-based routing. SNS лучше для простого fan-out и notifications. |
| 6 | D | SQS message max 256 KB |
| 7 | B | DLQ для failed messages |
| 8 | C | Filter Policy для matching subscribers |
| 9 | C | FIFO: 300 TPS (3000 batch, 70K high throughput) |
| 10 | D | Message Group ID для ordering в FIFO |
| 11 | B | Event patterns и scheduled rules |
| 12 | C | Archive для replay events |
| 13 | C | Step Functions для workflow orchestration |
| 14 | B | SQS batch max 10 messages |
| 15 | D | SNS FIFO для ordering и deduplication |
| 16 | B | Kinesis для real-time streaming и analytics |
| 17 | A | Amazon MQ для migration от ActiveMQ/RabbitMQ |
| 18 | B | EventBridge Pipes — point-to-point integrations |
| 19 | C | Delay Queue задерживает доставку |
| 20 | B | SNS push: iOS, Android, и другие платформы |

---
