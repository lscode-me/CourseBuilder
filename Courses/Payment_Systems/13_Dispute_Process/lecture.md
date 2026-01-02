# Процесс диспута: шаг за шагом
## От претензии клиента до арбитража платёжной системы

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:
- Понимать, что такое chargeback и его причины
- Знать роли участников платёжной цепочки (эмитент, эквайер, ПС)
- Понимать reason codes основных платёжных систем
- Быть знакомы с жизненным циклом транзакции

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:
- Описывать каждый этап процесса диспута от претензии до арбитража
- Понимать временные рамки и дедлайны на каждом этапе
- Формировать compelling evidence для representment
- Оценивать шансы на успешное оспаривание
- Принимать решения о целесообразности арбитража

---

## 1. Обзор процесса диспута

### 1.1 Полная схема диспута

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          ЖИЗНЕННЫЙ ЦИКЛ ДИСПУТА                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   Транзакция     Претензия      1st Chargeback    Representment             │
│   совершена      клиента        (возврат денег)   (ответ торговца)          │
│       │              │                │                │                    │
│       ▼              ▼                ▼                ▼                    │
│   ┌───────┐     ┌─────────┐      ┌─────────┐      ┌─────────┐               │
│   │ T + 0 │────►│ T + 1-90│─────►│T + 2-120│─────►│  +30-45 │               │
│   │ дней  │     │  дней   │      │  дней   │      │   дней  │               │
│   └───────┘     └─────────┘      └─────────┘      └────┬────┘               │
│                                                        │                    │
│                                      ┌─────────────────┴─────────────────┐  │
│                                      ▼                                   ▼  │
│                               Принят эмитентом                    Отклонён  │
│                               (диспут закрыт)                          │    │
│                                                                        ▼    │
│                                                              ┌─────────────┐│
│                                                              │ Pre-Arb /   ││
│                                                              │ 2nd CB      ││
│                                                              └──────┬──────┘│
│                                                                     │       │
│                                                        ┌────────────┴─────┐ │
│                                                        ▼                  ▼ │
│                                                   Принять          Арбитраж │
│                                                   (закрыть)       (ПС решает)│
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 1.2 Участники процесса

| Участник | Роль в диспуте |
|----------|----------------|
| **Держатель карты** | Инициирует претензию, предоставляет информацию |
| **Эмитент** | Принимает заявление, создаёт chargeback, защищает клиента |
| **Платёжная система** | Маршрутизирует сообщения, арбитраж, устанавливает правила |
| **Эквайер** | Получает chargeback, передаёт торговцу, представляет ответ |
| **Торговец** | Отвечает на chargeback, предоставляет доказательства |

### 1.3 Типы исходов

```
Возможные исходы диспута:

1. Торговец принимает chargeback
   └─► Деньги остаются у клиента
   └─► Диспут закрыт

2. Representment успешен
   └─► Деньги возвращаются торговцу
   └─► Эмитент может принять или продолжить

3. Pre-Arbitration / 2nd Chargeback
   └─► Эмитент не согласен с representment
   └─► Новый раунд доказательств

4. Арбитраж
   └─► Платёжная система принимает решение
   └─► Проигравший платит комиссию ($300-500)

5. Compliance Case (редко)
   └─► Сложные случаи вне стандартного процесса
```

---

## 2. Этап 1: Претензия клиента

### 2.1 Как клиент инициирует диспут

**Каналы обращения:**
- Звонок в банк
- Мобильное приложение банка
- Интернет-банк
- Письменное заявление
- Чат поддержки

**Типичное заявление клиента:**

```
Пример заявления:

Дата: 15.01.2024
Транзакция: 5 000 ₽, Магазин "ABC Online", 10.01.2024

Причина оспаривания:
☐ Не совершал данную операцию (fraud)
☑ Товар не получен
☐ Товар отличается от описания
☐ Услуга не оказана
☐ Двойное списание
☐ Отменил подписку, но списание продолжается
☐ Другое: ________________

Дополнительная информация:
"Заказал товар 10.01.2024, срок доставки был 5 рабочих дней.
По состоянию на 15.01.2024 товар не получен, трекинг не обновляется."

Подпись клиента: _______________
```

### 2.2 Проверка эмитентом

Перед созданием chargeback эмитент проверяет:

```
Checklist эмитента:

1. Идентификация транзакции
   ├── Найти транзакцию по дате, сумме, MCC
   └── Сопоставить с заявлением клиента

2. Проверка сроков
   ├── 120 дней от транзакции (стандарт)
   └── Исключения: подписки, отложенная доставка

3. Уточнение у клиента
   ├── Обращался ли к торговцу?
   └── Есть ли документы?

4. Первичный анализ
   ├── Очевидное мошенничество?
   └── История клиента (частые споры?)

5. Попытка решить без chargeback
   ├── Связь с торговцом напрямую
   └── Retrieval Request (опционально)
```

### 2.3 Retrieval Request (запрос информации)

Перед chargeback эмитент может отправить **Retrieval Request** — запрос дополнительной информации у торговца.

```
Retrieval Request Flow:

Эмитент ──── Retrieval Request ────► Эквайер ────► Торговец
    │                                                 │
    │            Response (документы)                 │
    ◄─────────────────────────────────────────────────┘
    │
    ▼
Решение: Chargeback или закрытие претензии
```

**Пример Retrieval Request:**

| Поле | Значение |
|------|----------|
| ARN | 74123456789012345678901 |
| Transaction Date | 2024-01-10 |
| Amount | 5000.00 RUB |
| Reason | Copy of Sales Draft Requested |
| Response Due | 2024-01-25 (15 дней) |

---

## 3. Этап 2: First Chargeback

### 3.1 Создание Chargeback

Если претензия обоснована, эмитент создаёт First Chargeback:

```
Chargeback Message (упрощённо):

┌─────────────────────────────────────────────────────────────┐
│ Message Type: First Chargeback                              │
├─────────────────────────────────────────────────────────────┤
│ ARN:              74123456789012345678901                   │
│ Transaction Date: 2024-01-10                                │
│ Chargeback Date:  2024-01-16                                │
│ Amount:           5000.00 RUB                               │
│ Reason Code:      13.1 (Merchandise Not Received)           │
│ Card Number:      4276****9012                              │
│ Merchant Name:    ABC ONLINE SHOP                           │
│ MCC:              5411                                      │
│                                                             │
│ Documentation:    Cardholder Statement attached             │
│ Response Due:     2024-02-15 (30 days)                      │
└─────────────────────────────────────────────────────────────┘
```

### 3.2 Reason Codes

**Visa Reason Codes (основные):**

| Code | Категория | Описание |
|------|-----------|----------|
| 10.4 | Fraud | Другая мошенническая транзакция |
| 10.5 | Fraud | Visa Fraud Monitoring Program |
| 11.1 | Authorization | Card Recovery Bulletin |
| 12.1 | Processing | Late Presentment |
| 12.4 | Processing | Incorrect Account Number |
| 12.5 | Processing | Incorrect Amount |
| 12.6 | Processing | Duplicate Processing |
| 13.1 | Consumer | Merchandise Not Received |
| 13.2 | Consumer | Cancelled Recurring Transaction |
| 13.3 | Consumer | Not as Described |
| 13.7 | Consumer | Cancelled Merchandise/Services |

**Mastercard Reason Codes (основные):**

| Code | Категория | Описание |
|------|-----------|----------|
| 4837 | Fraud | No Cardholder Authorization |
| 4840 | Fraud | Fraudulent Processing of Transaction |
| 4853 | Consumer | Cardholder Dispute |
| 4855 | Consumer | Goods or Services Not Provided |
| 4859 | Consumer | Addendum, No-show, or ATM Dispute |
| 4863 | Consumer | Cardholder Does Not Recognize |

### 3.3 Передача Chargeback

```
Маршрут Chargeback:

Эмитент ─────► Платёжная система ─────► Эквайер ─────► Торговец
                    │                       │              │
                    │                       │              ▼
                    │                       │         Уведомление
                    │                       │         в личном кабинете
                    │                       │         или email
                    │                       ▼
                    │                  Деньги списаны
                    │                  с расчётного счёта
                    ▼
               Финансовый клиринг
               (изменение settlement)
```

### 3.4 Что получает торговец

**Уведомление о Chargeback:**

```json
{
  "notification_type": "chargeback",
  "chargeback_id": "CB-2024-001234",
  "original_transaction": {
    "transaction_id": "TXN-2024-567890",
    "date": "2024-01-10T14:30:00Z",
    "amount": 5000.00,
    "currency": "RUB"
  },
  "chargeback_details": {
    "reason_code": "13.1",
    "reason_description": "Merchandise/Services Not Received",
    "chargeback_amount": 5000.00,
    "chargeback_date": "2024-01-16",
    "response_deadline": "2024-02-15"
  },
  "cardholder_statement": "Товар не получен, трекинг не обновляется",
  "arn": "74123456789012345678901"
}
```

---

## 4. Этап 3: Representment

### 4.1 Решение торговца

Торговец должен принять решение:

```
Дерево решений:

Получен Chargeback
        │
        ▼
┌───────────────────────┐
│ Есть ли доказательства│
│ в пользу торговца?    │
└───────────┬───────────┘
            │
     ┌──────┴──────┐
     ▼             ▼
    Да            Нет
     │             │
     ▼             ▼
┌─────────┐   ┌─────────────┐
│ Оценить │   │   Принять   │
│ сумму и │   │  Chargeback │
│ win rate│   └─────────────┘
└────┬────┘
     │
     ▼
┌─────────────────────────────┐
│ Сумма × Win Rate > Затраты? │
└─────────────┬───────────────┘
              │
       ┌──────┴──────┐
       ▼             ▼
      Да            Нет
       │             │
       ▼             ▼
┌────────────┐  ┌─────────────┐
│Representment│  │   Принять   │
│  (оспорить)│  │  Chargeback │
└────────────┘  └─────────────┘
```

### 4.2 Compelling Evidence

**Требуемые доказательства по типу dispute:**

**Reason Code 13.1: Merchandise Not Received**

```
Обязательные документы:
├── Proof of Delivery
│   ├── Tracking number с подтверждением доставки
│   ├── Подпись получателя (если есть)
│   └── Фото доставки (если есть)
│
├── Shipping Information
│   ├── Дата отправки
│   ├── Адрес доставки (совпадает с billing/shipping)
│   └── Перевозчик
│
└── Transaction Information
    ├── Описание товара
    ├── Invoice / Order confirmation
    └── Переписка с клиентом
```

**Reason Code 10.4: Fraud (EMV Liability Shift)**

```
Обязательные документы:
├── EMV Cryptogram
│   └── Подтверждение chip-транзакции
│
├── 3-D Secure Data (для CNP)
│   ├── ECI indicator
│   ├── CAVV/AAV
│   └── Дата аутентификации
│
├── Device Fingerprint
│   ├── IP address
│   ├── Device ID
│   └── Browser/OS info
│
└── Prior Transactions
    └── История успешных покупок с того же устройства
```

**Reason Code 13.3: Not as Described**

```
Обязательные документы:
├── Product Description
│   ├── Оригинальное описание на сайте
│   ├── Фото товара
│   └── Спецификации
│
├── Terms & Conditions
│   └── Политика возврата
│
├── Customer Communication
│   └── Переписка до и после покупки
│
└── Return Policy Compliance
    └── Клиент не воспользовался процедурой возврата
```

### 4.3 Формат Representment

**Сопроводительное письмо (пример):**

```
REPRESENTMENT LETTER

Date: 2024-01-25
Case ID: CB-2024-001234
ARN: 74123456789012345678901
Original Transaction: 2024-01-10, 5000.00 RUB
Reason Code: 13.1 - Merchandise Not Received

Dear Dispute Resolution Team,

We respectfully submit this representment in response to the 
chargeback filed on the above-referenced transaction.

SUMMARY:
The cardholder claims non-receipt of merchandise. However, our 
records indicate successful delivery.

EVIDENCE SUBMITTED:
1. Tracking confirmation (Exhibit A)
   - Carrier: DHL Express
   - Tracking: 1234567890
   - Delivery Date: 2024-01-15
   - Signature: Obtained
   
2. Delivery photo (Exhibit B)
   - Timestamp: 2024-01-15 14:32:00 MSK
   
3. Order confirmation (Exhibit C)
   - Sent to: customer@email.com
   - Date: 2024-01-10

CONCLUSION:
The merchandise was delivered to the cardholder's address with 
confirmed signature. We request reversal of this chargeback.

Sincerely,
[Merchant Name]
Dispute Department
```

### 4.4 API для Representment

**Пример отправки через PSP API:**

```python
import requests
import base64

def submit_representment(chargeback_id: str, evidence: dict) -> dict:
    """
    Отправка representment через API платёжного провайдера.
    """
    
    # Подготовка документов
    documents = []
    for doc in evidence.get('files', []):
        with open(doc['path'], 'rb') as f:
            documents.append({
                'name': doc['name'],
                'type': doc['type'],
                'content': base64.b64encode(f.read()).decode()
            })
    
    payload = {
        'chargeback_id': chargeback_id,
        'representment': {
            'response_type': 'DISPUTE',  # или 'ACCEPT'
            'reason': evidence.get('reason'),
            'narrative': evidence.get('letter'),
            'documents': documents,
            'amount': evidence.get('amount'),  # если частичное
        }
    }
    
    response = requests.post(
        'https://api.psp.com/v1/chargebacks/representment',
        json=payload,
        headers={
            'Authorization': f'Bearer {API_KEY}',
            'Content-Type': 'application/json'
        }
    )
    
    return response.json()

# Пример использования

evidence = {
    'reason': 'Товар доставлен, есть подтверждение',
    'letter': 'Representment letter text...',
    'files': [
        {'name': 'tracking.pdf', 'path': '/docs/tracking.pdf', 'type': 'PROOF_OF_DELIVERY'},
        {'name': 'invoice.pdf', 'path': '/docs/invoice.pdf', 'type': 'INVOICE'}
    ]
}

result = submit_representment('CB-2024-001234', evidence)
print(f"Representment submitted: {result['status']}")
```

---

## 5. Этап 4: Pre-Arbitration / Second Chargeback

### 5.1 Когда возникает

Если эмитент не согласен с representment:

```
Сценарии Pre-Arbitration:

1. Доказательства недостаточны
   └─► Эмитент считает, что документы не опровергают претензию

2. Новые аргументы клиента
   └─► Клиент предоставил дополнительную информацию

3. Процедурные нарушения
   └─► Торговец нарушил правила representment

4. Принципиальная позиция
   └─► Эмитент защищает клиента независимо от доказательств
```

### 5.2 Процесс Pre-Arbitration

```
Pre-Arbitration Flow:

Эмитент
    │
    ▼
┌─────────────────────────┐
│ Pre-Arb / 2nd Chargeback│
│ + Дополнительные        │
│   аргументы             │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│      Торговец           │
│                         │
│  Варианты:              │
│  1. Принять (закрыть)   │
│  2. Идти в арбитраж     │
└───────────┬─────────────┘
            │
     ┌──────┴──────┐
     ▼             ▼
  Принять      Арбитраж
     │             │
     ▼             ▼
  Диспут       Filing +
  закрыт       Fee deposit
```

### 5.3 Решение о арбитраже

**Калькуляция целесообразности:**

```python
def should_go_to_arbitration(
    chargeback_amount: float,
    evidence_strength: str,  # 'strong', 'medium', 'weak'
    arbitration_fee: float = 500
) -> dict:
    """
    Оценка целесообразности арбитража.
    """
    
    # Win rates по силе доказательств (примерные)
    win_rates = {
        'strong': 0.70,
        'medium': 0.40,
        'weak': 0.15
    }
    
    win_rate = win_rates.get(evidence_strength, 0.40)
    
    # Expected value
    expected_win = chargeback_amount * win_rate
    expected_loss = arbitration_fee * (1 - win_rate)
    expected_value = expected_win - expected_loss
    
    # Break-even analysis
    break_even_amount = arbitration_fee / win_rate
    
    decision = expected_value > 0
    
    return {
        'recommended_action': 'ARBITRATION' if decision else 'ACCEPT',
        'win_rate': win_rate,
        'expected_value': round(expected_value, 2),
        'break_even_amount': round(break_even_amount, 2),
        'analysis': {
            'chargeback_amount': chargeback_amount,
            'arbitration_fee': arbitration_fee,
            'expected_win': round(expected_win, 2),
            'expected_loss': round(expected_loss, 2)
        }
    }

# Примеры

print(should_go_to_arbitration(10000, 'strong'))
# {'recommended_action': 'ARBITRATION', 'expected_value': 6850.0, ...}

print(should_go_to_arbitration(1000, 'weak'))
# {'recommended_action': 'ACCEPT', 'expected_value': -275.0, ...}
```

---

## 6. Этап 5: Арбитраж

### 6.1 Процесс арбитража

```
Arbitration Flow:

┌─────────────────────────────────────────────────────────────────┐
│                       АРБИТРАЖ                                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1. Filing                                                      │
│     └─► Одна сторона подаёт заявление на арбитраж               │
│     └─► Депозит комиссии ($300-500)                             │
│                                                                 │
│  2. Documentation Review                                        │
│     └─► ПС собирает все документы от обеих сторон               │
│     └─► Проверка соблюдения правил                              │
│                                                                 │
│  3. Decision                                                    │
│     └─► Арбитр ПС принимает решение                             │
│     └─► Обычно 30-60 дней                                       │
│                                                                 │
│  4. Outcome                                                     │
│     ├─► В пользу торговца: деньги возвращаются                  │
│     │   └─► Эмитент платит комиссию                             │
│     └─► В пользу эмитента: деньги остаются у клиента            │
│         └─► Торговец платит комиссию                            │
│                                                                 │
│  5. Appeal (редко)                                              │
│     └─► Compliance case в особых обстоятельствах                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 6.2 Комиссии арбитража

| Платёжная система | Стандартная комиссия | Ускоренный процесс |
|-------------------|----------------------|-------------------|
| Visa | $500 | $900 |
| Mastercard | $300-500 | $500+ |
| American Express | $450 | — |

### 6.3 Статистика арбитража

```
Статистика исходов арбитража (примерные данные):

В пользу торговца:
├── При сильных доказательствах: 65-75%
├── При средних доказательствах: 35-45%
└── При слабых доказательствах: 10-20%

В пользу эмитента:
├── При явном мошенничестве: 80%+
├── При отсутствии доказательств торговца: 70%+
└── При процедурных нарушениях: 60%+

Среднее время рассмотрения:
├── Visa: 45-60 дней
└── Mastercard: 30-45 дней
```

---

## 7. Временные рамки

### 7.1 Полная timeline

```
TIMELINE ДИСПУТА (типичный сценарий)

Day 0:      Транзакция совершена
            │
Day 1-90:   Клиент обнаруживает проблему и обращается в банк
            │
Day 90:     ────── Deadline для претензии клиента ──────
            │
Day 91-120: Эмитент создаёт First Chargeback
            │
Day 120:    ────── Deadline для First Chargeback ──────
            │
            ▼
Day 121:    Торговец получает Chargeback
            │
            +30-45 дней
            │
Day 151-166: ────── Deadline для Representment ──────
            │
            ▼
Day 167:    Эмитент рассматривает
            │
            +30 дней
            │
Day 197:    ────── Deadline для Pre-Arbitration ──────
            │
            ▼
Day 198-227: Торговец рассматривает Pre-Arb
            │
            +10-30 дней
            │
Day 227:    ────── Deadline для Arbitration Filing ──────
            │
            ▼
            +30-60 дней
            │
Day 287:    Решение арбитража
```

### 7.2 Критические дедлайны

| Этап | Deadline | Последствия пропуска |
|------|----------|---------------------|
| First Chargeback | 120 дней от транзакции | Право на chargeback утрачено |
| Representment | 30-45 дней от CB | Chargeback принят автоматически |
| Pre-Arb Response | 30 дней | Pre-Arb принят автоматически |
| Arbitration Filing | 10-30 дней | Право на арбитраж утрачено |

---

## 8. Win Rate и факторы успеха

### 8.1 Статистика по типам диспутов

```
Win Rate по категориям (Representment):

Fraud Disputes:
├── С 3-D Secure: 60-70% (liability shift)
├── Без 3-D Secure: 20-30%
└── EMV chip: 50-60%

Service Disputes:
├── Merchandise Not Received: 40-50% (при наличии tracking)
├── Not as Described: 30-40%
└── Cancelled Services: 35-45%

Processing Errors:
├── Duplicate: 70-80% (легко доказать)
├── Wrong Amount: 60-70%
└── Expired Card: 50-60%
```

### 8.2 Факторы, влияющие на успех

| Фактор | Влияние | Описание |
|--------|---------|----------|
| **Качество доказательств** | Высокое | Tracking с подписью vs "отправлено" |
| **Своевременность ответа** | Высокое | Ответ в первые 7 дней vs за день до дедлайна |
| **Правильный reason code response** | Среднее | Ответ должен соответствовать reason code |
| **История торговца** | Среднее | Низкий chargeback rate помогает |
| **Сумма транзакции** | Низкое | Не влияет на решение напрямую |
| **Тип бизнеса** | Низкое | High-risk MCC может влиять косвенно |

### 8.3 Типичные ошибки

```
❌ Распространённые ошибки в representment:

1. Пропуск дедлайна
   └─► Автоматический проигрыш

2. Неполные доказательства
   └─► Tracking без подтверждения доставки

3. Несоответствие reason code
   └─► Ответ на 13.1 документами для 10.4

4. Нечитаемые документы
   └─► Сканы плохого качества

5. Отсутствие compelling narrative
   └─► Только документы без объяснения

6. Эмоциональный тон
   └─► "Клиент лжёт" вместо фактов

7. Игнорирование правил ПС
   └─► Неправильный формат, лишние документы
```

---

## 9. Автоматизация управления диспутами

### 9.1 Dispute Management System

```
┌─────────────────────────────────────────────────────────────────┐
│                 DISPUTE MANAGEMENT SYSTEM                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────┐   ┌─────────────┐   ┌─────────────┐           │
│  │  Chargeback │   │   Evidence  │   │  Response   │           │
│  │   Alerts    │──►│  Collection │──►│  Generation │           │
│  └─────────────┘   └─────────────┘   └─────────────┘           │
│         │                 │                 │                   │
│         ▼                 ▼                 ▼                   │
│  ┌─────────────┐   ┌─────────────┐   ┌─────────────┐           │
│  │   Webhook   │   │   Document  │   │   Template  │           │
│  │  Processing │   │   Storage   │   │   Engine    │           │
│  └─────────────┘   └─────────────┘   └─────────────┘           │
│         │                 │                 │                   │
│         └─────────────────┼─────────────────┘                   │
│                           ▼                                     │
│                   ┌─────────────┐                               │
│                   │  Analytics  │                               │
│                   │  Dashboard  │                               │
│                   └─────────────┘                               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 9.2 Webhook обработка

```python
from datetime import datetime, timedelta
from typing import Optional
from dataclasses import dataclass
from enum import Enum

class DisputeStatus(Enum):
    NEW = "new"
    EVIDENCE_NEEDED = "evidence_needed"
    READY_FOR_RESPONSE = "ready_for_response"
    SUBMITTED = "submitted"
    WON = "won"
    LOST = "lost"

@dataclass
class Dispute:
    id: str
    transaction_id: str
    amount: float
    reason_code: str
    received_at: datetime
    deadline: datetime
    status: DisputeStatus
    evidence: list

class DisputeManager:
    
    def handle_chargeback_webhook(self, payload: dict) -> Dispute:
        """Обработка входящего chargeback."""
        
        dispute = Dispute(
            id=payload['chargeback_id'],
            transaction_id=payload['original_transaction']['transaction_id'],
            amount=payload['chargeback_details']['chargeback_amount'],
            reason_code=payload['chargeback_details']['reason_code'],
            received_at=datetime.now(),
            deadline=datetime.fromisoformat(
                payload['chargeback_details']['response_deadline']
            ),
            status=DisputeStatus.NEW,
            evidence=[]
        )
        
        # Автоматический сбор доказательств
        dispute = self._collect_evidence(dispute)
        
        # Оценка и приоритизация
        priority = self._calculate_priority(dispute)
        
        # Уведомление команды
        self._notify_team(dispute, priority)
        
        return dispute
    
    def _collect_evidence(self, dispute: Dispute) -> Dispute:
        """Автоматический сбор доказательств из систем."""
        
        # Получаем данные о транзакции
        transaction = self.get_transaction(dispute.transaction_id)
        
        evidence = []
        
        # Добавляем чек/инвойс
        if transaction.invoice_url:
            evidence.append({
                'type': 'INVOICE',
                'url': transaction.invoice_url
            })
        
        # Добавляем данные доставки
        if transaction.tracking_number:
            shipping_info = self.shipping_service.get_tracking(
                transaction.tracking_number
            )
            evidence.append({
                'type': 'PROOF_OF_DELIVERY',
                'tracking': shipping_info
            })
        
        # Добавляем данные аутентификации
        if transaction.three_ds_data:
            evidence.append({
                'type': '3DS_AUTHENTICATION',
                'eci': transaction.three_ds_data.eci,
                'cavv': transaction.three_ds_data.cavv
            })
        
        dispute.evidence = evidence
        dispute.status = (
            DisputeStatus.READY_FOR_RESPONSE 
            if evidence 
            else DisputeStatus.EVIDENCE_NEEDED
        )
        
        return dispute
    
    def _calculate_priority(self, dispute: Dispute) -> str:
        """Расчёт приоритета диспута."""
        
        days_to_deadline = (dispute.deadline - datetime.now()).days
        
        if days_to_deadline <= 3:
            return 'CRITICAL'
        elif days_to_deadline <= 7:
            return 'HIGH'
        elif dispute.amount > 10000:
            return 'HIGH'
        elif days_to_deadline <= 14:
            return 'MEDIUM'
        else:
            return 'LOW'
```

---

## 10. Best Practices

### 10.1 Для торговцев

```markdown
## Чеклист управления диспутами

### Профилактика

- [ ] Используйте 3-D Secure для всех CNP-транзакций
- [ ] Чёткое описание товаров и условий
- [ ] Легкодоступная контактная информация
- [ ] Прозрачная политика возврата
- [ ] Распознаваемое имя в выписке (descriptor)

### При получении Chargeback

- [ ] Зарегистрируйте в системе немедленно
- [ ] Проверьте reason code
- [ ] Соберите все релевантные документы
- [ ] Оцените шансы на успех
- [ ] Примите решение (оспаривать/принять) в течение 7 дней

### Representment

- [ ] Следуйте требованиям к документам для reason code
- [ ] Напишите чёткое сопроводительное письмо
- [ ] Отправьте за 5+ дней до дедлайна
- [ ] Сохраните копию всех отправленных документов

### После результата

- [ ] Анализируйте причины выигранных/проигранных
- [ ] Обновляйте процессы на основе анализа
- [ ] Отслеживайте chargeback rate (< 1%)
```

### 10.2 Метрики для мониторинга

| Метрика | Целевое значение | Действие при превышении |
|---------|------------------|------------------------|
| Chargeback Rate | < 0.65% (Visa), < 1% (MC) | Срочный аудит и улучшение |
| Representment Win Rate | > 40% | Улучшить качество доказательств |
| Response Time | < 7 дней | Автоматизировать сбор |
| Dispute Resolution Time | < 60 дней | Оптимизировать процесс |
| Cost per Dispute | < 50% суммы | Пересмотреть стратегию |

---

## 💡 Key Takeaways

- **Процесс многоэтапный**: претензия → chargeback → representment → pre-arb → арбитраж
- **Сроки критичны**: пропуск любого дедлайна = автоматический проигрыш
- **Representment — право торговца**: но требует качественных доказательств
- **Win rate зависит от доказательств**: tracking с подписью лучше, чем "отправлено"
- **Арбитраж дорогой** ($300-500): только для крупных сумм с сильными доказательствами
- **Автоматизация необходима**: при объёме >50 disputes/месяц
- **Профилактика дешевле лечения**: 3-D Secure, чёткий descriptor, хороший сервис

---

## 🚀 Next Steps

**Следующий модуль:**
- [Защита от диспутов](../14_Dispute_Protection/) — предотвращение chargebacks, мониторинг, fraud detection

**Для углубления:**
- Visa Core Rules (раздел Dispute Resolution)
- Mastercard Chargeback Guide
- Практика representment с вашим PSP

**Практика:**
- Изучите dashboard вашего эквайера/PSP для диспутов
- Создайте шаблоны representment для топ-5 reason codes

---

## 📚 Additional Resources

**Документация платёжных систем:**
- [Visa Dispute Management Guidelines](https://usa.visa.com/support/merchant/library/)
- [Mastercard Chargeback Guide](https://www.mastercard.com/chargeback-guide/)

**Инструменты:**
- Chargebacks911, Midigator — платформы управления диспутами
- Ethoca, Verifi — предотвращение через alerts

---

