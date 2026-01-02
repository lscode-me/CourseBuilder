# NFC и бесконтактные платежи
## Токенизация, Apple Pay, Google Pay, архитектура мобильных платежей

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:
- Понимать базовые принципы EMV-технологии
- Знать структуру банковской карты (PAN, CVV, expiry date)
- Быть знакомы с процессом авторизации платежа
- Понимать роли участников платёжной системы

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:
- Объяснять принципы работы NFC и бесконтактной связи
- Описывать архитектуру мобильных кошельков и токенизации
- Понимать роль Secure Element и HCE
- Интегрировать Apple Pay и Google Pay в приложения
- Оценивать безопасность бесконтактных платежей

---

## 1. Технология NFC

### 1.1 Что такое NFC

**NFC (Near Field Communication)** — технология беспроводной связи малого радиуса действия, позволяющая обмениваться данными между устройствами на расстоянии до 4 см.

**Технические характеристики:**

| Параметр | Значение |
|----------|----------|
| Частота | 13.56 МГц |
| Дальность | до 4 см (практически до 2 см) |
| Скорость передачи | 106, 212, 424 кбит/с |
| Стандарты | ISO 14443, ISO 18092 |
| Время установки связи | < 0.1 секунды |

> **💡 Почему 4 см?**  
> Малый радиус действия — преимущество безопасности: невозможно перехватить данные с расстояния, как при Bluetooth или Wi-Fi.

### 1.2 История и эволюция

```
2002    Первый стандарт NFC (Sony + Philips)
2004    NFC Forum основан
2006    Первые телефоны с NFC (Nokia 6131)
2011    Google Wallet запущен
2014    Apple Pay — массовое adoption
2015    Android Pay, Samsung Pay
2018    Объединение в Google Pay
2020+   Пандемия ускорила рост бесконтактных платежей
```

### 1.3 Режимы работы NFC

NFC поддерживает три режима работы:

| Режим | Описание | Применение |
|-------|----------|------------|
| **Card Emulation** | Устройство эмулирует бесконтактную карту | Apple Pay, Google Pay, проездные |
| **Reader/Writer** | Устройство читает/пишет NFC-метки | Чтение информации, Smart Posters |
| **P2P (Peer-to-Peer)** | Обмен данными между устройствами | Android Beam (устарел), передача файлов |

**Для платежей используется режим Card Emulation:**

```
┌─────────────────┐        ┌─────────────────┐
│   Смартфон      │        │   POS-терминал  │
│  ┌───────────┐  │        │  ┌───────────┐  │
│  │   NFC     │◄─┼───4см──┼─►│   NFC     │  │
│  │Controller │  │   RF   │  │  Reader   │  │
│  └───────────┘  │        │  └───────────┘  │
│       ↑         │        │       ↑         │
│  ┌───────────┐  │        │  ┌───────────┐  │
│  │  Secure   │  │        │  │  Payment  │  │
│  │  Element  │  │        │  │  App      │  │
│  └───────────┘  │        │  └───────────┘  │
└─────────────────┘        └─────────────────┘
```

### 1.4 Сравнение с другими технологиями

| Параметр | NFC | Bluetooth | QR-код |
|----------|-----|-----------|--------|
| Дальность | 4 см | 10-100 м | Оптическая |
| Время подключения | < 0.1 сек | 2-6 сек | 1-2 сек |
| Безопасность | Высокая | Средняя | Средняя |
| Двунаправленность | Да | Да | Нет |
| Без батареи (пассивный) | Да | Нет | Да |

---

## 2. Бесконтактные карты

### 2.1 Архитектура бесконтактной карты

Бесконтактная карта содержит:
- **Антенну** — принимает RF-сигнал и получает питание
- **EMV-чип** — хранит данные и генерирует криптограммы
- **Конденсатор** — накапливает энергию

```
┌─────────────────────────────────────────────────┐
│                                                 │
│   ┌─────────────────────────────────────────┐   │
│   │           Антенна (витки)                │   │
│   │   ┌─────────────────────────────────┐   │   │
│   │   │                                 │   │   │
│   │   │        ┌─────────┐              │   │   │
│   │   │        │EMV Chip │              │   │   │
│   │   │        │ + NFC   │              │   │   │
│   │   │        └─────────┘              │   │   │
│   │   │                                 │   │   │
│   │   │      4276 1234 5678 9012        │   │   │
│   │   │                                 │   │   │
│   │   └─────────────────────────────────┘   │   │
│   └─────────────────────────────────────────┘   │
│                                                 │
│   CARDHOLDER NAME            VALID THRU: 12/27  │
└─────────────────────────────────────────────────┘
```

### 2.2 Процесс бесконтактного платежа

**Шаги транзакции:**

```
1. Карта подносится к терминалу
   └─► Расстояние < 4 см
   
2. Терминал генерирует RF-поле
   └─► 13.56 МГц, индуктивная связь
   
3. Поле индуцирует ток в антенне карты
   └─► Карта получает питание
   
4. Чип активируется
   └─► Запускается платёжное приложение
   
5. Обмен данными (APDU-команды)
   └─► SELECT, GPO, READ RECORD
   
6. Генерация криптограммы (ARQC)
   └─► Уникальна для транзакции
   
7. Передача данных терминалу
   └─► PAN, криптограмма, ATC
   
8. Авторизация через эквайера
```

### 2.3 APDU-команды бесконтактного платежа

**Application Protocol Data Unit (APDU)** — формат команд между терминалом и картой:

```
// SELECT PPSE (Proximity Payment System Environment)
>> 00 A4 04 00 0E 32 50 41 59 2E 53 59 53 2E 44 44 46 30 31 00

// Response: список платёжных приложений
<< 6F 23 84 0E 32 50 41 59 2E 53 59 53 2E 44 44 46 30 31 
   A5 11 BF 0C 0E 61 0C 4F 07 A0 00 00 00 04 10 10 87 01 01

// SELECT AID (Mastercard)
>> 00 A4 04 00 07 A0 00 00 00 04 10 10 00

// GET PROCESSING OPTIONS
>> 80 A8 00 00 02 83 00 00

// READ RECORD (получение данных карты)
>> 00 B2 01 0C 00
```

**Расшифровка AID (Application Identifier):**

| AID | Платёжная система |
|-----|-------------------|
| A0 00 00 00 03 | Visa |
| A0 00 00 00 04 | Mastercard |
| A0 00 00 00 25 | American Express |
| A0 00 00 06 58 | Мир |

### 2.4 Лимиты без PIN-кода

Бесконтактные платежи до определённой суммы не требуют ввода PIN:

| Страна | Лимит | Примечание |
|--------|-------|------------|
| Россия | 3 000 - 5 000 ₽ | Зависит от эмитента |
| Великобритания | £100 | Увеличен с £30 в 2021 |
| Еврозона | €50 | В некоторых странах €25 |
| США | $100-250 | Зависит от сети |
| Австралия | A$200 | Один из самых высоких |

> **⚠️ Важно:**  
> После нескольких бесконтактных транзакций подряд карта может потребовать ввод PIN для верификации присутствия держателя.

### 2.5 CVM (Cardholder Verification Method)

```
Бесконтактная транзакция:
                           │
        ┌──────────────────┴──────────────────┐
        ▼                                     ▼
   Сумма < лимита                        Сумма ≥ лимита
        │                                     │
        ▼                                     ▼
   No CVM (без PIN)                    PIN или CDCVM*
        │                                     │
        ▼                                     ▼
   Быстрая оплата                      Ввод PIN на терминале
                                       или биометрия на телефоне

* CDCVM = Consumer Device CVM (верификация на устройстве)
```

---

## 3. Мобильные кошельки

### 3.1 Основные платформы

| Кошелёк | Платформа | Запуск | Особенности |
|---------|-----------|--------|-------------|
| Apple Pay | iOS, watchOS | 2014 | Secure Enclave, Face ID |
| Google Pay | Android, Wear OS | 2015/2018 | HCE, широкая совместимость |
| Samsung Pay | Samsung Android | 2015 | MST + NFC |
| Mir Pay | Android (Россия) | 2019 | Интеграция с СБП |
| Huawei Pay | Huawei | 2020 | HMS |

### 3.2 Архитектура мобильного кошелька

```
┌─────────────────────────────────────────────────────────────┐
│                        СМАРТФОН                              │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────────────┐   ┌─────────────────────────────┐  │
│  │   Wallet App        │   │   Issuer App (опционально)  │  │
│  │   (Apple Pay/GPay)  │   │   (Сбербанк, Тинькофф)      │  │
│  └──────────┬──────────┘   └──────────────────────────────┘  │
│             │                                                │
│  ┌──────────▼──────────────────────────────────────────────┐│
│  │              Payment Framework (OS Layer)                ││
│  │     - PassKit (iOS) / Google Pay API (Android)          ││
│  └──────────┬───────────────────────────────────────────────┘│
│             │                                                │
│  ┌──────────▼──────────┐   ┌─────────────────────────────┐  │
│  │   Secure Element    │   │   Host Card Emulation       │  │
│  │   (Hardware SE)     │   │   (Cloud-based)             │  │
│  │                     │   │                             │  │
│  │   • Apple (Secure   │   │   • Google Pay (Primary)    │  │
│  │     Enclave)        │   │   • Mir Pay                 │  │
│  │   • Samsung Knox    │   │   • Huawei Pay              │  │
│  └──────────┬──────────┘   └──────────┬──────────────────┘  │
│             │                         │                      │
│  ┌──────────▼─────────────────────────▼──────────────────┐  │
│  │                    NFC Controller                      │  │
│  └──────────────────────────┬────────────────────────────┘  │
└─────────────────────────────┼────────────────────────────────┘
                              │
                    ┌─────────▼─────────┐
                    │   POS Terminal    │
                    └───────────────────┘
```

### 3.3 Secure Element vs HCE

**Secure Element (SE):**
- Аппаратный защищённый чип
- Физически изолирован от ОС
- Ключи никогда не покидают SE
- Используется Apple Pay

**Host Card Emulation (HCE):**
- Программная эмуляция карты
- Токены хранятся в облаке
- Загружаются перед использованием
- Используется Google Pay

```
┌─────────────────────────────┐  ┌─────────────────────────────┐
│      Secure Element         │  │      HCE (Cloud-based)      │
├─────────────────────────────┤  ├─────────────────────────────┤
│                             │  │                             │
│   ┌───────────────────┐     │  │   ┌───────────────────┐     │
│   │  Secure Enclave   │     │  │   │  Cloud Server     │     │
│   │  ┌─────────────┐  │     │  │   │  ┌─────────────┐  │     │
│   │  │ Private Key │  │     │  │   │  │ Token Vault │  │     │
│   │  │ (Never      │  │     │  │   │  │ LUK Pool    │  │     │
│   │  │  leaves)    │  │     │  │   │  └──────┬──────┘  │     │
│   │  └─────────────┘  │     │  │   └─────────┼─────────┘     │
│   └───────────────────┘     │  │             │               │
│            ↓                │  │   Download  │               │
│   Local cryptogram          │  │   tokens    ▼               │
│   generation                │  │   ┌───────────────────┐     │
│                             │  │   │  Device (TEE)     │     │
│                             │  │   │  Limited-use keys │     │
│                             │  │   └───────────────────┘     │
└─────────────────────────────┘  └─────────────────────────────┘
```

### 3.4 Процесс добавления карты

**Apple Pay:**

```
1. Пользователь открывает Wallet
   └─► Нажимает "+" для добавления карты

2. Сканирование или ввод данных карты
   └─► PAN, Expiry, CVV

3. Отправка в Apple Pay Server
   └─► Зашифрованные данные

4. Apple связывается с TSP эмитента
   └─► Visa Token Service / MDES

5. Верификация пользователя
   └─► SMS, push, звонок, приложение банка

6. Генерация DPAN
   └─► Device-specific token

7. DPAN загружается в Secure Enclave
   └─► С криптографическими ключами

8. Карта готова к использованию
```

**JSON-структура запроса на токенизацию (упрощённо):**

```json
{
  "paymentData": {
    "version": "EC_v1",
    "data": "encrypted_card_data",
    "signature": "signature_value",
    "header": {
      "ephemeralPublicKey": "MFkw...",
      "publicKeyHash": "hash_value",
      "transactionId": "transaction_uuid"
    }
  },
  "paymentMethod": {
    "displayName": "Visa 1234",
    "network": "Visa",
    "type": "debit"
  },
  "transactionIdentifier": "unique_tx_id"
}
```

---

## 4. Токенизация

### 4.1 Что такое токенизация

**Токенизация** — замена реального номера карты (PAN) на суррогатное значение (токен), которое безопасно для хранения и передачи.

```
┌────────────────────────────────────────────────────────────────┐
│                                                                │
│   Реальный PAN:     4276 1234 5678 9012                        │
│                              │                                 │
│                              ▼                                 │
│                     ┌─────────────────┐                        │
│                     │  Token Service  │                        │
│                     │    Provider     │                        │
│                     └────────┬────────┘                        │
│                              │                                 │
│                              ▼                                 │
│   Token (DPAN):     4276 9999 0000 1234                        │
│                                                                │
│   ┌──────────────────────────────────────────────────────┐     │
│   │ Токен привязан к:                                    │     │
│   │ • Конкретному устройству (device_id)                 │     │
│   │ • Конкретному мерчанту (merchant_id) — опционально   │     │
│   │ • Домену использования (ecommerce, in-app, in-store) │     │
│   └──────────────────────────────────────────────────────┘     │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

### 4.2 Типы токенов

| Тип | Описание | Пример |
|-----|----------|--------|
| **DPAN (Device PAN)** | Токен для конкретного устройства | Apple Pay на iPhone |
| **CPAN (Card-on-file)** | Токен для хранения у мерчанта | Amazon, Netflix |
| **MDES Token** | Mastercard Digital Enablement Service | Mastercard токенизация |
| **VTS Token** | Visa Token Service | Visa токенизация |

### 4.3 Token Service Providers (TSP)

| Платёжная система | TSP-сервис |
|-------------------|------------|
| Visa | VTS (Visa Token Service) |
| Mastercard | MDES (Mastercard Digital Enablement Service) |
| American Express | AETS (Amex Token Service) |
| МИР | НСПК Token Service |
| UnionPay | UPI Token Service |

### 4.4 Жизненный цикл токена

```
                    ┌──────────────────┐
                    │   Token Request  │
                    │   (Card Added)   │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │ Token Provisioned │
                    │  Status: ACTIVE  │
                    └────────┬─────────┘
                             │
            ┌────────────────┼────────────────┐
            │                │                │
            ▼                ▼                ▼
    ┌───────────────┐ ┌─────────────┐ ┌─────────────────┐
    │   SUSPENDED   │ │   DELETED   │ │   Token Used    │
    │ (временно     │ │ (удалён из  │ │   in Payment    │
    │  заблокирован)│ │  кошелька)  │ │                 │
    └───────────────┘ └─────────────┘ └────────┬────────┘
            │                                  │
            ▼                                  ▼
    ┌───────────────┐                 ┌─────────────────┐
    │   RESUMED     │                 │   De-token at   │
    │ (разблокиро-  │                 │   Issuer for    │
    │   ван)        │                 │   Auth          │
    └───────────────┘                 └─────────────────┘
```

### 4.5 Криптограмма и LUK

**Limited-Use Key (LUK)** — ключ с ограниченным сроком действия:

```
LUK Характеристики:
├── Время жизни: 24-48 часов
├── Количество транзакций: до 10-15
├── Сумма транзакций: ограничена
└── Обновляется автоматически из облака

Криптограмма генерируется:
├── Из LUK
├── Unpredictable Number (от терминала)
├── Transaction Counter (ATC)
└── Сумма и валюта транзакции
```

**Пример структуры криптограммы:**

```json
{
  "token": "4276999900001234",
  "tokenExpirationDate": "1227",
  "cryptogram": "AgAAAAAABk4DWZ4C28yMsKk=",
  "eci": "07",
  "tokenRequestorId": "40010030273"
}
```

---

## 5. Интеграция Apple Pay

### 5.1 Web-интеграция (Apple Pay JS)

**Проверка поддержки:**

```javascript
// Проверка доступности Apple Pay
if (window.ApplePaySession) {
    const merchantIdentifier = 'merchant.com.example';
    
    ApplePaySession.canMakePaymentsWithActiveCard(merchantIdentifier)
        .then(canMakePayments => {
            if (canMakePayments) {
                // Показать кнопку Apple Pay
                showApplePayButton();
            }
        });
}
```

**Создание платёжной сессии:**

```javascript
const paymentRequest = {
    countryCode: 'RU',
    currencyCode: 'RUB',
    supportedNetworks: ['visa', 'masterCard', 'mir'],
    merchantCapabilities: ['supports3DS'],
    total: {
        label: 'Магазин Example',
        amount: '1299.00'
    },
    lineItems: [
        { label: 'Товар 1', amount: '999.00' },
        { label: 'Доставка', amount: '300.00' }
    ]
};

const session = new ApplePaySession(3, paymentRequest);

// Валидация мерчанта
session.onvalidatemerchant = (event) => {
    fetch('/api/apple-pay/validate', {
        method: 'POST',
        body: JSON.stringify({ validationURL: event.validationURL })
    })
    .then(response => response.json())
    .then(merchantSession => {
        session.completeMerchantValidation(merchantSession);
    });
};

// Авторизация платежа
session.onpaymentauthorized = (event) => {
    const payment = event.payment;
    
    // Отправка токена на сервер для обработки
    fetch('/api/payments/process', {
        method: 'POST',
        body: JSON.stringify({
            token: payment.token,
            billingContact: payment.billingContact,
            shippingContact: payment.shippingContact
        })
    })
    .then(response => {
        if (response.ok) {
            session.completePayment(ApplePaySession.STATUS_SUCCESS);
        } else {
            session.completePayment(ApplePaySession.STATUS_FAILURE);
        }
    });
};

session.begin();
```

### 5.2 Обработка Apple Pay токена на сервере

```python
import json
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec
from base64 import b64decode

def decrypt_apple_pay_token(payment_data: dict, merchant_private_key: bytes) -> dict:
    """
    Расшифровка Apple Pay токена.
    
    В production используйте библиотеку вашего PSP (Stripe, Adyen, etc.)
    """
    # Извлекаем данные
    header = payment_data['header']
    encrypted_data = b64decode(payment_data['data'])
    ephemeral_pub_key = b64decode(header['ephemeralPublicKey'])
    
    # Загружаем приватный ключ мерчанта
    private_key = serialization.load_pem_private_key(
        merchant_private_key, 
        password=None
    )
    
    # ECDH Key Exchange
    ephemeral_public_key = ec.EllipticCurvePublicKey.from_encoded_point(
        ec.SECP256R1(), 
        ephemeral_pub_key
    )
    shared_secret = private_key.exchange(ec.ECDH(), ephemeral_public_key)
    
    # Derive symmetric key and decrypt
    # ... (implementation details)
    
    return decrypted_data
```

### 5.3 iOS SDK интеграция

```swift
import PassKit

class PaymentHandler: NSObject, PKPaymentAuthorizationViewControllerDelegate {
    
    func startApplePayPayment(amount: Decimal) {
        let request = PKPaymentRequest()
        request.merchantIdentifier = "merchant.com.example"
        request.supportedNetworks = [.visa, .masterCard, .mir]
        request.merchantCapabilities = .capability3DS
        request.countryCode = "RU"
        request.currencyCode = "RUB"
        
        let item = PKPaymentSummaryItem(
            label: "Покупка",
            amount: NSDecimalNumber(decimal: amount)
        )
        request.paymentSummaryItems = [item]
        
        if let controller = PKPaymentAuthorizationViewController(paymentRequest: request) {
            controller.delegate = self
            present(controller, animated: true)
        }
    }
    
    func paymentAuthorizationViewController(
        _ controller: PKPaymentAuthorizationViewController,
        didAuthorizePayment payment: PKPayment,
        handler completion: @escaping (PKPaymentAuthorizationResult) -> Void
    ) {
        // Отправляем payment.token на сервер
        let tokenData = payment.token.paymentData
        
        PaymentAPI.processApplePay(tokenData: tokenData) { result in
            switch result {
            case .success:
                completion(PKPaymentAuthorizationResult(status: .success, errors: nil))
            case .failure(let error):
                completion(PKPaymentAuthorizationResult(
                    status: .failure, 
                    errors: [error]
                ))
            }
        }
    }
}
```

---

## 6. Интеграция Google Pay

### 6.1 Web-интеграция

```javascript
// Инициализация Google Pay
const paymentsClient = new google.payments.api.PaymentsClient({
    environment: 'PRODUCTION'  // или 'TEST'
});

const baseRequest = {
    apiVersion: 2,
    apiVersionMinor: 0
};

const tokenizationSpecification = {
    type: 'PAYMENT_GATEWAY',
    parameters: {
        gateway: 'cloudpayments',  // Ваш PSP
        gatewayMerchantId: 'your_merchant_id'
    }
};

const cardPaymentMethod = {
    type: 'CARD',
    parameters: {
        allowedAuthMethods: ['PAN_ONLY', 'CRYPTOGRAM_3DS'],
        allowedCardNetworks: ['VISA', 'MASTERCARD', 'MIR']
    },
    tokenizationSpecification: tokenizationSpecification
};

// Проверка готовности к оплате
paymentsClient.isReadyToPay({
    ...baseRequest,
    allowedPaymentMethods: [cardPaymentMethod]
}).then(response => {
    if (response.result) {
        addGooglePayButton();
    }
});

// Создание кнопки
function addGooglePayButton() {
    const button = paymentsClient.createButton({
        onClick: onGooglePaymentButtonClicked,
        buttonColor: 'black',
        buttonType: 'pay',
        buttonLocale: 'ru'
    });
    document.getElementById('google-pay-container').appendChild(button);
}

// Обработка клика
function onGooglePaymentButtonClicked() {
    const paymentDataRequest = {
        ...baseRequest,
        allowedPaymentMethods: [cardPaymentMethod],
        transactionInfo: {
            totalPriceStatus: 'FINAL',
            totalPrice: '1299.00',
            currencyCode: 'RUB',
            countryCode: 'RU'
        },
        merchantInfo: {
            merchantName: 'Магазин Example',
            merchantId: 'BCR2DN4TXXXXXXXXXX'  // Production ID
        }
    };
    
    paymentsClient.loadPaymentData(paymentDataRequest)
        .then(paymentData => {
            processPayment(paymentData);
        })
        .catch(err => {
            console.error('Ошибка Google Pay:', err);
        });
}

function processPayment(paymentData) {
    const token = paymentData.paymentMethodData.tokenizationData.token;
    
    fetch('/api/payments/google-pay', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ token: JSON.parse(token) })
    }).then(handlePaymentResponse);
}
```

### 6.2 Структура Google Pay токена

```json
{
  "signature": "MEYCIQC...",
  "intermediateSigningKey": {
    "signedKey": "{\"keyValue\":\"MFkw...\",\"keyExpiration\":\"1234567890\"}",
    "signatures": ["MEUCIQC..."]
  },
  "protocolVersion": "ECv2",
  "signedMessage": "{\"encryptedMessage\":\"...\",\"ephemeralPublicKey\":\"...\",\"tag\":\"...\"}"
}
```

**После расшифровки:**

```json
{
  "paymentMethod": "CARD",
  "paymentMethodDetails": {
    "pan": "4111111111111111",
    "expirationMonth": 12,
    "expirationYear": 2027,
    "authMethod": "CRYPTOGRAM_3DS",
    "cryptogram": "AgAAAAAABk4DWZ4C28yMsKk=",
    "eciIndicator": "07"
  },
  "gatewayMerchantId": "your_merchant_id",
  "messageId": "AH2EjtfkYwG...",
  "messageExpiration": "1234567890000"
}
```

---

## 7. Samsung Pay MST

### 7.1 Особенности технологии

**MST (Magnetic Secure Transmission)** — уникальная технология Samsung, эмулирующая магнитную полосу:

```
┌─────────────────────────────────────────────────────────────┐
│                    Samsung Pay                               │
├──────────────────────────┬──────────────────────────────────┤
│         NFC              │            MST                    │
│                          │                                   │
│  • Стандартная технология│  • Только Samsung                 │
│  • Терминал с NFC        │  • Работает на старых терминалах  │
│  • Быстрее               │  • Эмуляция магнитной полосы      │
│  • Более распространён   │  • Постепенно убирается           │
└──────────────────────────┴──────────────────────────────────┘
```

### 7.2 Как работает MST

```
1. Телефон генерирует переменное магнитное поле
   └─► Имитирует движение магнитной полосы

2. Терминал воспринимает как обычный "свайп"
   └─► Не требует модификации терминала

3. Передаётся токенизированный PAN
   └─► Не реальный номер карты

4. Криптограмма Samsung Pay
   └─► Одноразовая, как при EMV
```

### 7.3 Ограничения MST

- ❌ Только устройства Samsung (до Galaxy S21)
- ❌ Samsung убирает поддержку MST с 2021
- ❌ Не работает с чиповыми ридерами
- ❌ Менее безопасно, чем NFC

---

## 8. Безопасность бесконтактных платежей

### 8.1 Методы аутентификации

| Метод | Описание | Устройства |
|-------|----------|------------|
| Touch ID | Отпечаток пальца | iPhone, некоторые Android |
| Face ID | 3D-сканирование лица | iPhone X+ |
| Сканер радужки | Сканирование глаза | Samsung Galaxy |
| PIN/Password | Код разблокировки | Все устройства |
| Голосовой ассистент | Не используется для платежей | — |

### 8.2 Многоуровневая защита

```
┌─────────────────────────────────────────────────────────────┐
│                    УРОВНИ БЕЗОПАСНОСТИ                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Уровень 1: Биометрическая аутентификация                   │
│  ├── Face ID / Touch ID обязательны для платежа             │
│  └── Или PIN устройства                                     │
│                                                             │
│  Уровень 2: Secure Element / TEE                            │
│  ├── Криптоключи изолированы от ОС                          │
│  └── Физически защищённое хранение                          │
│                                                             │
│  Уровень 3: Токенизация                                     │
│  ├── Реальный PAN никогда не передаётся                     │
│  └── Токен бесполезен без устройства                        │
│                                                             │
│  Уровень 4: Динамическая криптограмма                       │
│  ├── Уникальна для каждой транзакции                        │
│  └── Невозможно повторно использовать                       │
│                                                             │
│  Уровень 5: Device Binding                                  │
│  ├── Токен привязан к конкретному устройству                │
│  └── При смене устройства — новый токен                     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 8.3 Сценарии атак и защита

| Атака | Риск | Защита |
|-------|------|--------|
| Перехват NFC-сигнала | Низкий | Малый радиус (4 см), криптограмма |
| Клонирование токена | Очень низкий | Device binding, SE |
| Украденное устройство | Средний | Биометрия, Remote Wipe |
| Relay Attack | Низкий | Timing checks, distance bounding |
| Man-in-the-Middle | Очень низкий | End-to-end encryption |

### 8.4 Что делать при утере устройства

```
1. Удалённая блокировка устройства
   └─► Find My iPhone / Find My Device

2. Приостановка токенов
   └─► Через приложение банка или Apple/Google ID

3. Токены автоматически деактивируются
   └─► При отключении устройства от аккаунта

4. Отзыв карты не требуется!
   └─► Достаточно отозвать токен
```

---

## 9. Tap to Phone (Soft POS)

### 9.1 Что это

**Soft POS** — технология, превращающая обычный смартфон в POS-терминал для приёма бесконтактных платежей.

```
┌─────────────────────────────────────────────────────────────┐
│                    SOFT POS АРХИТЕКТУРА                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   Смартфон продавца          Карта/телефон покупателя       │
│   ┌─────────────────┐        ┌─────────────────┐            │
│   │   Soft POS App  │        │   Карта с NFC   │            │
│   │   ┌─────────┐   │◄──────►│   или Apple Pay │            │
│   │   │   NFC   │   │  NFC   │                 │            │
│   │   │ (Reader)│   │        └─────────────────┘            │
│   │   └────┬────┘   │                                       │
│   │        │        │                                       │
│   │   ┌────▼────┐   │                                       │
│   │   │   TEE   │   │                                       │
│   │   │ Secure  │   │                                       │
│   │   └────┬────┘   │                                       │
│   └────────┼────────┘                                       │
│            │                                                │
│            ▼                                                │
│   ┌─────────────────┐                                       │
│   │ Payment Backend │                                       │
│   │ (PSP/Acquirer)  │                                       │
│   └─────────────────┘                                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### 9.2 Требования PCI для Soft POS

| Требование | Описание |
|------------|----------|
| PIN on Glass | Безопасный ввод PIN на экране |
| TEE/SE | Защищённая среда выполнения |
| Kernel attestation | Проверка целостности ядра |
| App attestation | Подтверждение подлинности приложения |
| Secure communication | Шифрованный канал до PSP |

### 9.3 Примеры решений

| Решение | Платформа | Особенности |
|---------|-----------|-------------|
| Visa Tap to Phone | Android | Сертифицировано Visa |
| Mastercard Tap on Phone | Android | MDES интеграция |
| Square Terminal | iOS/Android | Своя экосистема |
| SumUp | Android | Популярен в Европе |
| CloudPayments Tap | Android | Россия |

---

## 10. Практические аспекты для бизнеса

### 10.1 Преимущества NFC-платежей

| Преимущество | Для бизнеса | Для покупателя |
|--------------|-------------|----------------|
| **Скорость** | Выше пропускная способность | Быстрее оплата |
| **Гигиена** | Меньше контакта с терминалом | Безопаснее |
| **Конверсия** | Меньше отказов | Удобнее платить |
| **Износ** | Меньше износ терминала | Карта не повреждается |
| **Безопасность** | Ниже риск мошенничества | Токенизация защищает |

### 10.2 Статистика adoption

```
Доля бесконтактных платежей (2023):
├── Великобритания: 85%+
├── Австралия: 90%+
├── Россия: 70%+ (в крупных городах 80%+)
├── США: 45%+
├── Германия: 50%+
└── Мировой средний: 55%+

Рост после COVID-19:
├── Увеличение лимитов без PIN
├── Осведомлённость о гигиене
└── Привычка избегать контакта
```

### 10.3 Checklist для мерчанта

```markdown
## Подготовка к приёму NFC-платежей

### Оборудование

- [ ] Терминал поддерживает NFC (contactless)
- [ ] Терминал обновлён до последней прошивки
- [ ] Терминал поддерживает Apple Pay/Google Pay
- [ ] Установлены логотипы contactless на терминале

### Интеграция (для e-commerce)

- [ ] Apple Pay настроен (merchant ID, сертификаты)
- [ ] Google Pay интегрирован
- [ ] Кнопки отображаются только при поддержке
- [ ] Обработка токенов реализована на backend

### Обучение персонала

- [ ] Сотрудники знают как принимать бесконтактные платежи
- [ ] Понимают разницу между NFC картой и телефоном
- [ ] Знают лимиты без PIN

### Отображение

- [ ] Наклейки "Contactless Accepted"
- [ ] Логотипы Apple Pay, Google Pay
- [ ] Указание лимитов без PIN (опционально)
```

---

## 💡 Key Takeaways

- **NFC** — бесконтактная связь до 4 см, основа мобильных платежей
- **Токенизация (DPAN)** — реальный PAN никогда не передаётся, токен бесполезен без устройства
- **Secure Element** — аппаратная защита криптоключей (Apple), HCE — облачный подход (Google)
- **Биометрия обязательна** — Face ID / Touch ID для каждой транзакции
- **Безопасность выше физических карт** — многоуровневая защита, device binding
- **Apple Pay / Google Pay** — разные подходы к хранению токенов, одинаковая безопасность для пользователя
- **Soft POS** — превращает смартфон в терминал, новый тренд

---

## 🚀 Next Steps

**Следующий модуль:**
- [Безопасность платежей](../17_Payment_Security/) — PCI DSS, 3-D Secure, fraud detection

**Для углубления:**
- Спецификации EMV Contactless
- Apple Pay Programming Guide
- Google Pay API Documentation

**Практика:**
- Интегрируйте Apple Pay в тестовое веб-приложение
- Изучите токенизацию через sandbox вашего PSP

---

## 📚 Additional Resources

**Документация:**
- [Apple Pay JS API](https://developer.apple.com/documentation/apple_pay_on_the_web)
- [Google Pay API](https://developers.google.com/pay/api)
- [EMV Contactless Specifications](https://www.emvco.com/)

**Стандарты:**
- ISO 14443 (бесконтактные карты)
- EMV Contactless Kernel C-2-C-8
- PCI Mobile Payment Security Guidelines

---

