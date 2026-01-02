# Онлайн-платежи и API
## Платёжные шлюзы, SDK и интеграции

---

## 📋 Prerequisites

- Базовое понимание web-разработки (HTTP, REST API)
- Знание JSON и работы с API
- Понимание карточных платежей и их жизненного цикла

---

## 🎯 Learning Objectives

- Понимать архитектуру онлайн-платежей и роль платёжного шлюза
- Выбирать подходящий способ интеграции (redirect, iframe, API)
- Работать с токенизацией для снижения PCI scope
- Реализовывать обработку webhooks и обеспечивать идемпотентность
- Правильно обрабатывать ошибки и 3-D Secure

---

## 1. Архитектура онлайн-платежей

### 1.1 Компоненты экосистемы

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    АРХИТЕКТУРА ОНЛАЙН-ПЛАТЕЖЕЙ                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ┌────────────┐                                                           │
│   │  Клиент    │ Браузер / Мобильное приложение                            │
│   │  (Buyer)   │                                                            │
│   └─────┬──────┘                                                           │
│         │ HTTPS                                                             │
│         ▼                                                                   │
│   ┌────────────┐                                                           │
│   │  Сайт /    │ Интернет-магазин, приложение                              │
│   │  Merchant  │                                                            │
│   └─────┬──────┘                                                           │
│         │ API                                                               │
│         ▼                                                                   │
│   ┌────────────┐                                                           │
│   │  Платёжный │ Stripe, ЮKassa, CloudPayments, Adyen                      │
│   │   шлюз     │ (Payment Gateway / PSP)                                    │
│   └─────┬──────┘                                                           │
│         │                                                                   │
│         ├──────────────────────────────────┐                               │
│         ▼                                  ▼                               │
│   ┌────────────┐                     ┌────────────┐                        │
│   │  Эквайер   │                     │  Fraud     │                        │
│   │  (Bank)    │                     │  Services  │                        │
│   └─────┬──────┘                     └────────────┘                        │
│         │                                                                   │
│         ▼                                                                   │
│   ┌────────────┐                                                           │
│   │ Платёжная  │ Visa, Mastercard, Мир                                     │
│   │  система   │                                                            │
│   └─────┬──────┘                                                           │
│         │                                                                   │
│         ▼                                                                   │
│   ┌────────────┐                                                           │
│   │  Эмитент   │ Банк держателя карты                                      │
│   │  (Issuer)  │                                                            │
│   └────────────┘                                                           │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 1.2 Роль платёжного шлюза (Payment Gateway)

**Платёжный шлюз (Payment Gateway / PSP)** — сервис, обеспечивающий приём онлайн-платежей.

| Функция | Описание |
|---------|----------|
| **Приём данных карты** | Безопасная форма для ввода card data |
| **Токенизация** | Замена PAN на токен для безопасности |
| **Маршрутизация** | Направление транзакции к нужному эквайеру |
| **3-D Secure** | Аутентификация держателя карты |
| **Fraud screening** | Анализ на мошенничество |
| **Авторизация** | Запрос одобрения у эмитента |
| **Webhooks** | Уведомления о событиях |
| **Reporting** | Отчётность и аналитика |
| **Compliance** | PCI DSS, регуляторные требования |

### 1.3 PSP vs Payment Gateway vs Acquirer

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    PSP vs GATEWAY vs ACQUIRER                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   PAYMENT GATEWAY (только технология):                                      │
│   • Передаёт данные транзакции                                             │
│   • Не принимает средства                                                   │
│   • Требует отдельный договор с эквайером                                  │
│   Пример: Authorize.net, NMI                                               │
│                                                                             │
│   ACQUIRER (только банк):                                                   │
│   • Принимает средства                                                      │
│   • Settlement на счёт мерчанта                                            │
│   • Часто требует интеграцию с gateway                                     │
│   Пример: Сбербанк-эквайринг, Worldpay                                     │
│                                                                             │
│   PSP (Payment Service Provider) = Gateway + Acquirer + Extras:            │
│   • Полное решение "под ключ"                                              │
│   • Gateway + процессинг + settlement                                       │
│   • Один договор, один API                                                  │
│   Пример: Stripe, ЮKassa, Adyen, CloudPayments                             │
│                                                                             │
│   PAYMENT FACILITATOR (PayFac):                                             │
│   • PSP, работающий как "зонтик" для мелких мерчантов                      │
│   • Мерчанты — sub-merchants под MID PayFac                                │
│   • Быстрое подключение, меньше проверок                                   │
│   Пример: Stripe Connect, Square                                           │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Способы интеграции

### 2.1 Сравнение способов

| Способ | PCI Scope | Контроль UX | Сложность | Применение |
|--------|-----------|-------------|-----------|------------|
| **Redirect (Hosted Page)** | SAQ A (минимум) | Минимум | Низкая | Простые интеграции |
| **Embedded (iFrame)** | SAQ A | Средний | Средняя | Большинство сайтов |
| **Tokenization (JS SDK)** | SAQ A-EP | Высокий | Средняя | Кастомный UX |
| **Direct API** | SAQ D (максимум) | Полный | Высокая | Крупные игроки |

### 2.2 Redirect (Hosted Payment Page)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    REDIRECT INTEGRATION                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ПРОЦЕСС:                                                                  │
│                                                                             │
│   1. Клиент нажимает "Оплатить" на сайте мерчанта                          │
│          │                                                                  │
│          ▼                                                                  │
│   2. Сервер мерчанта создаёт payment session через API                     │
│      POST /api/payments → { redirect_url: "https://pay.gateway.com/..." } │
│          │                                                                  │
│          ▼                                                                  │
│   3. Redirect клиента на страницу шлюза                                     │
│      302 Redirect → https://pay.gateway.com/session_abc123                 │
│          │                                                                  │
│          ▼                                                                  │
│   4. Клиент вводит данные карты на странице ШЛЮЗА                          │
│      (данные карты никогда не касаются сервера мерчанта!)                  │
│          │                                                                  │
│          ▼                                                                  │
│   5. Шлюз обрабатывает платёж, 3DS если нужно                              │
│          │                                                                  │
│          ▼                                                                  │
│   6. Redirect обратно на сайт мерчанта                                      │
│      302 Redirect → https://shop.com/payment/success?order_id=123          │
│          │                                                                  │
│          ▼                                                                  │
│   7. Webhook от шлюза подтверждает статус                                   │
│      POST /webhooks → { event: "payment.succeeded" }                       │
│                                                                             │
│   ✅ ПЛЮСЫ:                                                                 │
│   • Минимальный PCI scope (SAQ A)                                          │
│   • Простая интеграция                                                      │
│   • Шлюз отвечает за безопасность формы                                    │
│                                                                             │
│   ❌ МИНУСЫ:                                                                │
│   • Потеря контроля над UX                                                 │
│   • Клиент покидает сайт (меньше доверия)                                  │
│   • Ограниченная кастомизация                                              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2.3 Embedded (iFrame)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    IFRAME INTEGRATION                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   HTML:                                                                     │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │ <div id="payment-form">                                              │  │
│   │   <iframe src="https://gateway.com/form?session=abc123"             │  │
│   │           sandbox="allow-forms allow-scripts"                        │  │
│   │           style="width:100%; height:300px; border:0;">              │  │
│   │   </iframe>                                                          │  │
│   │ </div>                                                               │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│   ✅ ПЛЮСЫ:                                                                 │
│   • Форма на странице мерчанта (лучший UX)                                 │
│   • Минимальный PCI scope (SAQ A)                                          │
│   • Можно стилизовать окружение                                            │
│                                                                             │
│   ❌ МИНУСЫ:                                                                │
│   • Ограниченная кастомизация внутри iframe                                │
│   • Cross-origin ограничения                                               │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2.4 Tokenization (JavaScript SDK)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    TOKENIZATION WITH JS SDK                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ПРОЦЕСС:                                                                  │
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │                        БРАУЗЕР КЛИЕНТА                               │  │
│   │                                                                      │  │
│   │   ┌────────────────────────────────────────────────────────┐        │  │
│   │   │              Страница мерчанта                          │        │  │
│   │   │  ┌──────────────────────────────────────────────────┐  │        │  │
│   │   │  │   Card Number: [4242 4242 4242 4242]             │  │        │  │
│   │   │  │   Expiry: [12/25]   CVC: [123]                   │  │        │  │
│   │   │  │   [Pay $100]                                      │  │        │  │
│   │   │  └──────────────────────────────────────────────────┘  │        │  │
│   │   │       ↓ (1) JS SDK создаёт токен                       │        │  │
│   │   │       │    Данные карты → Шлюз напрямую                │        │  │
│   │   │       │    (HTTPS из браузера)                         │        │  │
│   │   └───────┼─────────────────────────────────────────────────┘        │  │
│   │           │                                                          │  │
│   │           ▼                                                          │  │
│   │   ┌────────────────┐                                                 │  │
│   │   │ Payment Gateway│ → Возвращает токен "tok_abc123"                 │  │
│   │   └────────────────┘                                                 │  │
│   │           │                                                          │  │
│   │           │ (2) Токен возвращается в JS                              │  │
│   │           ▼                                                          │  │
│   │   token = "tok_abc123"                                               │  │
│   │           │                                                          │  │
│   │           │ (3) Токен отправляется на сервер мерчанта               │  │
│   │           ▼                                                          │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │                      СЕРВЕР МЕРЧАНТА                                 │  │
│   │                                                                      │  │
│   │   (4) POST /api/payments                                             │  │
│   │       { "token": "tok_abc123", "amount": 10000 }                    │  │
│   │           │                                                          │  │
│   │           │ (5) Сервер мерчанта → API шлюза                         │  │
│   │           ▼                                                          │  │
│   │   Payment Gateway создаёт платёж                                     │  │
│   │           │                                                          │  │
│   │           │ (6) Ответ                                                │  │
│   │           ▼                                                          │  │
│   │   { "status": "succeeded" }                                          │  │
│   │                                                                      │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│   ⚠️ ВАЖНО: Данные карты НИКОГДА не проходят через сервер мерчанта!       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Пример кода (Stripe.js):**

```javascript
// 1. Инициализация
const stripe = Stripe('pk_live_xxx');
const elements = stripe.elements();

// 2. Создание элементов формы (hosted fields)
const cardNumber = elements.create('cardNumber');
const cardExpiry = elements.create('cardExpiry');
const cardCvc = elements.create('cardCvc');

// 3. Монтирование
cardNumber.mount('#card-number');
cardExpiry.mount('#card-expiry');
cardCvc.mount('#card-cvc');

// 4. Обработка оплаты
async function handlePayment() {
    const { token, error } = await stripe.createToken(cardNumber);
    
    if (error) {
        showError(error.message);
        return;
    }
    
    // 5. Отправка токена на сервер
    const response = await fetch('/api/charge', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ token: token.id, amount: 10000 })
    });
    
    const result = await response.json();
    if (result.success) {
        showSuccess();
    }
}
```

### 2.5 Direct API Integration

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    DIRECT API (НЕ РЕКОМЕНДУЕТСЯ)                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ⚠️ ВНИМАНИЕ: Требует полный PCI DSS Level 1 compliance (SAQ D)!          │
│                                                                             │
│   Данные карты проходят через сервер мерчанта:                             │
│                                                                             │
│   Client → Merchant Server (PAN) → Gateway → Acquirer                      │
│                                                                             │
│   POST /api/payments                                                        │
│   {                                                                         │
│     "card": {                                                               │
│       "number": "4242424242424242",  ← Полный PAN!                         │
│       "exp_month": 12,                                                      │
│       "exp_year": 2025,                                                     │
│       "cvc": "123"                                                          │
│     },                                                                      │
│     "amount": 10000                                                         │
│   }                                                                         │
│                                                                             │
│   ТРЕБОВАНИЯ:                                                               │
│   • PCI DSS Level 1 (годовой аудит QSA)                                    │
│   • HSM для хранения ключей                                                │
│   • Сегментация сети                                                        │
│   • Шифрование at rest и in transit                                        │
│   • Регулярные пентесты                                                     │
│   • Стоимость: $100K+ в год                                                │
│                                                                             │
│   КТО ИСПОЛЬЗУЕТ: Крупные процессоры, банки, enterprise                    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Типичный Payment API

### 3.1 Основные эндпоинты

| Endpoint | Метод | Описание |
|----------|-------|----------|
| `/payments` | POST | Создать платёж |
| `/payments/{id}` | GET | Получить статус |
| `/payments/{id}/capture` | POST | Подтвердить (для authorize-only) |
| `/payments/{id}/cancel` | POST | Отменить |
| `/payments/{id}/refund` | POST | Вернуть средства |
| `/tokens` | POST | Создать токен карты |
| `/customers` | POST/GET | Управление клиентами |
| `/subscriptions` | POST | Создать подписку |

### 3.2 Создание платежа

```http
POST /api/v1/payments HTTP/1.1
Host: api.payment.com
Authorization: Bearer sk_live_xxxxxxxxxxxxx
Content-Type: application/json
Idempotency-Key: order_12345_attempt_1

{
  "amount": 10000,
  "currency": "RUB",
  "payment_method": {
    "type": "card",
    "token": "tok_abc123"
  },
  "description": "Заказ #12345",
  "confirmation": {
    "type": "redirect",
    "return_url": "https://shop.com/payment/complete"
  },
  "metadata": {
    "order_id": "12345",
    "customer_email": "user@example.com"
  },
  "capture": true,
  "receipt": {
    "email": "user@example.com"
  }
}
```

### 3.3 Ответ API

```json
{
  "id": "pay_xyz789",
  "status": "pending",
  "amount": {
    "value": 10000,
    "currency": "RUB"
  },
  "confirmation": {
    "type": "redirect",
    "confirmation_url": "https://pay.gateway.com/confirm/xyz789"
  },
  "payment_method": {
    "type": "card",
    "card": {
      "last4": "4242",
      "brand": "visa",
      "exp_month": 12,
      "exp_year": 2025
    }
  },
  "metadata": {
    "order_id": "12345"
  },
  "created_at": "2024-03-15T10:30:00Z",
  "expires_at": "2024-03-15T11:30:00Z"
}
```

### 3.4 Статусы платежа

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    ЖИЗНЕННЫЙ ЦИКЛ ПЛАТЕЖА В API                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ┌──────────┐                                                             │
│   │ pending  │ Платёж создан, ожидает действия                             │
│   └────┬─────┘                                                             │
│        │                                                                    │
│        ├────────────────────────────────────────┐                          │
│        │                                        │                          │
│        ▼                                        ▼                          │
│   ┌────────────────┐                      ┌──────────┐                     │
│   │ waiting_for_   │                      │ canceled │                     │
│   │ capture        │ (authorize only)     └──────────┘                     │
│   └───────┬────────┘                                                       │
│           │                                                                 │
│           ├──────────────────────┐                                         │
│           │                      │                                         │
│           ▼                      ▼                                         │
│   ┌───────────┐           ┌──────────┐                                     │
│   │ succeeded │           │ canceled │                                     │
│   └─────┬─────┘           └──────────┘                                     │
│         │                                                                   │
│         ▼                                                                   │
│   ┌───────────────┐                                                        │
│   │ refunded /    │                                                        │
│   │ partially_    │                                                        │
│   │ refunded      │                                                        │
│   └───────────────┘                                                        │
│                                                                             │
│   СТАТУСЫ:                                                                  │
│   • pending — ожидает обработки или 3DS                                    │
│   • waiting_for_capture — авторизован, ждёт capture                       │
│   • succeeded — успешно завершён                                           │
│   • canceled — отменён (до capture)                                        │
│   • failed — ошибка                                                        │
│   • refunded — полностью возвращён                                         │
│   • partially_refunded — частично возвращён                                │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 4. Токенизация

### 4.1 Зачем нужна токенизация

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    ТОКЕНИЗАЦИЯ                                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ПРОБЛЕМА:                                                                 │
│   • Хранение PAN (номера карты) требует PCI DSS Level 1                    │
│   • Передача PAN через сервер увеличивает risk scope                       │
│   • Компрометация данных = огромные штрафы и репутационный ущерб          │
│                                                                             │
│   РЕШЕНИЕ — ТОКЕНИЗАЦИЯ:                                                    │
│                                                                             │
│   PAN: 4242 4242 4242 4242                                                 │
│         ↓ (токенизация)                                                    │
│   Token: tok_abc123xyz789                                                  │
│                                                                             │
│   СВОЙСТВА ТОКЕНА:                                                         │
│   • Не содержит данных карты                                               │
│   • Бесполезен без ключей шлюза                                            │
│   • Можно хранить без PCI DSS                                              │
│   • Можно использовать для повторных платежей                              │
│                                                                             │
│   ТИПЫ ТОКЕНОВ:                                                             │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │ Single-use token — для одной транзакции                             │  │
│   │ (tok_xxx, создаётся на клиенте, живёт минуты)                       │  │
│   │                                                                      │  │
│   │ Multi-use token — для повторных платежей                            │  │
│   │ (card_xxx, привязан к customer, живёт пока карта валидна)          │  │
│   │                                                                      │  │
│   │ Network token — токен от Visa/MC (DPAN)                             │  │
│   │ (для Apple Pay, Google Pay, улучшает approval rate)                │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 4.2 Сохранение карты для повторных платежей

```javascript
// 1. При первой оплате — создаём customer и сохраняем карту
const customer = await stripe.customers.create({
    email: 'user@example.com',
    payment_method: 'pm_card_visa',
    invoice_settings: { default_payment_method: 'pm_card_visa' }
});

// 2. Сохраняем customer.id в своей БД
db.saveCustomer(userId, customer.id);  // cus_abc123

// 3. При повторной оплате — используем сохранённую карту
const payment = await stripe.paymentIntents.create({
    customer: 'cus_abc123',
    amount: 10000,
    currency: 'rub',
    payment_method: customer.invoice_settings.default_payment_method,
    off_session: true,
    confirm: true
});
```

---

## 5. Webhooks

### 5.1 Зачем нужны webhooks

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    WEBHOOKS                                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ПРОБЛЕМА СИНХРОННОГО ПОДХОДА:                                            │
│                                                                             │
│   Client → Merchant → Gateway → ... → Response                             │
│                                                                             │
│   • 3DS требует redirect → клиент может закрыть браузер                    │
│   • Timeout на стороне клиента → платёж прошёл, но клиент не узнал        │
│   • Refunds, chargebacks происходят позже                                  │
│   • Нельзя полагаться только на синхронный ответ!                          │
│                                                                             │
│   РЕШЕНИЕ — WEBHOOKS:                                                       │
│                                                                             │
│   Gateway ──webhook──> Merchant Server                                      │
│                                                                             │
│   Шлюз отправляет HTTP POST на ваш endpoint при событиях:                  │
│   • payment.succeeded — платёж успешен                                      │
│   • payment.failed — платёж неуспешен                                       │
│   • payment.refunded — возврат                                              │
│   • payment.canceled — отмена                                               │
│   • dispute.created — открыт chargeback                                     │
│                                                                             │
│   ⚠️ ВАЖНО: Webhook — SOURCE OF TRUTH для статуса платежа!                 │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 5.2 Пример webhook payload

```json
POST /webhooks/payments HTTP/1.1
Host: shop.com
Content-Type: application/json
X-Signature: sha256=abc123...
X-Webhook-ID: wh_event_12345

{
  "id": "evt_12345",
  "type": "payment.succeeded",
  "created": "2024-03-15T10:35:00Z",
  "data": {
    "object": {
      "id": "pay_xyz789",
      "status": "succeeded",
      "amount": {
        "value": 10000,
        "currency": "RUB"
      },
      "payment_method": {
        "type": "card",
        "card": {
          "last4": "4242",
          "brand": "visa"
        }
      },
      "metadata": {
        "order_id": "12345"
      }
    }
  }
}
```

### 5.3 Обработка webhooks

```python
import hmac
import hashlib
from flask import Flask, request, jsonify

app = Flask(__name__)
WEBHOOK_SECRET = "whsec_xxxxx"

@app.post("/webhooks/payments")
def handle_webhook():
    # 1. Верификация подписи
    signature = request.headers.get("X-Signature")
    payload = request.get_data(as_text=True)
    
    expected_sig = "sha256=" + hmac.new(
        WEBHOOK_SECRET.encode(),
        payload.encode(),
        hashlib.sha256
    ).hexdigest()
    
    if not hmac.compare_digest(signature, expected_sig):
        return jsonify({"error": "Invalid signature"}), 401
    
    # 2. Парсинг события
    event = request.json
    event_type = event["type"]
    payment = event["data"]["object"]
    
    # 3. Идемпотентность — проверяем, не обработали ли уже
    event_id = event["id"]
    if db.is_event_processed(event_id):
        return jsonify({"status": "already_processed"}), 200
    
    # 4. Обработка
    if event_type == "payment.succeeded":
        order_id = payment["metadata"]["order_id"]
        fulfill_order(order_id)
    elif event_type == "payment.failed":
        order_id = payment["metadata"]["order_id"]
        handle_failed_payment(order_id)
    elif event_type == "payment.refunded":
        order_id = payment["metadata"]["order_id"]
        handle_refund(order_id)
    
    # 5. Отмечаем событие как обработанное
    db.mark_event_processed(event_id)
    
    # 6. Возвращаем 200 OK
    return jsonify({"status": "ok"}), 200
```

### 5.4 Best Practices для webhooks

| Практика | Описание |
|----------|----------|
| **Verify signature** | Всегда проверяйте подпись webhook |
| **Idempotency** | Обрабатывайте каждый event_id только один раз |
| **Quick response** | Возвращайте 200 OK быстро, обрабатывайте async |
| **Retry logic** | Шлюз повторит при 5xx, обеспечьте устойчивость |
| **Logging** | Логируйте все входящие webhooks |
| **Queue processing** | Для сложной логики — отправляйте в очередь |

---

## 6. 3-D Secure в API

### 6.1 Процесс 3DS в API

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    3DS FLOW В API                                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   1. Создаём платёж:                                                        │
│      POST /payments { amount: 10000, token: "tok_xxx" }                    │
│                                                                             │
│   2. Ответ — требуется 3DS:                                                 │
│      {                                                                      │
│        "id": "pay_xyz",                                                     │
│        "status": "pending",                                                 │
│        "next_action": {                                                     │
│          "type": "redirect",                                                │
│          "redirect_url": "https://3ds.bank.com/auth?id=xxx"                │
│        }                                                                    │
│      }                                                                      │
│                                                                             │
│   3. Redirect клиента на 3DS:                                               │
│      window.location.href = response.next_action.redirect_url               │
│                                                                             │
│   4. Клиент проходит 3DS у эмитента:                                        │
│      • Вводит OTP / подтверждает в приложении банка                        │
│                                                                             │
│   5. Redirect обратно + Webhook:                                            │
│      • Client → return_url                                                  │
│      • Webhook → payment.succeeded                                          │
│                                                                             │
│   ДЛЯ JS SDK (Stripe, etc.):                                               │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │ // Автоматическая обработка 3DS                                     │  │
│   │ const { paymentIntent, error } = await stripe.confirmCardPayment(   │  │
│   │   clientSecret,                                                      │  │
│   │   { payment_method: { card: cardElement } }                         │  │
│   │ );                                                                   │  │
│   │                                                                      │  │
│   │ // SDK сам показывает 3DS modal и ждёт завершения                   │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 7. Обработка ошибок

### 7.1 Типы ошибок

| Код | Тип | Описание | Действие |
|-----|-----|----------|----------|
| `card_declined` | Soft | Карта отклонена банком | Показать сообщение |
| `expired_card` | Hard | Карта просрочена | Ввести другую карту |
| `invalid_cvc` | Validation | Неверный CVV | Проверить ввод |
| `insufficient_funds` | Soft | Недостаточно средств | Другая карта или позже |
| `processing_error` | Transient | Временная ошибка системы | Retry через 5-10 сек |
| `rate_limit` | Transient | Превышен лимит запросов | Backoff и retry |
| `authentication_required` | Soft | Требуется 3DS | Redirect на 3DS |
| `invalid_request` | Validation | Неверные параметры | Исправить запрос |

### 7.2 Retry стратегия

```python
import time
import random

def create_payment_with_retry(payment_data, max_retries=3):
    retryable_errors = ["processing_error", "rate_limit", "network_error"]
    
    for attempt in range(max_retries):
        try:
            response = api.create_payment(payment_data)
            return response
            
        except PaymentError as e:
            if e.code not in retryable_errors:
                raise  # Не ретраим hard errors
            
            if attempt == max_retries - 1:
                raise  # Последняя попытка
            
            # Exponential backoff with jitter
            delay = (2 ** attempt) + random.uniform(0, 1)
            time.sleep(delay)
    
    raise PaymentError("Max retries exceeded")
```

### 7.3 Идемпотентность

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    ИДЕМПОТЕНТНОСТЬ                                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ПРОБЛЕМА:                                                                 │
│   • Запрос создания платежа отправлен                                      │
│   • Timeout на стороне клиента                                             │
│   • Клиент ретраит                                                          │
│   • Платёж создаётся ДВАЖДЫ! 💥                                            │
│                                                                             │
│   РЕШЕНИЕ — IDEMPOTENCY KEY:                                                │
│                                                                             │
│   POST /payments                                                            │
│   Idempotency-Key: order_12345_attempt_1                                   │
│                                                                             │
│   Первый запрос:                                                            │
│   • API создаёт платёж                                                      │
│   • Сохраняет результат с ключом "order_12345_attempt_1"                   │
│   • Возвращает { id: "pay_abc" }                                           │
│                                                                             │
│   Повторный запрос с тем же ключом:                                        │
│   • API находит сохранённый результат                                      │
│   • Возвращает ТОТ ЖЕ ответ { id: "pay_abc" }                              │
│   • НЕ создаёт новый платёж                                                 │
│                                                                             │
│   BEST PRACTICE:                                                            │
│   Idempotency-Key = order_id + "_" + attempt_number                        │
│                      или                                                    │
│   Idempotency-Key = UUID на стороне клиента                                │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 8. Безопасность

### 8.1 PCI DSS и уровни compliance

| SAQ Level | Когда применяется | Усилия |
|-----------|-------------------|--------|
| **SAQ A** | Redirect, iframe | Минимум (опросник ~20 вопросов) |
| **SAQ A-EP** | JS tokenization, hosted fields | Средние (~100 вопросов) |
| **SAQ D** | Direct API с PAN | Максимум (полный аудит, 300+ controls) |

### 8.2 Best Practices безопасности

| Практика | Описание |
|----------|----------|
| **HTTPS везде** | TLS 1.2+ для всех коммуникаций |
| **API Keys rotation** | Регулярная ротация ключей |
| **Webhook signatures** | Всегда верифицировать подпись |
| **IP whitelisting** | Ограничить доступ к API |
| **Logging** | Логировать всё, кроме card data |
| **Rate limiting** | Защита от brute force |
| **Error handling** | Не раскрывать внутренние ошибки |

---

## 9. Популярные платёжные шлюзы

### 9.1 Россия

| Шлюз | Особенности | Комиссия |
|------|-------------|----------|
| **ЮKassa** | Много способов оплаты, СБП | 2.8-3.5% |
| **CloudPayments** | Быстрое подключение, хороший API | 2.7-3.5% |
| **Тинькофф Касса** | Интеграция с Тинькофф Бизнес | 2.49-2.99% |
| **Сбербанк Эквайринг** | Широкое покрытие | 2.5-3% |
| **Robokassa** | Много альтернативных методов | 3-5% |

### 9.2 Международные

| Шлюз | Особенности | Комиссия |
|------|-------------|----------|
| **Stripe** | Лучший API, developer-friendly | 2.9% + $0.30 |
| **Adyen** | Enterprise, omnichannel | Custom pricing |
| **PayPal/Braintree** | Глобальный охват, PayPal wallet | 2.9% + $0.30 |
| **Square** | Простота, offline + online | 2.9% + $0.30 |
| **Checkout.com** | Enterprise, high volume | Custom pricing |

---

## 💡 Key Takeaways

- **Три способа интеграции**: Redirect (простой), Embedded (баланс), Direct API (сложный)
- **Токенизация** снижает PCI scope до SAQ A/A-EP — используйте JS SDK
- **Webhooks обязательны** — это source of truth для статуса платежа
- **3-D Secure** асинхронен — обрабатывайте redirect или используйте SDK
- **Idempotency Key** — защита от дублирования при retry
- **Верифицируйте подписи** webhooks — защита от подделки
- **Логируйте всё**, кроме card data — для debugging и compliance

---

## 📚 Дополнительные материалы

- [Stripe API Documentation](https://stripe.com/docs/api) — эталон API design
- [ЮKassa API](https://yookassa.ru/developers) — российский шлюз
- [PCI DSS Quick Reference Guide](https://www.pcisecuritystandards.org/pdfs/pci_ssc_quick_guide.pdf)
- [OWASP Payment Security Guidelines](https://owasp.org/www-project-web-security-testing-guide/)

---

## 🚀 Next Steps

**Следующий модуль:**
- [NFC и бесконтактные платежи](../16_NFC_Contactless/)

---

*Время чтения: 25 минут*
*Время практики: 45 минут (интеграция тестового шлюза)*

