# Альтернативные платёжные методы
## Open Banking, электронные кошельки, QR-платежи, BNPL

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:
- Понимать жизненный цикл карточного платежа
- Знать участников платёжной цепочки
- Понимать модель комиссий (interchange, MDR)
- Быть знакомы с API-интеграциями

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:
- Оценивать и выбирать альтернативные платёжные методы для бизнеса
- Интегрировать Open Banking и A2A-платежи
- Понимать экосистемы электронных кошельков разных регионов
- Внедрять QR-платежи и СБП
- Оценивать экономику BNPL для торговцев

---

## 1. Обзор альтернативных платёжных методов

### 1.1 Почему альтернативы важны

```
┌─────────────────────────────────────────────────────────────────┐
│             ДРАЙВЕРЫ АЛЬТЕРНАТИВНЫХ ПЛАТЕЖЕЙ                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ДЛЯ ТОРГОВЦЕВ:                                                 │
│  ├── Снижение комиссий (0.1-0.5% vs 1.5-3% карты)               │
│  ├── Мгновенное получение средств                               │
│  ├── Меньше chargebacks                                         │
│  └── Охват клиентов без карт                                    │
│                                                                 │
│  ДЛЯ КЛИЕНТОВ:                                                  │
│  ├── Удобство (нет ввода карты)                                 │
│  ├── Безопасность (не нужно делиться данными карты)             │
│  ├── Доступность (даже без банковской карты)                    │
│  └── Гибкость оплаты (рассрочка, BNPL)                          │
│                                                                 │
│  РЫНОЧНЫЕ ТРЕНДЫ:                                               │
│  ├── Регуляторное давление (PSD2, Open Banking)                 │
│  ├── Технологии (QR, NFC, API)                                  │
│  ├── Конкуренция (fintech vs банки)                             │
│  └── Глобализация e-commerce                                    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 1.2 Классификация альтернативных методов

| Категория | Примеры | Особенности |
|-----------|---------|-------------|
| **A2A (Account-to-Account)** | Open Banking, СБП, SEPA | Прямой перевод между счетами |
| **E-wallets** | PayPal, Alipay, Qiwi | Предоплаченные/привязанные средства |
| **QR-платежи** | СБП QR, Alipay, WeChat Pay | Сканирование для оплаты |
| **BNPL** | Klarna, Afterpay, Affirm | Рассрочка без процентов |
| **Crypto** | Bitcoin, stablecoins | Децентрализованные платежи |
| **Mobile Money** | M-Pesa, GCash | Платежи через мобильную связь |

### 1.3 Доля альтернативных методов по регионам (2023)

```
                          Доля альтернативных методов в e-commerce

Китай         ████████████████████████████████████████░░░░  80%+
               (Alipay, WeChat Pay доминируют)

Нидерланды    ████████████████████████████░░░░░░░░░░░░░░░░  60%+
               (iDEAL — A2A платежи)

Германия      ████████████████████████░░░░░░░░░░░░░░░░░░░░  50%+
               (SOFORT, Giropay)

Бразилия      ████████████████████████░░░░░░░░░░░░░░░░░░░░  50%+
               (Pix, Boleto)

Россия        ████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░  35%+
               (СБП растёт, но карты доминируют)

США           ████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  20%
               (Карты доминируют, но BNPL растёт)
```

---

## 2. Open Banking и A2A платежи

### 2.1 Что такое Open Banking

**Open Banking** — регуляторная инициатива, обязывающая банки предоставлять доступ к данным клиентов через стандартизированные API.

```
┌─────────────────────────────────────────────────────────────────┐
│                    OPEN BANKING ECOSYSTEM                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Клиент                                                        │
│      │                                                          │
│      │ Согласие                                                 │
│      ▼                                                          │
│   ┌───────────────┐          API          ┌───────────────┐     │
│   │   Третья      │◄────────────────────►│     Банк       │     │
│   │   сторона     │                       │    клиента     │     │
│   │   (TPP)       │                       │                │     │
│   └───────────────┘                       └───────────────┘     │
│          │                                                      │
│          │ Два типа TPP:                                        │
│          │                                                      │
│          ├── AISP (Account Information)                         │
│          │   └── Агрегация счетов, финансовый анализ            │
│          │                                                      │
│          └── PISP (Payment Initiation)                          │
│              └── Инициация платежей напрямую со счёта           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 2.2 PSD2 в Европе

**PSD2 (Payment Services Directive 2)** — регулирование Open Banking в ЕС:

| Компонент | Описание |
|-----------|----------|
| **AISP** | Account Information Service Provider — доступ к данным счёта (read-only) |
| **PISP** | Payment Initiation Service Provider — инициация платежей |
| **SCA** | Strong Customer Authentication — обязательная двухфакторная аутентификация |
| **APIs** | Стандартизированные интерфейсы (Berlin Group, UK Open Banking) |

### 2.3 A2A Payment Flow

```
A2A Payment (Open Banking):

┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐
│ Customer │  │ Merchant │  │   PISP   │  │  Payer's │  │ Merchant │
│          │  │  Website │  │ Provider │  │   Bank   │  │   Bank   │
└────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘
     │             │             │             │             │
     │ 1. Checkout │             │             │             │
     │────────────►│             │             │             │
     │             │             │             │             │
     │             │ 2. Init     │             │             │
     │             │    Payment  │             │             │
     │             │────────────►│             │             │
     │             │             │             │             │
     │ 3. Select   │             │             │             │
     │    Bank     │◄────────────│             │             │
     │────────────►│─────────────┼────────────►│             │
     │             │             │             │             │
     │ 4. Authenticate (SCA)     │             │             │
     │◄────────────────────────────────────────│             │
     │─────────────────────────────────────────│             │
     │             │             │             │             │
     │             │             │ 5. Payment  │             │
     │             │             │    Request  │             │
     │             │             │────────────►│             │
     │             │             │             │             │
     │             │             │             │ 6. Transfer │
     │             │             │             │────────────►│
     │             │             │             │             │
     │             │             │ 7. Confirm  │             │
     │             │             │◄────────────│             │
     │             │             │             │             │
     │             │ 8. Success  │             │             │
     │             │◄────────────│             │             │
     │ 9. Done     │             │             │             │
     │◄────────────│             │             │             │
```

### 2.4 Интеграция Open Banking

**Пример интеграции с TrueLayer (UK):**

```python
import requests
from typing import Optional

class OpenBankingPayment:
    def __init__(self, client_id: str, client_secret: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.base_url = "https://api.truelayer.com"
    
    def create_payment(
        self,
        amount: int,  # в пенсах
        currency: str,
        reference: str,
        redirect_uri: str,
        beneficiary_name: str,
        beneficiary_sort_code: str,
        beneficiary_account_number: str
    ) -> dict:
        """
        Создание A2A платежа через Open Banking.
        """
        
        # Получение токена
        token = self._get_access_token()
        
        # Создание платежа
        payment_request = {
            "amount_in_minor": amount,
            "currency": currency,
            "payment_method": {
                "type": "bank_transfer",
                "provider_selection": {
                    "type": "user_selected"
                },
                "beneficiary": {
                    "type": "merchant_account",
                    "merchant_account_id": self.merchant_account_id
                }
            },
            "user": {
                "name": "Customer Name",
                "email": "customer@example.com"
            }
        }
        
        response = requests.post(
            f"{self.base_url}/v3/payments",
            json=payment_request,
            headers={
                "Authorization": f"Bearer {token}",
                "Idempotency-Key": reference
            }
        )
        
        result = response.json()
        
        return {
            "payment_id": result["id"],
            "authorization_url": result["authorization_flow"]["actions"]["next"]["uri"],
            "status": result["status"]
        }
    
    def get_payment_status(self, payment_id: str) -> dict:
        """Получение статуса платежа."""
        
        token = self._get_access_token()
        
        response = requests.get(
            f"{self.base_url}/v3/payments/{payment_id}",
            headers={"Authorization": f"Bearer {token}"}
        )
        
        return response.json()

# Использование

ob = OpenBankingPayment(client_id="...", client_secret="...")

payment = ob.create_payment(
    amount=10000,  # £100.00
    currency="GBP",
    reference="ORDER-12345",
    redirect_uri="https://shop.example.com/callback",
    beneficiary_name="Example Shop Ltd",
    beneficiary_sort_code="123456",
    beneficiary_account_number="12345678"
)

print(f"Redirect customer to: {payment['authorization_url']}")
```

### 2.5 Преимущества A2A платежей

| Аспект | Карты | A2A (Open Banking) |
|--------|-------|-------------------|
| Комиссия торговца | 1.5-3% | 0.1-0.5% |
| Скорость получения | T+1 до T+3 | Мгновенно |
| Chargebacks | Да | Нет* |
| 3-D Secure | Требуется | Нет (SCA в банке) |
| Охват | Глобальный | Региональный |

*\* Нет стандартного chargeback процесса, но возможны disputes через банк*

---

## 3. Электронные кошельки

### 3.1 Типы электронных кошельков

```
┌─────────────────────────────────────────────────────────────────┐
│                    ТИПЫ E-WALLETS                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  CLOSED-LOOP (Замкнутые)                                        │
│  ├── Работают только у одного продавца                          │
│  ├── Примеры: подарочные карты, Starbucks App                   │
│  └── Минимальное регулирование                                  │
│                                                                 │
│  SEMI-OPEN (Полуоткрытые)                                       │
│  ├── Несколько продавцов в сети                                 │
│  ├── Примеры: кошельки торговых центров                         │
│  └── Ограниченное регулирование                                 │
│                                                                 │
│  OPEN-LOOP (Открытые)                                           │
│  ├── Можно платить везде                                        │
│  ├── Примеры: PayPal, Alipay, Google Pay                        │
│  └── Полное банковское регулирование                            │
│                                                                 │
│  PASS-THROUGH (Проходные)                                       │
│  ├── Хранят данные карт, а не средства                          │
│  ├── Примеры: Apple Pay, Google Pay (для NFC)                   │
│  └── Токенизация, не хранят баланс                              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 3.2 Глобальные кошельки

**PayPal:**

| Характеристика | Значение |
|----------------|----------|
| Пользователи | 400+ млн активных |
| Страны | 200+ |
| Комиссия торговца | 2.9% + $0.30 (США) |
| Защита покупателя | До 180 дней |
| Особенности | Venmo, Braintree, BNPL |

```python
import paypalrestsdk

# Настройка PayPal SDK

paypalrestsdk.configure({
    "mode": "live",  # или "sandbox"
    "client_id": "YOUR_CLIENT_ID",
    "client_secret": "YOUR_CLIENT_SECRET"
})

# Создание заказа

def create_paypal_order(amount: str, currency: str, return_url: str, cancel_url: str):
    order = paypalrestsdk.Order({
        "intent": "CAPTURE",
        "purchase_units": [{
            "amount": {
                "currency_code": currency,
                "value": amount
            }
        }],
        "application_context": {
            "return_url": return_url,
            "cancel_url": cancel_url
        }
    })
    
    if order.create():
        # Найти URL для редиректа
        for link in order.links:
            if link.rel == "approve":
                return {
                    "order_id": order.id,
                    "approval_url": link.href
                }
    else:
        raise Exception(order.error)

# Capture после возврата клиента

def capture_paypal_order(order_id: str):
    order = paypalrestsdk.Order.find(order_id)
    if order.capture():
        return {
            "status": "COMPLETED",
            "capture_id": order.purchase_units[0].payments.captures[0].id
        }
    else:
        raise Exception(order.error)
```

### 3.3 Региональные лидеры

**Китай — Alipay и WeChat Pay:**

```
Китайский рынок e-payments:

┌────────────────────────────────────────────────────────────┐
│                                                            │
│   Alipay (Ant Group / Alibaba)                             │
│   ├── 1.3 млрд пользователей                               │
│   ├── Интеграция с Taobao, Tmall                           │
│   ├── QR-платежи, mini-programs                            │
│   └── Super app (платежи, кредиты, инвестиции)             │
│                                                            │
│   WeChat Pay (Tencent)                                     │
│   ├── 1.2+ млрд пользователей WeChat                       │
│   ├── Интеграция с мессенджером                            │
│   ├── Hongbao (красные конверты)                           │
│   └── Mini-programs для бизнеса                            │
│                                                            │
│   Доля рынка:                                              │
│   Alipay: ~55%                                             │
│   WeChat Pay: ~40%                                         │
│   Другие: ~5%                                              │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

**Россия — Qiwi и ЮMoney:**

| Кошелёк | Особенности |
|---------|-------------|
| **Qiwi** | Терминалы пополнения, виртуальные карты, P2P |
| **ЮMoney** | Ex-Яндекс.Деньги, интеграция с Яндекс-сервисами |
| **СБерБанк** | SberPay, интеграция с экосистемой |
| **Тинькофф** | Tinkoff Pay, BNPL |

### 3.4 Интеграция e-wallet

```javascript
// Интеграция PayPal с Smart Payment Buttons
<script src="https://www.paypal.com/sdk/js?client-id=YOUR_CLIENT_ID&currency=USD"></script>

<div id="paypal-button-container"></div>

<script>
paypal.Buttons({
    // Стиль кнопки
    style: {
        layout: 'vertical',
        color: 'gold',
        shape: 'rect',
        label: 'paypal'
    },
    
    // Создание заказа
    createOrder: function(data, actions) {
        return fetch('/api/orders', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                cart: cartItems
            })
        }).then(res => res.json())
          .then(order => order.id);
    },
    
    // Обработка успешной оплаты
    onApprove: function(data, actions) {
        return fetch(`/api/orders/${data.orderID}/capture`, {
            method: 'POST'
        }).then(res => res.json())
          .then(details => {
              alert('Оплата успешна!');
              window.location.href = '/thank-you';
          });
    },
    
    // Обработка ошибок
    onError: function(err) {
        console.error('PayPal error:', err);
        alert('Ошибка оплаты');
    }
}).render('#paypal-button-container');
</script>
```

---

## 4. QR-платежи

### 4.1 Типы QR-кодов

```
┌─────────────────────────────────────────────────────────────────┐
│                    ТИПЫ QR-ПЛАТЕЖЕЙ                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  STATIC QR (Статический)                                        │
│  ┌─────────────────┐                                            │
│  │  ███████████████ │  • Один код для всех платежей             │
│  │  ███████████████ │  • Клиент вводит сумму                    │
│  │  █████   ███████ │  • Дёшево для торговца                    │
│  │  ███████████████ │  • Подходит для малого бизнеса            │
│  │  ███████████████ │                                           │
│  └─────────────────┘                                            │
│                                                                 │
│  DYNAMIC QR (Динамический)                                      │
│  ┌─────────────────┐                                            │
│  │  ░░░░░░░░░░░░░░░ │  • Уникальный код для каждой транзакции   │
│  │  ░░░░░░░░░░░░░░░ │  • Сумма включена в код                   │
│  │  ░░░░░   ░░░░░░░ │  • Генерируется POS или онлайн            │
│  │  ░░░░░░░░░░░░░░░ │  • Более безопасный                       │
│  │  ░░░░░░░░░░░░░░░ │                                           │
│  └─────────────────┘                                            │
│                                                                 │
│  MERCHANT-PRESENTED vs CUSTOMER-PRESENTED                       │
│  ├── MPM: Торговец показывает → Клиент сканирует                │
│  └── CPM: Клиент показывает → Торговец сканирует                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 4.2 СБП в России

**Система быстрых платежей (СБП)** — инфраструктура ЦБ РФ для мгновенных платежей:

| Параметр | Значение |
|----------|----------|
| Запуск | 2019 |
| Оператор | НСПК |
| Банки-участники | 200+ |
| Комиссия C2C | Бесплатно до 100 000 ₽/мес |
| Комиссия B2C | 0.4-0.7% |
| Скорость | До 15 секунд |

**Интеграция СБП QR:**

```python
import requests
import qrcode
from io import BytesIO
import base64

class SBPPayment:
    def __init__(self, bank_api_url: str, merchant_id: str, api_key: str):
        self.api_url = bank_api_url
        self.merchant_id = merchant_id
        self.api_key = api_key
    
    def create_qr_payment(
        self,
        amount: int,  # в копейках
        order_id: str,
        description: str
    ) -> dict:
        """
        Создание QR-кода для оплаты через СБП.
        """
        
        # Запрос к API банка
        response = requests.post(
            f"{self.api_url}/v1/qr/create",
            json={
                "merchantId": self.merchant_id,
                "amount": amount,
                "currency": "RUB",
                "orderId": order_id,
                "description": description,
                "ttl": 3600  # Время жизни QR в секундах
            },
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
        )
        
        data = response.json()
        
        # Генерация QR-изображения
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(data['qrPayload'])
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Конвертация в base64
        buffer = BytesIO()
        img.save(buffer, format='PNG')
        qr_image_base64 = base64.b64encode(buffer.getvalue()).decode()
        
        return {
            "qr_id": data['qrId'],
            "qr_payload": data['qrPayload'],
            "qr_image": f"data:image/png;base64,{qr_image_base64}",
            "expires_at": data['expiresAt']
        }
    
    def check_payment_status(self, qr_id: str) -> dict:
        """Проверка статуса платежа."""
        
        response = requests.get(
            f"{self.api_url}/v1/qr/{qr_id}/status",
            headers={"Authorization": f"Bearer {self.api_key}"}
        )
        
        data = response.json()
        
        return {
            "qr_id": qr_id,
            "status": data['status'],  # PENDING, PAID, EXPIRED, CANCELLED
            "paid_at": data.get('paidAt'),
            "payer_bank": data.get('payerBank')
        }

# Использование

sbp = SBPPayment(
    bank_api_url="https://api.bank.ru/sbp",
    merchant_id="MERCHANT123",
    api_key="your_api_key"
)

# Создание QR для оплаты

qr = sbp.create_qr_payment(
    amount=150000,  # 1500.00 RUB
    order_id="ORDER-2024-001",
    description="Оплата заказа #001"
)

print(f"QR Code: {qr['qr_image']}")
print(f"Expires: {qr['expires_at']}")
```

### 4.3 EMVCo QR Standard

```
EMVCo QR Code Structure:

┌────────────────────────────────────────────────────────────────┐
│  ID  │  Length  │  Value                                       │
├──────┼──────────┼──────────────────────────────────────────────┤
│  00  │    02    │  01 (Payload Format Indicator)               │
│  01  │    02    │  12 (Point of Initiation: Dynamic)           │
│  26  │    XX    │  Merchant Account Information                │
│      │          │  └── 00: Globally Unique Identifier          │
│      │          │  └── 01: Payment Network Specific Data       │
│  52  │    04    │  5812 (MCC: Restaurants)                     │
│  53  │    03    │  643 (Currency: RUB)                         │
│  54  │    XX    │  1500.00 (Amount)                            │
│  58  │    02    │  RU (Country)                                │
│  59  │    XX    │  Merchant Name                               │
│  60  │    XX    │  City                                        │
│  63  │    04    │  CRC16 Checksum                              │
└────────────────────────────────────────────────────────────────┘
```

---

## 5. BNPL (Buy Now Pay Later)

### 5.1 Как работает BNPL

```
┌─────────────────────────────────────────────────────────────────┐
│                    BNPL FLOW                                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Customer          Merchant           BNPL Provider            │
│       │                 │                    │                  │
│       │  1. Checkout    │                    │                  │
│       │────────────────►│                    │                  │
│       │                 │                    │                  │
│       │  2. Choose BNPL │                    │                  │
│       │────────────────►│                    │                  │
│       │                 │                    │                  │
│       │                 │ 3. Auth Request    │                  │
│       │                 │───────────────────►│                  │
│       │                 │                    │                  │
│       │  4. Approval    │                    │                  │
│       │◄────────────────────────────────────│ (кредитное       │
│       │                 │                    │  решение)        │
│       │                 │                    │                  │
│       │                 │ 5. Full Payment    │                  │
│       │                 │◄───────────────────│                  │
│       │                 │    (сразу)         │                  │
│       │                 │                    │                  │
│       │ 6. Pay in       │                    │                  │
│       │    installments │                    │                  │
│       │────────────────────────────────────►│                  │
│       │    (4 платежа)  │                    │                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 5.2 Ключевые игроки

| Провайдер | Регион | Модель | Особенности |
|-----------|--------|--------|-------------|
| **Klarna** | Глобальный | Pay in 4, Pay Later | Крупнейший в Европе |
| **Afterpay** | Австралия, США | Pay in 4 | Куплен Square |
| **Affirm** | США | Flexible terms | Партнёр Amazon, Shopify |
| **Sezzle** | США, Канада | Pay in 4 | Фокус на молодёжь |
| **Clearpay** | Великобритания | Pay in 4 | Часть Afterpay |
| **Tinkoff** | Россия | Рассрочка | Встроен в карты |

### 5.3 Экономика BNPL

```python
def calculate_bnpl_economics(
    order_amount: float,
    merchant_bnpl_fee_pct: float = 4.0,  # 4%
    card_fee_pct: float = 2.0,           # 2% обычные карты
    conversion_lift_pct: float = 20.0,    # Увеличение конверсии
    aov_lift_pct: float = 30.0            # Увеличение среднего чека
) -> dict:
    """
    Расчёт экономики BNPL для торговца.
    """
    
    # Сравнение комиссий
    bnpl_fee = order_amount * (merchant_bnpl_fee_pct / 100)
    card_fee = order_amount * (card_fee_pct / 100)
    extra_fee = bnpl_fee - card_fee
    
    # Дополнительная выручка от лифта конверсии и AOV
    # Предполагаем базовую конверсию 2% и базовый AOV = order_amount
    baseline_revenue = order_amount
    bnpl_revenue = order_amount * (1 + aov_lift_pct / 100)
    
    # ROI от внедрения BNPL
    additional_revenue = bnpl_revenue - baseline_revenue
    roi = (additional_revenue - extra_fee) / extra_fee * 100 if extra_fee > 0 else 0
    
    return {
        "order_amount": order_amount,
        "bnpl_fee": round(bnpl_fee, 2),
        "card_fee": round(card_fee, 2),
        "extra_fee": round(extra_fee, 2),
        "expected_aov_lift": round(order_amount * aov_lift_pct / 100, 2),
        "net_benefit": round(additional_revenue - extra_fee, 2),
        "roi_pct": round(roi, 1),
        "recommendation": "ADOPT" if roi > 50 else "EVALUATE"
    }

# Пример расчёта

result = calculate_bnpl_economics(order_amount=5000)
print(f"BNPL Fee: {result['bnpl_fee']} RUB")
print(f"Extra vs Card: {result['extra_fee']} RUB")
print(f"Expected AOV Lift: {result['expected_aov_lift']} RUB")
print(f"Net Benefit: {result['net_benefit']} RUB")
print(f"ROI: {result['roi_pct']}%")
print(f"Recommendation: {result['recommendation']}")
```

### 5.4 Интеграция Klarna

```javascript
// Frontend интеграция Klarna
<script src="https://x.klarnacdn.net/kp/lib/v1/api.js" async></script>

<script>
// Инициализация Klarna Payments
Klarna.Payments.init({
    client_token: 'your_client_token_from_backend'
});

// Загрузка виджета
Klarna.Payments.load({
    container: '#klarna-payments-container',
    payment_method_category: 'pay_later'
}, function(res) {
    if (res.show_form) {
        // Форма Klarna отображена
    }
});

// Авторизация платежа
function authorizeKlarna() {
    Klarna.Payments.authorize({
        payment_method_category: 'pay_later'
    }, {
        // Данные заказа
    }, function(res) {
        if (res.approved) {
            // Отправляем authorization_token на сервер
            fetch('/api/klarna/place-order', {
                method: 'POST',
                body: JSON.stringify({
                    authorization_token: res.authorization_token
                })
            });
        }
    });
}
</script>
```

---

## 6. P2P переводы

### 6.1 Глобальный ландшафт P2P

| Страна/Регион | Система | Особенности |
|---------------|---------|-------------|
| **Россия** | СБП | По номеру телефона, бесплатно |
| **США** | Zelle, Venmo, Cash App | Bank-owned (Zelle) vs fintech |
| **ЕС** | SEPA Instant | Instant CT, до €100K |
| **UK** | Faster Payments | 24/7, до £1M |
| **Индия** | UPI | 300+ млрд транзакций/год |
| **Бразилия** | Pix | Мгновенные, QR |

### 6.2 UPI — история успеха Индии

```
UPI (Unified Payments Interface) Statistics (2023):
├── Транзакции: 10+ млрд/месяц
├── Объём: $150+ млрд/месяц
├── Участники: 350+ банков
├── Apps: PhonePe, Google Pay, Paytm
└── Особенности:
    ├── VPA (Virtual Payment Address): user@bank
    ├── QR-платежи
    ├── Recurring payments
    └── Interoperability
```

### 6.3 Использование P2P для бизнеса

```
P2P → P2M (Peer-to-Merchant) эволюция:

┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   Изначально P2P:                                               │
│   ├── Переводы между физлицами                                  │
│   └── Бесплатно, просто                                         │
│                                                                 │
│   Эволюция в P2M:                                               │
│   ├── Малый бизнес принимает по номеру телефона                 │
│   ├── QR-коды для торговых точек                                │
│   ├── Интеграция с кассовым ПО                                  │
│   └── Отчётность для ИП/ООО                                     │
│                                                                 │
│   Регуляторные вызовы:                                          │
│   ├── Лимиты на P2P для бизнеса                                 │
│   ├── Налоговый мониторинг                                      │
│   └── AML/KYC требования                                        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 7. Сравнительный анализ

### 7.1 Комиссии и условия

| Метод | Комиссия торговца | Settlement | Chargebacks | Охват |
|-------|-------------------|------------|-------------|-------|
| **Карты** | 1.5-3% | T+1 до T+3 | Да | Глобальный |
| **СБП** | 0.4-0.7% | Мгновенно | Нет | Россия |
| **Open Banking** | 0.1-0.5% | Мгновенно | Ограниченно | ЕС, UK |
| **PayPal** | 2.9% + $0.30 | Мгновенно | Да (180 дней) | Глобальный |
| **Alipay** | 1-3% | T+1 | Да | Китай + туристы |
| **BNPL** | 3-6% | T+1 | Ограниченно | Региональный |

### 7.2 Выбор метода по сценарию

```python
def recommend_payment_method(
    business_type: str,
    average_order_value: float,
    primary_market: str,
    customer_demographics: str
) -> list:
    """
    Рекомендация платёжных методов для бизнеса.
    """
    
    recommendations = []
    
    # Базовые методы (всегда)
    recommendations.append({
        "method": "cards",
        "priority": "essential",
        "reason": "Универсальный охват"
    })
    
    # По рынку
    if primary_market == "russia":
        recommendations.append({
            "method": "sbp",
            "priority": "high",
            "reason": "Низкие комиссии, мгновенные расчёты"
        })
        recommendations.append({
            "method": "mir_pay",
            "priority": "medium",
            "reason": "Локальные карты"
        })
    
    elif primary_market == "europe":
        recommendations.append({
            "method": "open_banking",
            "priority": "high",
            "reason": "PSD2, низкие комиссии"
        })
        recommendations.append({
            "method": "klarna",
            "priority": "medium" if average_order_value > 50 else "low",
            "reason": "BNPL для высокого AOV"
        })
    
    elif primary_market == "china":
        recommendations.append({
            "method": "alipay",
            "priority": "essential",
            "reason": "Доминирует в Китае"
        })
        recommendations.append({
            "method": "wechat_pay",
            "priority": "essential",
            "reason": "Обязателен для Китая"
        })
    
    # По демографии
    if customer_demographics == "young" and average_order_value > 100:
        recommendations.append({
            "method": "bnpl",
            "priority": "high",
            "reason": "Популярен у молодёжи, повышает конверсию"
        })
    
    return sorted(recommendations, key=lambda x: 
                  {"essential": 0, "high": 1, "medium": 2, "low": 3}[x["priority"]])

# Пример

recs = recommend_payment_method(
    business_type="ecommerce",
    average_order_value=3000,
    primary_market="russia",
    customer_demographics="mixed"
)

for rec in recs:
    print(f"{rec['priority'].upper()}: {rec['method']} — {rec['reason']}")
```

---

## 💡 Key Takeaways

- **Open Banking революционизирует платежи** — A2A дешевле карт (0.1-0.5% vs 1.5-3%)
- **E-wallets доминируют регионально** — Alipay/WeChat в Китае, PayPal глобально, СБП в России
- **QR-платежи — простой вход для малого бизнеса** — Static QR бесплатен, Dynamic QR масштабируется
- **BNPL повышает конверсию** — но комиссии 3-6% выше карт
- **P2P эволюционирует в P2M** — СБП, UPI, Pix показывают путь
- **Карты остаются фундаментом** — но доля снижается
- **Выбор зависит от рынка** — локальные методы критичны для конверсии

---

## 🚀 Next Steps

**Следующий модуль:**
- [Национальные и региональные системы](../19_National_Regional_Systems/) — iDEAL, Boleto, СБП, локальные особенности

**Для углубления:**
- PSD2 Technical Standards
- СБП API документация НСПК
- Klarna/Afterpay Merchant Integration Guides

**Практика:**
- Интегрируйте СБП QR в тестовом окружении
- Изучите Open Banking sandbox (TrueLayer, Plaid)
- Проанализируйте экономику BNPL для вашего бизнеса

---

## 📚 Additional Resources

**Open Banking:**
- [Open Banking UK](https://www.openbanking.org.uk/)
- [Berlin Group Standards](https://www.berlin-group.org/)

**СБП:**
- [НСПК — Система быстрых платежей](https://sbp.nspk.ru/)

**BNPL:**
- [Klarna Developer Portal](https://developers.klarna.com/)
- [Affirm Docs](https://docs.affirm.com/)

---

