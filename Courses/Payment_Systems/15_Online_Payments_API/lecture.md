# Онлайн-платежи и API
## Платёжные шлюзы, SDK и интеграции

---

## 📋 Prerequisites

- Базовое понимание web-разработки
- Знание HTTP/REST API
- Понимание карточных платежей

---

## 🎯 Learning Objectives

- Понимать архитектуру онлайн-платежей
- Выбирать способ интеграции
- Работать с webhooks
- Обрабатывать ошибки

---

## 1. Архитектура онлайн-платежей

### 1.1 Компоненты

```
┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐
│ Сайт/   │───►│Платёжный│───►│Эквайер  │───►│   ПС    │
│ App     │    │ шлюз    │    │         │    │         │
└─────────┘    └─────────┘    └─────────┘    └─────────┘
```

### 1.2 Платёжный шлюз

**Функции:**
- Приём данных карты
- Шифрование и токенизация
- Маршрутизация к эквайеру
- Обработка ответов
- Уведомления (webhooks)

---

## 2. Способы интеграции

### 2.1 Redirect (Hosted Page)

Переход на страницу платёжного шлюза:

```
Сайт → Redirect → Страница шлюза → Оплата → Redirect back
```

**Плюсы:** Простота, PCI compliance на стороне шлюза
**Минусы:** Потеря контроля над UX

### 2.2 Embedded Form (iFrame)

Форма шлюза встроена на сайт:

```html
<iframe src="https://gateway.com/form?order=123"></iframe>
```

**Плюсы:** Лучший UX, PCI на стороне шлюза
**Минусы:** Ограниченная кастомизация

### 2.3 Direct API

Полная интеграция через API:

```
POST /api/payments
{
  "amount": 1000,
  "card_token": "tok_xxx",
  "order_id": "123"
}
```

**Плюсы:** Полный контроль
**Минусы:** Требует PCI DSS (SAQ A-EP или выше)

---

## 3. Типичный API

### 3.1 Создание платежа

```http
POST /api/v1/payments HTTP/1.1
Host: api.payment.com
Authorization: Bearer sk_live_xxx
Content-Type: application/json

{
  "amount": 10000,
  "currency": "RUB",
  "card_token": "tok_abc123",
  "description": "Заказ #12345",
  "metadata": {
    "order_id": "12345"
  }
}
```

### 3.2 Ответ

```json
{
  "id": "pay_xyz789",
  "status": "succeeded",
  "amount": 10000,
  "currency": "RUB",
  "created_at": "2024-03-15T10:30:00Z"
}
```

### 3.3 Статусы платежа

| Статус | Описание |
|--------|----------|
| pending | Ожидает обработки |
| succeeded | Успешно |
| failed | Ошибка |
| canceled | Отменён |
| refunded | Возвращён |

---

## 4. Токенизация

### 4.1 Зачем

**Проблема:** Хранить данные карты опасно и требует PCI DSS.

**Решение:** Токенизация — замена карты на токен.

### 4.2 Как работает

```
1. Клиент вводит карту → JavaScript SDK
2. SDK отправляет в шлюз → Токен
3. Токен возвращается на сайт
4. Сайт отправляет токен на сервер
5. Сервер создаёт платёж с токеном
```

### 4.3 Пример (Stripe.js)

```javascript
const stripe = Stripe('pk_live_xxx');
const elements = stripe.elements();
const card = elements.create('card');
card.mount('#card-element');

const {token, error} = await stripe.createToken(card);
// token.id → отправить на сервер
```

---

## 5. Webhooks

### 5.1 Что это

**Webhook** — уведомление от шлюза о событии.

### 5.2 Зачем нужны

- Платёж может завершиться после redirect
- 3-D Secure асинхронен
- Refunds, chargebacks приходят позже

### 5.3 Пример webhook

```json
POST /webhooks/payments HTTP/1.1
Host: yoursite.com

{
  "event": "payment.succeeded",
  "data": {
    "id": "pay_xyz789",
    "amount": 10000,
    "status": "succeeded"
  }
}
```

### 5.4 Обработка

```python
@app.post("/webhooks/payments")
def handle_webhook(request):
    # Проверить подпись
    verify_signature(request)
    
    event = request.json
    if event["event"] == "payment.succeeded":
        order_id = event["data"]["metadata"]["order_id"]
        fulfill_order(order_id)
    
    return {"status": "ok"}
```

### 5.5 Идемпотентность

Webhook может прийти несколько раз — обработка должна быть идемпотентной.

---

## 6. 3-D Secure в API

### 6.1 Процесс

```
1. Создать платёж → status: requires_action
2. Redirect клиента на 3DS
3. Клиент проходит 3DS
4. Webhook: payment.succeeded
```

### 6.2 Пример ответа

```json
{
  "id": "pay_xyz",
  "status": "requires_action",
  "next_action": {
    "type": "redirect_to_url",
    "url": "https://3ds.bank.com/auth?id=xxx"
  }
}
```

---

## 7. Обработка ошибок

### 7.1 Типы ошибок

| Тип | Описание | Действие |
|-----|----------|----------|
| card_declined | Карта отклонена | Показать сообщение |
| expired_card | Карта просрочена | Ввести другую |
| invalid_cvc | Неверный CVV | Проверить ввод |
| insufficient_funds | Нет средств | Другая карта |
| processing_error | Ошибка системы | Retry |

### 7.2 Retry стратегия

- Сетевые ошибки → retry с exponential backoff
- card_declined → не retry
- processing_error → 1-2 retry

---

## 8. Безопасность

### 8.1 PCI DSS

| SAQ | Требования |
|-----|------------|
| SAQ A | Redirect/iFrame |
| SAQ A-EP | Токенизация |
| SAQ D | Полный процессинг |

### 8.2 Best Practices

- HTTPS везде
- Подпись webhooks
- Идемпотентность
- Логирование (без PAN!)
- Rate limiting

---

## 9. Популярные платёжные шлюзы

### 9.1 Россия

| Шлюз | Особенности |
|------|-------------|
| ЮKassa | Популярный, много методов |
| CloudPayments | Быстрое подключение |
| Robokassa | Много способов оплаты |
| Тинькофф Касса | Интеграция с банком |

### 9.2 Международные

| Шлюз | Особенности |
|------|-------------|
| Stripe | Лучший API, developer-friendly |
| PayPal | Глобальный охват |
| Adyen | Enterprise |
| Braintree | PayPal-owned |

---

## 💡 Key Takeaways

- **Три способа интеграции**: Redirect, Embedded, Direct API
- **Токенизация** снижает PCI scope
- **Webhooks обязательны** для надёжной обработки
- **3-D Secure асинхронен** — нужен redirect или webhook
- **Идемпотентность** — защита от дублирования

---

## 🚀 Next Steps

**Следующий модуль:**
- [NFC и бесконтактные платежи](../16_NFC_Contactless/)

---

