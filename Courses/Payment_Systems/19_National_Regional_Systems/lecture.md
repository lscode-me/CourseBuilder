# Национальные и региональные платёжные системы
## Локальные методы, регуляторные особенности и интеграция

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:
- Понимать модель работы международных платёжных систем (Visa, Mastercard)
- Знать основы A2A платежей и Open Banking
- Понимать роль центральных банков в платёжной инфраструктуре
- Быть знакомы с альтернативными платёжными методами

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:
- Объяснять причины создания национальных платёжных систем
- Описывать особенности ключевых региональных рынков
- Интегрировать локальные платёжные методы в e-commerce
- Понимать регуляторные требования разных юрисдикций
- Выбирать оптимальные методы для конкретных рынков

---

## 1. Зачем нужны национальные системы

### 1.1 Драйверы создания

```
┌─────────────────────────────────────────────────────────────────┐
│          ПРИЧИНЫ СОЗДАНИЯ НАЦИОНАЛЬНЫХ ПЛАТЁЖНЫХ СИСТЕМ          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ГЕОПОЛИТИЧЕСКИЕ:                                               │
│  ├── Независимость от иностранной инфраструктуры                │
│  ├── Защита от санкций и отключений                             │
│  ├── Контроль над критической инфраструктурой                   │
│  └── Суверенитет в финансовой сфере                             │
│                                                                 │
│  ЭКОНОМИЧЕСКИЕ:                                                 │
│  ├── Снижение комиссий для рынка                                │
│  ├── Удержание interchange внутри страны                        │
│  ├── Поддержка локального fintech                               │
│  └── Конкуренция с международными игроками                      │
│                                                                 │
│  СОЦИАЛЬНЫЕ:                                                    │
│  ├── Финансовая инклюзия (доступ для населения)                 │
│  ├── Мгновенные переводы между гражданами                       │
│  └── Удобство для локального бизнеса                            │
│                                                                 │
│  ТЕХНОЛОГИЧЕСКИЕ:                                               │
│  ├── Внедрение инноваций (real-time, QR)                        │
│  ├── CBDC и цифровые валюты                                     │
│  └── Локализация данных                                         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 1.2 Типы национальных систем

| Тип | Описание | Примеры |
|-----|----------|---------|
| **Карточные ПС** | Национальные бренды карт | МИР, RuPay, UnionPay |
| **Мгновенные платежи** | Real-time A2A переводы | СБП, UPI, PIX, FPS |
| **CBDC** | Цифровые валюты ЦБ | Цифровой рубль, e-CNY |
| **Региональные сети** | Межстрановые системы | SEPA, BRICS Pay |

### 1.3 Глобальный ландшафт

```
Национальные системы по регионам:

    ┌─────────────────────────────────────────────────────────────┐
    │                     ЕВРОПА                                   │
    │   SEPA, iDEAL, Bancontact, Giropay, BLIK                    │
    └─────────────────────────────────────────────────────────────┘
              ▲
              │
    ┌─────────┴─────────┐                     ┌───────────────────┐
    │      РОССИЯ       │                     │       АЗИЯ        │
    │   МИР, СБП        │                     │  UnionPay, UPI,   │
    │   Цифровой рубль  │                     │  PromptPay, QR Pay│
    └───────────────────┘                     └───────────────────┘
              
    ┌───────────────────┐                     ┌───────────────────┐
    │  ЛАТИНСКАЯ        │                     │      АФРИКА       │
    │   АМЕРИКА         │                     │   M-Pesa, Orange  │
    │  PIX, Boleto      │                     │   Money           │
    └───────────────────┘                     └───────────────────┘
```

---

## 2. Россия

### 2.1 Платёжная система МИР

**История и развитие:**

| Год | Событие |
|-----|---------|
| 2014 | Создание НСПК (Национальная система платёжных карт) |
| 2015 | Запуск карт МИР |
| 2017 | Обязательный приём МИР во всех ПОС |
| 2019 | 50 млн карт |
| 2022 | 200+ млн карт, отключение Visa/MC |

**Технические особенности:**

```
МИР Card Structure:

BIN (Bank Identification Number):
├── 2200 - 2204 (МИР Standard)
├── 2201 - 2202 (МИР Premium)
└── 2203 - 2204 (МИР Corporate)

Технологии:
├── EMV чип (обязательно)
├── NFC (contactless)
├── 3-D Secure (MirAccept)
├── Токенизация (Mir Token Service)
└── Кобейджинг: МИР-UnionPay, МИР-JCB, МИР-Maestro
```

**Международное принятие:**

| Страна | Статус |
|--------|--------|
| Турция | Полный приём |
| Вьетнам | Ограниченный |
| Армения | Полный приём |
| Беларусь | Полный приём |
| Казахстан | Развивается |
| ОАЭ | Ограниченный |

### 2.2 СБП (Система быстрых платежей)

**Архитектура СБП:**

```
┌─────────────────────────────────────────────────────────────────┐
│                     АРХИТЕКТУРА СБП                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Плательщик ◄─────────────────────────────────► Получатель     │
│       │                                               ▲         │
│       │ 1. Инициация                                 │         │
│       ▼                                               │         │
│   ┌─────────────┐                           ┌─────────────┐     │
│   │ Банк        │     3. Перевод через      │    Банк     │     │
│   │ плательщика │◄──────────────────────────│ получателя  │     │
│   └──────┬──────┘           НСПК            └─────────────┘     │
│          │                   ▲                                  │
│          │ 2. Запрос        │ 4. Подтверждение                  │
│          │    перевода      │                                   │
│          ▼                   │                                   │
│   ┌─────────────────────────┴─────────────────────────────┐     │
│   │                          НСПК                          │     │
│   │               (Оператор СБП)                          │     │
│   │                                                       │     │
│   │   • Маршрутизация                                     │     │
│   │   • Клиринг                                           │     │
│   │   • Реестр участников                                 │     │
│   │   • API для банков                                    │     │
│   └───────────────────────────────────────────────────────┘     │
│                                                                 │
│   Время исполнения: до 15 секунд (обычно 2-5 сек)               │
│   Лимит C2C: 1 000 000 ₽ за операцию                            │
│   Комиссия C2C: бесплатно до 100 000 ₽/мес                      │
│   Комиссия B2C: 0.4-0.7%                                        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Типы операций СБП:**

| Операция | Описание | Комиссия |
|----------|----------|----------|
| **C2C** | Перевод между физлицами | Бесплатно до лимита |
| **C2B** | Оплата юрлицу | 0.4-0.7% |
| **Me2Me** | Перевод между своими счетами | Бесплатно |
| **QR Static** | Статический QR-код | 0.4-0.7% |
| **QR Dynamic** | Динамический QR-код | 0.4-0.7% |
| **SBPay** | Оплата в интернете | 0.4-0.7% |

**Интеграция СБП для торговцев:**

```python
import requests
from datetime import datetime
import uuid

class SBPMerchantAPI:
    """
    Интеграция с СБП через банк-эквайер.
    """
    
    def __init__(self, bank_url: str, merchant_id: str, api_key: str):
        self.bank_url = bank_url
        self.merchant_id = merchant_id
        self.api_key = api_key
    
    def create_c2b_payment(
        self,
        amount: int,  # в копейках
        order_id: str,
        purpose: str,
        ttl_minutes: int = 60
    ) -> dict:
        """Создание платежа C2B (QR или SBPay)."""
        
        payload = {
            "merchantId": self.merchant_id,
            "amount": amount,
            "currency": "RUB",
            "orderId": order_id,
            "purpose": purpose,
            "ttl": ttl_minutes * 60,
            "redirectUrl": f"https://shop.example.com/callback/{order_id}",
            "paymentMethods": ["QR", "SBPAY"]  # Доступные методы
        }
        
        response = requests.post(
            f"{self.bank_url}/api/v1/payments/sbp/c2b",
            json=payload,
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "X-Request-ID": str(uuid.uuid4()),
                "Content-Type": "application/json"
            }
        )
        
        data = response.json()
        
        return {
            "payment_id": data["paymentId"],
            "qr_url": data.get("qrUrl"),
            "qr_payload": data.get("qrPayload"),
            "sbpay_url": data.get("sbpayUrl"),  # deeplink для SBPay
            "expires_at": data["expiresAt"],
            "status": data["status"]
        }
    
    def get_payment_status(self, payment_id: str) -> dict:
        """Получение статуса платежа."""
        
        response = requests.get(
            f"{self.bank_url}/api/v1/payments/sbp/{payment_id}",
            headers={"Authorization": f"Bearer {self.api_key}"}
        )
        
        data = response.json()
        
        return {
            "payment_id": payment_id,
            "status": data["status"],  # PENDING, PAID, EXPIRED, FAILED
            "paid_at": data.get("paidAt"),
            "payer_bank_name": data.get("payerBankName")
        }
    
    def refund(self, payment_id: str, amount: int = None) -> dict:
        """Возврат платежа (полный или частичный)."""
        
        payload = {"paymentId": payment_id}
        if amount:
            payload["amount"] = amount  # Частичный возврат
        
        response = requests.post(
            f"{self.bank_url}/api/v1/payments/sbp/refund",
            json=payload,
            headers={"Authorization": f"Bearer {self.api_key}"}
        )
        
        return response.json()
```

### 2.3 Цифровой рубль (CBDC)

```
Цифровой рубль — третья форма денег:

┌──────────────────────────────────────────────────────────────────┐
│                     ТРИ ФОРМЫ ДЕНЕГ                               │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│   ┌────────────┐   ┌────────────┐   ┌────────────────────────┐   │
│   │  НАЛИЧНЫЕ  │   │ БЕЗНАЛИЧНЫЕ│   │   ЦИФРОВОЙ РУБЛЬ       │   │
│   │            │   │            │   │                        │   │
│   │ • Купюры   │   │ • Записи   │   │ • Цифровые токены      │   │
│   │ • Монеты   │   │   в банках │   │ • На платформе ЦБ      │   │
│   │            │   │            │   │ • Уникальный номер     │   │
│   │ Эмитент:   │   │ Создают:   │   │ Эмитент: ЦБ РФ         │   │
│   │ ЦБ РФ      │   │ Ком. банки │   │                        │   │
│   └────────────┘   └────────────┘   └────────────────────────┘   │
│                                                                  │
│   Особенности цифрового рубля:                                   │
│   ├── Прямые обязательства ЦБ (как наличные)                     │
│   ├── Офлайн-платежи (в перспективе)                             │
│   ├── Программируемость (целевые расходы)                        │
│   ├── Прозрачность для регулятора                                │
│   └── Работа через банки-посредники                              │
│                                                                  │
│   Timeline:                                                      │
│   2021: Концепция                                                │
│   2022: Прототип                                                 │
│   2023: Пилот с банками                                          │
│   2025+: Масштабирование                                         │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

---

## 3. Китай

### 3.1 UnionPay

**Крупнейшая карточная система мира (по числу карт):**

| Метрика | Значение |
|---------|----------|
| Карт в обращении | 9+ млрд |
| Транзакции в год | 350+ млрд |
| Страны приёма | 180+ |
| Доля рынка в Китае | 95%+ |

**Особенности UnionPay:**

```
UnionPay Card Types:

Classic Series:
├── UnionPay Classic (базовые)
├── UnionPay Gold (средний класс)
├── UnionPay Platinum (премиум)
└── UnionPay Diamond (ультра-премиум)

Technology:
├── EMV chip (QuickPass)
├── NFC contactless
├── UnionPay QR (扫码支付)
└── Mobile Pay (云闪付 - YunShanFu)

Cobadging:
├── UnionPay-Visa (для международных поездок)
├── UnionPay-JCB (Япония)
└── UnionPay-Discover (США)
```

### 3.2 Alipay и WeChat Pay

**Дуополия мобильных платежей:**

```
┌─────────────────────────────────────────────────────────────────┐
│                 КИТАЙСКИЙ РЫНОК МОБИЛЬНЫХ ПЛАТЕЖЕЙ               │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Alipay (支付宝) - Ant Group                                    │
│   ├── 1.3+ млрд пользователей                                   │
│   ├── Интеграция: Taobao, Tmall, Alibaba                        │
│   ├── Финансовые сервисы: Yu'e Bao, кредиты, страхование        │
│   ├── Доля: ~55%                                                │
│   │                                                             │
│   │   Mini-programs                                             │
│   │   ├── Магазины                                              │
│   │   ├── Сервисы доставки                                      │
│   │   ├── Билеты, бронирования                                  │
│   │   └── Коммунальные платежи                                  │
│   │                                                             │
│   WeChat Pay (微信支付) - Tencent                                │
│   ├── 1.2+ млрд пользователей WeChat                            │
│   ├── Интеграция: WeChat мессенджер                             │
│   ├── Hongbao (红包) — красные конверты                          │
│   ├── Доля: ~40%                                                │
│   │                                                             │
│   │   Уникальные функции                                        │
│   │   ├── Платежи в чатах                                       │
│   │   ├── Групповые платежи                                     │
│   │   └── Социальные переводы                                   │
│                                                                 │
│   Остальные (UnionPay Mobile и др.): ~5%                        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 3.3 e-CNY (Цифровой юань)

| Аспект | Детали |
|--------|--------|
| Оператор | People's Bank of China (PBOC) |
| Пилотные города | Shenzhen, Suzhou, Chengdu, Xiongan и др. |
| Кошельки | 260+ млн |
| Транзакции | 100+ млрд юаней |
| Особенности | Офлайн NFC, анонимность малых платежей |

---

## 4. Индия

### 4.1 RuPay

**Национальная карточная система:**

```
RuPay Development:

2012: Запуск NPCI (National Payments Corporation of India)
2013: Первые карты RuPay
2016: Интеграция с Jan Dhan (финансовая инклюзия)
2020: 600+ млн карт
2023: 700+ млн карт, 30%+ доля рынка

Card Types:
├── RuPay Classic
├── RuPay Platinum
├── RuPay Select
├── RuPay Corporate
└── RuPay Prepaid

Technologies:
├── EMV chip
├── NFC (RuPay Contactless)
├── Tokenization
└── UPI integration (RuPay on UPI)
```

### 4.2 UPI — Революция платежей

**Unified Payments Interface — самая быстрорастущая система:**

```
UPI Statistics (2023-2024):

Транзакции:     12+ млрд/месяц (пик)
Объём:          $200+ млрд/месяц
Участники:      400+ банков
Приложения:     PhonePe (47%), Google Pay (34%), Paytm (15%), др.

┌─────────────────────────────────────────────────────────────────┐
│                      UPI ARCHITECTURE                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Payer App                              Payee                  │
│   (PhonePe, GPay)                        (VPA/QR)               │
│        │                                     ▲                  │
│        │ 1. Initiate                        │ 5. Credit         │
│        ▼                                     │                  │
│   ┌─────────────┐                      ┌─────────────┐          │
│   │ Payer PSP   │     2. Authorize     │ Payee PSP   │          │
│   │ (Bank App   │──────────────────────│ (Bank)      │          │
│   │  Provider)  │                      │             │          │
│   └──────┬──────┘                      └──────┬──────┘          │
│          │                                    │                 │
│          │ 3. NPCI Switch                     │ 4. Settlement   │
│          ▼                                    ▼                 │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │                          NPCI                            │   │
│   │   • Transaction routing                                  │   │
│   │   • Dispute resolution                                   │   │
│   │   • Settlement                                           │   │
│   └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│   VPA Format: username@bankhandle                               │
│   Example: john@okicici, shop@ybl                               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

**UPI Features:**

| Feature | Description |
|---------|-------------|
| **VPA** | Virtual Payment Address (не нужен номер счёта) |
| **QR Pay** | Статический и динамический QR |
| **Collect Request** | Запрос платежа от получателя |
| **AutoPay** | Регулярные платежи |
| **UPI Lite** | Офлайн-платежи до ₹200 |
| **UPI 123Pay** | Для feature phones |

### 4.3 Aadhaar и биометрия

```
Aadhaar Enabled Payment System (AePS):

Aadhaar Number (12 цифр) + Биометрия → Платёж

Применение:
├── Снятие наличных без карты
├── Оплата в POS через отпечаток
├── Государственные выплаты (DBT)
└── Финансовая инклюзия для сельского населения

Coverage:
├── 1.4 млрд регистраций
└── 99%+ населения Индии
```

---

## 5. Бразилия

### 5.1 PIX

**Мгновенная платёжная система Центрального банка:**

```
PIX — История успеха:

Ноябрь 2020:  Запуск
Декабрь 2020: 100 млн транзакций
2021:         10 млрд транзакций за год
2023:         3+ млрд транзакций/месяц
              140+ млн пользователей (70% взрослого населения)

┌─────────────────────────────────────────────────────────────────┐
│                        PIX KEYS                                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Типы ключей PIX:                                              │
│   ├── CPF/CNPJ (налоговый номер)                                │
│   ├── Email                                                     │
│   ├── Номер телефона                                            │
│   └── EVP (случайный ключ)                                      │
│                                                                 │
│   Пример:                                                       │
│   Вместо: Banco 001, Agência 1234, Conta 56789-0                │
│   Просто: pix@empresa.com.br                                    │
│                                                                 │
│   Особенности:                                                  │
│   ├── 24/7/365                                                  │
│   ├── Settlement в секунды                                      │
│   ├── Бесплатно для физлиц                                      │
│   ├── До R$500 для юрлиц (дешевле карт)                         │
│   └── QR-коды (статические и динамические)                      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 5.2 Boleto Bancário

**Традиционный бразильский метод:**

```
Boleto Payment Flow:

1. Торговец генерирует Boleto
   └── Штрих-код + данные платежа

2. Покупатель получает Boleto (email/checkout)

3. Покупатель оплачивает:
   ├── В банке
   ├── В лотерейном киоске
   ├── В интернет-банке
   └── В приложении

4. Подтверждение (D+1 до D+3)

Особенности:
├── Не требует карту/счёт (наличными в киоске)
├── Популярен для e-commerce
├── Длинный settlement (1-3 дня)
├── Высокий abandonment rate (30-40%)
└── Риск неоплаты
```

---

## 6. Европа

### 6.1 SEPA

**Single Euro Payments Area:**

| Параметр | SEPA CT | SEPA Instant |
|----------|---------|--------------|
| Время исполнения | D+1 | 10 секунд |
| Лимит | Без лимита | €100,000 |
| Стоимость | Минимальная | Чуть выше |
| Доступность | Бизнес-часы | 24/7/365 |
| Охват | 34 страны | 2,300+ банков |

### 6.2 Локальные A2A методы

```
Локальные методы по странам:

┌─────────────────────────────────────────────────────────────────┐
│  Страна        │ Метод        │ Доля в e-commerce │ Тип        │
├────────────────┼──────────────┼───────────────────┼────────────┤
│ Нидерланды     │ iDEAL        │ 60%+              │ A2A        │
│ Германия       │ Giropay      │ 15%               │ A2A        │
│                │ SOFORT       │ 10%               │ A2A        │
│ Бельгия        │ Bancontact   │ 50%+              │ Card       │
│ Польша         │ BLIK         │ 50%+              │ Mobile     │
│ Швеция         │ Swish        │ 30%               │ Mobile P2P │
│ Финляндия      │ MobilePay    │ 25%               │ Mobile     │
│ Австрия        │ EPS          │ 20%               │ A2A        │
└─────────────────────────────────────────────────────────────────┘
```

**iDEAL (Нидерланды):**

```python
# Пример интеграции iDEAL через Mollie

import mollie

client = mollie.Client()
client.set_api_key("test_xxx")

def create_ideal_payment(amount: str, description: str, redirect_url: str):
    """Создание iDEAL платежа."""
    
    payment = client.payments.create({
        "amount": {
            "currency": "EUR",
            "value": amount  # "10.00"
        },
        "description": description,
        "redirectUrl": redirect_url,
        "method": "ideal",
        "issuer": "ideal_INGBNL2A"  # ING bank или null для выбора
    })
    
    return {
        "payment_id": payment.id,
        "checkout_url": payment.checkout_url,
        "status": payment.status
    }
```

### 6.3 PSD2 и Open Banking

```
PSD2 Impact на платежи:

┌─────────────────────────────────────────────────────────────────┐
│                         PSD2                                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Strong Customer Authentication (SCA):                          │
│  ├── 2 из 3 факторов обязательны                                │
│  │   ├── Knowledge (пароль)                                     │
│  │   ├── Possession (телефон)                                   │
│  │   └── Inherence (биометрия)                                  │
│  │                                                              │
│  │  Исключения:                                                 │
│  │  ├── Транзакции < €30 (до 5 подряд или €100 суммарно)        │
│  │  ├── Trusted beneficiaries (whitelist)                       │
│  │  ├── Recurring (после первого платежа)                       │
│  │  └── Low risk (TRA — Transaction Risk Analysis)              │
│  │                                                              │
│  Open Banking APIs:                                             │
│  ├── AISP — чтение данных счёта                                 │
│  ├── PISP — инициация платежей                                  │
│  └── CBPII — подтверждение наличия средств                      │
│                                                                 │
│  Standards:                                                     │
│  ├── Berlin Group (EU)                                          │
│  ├── UK Open Banking                                            │
│  └── STET (France)                                              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 7. Другие регионы

### 7.1 Африка — Mobile Money

```
M-Pesa и Mobile Money:

┌─────────────────────────────────────────────────────────────────┐
│                    MOBILE MONEY В АФРИКЕ                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Почему Mobile Money?                                           │
│  ├── Низкое проникновение банков                                │
│  ├── Высокое проникновение мобильной связи                      │
│  ├── Агентская сеть для cash-in/cash-out                        │
│  └── Финансовая инклюзия                                        │
│                                                                 │
│  M-Pesa (Kenya, Tanzania):                                      │
│  ├── Запуск: 2007 (Safaricom)                                   │
│  ├── Пользователи: 50+ млн                                      │
│  ├── Транзакции: $300+ млрд/год                                 │
│  └── Модель: агенты + USSD/app                                  │
│                                                                 │
│  Другие игроки:                                                 │
│  ├── Orange Money (West Africa)                                 │
│  ├── MTN Mobile Money (pan-African)                             │
│  ├── Airtel Money (multiple countries)                          │
│  └── EcoCash (Zimbabwe)                                         │
│                                                                 │
│  Interoperability:                                              │
│  └── TIPS Africa, PAPSS (pan-African settlement)                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 7.2 Япония

| Система | Описание |
|---------|----------|
| **JCB** | Национальная карточная ПС, 140+ млн карт |
| **Suica/Pasmo** | Транспортные карты, используемые для платежей |
| **PayPay** | Mobile wallet (SoftBank + Yahoo) |
| **Line Pay** | Интеграция с мессенджером |
| **Наличные** | Всё ещё ~50% транзакций |

### 7.3 Юго-Восточная Азия

```
Платёжные системы ЮВА:

Таиланд:     PromptPay (real-time, QR)
Сингапур:    PayNow, NETS
Индонезия:   QRIS (QR стандарт), GoPay, OVO
Филиппины:   GCash, Maya (ex-PayMaya)
Вьетнам:     MoMo, VNPay
Малайзия:    DuitNow, Touch 'n Go

Interoperability:
├── QR-based cross-border (Singapore-Thailand)
└── ASEAN Payment Connectivity
```

---

## 8. Интеграция для глобального бизнеса

### 8.1 Выбор платёжных методов

```python
from typing import List, Dict
from dataclasses import dataclass

@dataclass
class PaymentMethod:
    name: str
    type: str
    countries: List[str]
    priority: str
    integration_effort: str
    settlement_time: str

def recommend_payment_methods(target_countries: List[str]) -> Dict[str, List[PaymentMethod]]:
    """
    Рекомендация платёжных методов по странам.
    """
    
    methods_db = {
        "RU": [
            PaymentMethod("Cards (МИР)", "card", ["RU"], "essential", "low", "T+1"),
            PaymentMethod("СБП", "a2a", ["RU"], "essential", "medium", "instant"),
            PaymentMethod("SberPay", "wallet", ["RU"], "high", "medium", "instant"),
        ],
        "CN": [
            PaymentMethod("Alipay", "wallet", ["CN"], "essential", "medium", "T+1"),
            PaymentMethod("WeChat Pay", "wallet", ["CN"], "essential", "medium", "T+1"),
            PaymentMethod("UnionPay", "card", ["CN"], "high", "low", "T+1"),
        ],
        "IN": [
            PaymentMethod("UPI", "a2a", ["IN"], "essential", "medium", "instant"),
            PaymentMethod("RuPay", "card", ["IN"], "high", "low", "T+1"),
            PaymentMethod("Paytm", "wallet", ["IN"], "medium", "medium", "instant"),
        ],
        "BR": [
            PaymentMethod("PIX", "a2a", ["BR"], "essential", "medium", "instant"),
            PaymentMethod("Boleto", "voucher", ["BR"], "high", "low", "D+1 to D+3"),
            PaymentMethod("Cards", "card", ["BR"], "high", "low", "T+1"),
        ],
        "NL": [
            PaymentMethod("iDEAL", "a2a", ["NL"], "essential", "medium", "instant"),
            PaymentMethod("Cards", "card", ["NL"], "medium", "low", "T+1"),
        ],
        "DE": [
            PaymentMethod("Cards", "card", ["DE"], "high", "low", "T+1"),
            PaymentMethod("SEPA", "a2a", ["DE"], "high", "medium", "D+1"),
            PaymentMethod("Giropay", "a2a", ["DE"], "medium", "medium", "instant"),
            PaymentMethod("SOFORT", "a2a", ["DE"], "medium", "medium", "instant"),
        ],
    }
    
    recommendations = {}
    
    for country in target_countries:
        country_upper = country.upper()
        if country_upper in methods_db:
            recommendations[country_upper] = methods_db[country_upper]
        else:
            # Fallback: международные карты
            recommendations[country_upper] = [
                PaymentMethod("Visa/Mastercard", "card", ["GLOBAL"], "essential", "low", "T+1"),
                PaymentMethod("PayPal", "wallet", ["GLOBAL"], "medium", "low", "instant"),
            ]
    
    return recommendations

# Использование

countries = ["RU", "DE", "BR", "IN"]
methods = recommend_payment_methods(countries)

for country, payment_methods in methods.items():
    print(f"\n{country}:")
    for pm in payment_methods:
        print(f"  [{pm.priority}] {pm.name} ({pm.type})")
```

### 8.2 Чеклист локализации

```markdown
## Чеклист: Выход на новый рынок

### Исследование

- [ ] Определить top-5 платёжных методов рынка
- [ ] Изучить регуляторные требования
- [ ] Оценить стоимость интеграции
- [ ] Проверить settlement сроки

### Техническая интеграция

- [ ] Выбрать PSP с поддержкой локальных методов
- [ ] Интегрировать обязательные методы (essential)
- [ ] Добавить альтернативы (high priority)
- [ ] Настроить валютные конвертации

### UX адаптация

- [ ] Локализовать checkout на язык рынка
- [ ] Отображать локальную валюту
- [ ] Показывать знакомые лого методов
- [ ] Адаптировать порядок методов под предпочтения

### Compliance

- [ ] Получить необходимые лицензии
- [ ] Настроить локализацию данных (если требуется)
- [ ] Внедрить KYC/AML процессы
- [ ] Обеспечить отчётность регулятору
```

---

## 💡 Key Takeaways

- **Каждый рынок уникален** — универсальных решений не существует
- **Национальные системы растут** — СБП, UPI, PIX показывают путь
- **A2A дешевле карт** — 0.1-0.7% vs 1.5-3%
- **Регуляторика критична** — локализация данных, лицензии, отчётность
- **Mobile money** — решение для emerging markets без банковской инфраструктуры
- **CBDC на горизонте** — цифровой рубль, e-CNY, digital euro
- **Интероперабельность** — QR-стандарты, cross-border initiatives

---

## 🚀 Next Steps

**Следующий модуль:**
- [Криптовалюты и блокчейн](../20_Crypto_Blockchain/) — stablecoins, CBDC, DeFi

**Для углубления:**
- Документация СБП (НСПК)
- UPI Developer Guidelines (NPCI)
- PSD2 Technical Standards (EBA)

**Практика:**
- Изучите PSP, поддерживающие ваши целевые рынки (Adyen, Stripe, PayU)
- Проанализируйте конверсию по методам оплаты в вашем бизнесе

---

## 📚 Additional Resources

**Официальные источники:**
- [НСПК (СБП, МИР)](https://www.nspk.ru/)
- [NPCI (UPI, RuPay)](https://www.npci.org.in/)
- [Banco Central do Brasil (PIX)](https://www.bcb.gov.br/estabilidadefinanceira/pix)
- [European Payments Council (SEPA)](https://www.europeanpaymentscouncil.eu/)

---

