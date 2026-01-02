# Эквайринг
## Торговый и интернет-эквайринг, подключение, комиссии и интеграция

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:
- Понимать четырёхстороннюю модель платежей (эмитент, эквайер, ПС, торговец)
- Знать финансовые потоки и комиссии (interchange, MDR)
- Понимать жизненный цикл транзакции
- Быть знакомы с основами банковских карт

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:
- Объяснять виды эквайринга и их особенности
- Проходить процесс подключения торговца к эквайрингу
- Рассчитывать и оптимизировать комиссии
- Интегрировать платёжные шлюзы в e-commerce
- Оценивать и снижать риски эквайринга

---

## 1. Что такое эквайринг

### 1.1 Определение

**Эквайринг** (от англ. acquire — приобретать) — банковская услуга по приёму безналичных платежей от держателей платёжных карт в пользу торговца.

```
┌─────────────────────────────────────────────────────────────────┐
│                    ЭКОСИСТЕМА ЭКВАЙРИНГА                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Держатель          Торговец          Эквайер         ПС       │
│   карты              (Merchant)        (Acquirer)      (Visa/MC)│
│      │                   │                 │              │     │
│      │ 1. Оплата        │                 │              │     │
│      │   картой         │                 │              │     │
│      ├──────────────────►│                 │              │     │
│      │                   │                 │              │     │
│      │                   │ 2. Авторизация  │              │     │
│      │                   │    через        │              │     │
│      │                   │    терминал     │              │     │
│      │                   ├────────────────►│              │     │
│      │                   │                 │              │     │
│      │                   │                 │ 3. Запрос к ПС     │
│      │                   │                 ├─────────────►│     │
│      │                   │                 │              │     │
│      │                   │                 │ 4. Одобрено  │     │
│      │                   │                 │◄─────────────┤     │
│      │                   │                 │              │     │
│      │                   │ 5. Подтверждено │              │     │
│      │                   │◄────────────────┤              │     │
│      │                   │                 │              │     │
│      │ 6. Товар/услуга  │                 │              │     │
│      │◄──────────────────┤                 │              │     │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 1.2 Роль банка-эквайера

| Функция | Описание |
|---------|----------|
| **Подключение торговцев** | Онбординг, договор, KYC |
| **Предоставление оборудования** | Терминалы, POS-системы |
| **Обработка транзакций** | Авторизация, clearing, settlement |
| **Выплата средств** | Перевод выручки на счёт торговца |
| **Управление рисками** | Мониторинг fraud, chargebacks |
| **Поддержка** | Техническая помощь, обучение |

### 1.3 Банк-эквайер vs Платёжный агрегатор

```
┌─────────────────────────────────────────────────────────────────┐
│           ПРЯМОЙ ЭКВАЙРИНГ vs АГРЕГАТОР                          │
├───────────────────────────────┬─────────────────────────────────┤
│     ПРЯМОЙ ЭКВАЙРИНГ          │      ПЛАТЁЖНЫЙ АГРЕГАТОР        │
│     (Сбербанк, ВТБ)           │      (ЮKassa, CloudPayments)    │
├───────────────────────────────┼─────────────────────────────────┤
│                               │                                 │
│  Торговец ────────► Эквайер   │  Торговец ──► Агрегатор ──► Банк│
│                               │                                 │
│  ✅ Ниже комиссии (1.5-2%)    │  ⚠️ Выше комиссии (2.5-3.5%)    │
│  ✅ Прямой счёт в банке       │  ✅ Быстрое подключение         │
│  ⚠️ Долгий онбординг (недели) │  ✅ Быстрый онбординг (часы)    │
│  ⚠️ Больше документов         │  ✅ Меньше требований           │
│  ⚠️ Сложная интеграция        │  ✅ Готовые SDK и плагины       │
│  ✅ Индивидуальные условия    │  ⚠️ Стандартные условия         │
│                               │                                 │
│  Подходит для:                │  Подходит для:                  │
│  • Крупный бизнес             │  • Стартапы                     │
│  • Высокий оборот             │  • Малый бизнес                 │
│  • Опыт интеграций            │  • Быстрый запуск               │
│                               │                                 │
└───────────────────────────────┴─────────────────────────────────┘
```

---

## 2. Виды эквайринга

### 2.1 Торговый эквайринг (POS)

**Point-of-Sale эквайринг** — приём карт в физических точках продаж.

**Характеристики:**
- Карта физически присутствует (Card Present)
- Чип + PIN или NFC
- Низкий риск мошенничества
- Комиссии ниже, чем в интернете

**Применение:**
- Розничные магазины
- Рестораны и кафе
- Отели
- АЗС
- Транспорт

### 2.2 Интернет-эквайринг (CNP)

**Card-Not-Present эквайринг** — приём карт в интернете.

```
Интернет-эквайринг Flow:

┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐
│ Customer │  │ Merchant │  │ Payment  │  │ Acquirer │  │ Card     │
│          │  │ Website  │  │ Gateway  │  │          │  │ Network  │
└────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘
     │             │             │             │             │
     │ 1. Checkout │             │             │             │
     │────────────►│             │             │             │
     │             │             │             │             │
     │ 2. Card Form│             │             │             │
     │◄────────────│             │             │             │
     │             │             │             │             │
     │ 3. Card Data│             │             │             │
     │────────────►│             │             │             │
     │             │             │             │             │
     │             │ 4. Auth Req │             │             │
     │             │────────────►│             │             │
     │             │             │             │             │
     │             │             │ 5. Process  │             │
     │             │             │────────────►│             │
     │             │             │             │             │
     │             │             │             │ 6. Auth     │
     │             │             │             │────────────►│
     │             │             │             │             │
     │ 7. 3-D Secure (если требуется)         │◄────────────│
     │◄──────────────────────────────────────────────────────│
     │             │             │             │             │
     │ 8. Result   │             │             │             │
     │◄────────────│             │             │             │
```

**Особенности:**
- Выше риск мошенничества
- Требуется 3-D Secure
- Комиссии выше (2.5-3.5%)
- Необходима PCI DSS compliance

### 2.3 Мобильный эквайринг (mPOS)

**Mobile Point-of-Sale** — приём карт через мобильное устройство с ридером.

| Характеристика | Описание |
|----------------|----------|
| **Оборудование** | Смартфон + Bluetooth ридер |
| **Стоимость ридера** | 2 000 - 10 000 ₽ |
| **Комиссии** | 1.8-2.5% |
| **Применение** | Курьеры, такси, рынки |

**Примеры решений:**
- SumUp
- iZettle (PayPal)
- Square
- 2can
- Сбербанк mPOS

### 2.4 Soft POS (Tap-to-Phone)

**Смартфон как терминал** — приём NFC-платежей без дополнительного оборудования.

```
Soft POS Architecture:

┌─────────────────────────────────────────────────────────────────┐
│                       СМАРТФОН ПРОДАВЦА                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   ┌───────────────────────────────────────────────────────┐     │
│   │                    Soft POS App                       │     │
│   │   ┌─────────────┐  ┌─────────────┐  ┌─────────────┐   │     │
│   │   │   Payment   │  │    PIN on   │  │   Receipt   │   │     │
│   │   │    UI       │  │    Glass    │  │   Engine    │   │     │
│   │   └─────────────┘  └─────────────┘  └─────────────┘   │     │
│   └───────────────────────────────────────────────────────┘     │
│                            │                                    │
│   ┌────────────────────────▼────────────────────────────────┐   │
│   │            TEE (Trusted Execution Environment)          │   │
│   │   ┌─────────────────────────────────────────────────┐   │   │
│   │   │   • Secure PIN entry                            │   │   │
│   │   │   • Cryptographic operations                    │   │   │
│   │   │   • Kernel attestation                          │   │   │
│   │   └─────────────────────────────────────────────────┘   │   │
│   └─────────────────────────────────────────────────────────┘   │
│                            │                                    │
│   ┌────────────────────────▼────────────────────────────────┐   │
│   │                    NFC Controller                        │   │
│   │              (EMV Contactless Reader)                    │   │
│   └─────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

Requirements:
├── Android 8.0+ с NFC
├── TEE поддержка
├── Сертификация PCI PTS (для PIN)
└── Сертификация EMV L1/L2/L3
```

---

## 3. Процесс подключения торговца

### 3.1 Этапы онбординга

```
Timeline подключения:

Агрегатор (ЮKassa, CloudPayments):
┌────┬────┬────┬────┬────┬────┬────┐
│ D0 │ D1 │ D2 │ D3 │ D4 │ D5 │ D6 │ ...
│    │    │    │    │    │    │    │
│ Заявка      Проверка  Активация  │
│ + Документы │        │          │
└─────────────┴────────┴──────────┘
              1-3 дня

Прямой эквайринг (банк):
┌────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┐
│ D0 │ D1 │ D2 │ D3 │ D4 │ D5 │ D6 │ D7 │ D8 │ D9 │D10 │D11 │D12 │...
│    │    │    │    │    │    │    │    │    │    │    │    │    │
│ Заявка          Проверка KYC      Договор    Интеграция  Запуск │
└─────────────────────────────────────────────────────────────────┘
                        2-4 недели
```

### 3.2 Документы для подключения

**Для ООО:**
- Устав (с изменениями)
- Решение/Протокол о назначении директора
- Выписка ЕГРЮЛ (свежая)
- Карточка с образцами подписей
- Паспорт директора
- Лицензии (если требуются)
- Финансовая отчётность (для высокого оборота)

**Для ИП:**
- Паспорт
- Свидетельство о регистрации ИП
- Выписка ЕГРИП
- Лицензии (если требуются)

### 3.3 MCC (Merchant Category Code)

**MCC** — четырёхзначный код категории торговца, влияющий на комиссии:

| MCC | Категория | Типичный MDR |
|-----|-----------|--------------|
| 5411 | Супермаркеты | 1.5-1.8% |
| 5812 | Рестораны | 1.8-2.2% |
| 5912 | Аптеки | 1.6-2.0% |
| 5541 | АЗС | 1.2-1.5% |
| 5999 | Прочая розница | 2.0-2.5% |
| 5816 | Цифровые товары | 3.0-4.0% |
| 7995 | Азартные игры | 5.0%+ (high-risk) |

### 3.4 Оценка рисков торговца

```python
from dataclasses import dataclass
from enum import Enum
from typing import Optional

class RiskLevel(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    PROHIBITED = "prohibited"

@dataclass
class MerchantRiskProfile:
    mcc: str
    annual_volume: float
    average_ticket: float
    chargeback_rate: Optional[float]
    years_in_business: int
    is_online: bool
    sells_digital_goods: bool
    has_recurring: bool

def assess_merchant_risk(profile: MerchantRiskProfile) -> dict:
    """
    Оценка риска торговца для эквайринга.
    """
    
    risk_score = 0
    factors = []
    
    # High-risk MCC
    high_risk_mcc = ['7995', '5816', '5967', '4829', '6051']
    if profile.mcc in high_risk_mcc:
        risk_score += 40
        factors.append("High-risk MCC")
    
    # Chargeback rate
    if profile.chargeback_rate:
        if profile.chargeback_rate > 0.01:  # > 1%
            risk_score += 30
            factors.append("High chargeback rate")
        elif profile.chargeback_rate > 0.005:  # > 0.5%
            risk_score += 15
            factors.append("Elevated chargeback rate")
    
    # New business
    if profile.years_in_business < 1:
        risk_score += 15
        factors.append("New business")
    
    # Digital goods + online
    if profile.sells_digital_goods and profile.is_online:
        risk_score += 20
        factors.append("Digital goods (high fraud risk)")
    
    # Recurring payments
    if profile.has_recurring:
        risk_score += 10
        factors.append("Recurring payments model")
    
    # High average ticket
    if profile.average_ticket > 50000:
        risk_score += 10
        factors.append("High average ticket")
    
    # Determine risk level
    if risk_score >= 60:
        risk_level = RiskLevel.HIGH
    elif risk_score >= 30:
        risk_level = RiskLevel.MEDIUM
    else:
        risk_level = RiskLevel.LOW
    
    # MDR adjustment based on risk
    base_mdr = 2.0
    risk_premium = risk_score * 0.02  # +0.02% per risk point
    suggested_mdr = min(base_mdr + risk_premium, 5.0)
    
    return {
        "risk_level": risk_level.value,
        "risk_score": risk_score,
        "factors": factors,
        "suggested_mdr": round(suggested_mdr, 2),
        "requires_reserve": risk_level == RiskLevel.HIGH,
        "reserve_percent": 10 if risk_level == RiskLevel.HIGH else 0
    }

# Пример использования

profile = MerchantRiskProfile(
    mcc="5816",
    annual_volume=5000000,
    average_ticket=500,
    chargeback_rate=0.008,
    years_in_business=2,
    is_online=True,
    sells_digital_goods=True,
    has_recurring=True
)

risk = assess_merchant_risk(profile)
print(f"Risk Level: {risk['risk_level']}")
print(f"Suggested MDR: {risk['suggested_mdr']}%")
print(f"Factors: {', '.join(risk['factors'])}")
```

---

## 4. Терминалы и оборудование

### 4.1 Типы POS-терминалов

```
┌─────────────────────────────────────────────────────────────────┐
│                    ТИПЫ POS-ТЕРМИНАЛОВ                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  СТАЦИОНАРНЫЙ                                                   │
│  ┌─────────────┐                                                │
│  │   [====]    │  • Ethernet/GPRS подключение                   │
│  │   [    ]    │  • Принтер чеков встроен                       │
│  │   [1234]    │  • Для касс магазинов                          │
│  │   [5678]    │  • Ingenico, Verifone, PAX                     │
│  │   [    ]    │                                                │
│  └─────────────┘                                                │
│                                                                 │
│  МОБИЛЬНЫЙ (GPRS/Wi-Fi)                                         │
│  ┌─────────────┐                                                │
│  │   [====]    │  • Аккумулятор                                 │
│  │   [1234]    │  • Для ресторанов, доставки                    │
│  │   [5678]    │  • GPRS + Wi-Fi                                │
│  └─────────────┘  • Ingenico Move, Verifone V240m               │
│                                                                 │
│  mPOS (Bluetooth ридер)                                         │
│  ┌───────┐                                                      │
│  │ [  ]  │ + 📱  • Подключается к смартфону                     │
│  └───────┘       • Для малого бизнеса                           │
│                  • SumUp, iZettle, Square                       │
│                                                                 │
│  SMART POS (Android-based)                                      │
│  ┌─────────────┐                                                │
│  │   📱🖥️      │  • Полноценный Android                         │
│  │   [====]    │  • Приложения, аналитика                       │
│  │   [    ]    │  • PAX A920, Ingenico AXIUM                    │
│  │   [1234]    │  • Интеграция с кассовым ПО                    │
│  └─────────────┘                                                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 4.2 Интеграция с кассовым ПО

```
Интеграция терминала и кассы:

┌────────────────┐           ┌────────────────┐
│   Кассовое ПО  │  1. Сумма │  POS-терминал  │
│   (1C, iiko)   │──────────►│                │
│                │           │   ┌──────────┐ │
│                │  2. Чек   │   │ Читаем   │ │
│                │◄──────────│   │ карту    │ │
│                │           │   └──────────┘ │
│   ┌──────────┐ │           │                │
│   │ Фиск.    │ │           │   ┌──────────┐ │
│   │ чек      │ │           │   │Связь с   │ │
│   └──────────┘ │           │   │эквайером │ │
│                │           │   └──────────┘ │
└────────────────┘           └────────────────┘

Протоколы интеграции:
├── ECR (Electronic Cash Register) — классический
├── SPDH (Smart POS Direct Host) — современный
├── Nexo — европейский стандарт
└── Proprietary (Ingenico TLV, Verifone API)
```

### 4.3 EMV Configuration

```
EMV терминальные параметры:

Application Identifier (AID):
├── Visa:       A0000000031010
├── Mastercard: A0000000041010
├── МИР:        A0000006580101
└── UnionPay:   A000000333010101

Terminal Type:
├── 22 — Attended, online only
├── 23 — Attended, offline + online
└── 24 — Unattended, online only

Terminal Capabilities:
├── Manual key entry
├── Magnetic stripe
├── ICC (chip)
└── Contactless
```

---

## 5. Комиссии эквайринга

### 5.1 Структура MDR

**MDR (Merchant Discount Rate)** — комиссия, удерживаемая с торговца.

```
MDR Breakdown:

┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   MDR = Interchange + Scheme Fee + Acquirer Margin             │
│                                                                 │
│   Пример для транзакции 10 000 ₽:                               │
│                                                                 │
│   ┌───────────────────────────────────────────────────────┐     │
│   │                      MDR 2.0%                         │     │
│   │                     (200 ₽)                           │     │
│   │  ┌─────────────┬────────────┬────────────────────┐    │     │
│   │  │ Interchange │ Scheme Fee │   Acquirer Margin  │    │     │
│   │  │   1.4%      │   0.15%    │       0.45%        │    │     │
│   │  │  (140 ₽)    │  (15 ₽)    │      (45 ₽)        │    │     │
│   │  │             │            │                    │    │     │
│   │  │  → Эмитенту │ → Visa/MC  │    → Эквайеру     │    │     │
│   │  └─────────────┴────────────┴────────────────────┘    │     │
│   └───────────────────────────────────────────────────────┘     │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 5.2 Interchange в России

| Категория | Дебетовые | Кредитные |
|-----------|-----------|-----------|
| Супермаркеты | 1.0-1.2% | 1.2-1.5% |
| Рестораны | 1.2-1.4% | 1.4-1.7% |
| Отели | 1.3-1.5% | 1.5-1.8% |
| E-commerce | 1.5-1.8% | 1.8-2.2% |

### 5.3 Модели ценообразования

```python
from enum import Enum
from dataclasses import dataclass
from typing import List

class PricingModel(Enum):
    BLENDED = "blended"
    IC_PLUS = "ic_plus"
    IC_PLUS_PLUS = "ic_plus_plus"

@dataclass
class Transaction:
    amount: float
    card_type: str  # "debit", "credit", "corporate"
    is_international: bool
    is_online: bool

def calculate_mdr(
    transaction: Transaction,
    pricing_model: PricingModel,
    blended_rate: float = 2.0,
    acquirer_margin: float = 0.5,
    scheme_fee: float = 0.15
) -> dict:
    """
    Расчёт комиссии в зависимости от модели ценообразования.
    """
    
    # Определяем interchange
    interchange_rates = {
        ("debit", False, False): 1.0,
        ("debit", False, True): 1.3,
        ("credit", False, False): 1.4,
        ("credit", False, True): 1.8,
        ("corporate", False, False): 1.8,
        ("corporate", False, True): 2.0,
    }
    
    key = (
        transaction.card_type,
        transaction.is_international,
        transaction.is_online
    )
    interchange = interchange_rates.get(key, 1.5)
    
    # International surcharge
    if transaction.is_international:
        interchange += 0.5
        scheme_fee += 0.1
    
    if pricing_model == PricingModel.BLENDED:
        # Единая ставка
        mdr = blended_rate
        components = {"blended": blended_rate}
        
    elif pricing_model == PricingModel.IC_PLUS:
        # Interchange + фиксированная маржа
        mdr = interchange + acquirer_margin
        components = {
            "interchange": interchange,
            "acquirer_margin": acquirer_margin
        }
        
    elif pricing_model == PricingModel.IC_PLUS_PLUS:
        # Полная прозрачность
        mdr = interchange + scheme_fee + acquirer_margin
        components = {
            "interchange": interchange,
            "scheme_fee": scheme_fee,
            "acquirer_margin": acquirer_margin
        }
    
    fee = transaction.amount * (mdr / 100)
    net_amount = transaction.amount - fee
    
    return {
        "pricing_model": pricing_model.value,
        "mdr_percent": round(mdr, 2),
        "fee_amount": round(fee, 2),
        "net_amount": round(net_amount, 2),
        "components": {k: round(v, 2) for k, v in components.items()}
    }

# Сравнение моделей

tx = Transaction(amount=10000, card_type="credit", is_international=False, is_online=True)

for model in PricingModel:
    result = calculate_mdr(tx, model)
    print(f"\n{model.value}:")
    print(f"  MDR: {result['mdr_percent']}%")
    print(f"  Fee: {result['fee_amount']} ₽")
    print(f"  Components: {result['components']}")
```

### 5.4 Дополнительные комиссии

| Комиссия | Размер (Россия) | Комментарий |
|----------|-----------------|-------------|
| Аренда терминала | 500-3000 ₽/мес | Можно купить свой |
| Подключение | 0-10 000 ₽ | Часто бесплатно |
| Минимальная комиссия | 15-30 ₽ | За маленькие транзакции |
| Chargeback fee | 1000-3000 ₽ | За каждый chargeback |
| Refund fee | 0-1% | Иногда бесплатно |
| International | +0.5-1% | За международные карты |

---

## 6. Интернет-эквайринг и интеграция

### 6.1 Платёжные шлюзы

```
┌─────────────────────────────────────────────────────────────────┐
│                    ПЛАТЁЖНЫЕ ШЛЮЗЫ                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  РОССИЙСКИЕ:                                                    │
│  ├── ЮKassa (ex-Яндекс.Касса)                                   │
│  │   └── 2.8-3.5%, интеграция с Яндекс-экосистемой              │
│  ├── CloudPayments                                              │
│  │   └── 2.5-3.0%, современный API                              │
│  ├── Robokassa                                                  │
│  │   └── 3.0-3.5%, агрегация многих методов                     │
│  ├── PayKeeper                                                  │
│  │   └── 2.7-3.2%, фокус на B2B                                 │
│  └── Банковские (Сбербанк, Тинькофф)                            │
│      └── 1.5-2.5%, прямая интеграция                            │
│                                                                 │
│  МЕЖДУНАРОДНЫЕ:                                                 │
│  ├── Stripe                                                     │
│  │   └── 2.9% + $0.30, лучший Developer Experience              │
│  ├── Adyen                                                      │
│  │   └── IC++, enterprise-grade                                 │
│  ├── Braintree (PayPal)                                         │
│  │   └── 2.9% + $0.30, интеграция с PayPal                      │
│  └── Checkout.com                                               │
│      └── IC++, low latency                                      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 6.2 Типы интеграции

**1. Redirect (Hosted Payment Page):**

```python
# Пример redirect-интеграции с ЮKassa

from yookassa import Configuration, Payment
import uuid

Configuration.account_id = "YOUR_SHOP_ID"
Configuration.secret_key = "YOUR_SECRET_KEY"

def create_payment_redirect(amount: float, order_id: str, return_url: str) -> str:
    """Создание платежа с редиректом на страницу ЮKassa."""
    
    payment = Payment.create({
        "amount": {
            "value": str(amount),
            "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": return_url
        },
        "capture": True,
        "description": f"Заказ #{order_id}",
        "metadata": {
            "order_id": order_id
        }
    }, uuid.uuid4())
    
    return payment.confirmation.confirmation_url

# Использование

checkout_url = create_payment_redirect(
    amount=1500.00,
    order_id="ORDER-12345",
    return_url="https://shop.example.com/payment/success"
)
print(f"Redirect to: {checkout_url}")
```

**2. Embedded (iFrame/Widget):**

```html
<!-- CloudPayments Widget -->
<script src="https://widget.cloudpayments.ru/bundles/cloudpayments.js"></script>

<button onclick="pay()">Оплатить</button>

<script>
function pay() {
    var widget = new cp.CloudPayments();
    widget.pay('charge', {
        publicId: 'YOUR_PUBLIC_ID',
        description: 'Оплата заказа #12345',
        amount: 1500.00,
        currency: 'RUB',
        accountId: 'user@email.com',
        invoiceId: 'ORDER-12345',
        skin: 'modern'
    }, {
        onSuccess: function(options) {
            console.log('Оплата успешна!');
            window.location.href = '/success';
        },
        onFail: function(reason, options) {
            console.log('Ошибка оплаты:', reason);
        }
    });
}
</script>
```

**3. Direct API (Server-to-Server):**

```python
import requests
import base64
from typing import Optional

class DirectPaymentAPI:
    """Прямая интеграция с API для tokenized payments."""
    
    def __init__(self, api_key: str, merchant_id: str):
        self.api_key = api_key
        self.merchant_id = merchant_id
        self.base_url = "https://api.payment-provider.com/v1"
    
    def charge(
        self,
        token: str,  # Токен от карточной формы
        amount: int,  # В копейках
        order_id: str,
        three_ds_data: Optional[dict] = None
    ) -> dict:
        """
        Списание средств по токену карты.
        """
        
        payload = {
            "merchant_id": self.merchant_id,
            "payment_token": token,
            "amount": amount,
            "currency": "RUB",
            "order_id": order_id,
            "capture": True,  # Сразу списать (не hold)
            "description": f"Payment for order {order_id}"
        }
        
        if three_ds_data:
            payload["three_ds"] = three_ds_data
        
        response = requests.post(
            f"{self.base_url}/payments",
            json=payload,
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
                "X-Idempotency-Key": order_id
            }
        )
        
        result = response.json()
        
        if result.get("status") == "requires_action":
            # Нужна 3-D Secure аутентификация
            return {
                "status": "requires_3ds",
                "acs_url": result["redirect"]["url"],
                "payment_id": result["id"]
            }
        
        return {
            "status": result["status"],
            "payment_id": result["id"],
            "captured_amount": result.get("captured_amount")
        }
```

### 6.3 Webhook обработка

```python
from flask import Flask, request, jsonify
import hmac
import hashlib

app = Flask(__name__)
WEBHOOK_SECRET = "your_webhook_secret"

@app.route('/webhooks/payment', methods=['POST'])
def handle_payment_webhook():
    """Обработка webhook от платёжной системы."""
    
    # 1. Проверка подписи
    signature = request.headers.get('X-Signature')
    payload = request.data
    
    expected_signature = hmac.new(
        WEBHOOK_SECRET.encode(),
        payload,
        hashlib.sha256
    ).hexdigest()
    
    if not hmac.compare_digest(signature, expected_signature):
        return jsonify({"error": "Invalid signature"}), 401
    
    # 2. Обработка события
    event = request.json
    
    if event['type'] == 'payment.succeeded':
        order_id = event['data']['metadata']['order_id']
        amount = event['data']['amount']['value']
        
        # Обновить статус заказа
        update_order_status(order_id, 'paid', amount)
        
        # Отправить подтверждение клиенту
        send_confirmation_email(order_id)
        
    elif event['type'] == 'payment.failed':
        order_id = event['data']['metadata']['order_id']
        reason = event['data']['cancellation_details']['reason']
        
        # Обработать неудачу
        update_order_status(order_id, 'failed', reason=reason)
        
    elif event['type'] == 'refund.succeeded':
        # Обработать возврат
        pass
    
    return jsonify({"status": "ok"}), 200
```

---

## 7. Риски и управление

### 7.1 Риски для эквайера

```
┌─────────────────────────────────────────────────────────────────┐
│                    РИСКИ ЭКВАЙРИНГА                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  КРЕДИТНЫЙ РИСК                                                 │
│  ├── Торговец обанкротился, chargebacks не покрыты              │
│  ├── Торговец исчез с деньгами                                  │
│  └── Митигация: резервирование, мониторинг, underwriting        │
│                                                                 │
│  FRAUD RISK                                                     │
│  ├── Украденные карты используются у торговца                   │
│  ├── Transaction laundering                                     │
│  └── Митигация: fraud monitoring, velocity checks               │
│                                                                 │
│  COMPLIANCE RISK                                                │
│  ├── Нарушение правил ПС                                        │
│  ├── Санкции регулятора                                         │
│  └── Митигация: KYC, мониторинг, аудит                          │
│                                                                 │
│  OPERATIONAL RISK                                               │
│  ├── Сбои в процессинге                                         │
│  ├── Data breach                                                │
│  └── Митигация: DR/BC planning, security                        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 7.2 Программы мониторинга ПС

| Программа | Порог | Последствия |
|-----------|-------|-------------|
| **Visa VFMP** | Fraud >100bp | Штрафы, мониторинг |
| **Visa VDMP** | CB >0.9% или >100/мес | $25K-100K/мес |
| **MC ECMP** | CB >1.5% или >100/мес | Штрафы, отключение |
| **MC BRAM** | High-risk мерчанты | Усиленный мониторинг |

### 7.3 Reserve (обеспечительный депозит)

```python
def calculate_reserve_requirements(
    monthly_volume: float,
    chargeback_rate: float,
    business_type: str,
    is_high_risk: bool
) -> dict:
    """
    Расчёт требований к резерву.
    """
    
    base_reserve_pct = 0
    
    # По типу бизнеса
    if is_high_risk:
        base_reserve_pct = 10
    elif business_type in ['travel', 'subscriptions']:
        base_reserve_pct = 5
    
    # По chargeback rate
    if chargeback_rate > 0.02:  # > 2%
        base_reserve_pct = max(base_reserve_pct, 20)
    elif chargeback_rate > 0.01:  # > 1%
        base_reserve_pct = max(base_reserve_pct, 10)
    
    reserve_amount = monthly_volume * (base_reserve_pct / 100)
    
    return {
        "reserve_percent": base_reserve_pct,
        "reserve_amount": round(reserve_amount, 2),
        "hold_period_days": 180 if is_high_risk else 90,
        "release_schedule": "rolling" if is_high_risk else "fixed"
    }
```

---

## 💡 Key Takeaways

- **Эквайринг** — услуга банка по приёму карточных платежей для торговцев
- **Виды**: торговый (POS), интернет (CNP), мобильный (mPOS), Soft POS
- **MDR = Interchange + Scheme Fee + Acquirer Margin** — типично 1.5-3.5%
- **Агрегаторы быстрее, прямой эквайринг дешевле** — выбор зависит от стадии бизнеса
- **3-D Secure обязателен для онлайна** — liability shift и защита от fraud
- **MCC влияет на комиссии** — high-risk категории платят больше
- **Reserve требуется для high-risk** — защита эквайера от chargebacks

---

## 🚀 Next Steps

**Следующий модуль:**
- [Процессинг и банки](../11_Processing_Banks/) — роли эмитента и эквайера, процессинговые центры

**Для углубления:**
- Изучите документацию ЮKassa / CloudPayments API
- Получите тестовый аккаунт в sandbox
- Проанализируйте структуру MDR вашего бизнеса

**Практика:**
- Интегрируйте payment widget на тестовый сайт
- Настройте обработку webhooks
- Изучите dashboard эквайера/агрегатора

---

## 📚 Additional Resources

**API документация:**
- [ЮKassa API](https://yookassa.ru/developers)
- [CloudPayments API](https://developers.cloudpayments.ru/)
- [Stripe Docs](https://stripe.com/docs)

**Стандарты:**
- EMV Terminal Specifications
- PCI DSS Requirements

---

