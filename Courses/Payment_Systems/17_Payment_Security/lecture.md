# Безопасность платежей
## PCI DSS, 3-D Secure, Fraud Detection и защита платёжной инфраструктуры

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:
- Понимать жизненный цикл платежа от авторизации до расчётов
- Знать структуру данных банковской карты (PAN, CVV, expiry)
- Быть знакомы с основами веб-безопасности (HTTPS, шифрование)
- Понимать роли участников платёжной системы

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:
- Применять требования PCI DSS к разработке платёжных систем
- Интегрировать 3-D Secure 2.0 в e-commerce приложения
- Проектировать системы fraud detection
- Обеспечивать безопасное хранение и передачу платёжных данных
- Оценивать и снижать риски в платёжной инфраструктуре

---

## 1. PCI DSS

### 1.1 Что такое PCI DSS

**PCI DSS (Payment Card Industry Data Security Standard)** — глобальный стандарт безопасности данных платёжных карт, разработанный PCI Security Standards Council (Visa, Mastercard, AmEx, Discover, JCB).

```
PCI DSS применяется к:

┌─────────────────────────────────────────────────────────────────┐
│                   SCOPE PCI DSS                                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Cardholder Data Environment (CDE)                             │
│   ┌─────────────────────────────────────────────────────────┐   │
│   │                                                         │   │
│   │  • Системы, хранящие PAN                                │   │
│   │  • Системы, обрабатывающие PAN                          │   │
│   │  • Системы, передающие PAN                              │   │
│   │  • Сети, связанные с CDE                                │   │
│   │                                                         │   │
│   └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│   Sensitive Authentication Data (SAD):                          │
│   • CVV/CVC (нельзя хранить после авторизации!)                 │
│   • PIN / PIN block                                             │
│   • Полные данные магнитной полосы                              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 1.2 Кто должен соответствовать

| Организация | Примеры | Требования |
|-------------|---------|------------|
| **Торговцы** | Интернет-магазины, ритейл | Зависит от объёма |
| **Сервис-провайдеры** | PSP, процессоры, хостинг | Всегда высокие |
| **Эмитенты/Эквайеры** | Банки | Полное соответствие |
| **Разработчики** | Платёжное ПО | PA-DSS / PCI SSC |

### 1.3 12 требований PCI DSS

**Группа 1: Построение и поддержка защищённой сети**

| # | Требование | Практика |
|---|------------|----------|
| 1 | Firewall для защиты данных | Сегментация сети, DMZ |
| 2 | Не использовать дефолтные пароли | Смена всех паролей по умолчанию |

**Группа 2: Защита данных держателей карт**

| # | Требование | Практика |
|---|------------|----------|
| 3 | Защита хранимых данных | Шифрование, токенизация |
| 4 | Шифрование при передаче | TLS 1.2+, no SSL 3.0 |

**Группа 3: Управление уязвимостями**

| # | Требование | Практика |
|---|------------|----------|
| 5 | Антивирус | На всех системах |
| 6 | Безопасная разработка | Secure SDLC, code review |

**Группа 4: Контроль доступа**

| # | Требование | Практика |
|---|------------|----------|
| 7 | Ограничение доступа | Need-to-know basis |
| 8 | Уникальные ID пользователей | No shared accounts |
| 9 | Физическая безопасность | Контроль доступа в ЦОД |

**Группа 5: Мониторинг и тестирование**

| # | Требование | Практика |
|---|------------|----------|
| 10 | Логирование и мониторинг | SIEM, audit trails |
| 11 | Тестирование безопасности | Pentest, vuln scanning |

**Группа 6: Политики**

| # | Требование | Практика |
|---|------------|----------|
| 12 | Политики безопасности | Документированные процессы |

### 1.4 Уровни соответствия для торговцев

```
┌─────────────────────────────────────────────────────────────────┐
│              УРОВНИ PCI DSS ДЛЯ ТОРГОВЦЕВ                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Level 1:  > 6 млн транзакций/год                               │
│  ├── Ежегодный аудит QSA (Qualified Security Assessor)          │
│  ├── Квартальное ASV сканирование                               │
│  └── ROC (Report on Compliance)                                 │
│                                                                 │
│  Level 2:  1-6 млн транзакций/год                               │
│  ├── SAQ (Self-Assessment Questionnaire)                        │
│  ├── Квартальное ASV сканирование                               │
│  └── AOC (Attestation of Compliance)                            │
│                                                                 │
│  Level 3:  20K-1 млн e-commerce транзакций/год                  │
│  ├── SAQ                                                        │
│  └── Квартальное ASV сканирование                               │
│                                                                 │
│  Level 4:  < 20K e-commerce или < 1 млн других                  │
│  ├── SAQ (обычно SAQ A для redirect)                            │
│  └── ASV сканирование рекомендуется                             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 1.5 Типы SAQ

| SAQ | Применение | Scope |
|-----|------------|-------|
| SAQ A | Полный redirect на PSP | Минимальный |
| SAQ A-EP | iFrame, но без хранения | Ограниченный |
| SAQ B | Только imprinт-машинки | Минимальный |
| SAQ B-IP | IP-терминалы | Ограниченный |
| SAQ C | Web-based виртуальные терминалы | Средний |
| SAQ C-VT | VT + интернет-соединение | Средний |
| SAQ D | Хранение, обработка PAN | Полный |

### 1.6 Пример снижения PCI Scope

```python
# ❌ ПЛОХО: Данные карты проходят через ваш сервер
# SAQ D, полный PCI scope

@app.post("/api/pay")
def bad_payment(card_number: str, cvv: str, expiry: str):
    # Ваш сервер видит PAN — вы в scope PCI DSS!
    result = payment_processor.charge(
        pan=card_number,
        cvv=cvv,
        expiry=expiry,
        amount=100
    )
    return result

# ✅ ХОРОШО: Токенизация на стороне клиента
# SAQ A или SAQ A-EP, минимальный scope

@app.post("/api/pay")
def good_payment(payment_token: str):
    # Токен от Stripe.js / PayPal / другого PSP
    # Ваш сервер никогда не видит PAN
    result = stripe.PaymentIntent.confirm(
        payment_token,
        amount=10000,  # в копейках
        currency="rub"
    )
    return {"status": result.status}
```

**Архитектура с минимальным scope:**

```
┌─────────────────────────────────────────────────────────────────┐
│                    SAQ A АРХИТЕКТУРА                             │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Browser                                                       │
│   ┌─────────────────┐                                           │
│   │   Stripe.js     │──────────────┐                            │
│   │   (iFrame)      │              │                            │
│   │                 │              │ PAN                        │
│   │   [Card Input]  │              ▼                            │
│   └─────────────────┘        ┌─────────────┐                    │
│          │                   │   Stripe    │                    │
│          │ Payment Token     │   Server    │                    │
│          ▼                   └──────┬──────┘                    │
│   ┌─────────────────┐              │                            │
│   │   Your Server   │◄─────────────┘                            │
│   │                 │  Confirmation                             │
│   │   (No PAN ever!)│                                           │
│   └─────────────────┘                                           │
│                                                                 │
│   Your PCI Scope: Минимальный (только защита токенов)           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 2. 3-D Secure

### 2.1 Что такое 3-D Secure

**3-D Secure** — протокол аутентификации держателя карты для CNP-транзакций (Card Not Present).

**3 домена (3-D):**
1. **Issuer Domain** — эмитент и держатель
2. **Acquirer Domain** — эквайер и торговец
3. **Interoperability Domain** — платёжная система (Directory Server)

```
3-D Secure Flow:

┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐
│ Cardholder│   │ Merchant │   │ MPI/     │   │ Directory│   │  ACS     │
│          │   │ Server   │   │ 3DS Srv  │   │ Server   │   │ (Issuer) │
└────┬─────┘   └────┬─────┘   └────┬─────┘   └────┬─────┘   └────┬─────┘
     │              │              │              │              │
     │ 1. Purchase  │              │              │              │
     │─────────────►│              │              │              │
     │              │              │              │              │
     │              │ 2. Initiate  │              │              │
     │              │─────────────►│              │              │
     │              │              │              │              │
     │              │              │ 3. VeReq     │              │
     │              │              │─────────────►│              │
     │              │              │              │              │
     │              │              │              │ 4. Enrolled? │
     │              │              │              │─────────────►│
     │              │              │              │              │
     │              │              │ 5. VeRes     │◄─────────────│
     │              │              │◄─────────────│              │
     │              │              │              │              │
     │              │ 6. Auth URL  │              │              │
     │              │◄─────────────│              │              │
     │              │              │              │              │
     │ 7. Redirect  │              │              │              │
     │◄─────────────│              │              │              │
     │              │              │              │              │
     │ 8. Challenge │              │              │              │
     │─────────────────────────────────────────────────────────►│
     │              │              │              │              │
     │ 9. OTP/Bio   │              │              │              │
     │◄────────────────────────────────────────────────────────│
     │              │              │              │              │
     │ 10. PARes    │              │              │              │
     │─────────────────────────────────────────────────────────►│
     │              │              │              │              │
     │              │              │ 11. CAVV     │◄─────────────│
     │              │              │◄─────────────│              │
     │              │              │              │              │
```

### 2.2 3-D Secure 1.0 vs 2.0

| Аспект | 3DS 1.0 | 3DS 2.0 |
|--------|---------|---------|
| UX | Pop-up, плохой | Встроенный, хороший |
| Аутентификация | Статический пароль | Биометрия, OTP, push |
| Mobile | Плохо работает | Нативная поддержка |
| Data sharing | Минимум | 100+ data points |
| Frictionless | Нет | Да (Risk-Based Auth) |
| Конверсия | Падение 10-15% | Падение 2-5% |
| SCA (EU) | Не соответствует | Соответствует |

### 2.3 Frictionless vs Challenge Flow

```
3DS 2.0 Decision Flow:

                    ┌─────────────────┐
                    │ AReq received   │
                    │ (Authentication │
                    │  Request)       │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  Risk Analysis  │
                    │  (by Issuer)    │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
              ▼              ▼              ▼
      ┌───────────┐  ┌───────────┐  ┌───────────┐
      │ Low Risk  │  │ Med Risk  │  │ High Risk │
      │           │  │           │  │           │
      │ Frictionless│ │ Challenge │  │  Reject   │
      │ (no action)│  │ (OTP/Bio) │  │ (decline) │
      └───────────┘  └───────────┘  └───────────┘
            │              │              │
            ▼              ▼              ▼
      transStatus=Y  transStatus=C  transStatus=R
```

### 2.4 Интеграция 3DS 2.0

**Сбор данных браузера (Browser Info):**

```javascript
// Данные, отправляемые в 3DS Server
const browserInfo = {
    browserAcceptHeader: navigator.accept || "*/*",
    browserJavaEnabled: navigator.javaEnabled(),
    browserJavascriptEnabled: true,
    browserLanguage: navigator.language,
    browserColorDepth: screen.colorDepth.toString(),
    browserScreenHeight: screen.height.toString(),
    browserScreenWidth: screen.width.toString(),
    browserTZ: new Date().getTimezoneOffset().toString(),
    browserUserAgent: navigator.userAgent
};

// Отправка на сервер
async function initiate3DS(paymentData) {
    const response = await fetch('/api/3ds/initiate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            ...paymentData,
            browserInfo
        })
    });
    
    const result = await response.json();
    
    if (result.transStatus === 'C') {
        // Challenge required
        handle3DSChallenge(result.acsURL, result.creq);
    } else if (result.transStatus === 'Y') {
        // Frictionless success
        completePayment(result.authenticationValue);
    }
}

function handle3DSChallenge(acsURL, creq) {
    // Отображение iframe для challenge
    const iframe = document.createElement('iframe');
    iframe.id = '3ds-challenge';
    iframe.src = acsURL;
    iframe.style.cssText = 'width:400px;height:600px;border:none;';
    
    document.body.appendChild(iframe);
    
    // Отправка CReq в ACS
    iframe.contentWindow.postMessage({
        type: '3DS-challenge',
        creq: creq
    }, acsURL);
}
```

**Server-side 3DS обработка:**

```python
import requests
from dataclasses import dataclass
from typing import Optional

@dataclass
class ThreeDSResult:
    trans_status: str  # Y, N, C, R, U
    authentication_value: Optional[str]  # CAVV/AAV
    eci: Optional[str]  # ECI indicator
    ds_trans_id: str
    acs_url: Optional[str]  # for challenge
    creq: Optional[str]  # challenge request

class ThreeDSService:
    def __init__(self, server_url: str, api_key: str):
        self.server_url = server_url
        self.api_key = api_key
    
    def authenticate(
        self,
        card_token: str,
        amount: int,
        currency: str,
        browser_info: dict
    ) -> ThreeDSResult:
        """
        Инициация 3DS аутентификации.
        """
        
        # Шаг 1: Versioning (определение версии 3DS)
        version_response = self._version_request(card_token)
        
        if not version_response.enrolled:
            # Карта не enrolled в 3DS
            return ThreeDSResult(
                trans_status='U',
                authentication_value=None,
                eci=None,
                ds_trans_id=None,
                acs_url=None,
                creq=None
            )
        
        # Шаг 2: Authentication Request
        auth_response = self._authentication_request(
            card_token=card_token,
            amount=amount,
            currency=currency,
            browser_info=browser_info,
            ds_trans_id=version_response.ds_trans_id
        )
        
        return ThreeDSResult(
            trans_status=auth_response['transStatus'],
            authentication_value=auth_response.get('authenticationValue'),
            eci=auth_response.get('eci'),
            ds_trans_id=auth_response['dsTransID'],
            acs_url=auth_response.get('acsURL'),
            creq=auth_response.get('creq')
        )
    
    def _authentication_request(self, **kwargs) -> dict:
        """Отправка AReq в Directory Server."""
        
        payload = {
            'messageType': 'AReq',
            'messageVersion': '2.2.0',
            'threeDSServerTransID': self._generate_trans_id(),
            'deviceChannel': '02',  # Browser
            'messageCategory': '01',  # Payment
            'purchaseAmount': kwargs['amount'],
            'purchaseCurrency': kwargs['currency'],
            'browserInfo': kwargs['browser_info'],
            # ... дополнительные поля
        }
        
        response = requests.post(
            f"{self.server_url}/v2/authentication",
            json=payload,
            headers={'Authorization': f'Bearer {self.api_key}'}
        )
        
        return response.json()
```

### 2.5 ECI (Electronic Commerce Indicator)

| ECI | Visa | Mastercard | Значение |
|-----|------|------------|----------|
| 05 | ✓ | — | Fully authenticated |
| 06 | ✓ | — | Attempted authentication |
| 07 | ✓ | — | Non-3DS transaction |
| 02 | — | ✓ | Fully authenticated |
| 01 | — | ✓ | Attempted authentication |
| 00 | — | ✓ | Non-3DS transaction |

### 2.6 Liability Shift

```
Liability Shift Rules:

┌─────────────────────────────────────────────────────────────────┐
│                     LIABILITY SHIFT                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  3DS Result          │  Fraud Liability    │  Notes             │
│  ────────────────────┼─────────────────────┼──────────────────  │
│  Fully Auth (ECI 05) │  Issuer             │  Full protection   │
│  Attempted (ECI 06)  │  Issuer             │  Issuer didn't auth│
│  Not Enrolled        │  Merchant*          │  Depends on region │
│  Failed Auth (ECI 07)│  Merchant           │  No protection     │
│  Declined Auth       │  Merchant           │  Should not proceed│
│                                                                 │
│  * В некоторых регионах liability shift даже при "not enrolled" │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 3. Fraud Detection

### 3.1 Типы мошенничества

```
┌─────────────────────────────────────────────────────────────────┐
│                    ТИПЫ PAYMENT FRAUD                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1. TRUE FRAUD (Внешнее мошенничество)                          │
│     ├── Card theft — украденные данные карты                    │
│     ├── Account takeover — взлом аккаунта                       │
│     ├── Identity theft — кража личности                         │
│     ├── Phishing — социальная инженерия                         │
│     └── Card testing — проверка украденных карт                 │
│                                                                 │
│  2. FRIENDLY FRAUD (Первого лица)                               │
│     ├── Buyer's remorse — передумал                             │
│     ├── Family fraud — покупка членом семьи                     │
│     ├── Cyber shoplifting — намеренный chargeback               │
│     └── Subscription abuse — "забыл отменить"                   │
│                                                                 │
│  3. MERCHANT FRAUD                                              │
│     ├── Transaction laundering — отмывание через процессинг     │
│     ├── Bust-out — набор chargebacks перед закрытием            │
│     └── Collusion — сговор с держателем                         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 3.2 Сигналы риска (Risk Signals)

**Категории сигналов:**

```python
from dataclasses import dataclass
from typing import Optional, List
from enum import Enum

class RiskLevel(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

@dataclass
class RiskSignal:
    name: str
    value: any
    risk_level: RiskLevel
    weight: float

@dataclass
class TransactionRiskProfile:
    # Информация о покупателе
    is_new_customer: bool
    customer_age_days: int
    previous_orders: int
    previous_chargebacks: int
    
    # Информация об устройстве
    device_fingerprint: str
    device_first_seen: bool
    device_trust_score: float
    
    # Геолокация
    ip_country: str
    billing_country: str
    shipping_country: str
    is_vpn: bool
    is_tor: bool
    is_datacenter_ip: bool
    
    # Поведение
    time_on_page: float
    checkout_velocity: float
    failed_attempts: int
    session_device_switches: int
    
    # Транзакция
    amount: float
    is_high_risk_mcc: bool
    is_digital_goods: bool

def calculate_risk_signals(profile: TransactionRiskProfile) -> List[RiskSignal]:
    """Расчёт сигналов риска для транзакции."""
    
    signals = []
    
    # Новый клиент с большим заказом
    if profile.is_new_customer and profile.amount > 10000:
        signals.append(RiskSignal(
            name="new_customer_high_value",
            value=profile.amount,
            risk_level=RiskLevel.HIGH,
            weight=0.3
        ))
    
    # Разные страны billing/shipping
    if profile.billing_country != profile.shipping_country:
        signals.append(RiskSignal(
            name="billing_shipping_mismatch",
            value=f"{profile.billing_country}/{profile.shipping_country}",
            risk_level=RiskLevel.MEDIUM,
            weight=0.15
        ))
    
    # VPN/Tor
    if profile.is_vpn or profile.is_tor:
        signals.append(RiskSignal(
            name="anonymizing_proxy",
            value="VPN" if profile.is_vpn else "Tor",
            risk_level=RiskLevel.HIGH,
            weight=0.25
        ))
    
    # Много неудачных попыток
    if profile.failed_attempts > 3:
        signals.append(RiskSignal(
            name="multiple_failed_attempts",
            value=profile.failed_attempts,
            risk_level=RiskLevel.HIGH,
            weight=0.35
        ))
    
    # История chargebacks
    if profile.previous_chargebacks > 0:
        signals.append(RiskSignal(
            name="previous_chargebacks",
            value=profile.previous_chargebacks,
            risk_level=RiskLevel.CRITICAL,
            weight=0.5
        ))
    
    # Datacenter IP (боты)
    if profile.is_datacenter_ip:
        signals.append(RiskSignal(
            name="datacenter_ip",
            value=True,
            risk_level=RiskLevel.HIGH,
            weight=0.3
        ))
    
    return signals
```

### 3.3 Архитектура Fraud Detection System

```
┌─────────────────────────────────────────────────────────────────┐
│                 FRAUD DETECTION SYSTEM                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   Transaction                                                   │
│       │                                                         │
│       ▼                                                         │
│   ┌─────────────────┐                                           │
│   │  Data Enrichment│                                           │
│   │  ├── IP info    │                                           │
│   │  ├── Device FP  │                                           │
│   │  ├── Email score│                                           │
│   │  └── Card BIN   │                                           │
│   └────────┬────────┘                                           │
│            │                                                    │
│            ▼                                                    │
│   ┌─────────────────┐                                           │
│   │   Rules Engine  │                                           │
│   │                 │                                           │
│   │ • Velocity      │                                           │
│   │ • Blacklists    │                                           │
│   │ • Geo rules     │                                           │
│   │ • Amount limits │                                           │
│   └────────┬────────┘                                           │
│            │                                                    │
│            ▼                                                    │
│   ┌─────────────────┐                                           │
│   │   ML Model      │                                           │
│   │                 │                                           │
│   │ • Gradient Boost│                                           │
│   │ • Neural Net    │                                           │
│   │ • Ensemble      │                                           │
│   └────────┬────────┘                                           │
│            │                                                    │
│            ▼                                                    │
│   ┌─────────────────┐                                           │
│   │  Final Decision │                                           │
│   │                 │                                           │
│   │  ┌───────────┐  │                                           │
│   │  │ APPROVE   │  │◄─── Score < 30                            │
│   │  └───────────┘  │                                           │
│   │  ┌───────────┐  │                                           │
│   │  │ 3DS/REVIEW│  │◄─── Score 30-70                           │
│   │  └───────────┘  │                                           │
│   │  ┌───────────┐  │                                           │
│   │  │  DECLINE  │  │◄─── Score > 70                            │
│   │  └───────────┘  │                                           │
│   └─────────────────┘                                           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 3.4 Velocity Checks

```python
from datetime import datetime, timedelta
from redis import Redis

class VelocityChecker:
    def __init__(self, redis: Redis):
        self.redis = redis
    
    def check_velocity(
        self,
        card_token: str,
        email: str,
        ip_address: str,
        device_id: str
    ) -> dict:
        """
        Проверка velocity (частоты) по разным идентификаторам.
        """
        
        now = datetime.now()
        checks = {}
        
        # Транзакции с одной карты за час
        card_key = f"velocity:card:{card_token}:hourly"
        card_count = self._increment_and_get(card_key, ttl=3600)
        checks['card_hourly'] = {
            'count': card_count,
            'limit': 5,
            'exceeded': card_count > 5
        }
        
        # Транзакции с одного IP за час
        ip_key = f"velocity:ip:{ip_address}:hourly"
        ip_count = self._increment_and_get(ip_key, ttl=3600)
        checks['ip_hourly'] = {
            'count': ip_count,
            'limit': 10,
            'exceeded': ip_count > 10
        }
        
        # Уникальные карты с одного устройства за день
        device_card_key = f"velocity:device:{device_id}:cards:daily"
        self.redis.sadd(device_card_key, card_token)
        self.redis.expire(device_card_key, 86400)
        unique_cards = self.redis.scard(device_card_key)
        checks['device_unique_cards'] = {
            'count': unique_cards,
            'limit': 3,
            'exceeded': unique_cards > 3
        }
        
        # Неудачные попытки
        fail_key = f"velocity:email:{email}:failed:hourly"
        failed_count = int(self.redis.get(fail_key) or 0)
        checks['failed_attempts'] = {
            'count': failed_count,
            'limit': 5,
            'exceeded': failed_count > 5
        }
        
        return {
            'checks': checks,
            'any_exceeded': any(c['exceeded'] for c in checks.values())
        }
    
    def _increment_and_get(self, key: str, ttl: int) -> int:
        pipe = self.redis.pipeline()
        pipe.incr(key)
        pipe.expire(key, ttl)
        result = pipe.execute()
        return result[0]
    
    def record_failed_attempt(self, email: str):
        """Запись неудачной попытки."""
        key = f"velocity:email:{email}:failed:hourly"
        self.redis.incr(key)
        self.redis.expire(key, 3600)
```

### 3.5 Device Fingerprinting

```javascript
// Сбор device fingerprint на клиенте
async function collectDeviceFingerprint() {
    const fingerprint = {
        // Экран
        screenResolution: `${screen.width}x${screen.height}`,
        colorDepth: screen.colorDepth,
        pixelRatio: window.devicePixelRatio,
        
        // Timezone
        timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,
        timezoneOffset: new Date().getTimezoneOffset(),
        
        // Браузер
        userAgent: navigator.userAgent,
        language: navigator.language,
        languages: navigator.languages,
        platform: navigator.platform,
        cookiesEnabled: navigator.cookieEnabled,
        doNotTrack: navigator.doNotTrack,
        
        // Capabilities
        touchSupport: 'ontouchstart' in window,
        webglVendor: getWebGLVendor(),
        webglRenderer: getWebGLRenderer(),
        
        // Canvas fingerprint
        canvasHash: await getCanvasFingerprint(),
        
        // Audio fingerprint
        audioHash: await getAudioFingerprint(),
        
        // Fonts
        installedFonts: await detectFonts()
    };
    
    // Генерация хеша
    const hash = await sha256(JSON.stringify(fingerprint));
    
    return {
        hash,
        components: fingerprint
    };
}

function getWebGLVendor() {
    try {
        const canvas = document.createElement('canvas');
        const gl = canvas.getContext('webgl');
        const debugInfo = gl.getExtension('WEBGL_debug_renderer_info');
        return gl.getParameter(debugInfo.UNMASKED_VENDOR_WEBGL);
    } catch {
        return null;
    }
}

async function getCanvasFingerprint() {
    const canvas = document.createElement('canvas');
    const ctx = canvas.getContext('2d');
    
    // Рисуем уникальный текст
    ctx.textBaseline = 'top';
    ctx.font = '14px Arial';
    ctx.fillText('Device fingerprint 🔐', 2, 2);
    
    // Добавляем градиент
    const gradient = ctx.createLinearGradient(0, 0, 100, 0);
    gradient.addColorStop(0, 'red');
    gradient.addColorStop(1, 'blue');
    ctx.fillStyle = gradient;
    ctx.fillRect(0, 20, 100, 50);
    
    return await sha256(canvas.toDataURL());
}
```

---

## 4. Шифрование и защита данных

### 4.1 Данные в покое (At Rest)

```python
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os
import base64

class CardDataEncryption:
    """
    Шифрование данных карт в соответствии с PCI DSS.
    В production используйте HSM!
    """
    
    def __init__(self, master_key: bytes, salt: bytes):
        # Derive encryption key from master key
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=480000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(master_key))
        self.fernet = Fernet(key)
    
    def encrypt_pan(self, pan: str) -> str:
        """Шифрование PAN."""
        return self.fernet.encrypt(pan.encode()).decode()
    
    def decrypt_pan(self, encrypted_pan: str) -> str:
        """Расшифровка PAN (только для авторизованных операций)."""
        return self.fernet.decrypt(encrypted_pan.encode()).decode()
    
    def mask_pan(self, pan: str) -> str:
        """Маскирование PAN для отображения."""
        return f"{pan[:6]}{'*' * (len(pan) - 10)}{pan[-4:]}"

# Правильное хранение в БД

"""
CREATE TABLE payment_methods (
    id UUID PRIMARY KEY,
    customer_id UUID REFERENCES customers(id),
    
    -- Зашифрованные данные (если храните)
    encrypted_pan BYTEA,  -- AES-256 encrypted
    
    -- Или лучше: токен от PSP
    payment_token VARCHAR(255),  -- tok_xxx
    
    -- Безопасно хранить
    last_four VARCHAR(4),
    card_brand VARCHAR(20),
    exp_month INT,
    exp_year INT,
    
    -- НЕ ХРАНИТЬ: CVV, полная магнитная полоса
    
    created_at TIMESTAMP DEFAULT NOW()
);
"""
```

### 4.2 Данные при передаче (In Transit)

```python
# Требования к TLS для PCI DSS

"""
Минимальные требования:
- TLS 1.2 или выше
- Сильные cipher suites
- Правильная цепочка сертификатов
- HSTS headers
"""

# Nginx конфигурация для PCI DSS

NGINX_CONFIG = """
server {
    listen 443 ssl http2;
    server_name payments.example.com;
    
    # Сертификаты
    ssl_certificate /etc/ssl/certs/payments.crt;
    ssl_certificate_key /etc/ssl/private/payments.key;
    
    # Протоколы
    ssl_protocols TLSv1.2 TLSv1.3;
    
    # Cipher suites (PCI DSS compliant)
    ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384;
    ssl_prefer_server_ciphers on;
    
    # HSTS
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
    
    # OCSP Stapling
    ssl_stapling on;
    ssl_stapling_verify on;
}
"""

# Проверка TLS конфигурации

import ssl
import socket

def check_tls_config(hostname: str, port: int = 443) -> dict:
    """Проверка TLS конфигурации сервера."""
    
    context = ssl.create_default_context()
    
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            return {
                'protocol': ssock.version(),
                'cipher': ssock.cipher(),
                'certificate': ssock.getpeercert(),
                'is_pci_compliant': ssock.version() in ('TLSv1.2', 'TLSv1.3')
            }
```

### 4.3 Токенизация

```python
from typing import Optional
import uuid
import hashlib

class TokenizationService:
    """
    Сервис токенизации для снижения PCI scope.
    """
    
    def __init__(self, vault_client):
        self.vault = vault_client
    
    def tokenize(
        self,
        pan: str,
        exp_month: int,
        exp_year: int,
        cvv: str  # Используется только для первой транзакции!
    ) -> dict:
        """
        Токенизация данных карты.
        CVV не сохраняется после авторизации.
        """
        
        # Генерируем уникальный токен
        token = f"tok_{uuid.uuid4().hex}"
        
        # Сохраняем в vault (HSM-protected)
        self.vault.store(
            key=token,
            data={
                'pan': pan,
                'exp_month': exp_month,
                'exp_year': exp_year
                # CVV НЕ сохраняем!
            },
            ttl=None  # Бессрочно или до отзыва
        )
        
        # Возвращаем токен и метаданные
        return {
            'token': token,
            'last_four': pan[-4:],
            'brand': self._detect_brand(pan),
            'exp_month': exp_month,
            'exp_year': exp_year,
            'fingerprint': self._fingerprint(pan)
        }
    
    def detokenize(self, token: str, reason: str) -> Optional[dict]:
        """
        Получение данных карты по токену.
        Только для авторизованных операций!
        """
        
        # Логируем доступ (PCI DSS requirement)
        self._audit_log(token, reason)
        
        return self.vault.retrieve(token)
    
    def _detect_brand(self, pan: str) -> str:
        """Определение бренда карты по BIN."""
        if pan.startswith('4'):
            return 'visa'
        elif pan.startswith(('51', '52', '53', '54', '55')):
            return 'mastercard'
        elif pan.startswith('2'):
            return 'mir'
        elif pan.startswith(('34', '37')):
            return 'amex'
        return 'unknown'
    
    def _fingerprint(self, pan: str) -> str:
        """Создание fingerprint для дедупликации."""
        return hashlib.sha256(f"fp:{pan}".encode()).hexdigest()[:16]
```

---

## 5. Best Practices

### 5.1 Для разработчиков

```markdown
## Security Checklist для Payment Integration

### Никогда не делайте

- ❌ Логировать PAN, CVV, магнитную полосу
- ❌ Хранить CVV после авторизации
- ❌ Передавать PAN в URL parameters
- ❌ Хранить PAN в cookies/localStorage
- ❌ Отображать полный PAN в UI
- ❌ Использовать HTTP (только HTTPS)
- ❌ Использовать собственную криптографию

### Всегда делайте

- ✅ Использовать токенизацию от PSP
- ✅ Валидировать входные данные на сервере
- ✅ Использовать prepared statements (SQL injection)
- ✅ Применять rate limiting
- ✅ Логировать security events
- ✅ Использовать 3-D Secure
- ✅ Проверять webhook signatures
- ✅ Использовать CSP headers
```

### 5.2 Для бизнеса

```markdown
## PCI DSS Compliance Roadmap

### Квартал 1: Assessment

- [ ] Gap analysis текущего состояния
- [ ] Определение scope (что в CDE)
- [ ] Выбор SAQ типа
- [ ] Выбор ASV для сканирования

### Квартал 2: Remediation

- [ ] Устранение выявленных gaps
- [ ] Сегментация сети
- [ ] Обновление политик
- [ ] Обучение персонала

### Квартал 3: Validation

- [ ] Internal testing
- [ ] ASV scan (quarterly)
- [ ] Penetration test (annual)
- [ ] Заполнение SAQ

### Квартал 4: Maintenance

- [ ] Continuous monitoring
- [ ] Incident response drill
- [ ] Policy review
- [ ] Vendor assessment
```

### 5.3 Incident Response

```python
from enum import Enum
from datetime import datetime
from dataclasses import dataclass
from typing import List

class IncidentSeverity(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

@dataclass
class SecurityIncident:
    id: str
    severity: IncidentSeverity
    type: str
    description: str
    affected_cards: int
    detected_at: datetime
    status: str

class IncidentResponsePlan:
    """
    План реагирования на инциденты (PCI DSS Requirement 12.10).
    """
    
    ESCALATION_MATRIX = {
        IncidentSeverity.LOW: ["security_team"],
        IncidentSeverity.MEDIUM: ["security_team", "engineering_lead"],
        IncidentSeverity.HIGH: ["security_team", "cto", "legal"],
        IncidentSeverity.CRITICAL: ["security_team", "cto", "ceo", "legal", "pr"]
    }
    
    def handle_incident(self, incident: SecurityIncident):
        """Обработка инцидента."""
        
        # 1. Containment (сдерживание)
        self._contain_incident(incident)
        
        # 2. Eradication (устранение)
        self._eradicate_threat(incident)
        
        # 3. Notification (уведомление)
        self._notify_stakeholders(incident)
        
        # 4. Documentation (документирование)
        self._document_incident(incident)
        
        # 5. Recovery (восстановление)
        self._recover_systems(incident)
    
    def _contain_incident(self, incident: SecurityIncident):
        """Немедленные меры сдерживания."""
        
        if incident.severity >= IncidentSeverity.HIGH:
            # Блокировка скомпрометированных карт
            self._block_affected_cards(incident.affected_cards)
            
            # Изоляция затронутых систем
            self._isolate_systems()
    
    def _notify_stakeholders(self, incident: SecurityIncident):
        """Уведомление заинтересованных сторон."""
        
        # Внутреннее уведомление
        teams = self.ESCALATION_MATRIX[incident.severity]
        self._notify_internal(teams, incident)
        
        # Уведомление ПС (в течение 24 часов при компрометации)
        if incident.affected_cards > 0:
            self._notify_payment_networks(incident)
        
        # Уведомление регуляторов (если требуется)
        if incident.severity == IncidentSeverity.CRITICAL:
            self._notify_regulators(incident)
```

---

## 💡 Key Takeaways

- **PCI DSS обязателен** для всех, кто работает с картами — используйте токенизацию для снижения scope
- **3-D Secure 2.0** — liability shift + frictionless flow для лучшей конверсии
- **Fraud detection** — комбинация rules + ML + velocity checks
- **Токенизация** — снижает PCI scope, реальный PAN не нужно хранить
- **TLS 1.2+ обязателен** — SSL и старые версии TLS запрещены
- **CVV нельзя хранить** — только для первичной авторизации
- **Incident Response Plan** — обязателен по PCI DSS, тестируйте регулярно

---

## 🚀 Next Steps

**Следующий модуль:**
- [Альтернативные платёжные методы](../18_Alternative_Payments/) — Open Banking, кошельки, QR, P2P

**Для углубления:**
- PCI DSS v4.0 Requirements
- EMV 3-D Secure 2.2 Specification
- Изучите fraud prevention solutions (Sift, Forter, Riskified)

**Практика:**
- Пройдите SAQ A self-assessment
- Настройте 3-D Secure в sandbox вашего PSP
- Изучите dashboard fraud analytics

---

## 📚 Additional Resources

**Официальные документы:**
- [PCI Security Standards Council](https://www.pcisecuritystandards.org/)
- [EMVCo 3-D Secure](https://www.emvco.com/emv-technologies/3d-secure/)

**Инструменты:**
- Qualys SSL Labs — тестирование TLS
- SecurityScorecard — оценка безопасности
- Stripe Radar, Adyen RevenueProtect — fraud prevention

---

