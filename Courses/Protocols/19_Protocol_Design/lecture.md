# Как проектировать протоколы
## Минимализм, Explicit over implicit, Версионирование, Backward compatibility, Документация

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать характеристики хороших протоколов (модуль 18)
- Иметь опыт работы с различными протоколами
- Понимать концепции из всех предыдущих модулей

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Применять принципы минимализма при проектировании протоколов
- Проектировать явные и недвусмысленные протоколы
- Реализовывать версионирование и обратную совместимость
- Создавать качественную документацию протоколов

---

## 1. Введение: процесс проектирования

**Проектирование протокола** — итеративный процесс:
1. Определение требований
2. Выбор базовых характеристик
3. Дизайн структуры сообщений
4. Обработка ошибок
5. Версионирование
6. Документация
7. Тестирование и итерация

В этом модуле мы рассмотрим ключевые принципы каждого этапа.

---

## 2. Минимализм

### 2.1 Принцип

**Минимализм:** Включайте только то, что необходимо. Не добавляйте "на будущее".

**YAGNI (You Aren't Gonna Need It):** Если функциональность не нужна сейчас, не добавляйте её.

### 2.2 Определение минимального набора

**Вопросы:**

1. Какая минимальная информация нужна для операции?
2. Какие операции действительно необходимы?
3. Можно ли объединить операции?

**Пример: User API**

**Избыточно:**
```
GET /users
GET /users/:id
GET /users/:id/profile
GET /users/:id/profile/full
GET /users/:id/profile/short
GET /users/search
GET /users/filter
```

**Минимально:**
```
GET /users?id=:id&fields=name,email
```

Один endpoint с параметрами покрывает все случаи.

### 2.3 Когда добавлять features

**Правило:** Добавляйте только когда есть **реальная потребность**.

**Индикаторы потребности:**

- Множественные запросы пользователей
- Workarounds в клиентском коде
- Performance проблемы, которые решает feature

**Не добавляйте если:**

- "Может пригодиться"
- "Другие API так делают"
- "Для полноты"

---

## 3. Explicit over Implicit

### 3.1 Принцип

**Explicit over implicit:** Всё должно быть явно, без неявных предположений.

### 3.2 Явные имена

**Плохо (неявно):**
```json
{"u": 123, "n": "John", "s": 1}
```

**Хорошо (явно):**
```json
{"user_id": 123, "name": "John", "status": "active"}
```

### 3.3 Явные типы

**Плохо (неявно):**
```json
{"created": "2024-01-15"}  // Дата? Время? Timezone?
```

**Хорошо (явно):**
```json
{"created_at": "2024-01-15T10:00:00Z"}  // ISO 8601, UTC
```

### 3.4 Явные единицы измерения

**Плохо:**
```json
{"timeout": 5}  // Секунды? Миллисекунды?
```

**Хорошо:**
```json
{"timeout_ms": 5000}  // Явно миллисекунды
```

или

```json
{"timeout": {"value": 5, "unit": "seconds"}}
```

### 3.5 Явные defaults

**Документируйте defaults явно:**
```
Field "limit":
  Type: integer
  Required: no
  Default: 10
  Range: 1-100
```

---

## 4. Версионирование

### 4.1 Зачем версионировать

**Причины:**

- Изменения могут быть breaking
- Нужна обратная совместимость
- Постепенная миграция клиентов

### 4.2 Стратегии версионирования

**URL versioning:**
```
/api/v1/users
/api/v2/users
```

**Преимущества:**

- Явно
- Легко маршрутизировать
- Видно в логах

**Недостатки:**

- URL меняется
- Может привести к дублированию кода

**Header versioning:**
```
GET /api/users
Accept: application/vnd.myapi.v2+json
```

**Преимущества:**

- URL стабильный
- Более RESTful

**Недостатки:**

- Менее явно
- Сложнее тестировать в браузере

### 4.3 Semantic versioning

**Format:** MAJOR.MINOR.PATCH

- **MAJOR:** Breaking changes

- **MINOR:** New features (backward compatible)

- **PATCH:** Bug fixes

**Пример:**
```
v1.0.0 → v1.1.0 (добавлено поле, compatible)
v1.1.0 → v2.0.0 (удалено поле, breaking)
```

### 4.4 Deprecation

**Процесс:**

1. Объявить deprecated в документации
2. Добавить warning в API ответах
3. Установить deadline для удаления
4. Удалить после deadline

**Пример:**
```
Deprecated: This endpoint will be removed on 2025-01-01.
Use /api/v2/users instead.
```

---

## 5. Backward Compatibility

### 5.1 Правила обратной совместимости

**Можно (безопасно):**

- Добавлять опциональные поля
- Добавлять новые endpoints
- Добавлять новые значения enum (с осторожностью)

**Нельзя (breaking):**

- Удалять поля
- Переименовывать поля
- Менять типы полей
- Менять семантику операций

### 5.2 Добавление полей

**Правило:** Новые поля — опциональные.

**Версия 1:**
```json
{"id": 123, "name": "John"}
```

**Версия 2 (compatible):**
```json
{"id": 123, "name": "John", "email": "john@example.com"}
```

Старые клиенты игнорируют `email`.

### 5.3 Изменение типов

**Плохо (breaking):**
```json
// v1
{"user_id": "123"}

// v2
{"user_id": 123}  // Тип изменился!
```

**Хорошо:**
```json
// v1
{"user_id": "123"}

// v2
{"user_id": "123", "user_id_numeric": 123}
```

Добавлено новое поле, старое сохранено.

### 5.4 Graceful degradation

**Принцип:** Старые клиенты продолжают работать с новым сервером.

**Пример:**
```
Клиент v1 → Сервер v2
Сервер возвращает v2 response с новыми полями
Клиент v1 игнорирует новые поля, работает с известными
```

---

## 6. Документация

### 6.1 Что документировать

**Обязательно:**

- Описание протокола
- Формат сообщений
- Поля: типы, обязательность, defaults
- Примеры запросов и ответов
- Коды ошибок
- Версионирование

**Желательно:**

- Rate limits
- Authentication
- Best practices
- FAQ

### 6.2 OpenAPI (Swagger)

**Пример:**
```yaml
openapi: 3.0.0
info:
  title: User API
  version: 1.0.0

paths:
  /users/{id}:
    get:
      summary: Get user by ID
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: integer
      responses:
        '200':
          description: User found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
        '404':
          description: User not found

components:
  schemas:
    User:
      type: object
      required:

        - id
        - name
      properties:
        id:
          type: integer
        name:
          type: string
        email:
          type: string
          format: email
```

### 6.3 Примеры

**Включайте примеры:**

- Успешных запросов
- Ошибочных запросов
- Edge cases

**Пример:**
```markdown
## Get User

### Request
```http
GET /api/users/123
Authorization: Bearer token123

```
### Response (Success)
```json
{
  "id": 123,
  "name": "John Doe",
  "email": "john@example.com"
}

```
### Response (Not Found)
```json
{
  "error": "User not found",
  "user_id": 123
}

```
```

### 6.4 Changelog

**Ведите changelog для всех версий:**

```markdown
## v2.0.0 (2024-02-01)
### Breaking Changes

- Removed field `phone` from User

### Added

- Added field `email` to User

### Fixed

- Fixed timezone handling in `created_at`

## v1.1.0 (2024-01-15)
### Added

- Added endpoint GET /users/search
```

---

## 7. Тестирование

### 7.1 Типы тестов

**Unit tests:**

- Парсинг сообщений
- Валидация полей
- Сериализация/десериализация

**Integration tests:**

- Полный цикл запрос-ответ
- Обработка ошибок
- Timeout handling

**Compatibility tests:**

- Старый клиент + новый сервер
- Новый клиент + старый сервер

### 7.2 Тестирование обратной совместимости

```python
def test_backward_compatibility():
    # v1 client
    response = old_client.get_user(123)
    assert response['id'] == 123
    assert 'name' in response
    # Игнорируем новые поля v2
    
    # v2 client
    response = new_client.get_user(123)
    assert response['id'] == 123
    assert 'name' in response
    assert 'email' in response  # Новое поле v2
```

### 7.3 Contract testing

**Contract tests:** Проверяют, что API соответствует контракту.

**Инструменты:**

- Pact (consumer-driven contract testing)
- Spring Cloud Contract
- OpenAPI validators

---

## 8. Итеративный процесс

### 8.1 MVP протокола

**Начните с минимального протокола:**

1. Определите core functionality
2. Реализуйте минимальный набор операций
3. Соберите feedback
4. Итерируйте

### 8.2 Beta версии

**Beta протокол:**

- Пометить как beta/experimental
- Собрать feedback от ранних adopters
- Внести изменения (breaking допустимы в beta)
- Стабилизировать в v1.0

### 8.3 Эволюция

**Планируйте эволюцию:**

- Extensibility points
- Версионирование с первого дня
- Deprecated warnings

---

## 9. Checklist проектирования

### 9.1 Before implementation

- [ ] Определены требования
- [ ] Выбраны базовые характеристики (stateful/stateless, sync/async)
- [ ] Спроектирована структура сообщений
- [ ] Определены типы всех полей
- [ ] Определены обязательные и опциональные поля
- [ ] Определены defaults
- [ ] Спланирована обработка ошибок
- [ ] Выбрана стратегия версионирования

### 9.2 During implementation

- [ ] Реализованы unit tests
- [ ] Реализованы integration tests
- [ ] Написана документация
- [ ] Созданы примеры

### 9.3 Before release

- [ ] Проведён security review
- [ ] Протестирована backward compatibility
- [ ] Документация полна
- [ ] Примеры работают
- [ ] Changelog обновлён

---

## 💡 Key Takeaways

- **Минимализм с первого дня**: YAGNI — добавляйте только необходимое. Не проектируйте "на будущее". Начните с MVP, итерируйте на основе реальных потребностей.

- **Explicit over implicit везде**: Явные имена, типы, единицы измерения, defaults. Избегайте неявных предположений — они источник bugs и несовместимости.

- **Версионирование обязательно**: Semantic versioning (MAJOR.MINOR.PATCH) для явности изменений. Deprecation process для graceful удаления старого функционала.

- **Backward compatibility критична**: Можно добавлять опциональные поля, нельзя удалять или менять существующие. Contract testing для проверки совместимости.

- **Документация — часть протокола**: OpenAPI для машинночитаемых спецификаций, примеры для людей, changelog для истории изменений. Документация должна быть актуальной.

---

## 🚀 Next Steps

**Related Modules:**

- [20_Protocol_Evolution](../20_Protocol_Evolution/) — эволюция протоколов и будущее: стандартизация, AI-агенты
- [18_Good_Vs_Bad_Protocols](../18_Good_Vs_Bad_Protocols/) — хороший vs плохой протокол: примеры и anti-patterns

**Practice Ideas:**

1. Спроектируйте простой протокол для вашего use case, следуя всем принципам
2. Создайте OpenAPI спецификацию для существующего API
3. Проведите review существующего протокола по checklist

**Going Deeper:**

- Изучите RFC process для понимания стандартизации протоколов
- Изучите API Design Guidelines от Google, Microsoft, Stripe
- Изучите Protocol Buffers и gRPC для примеров хорошего дизайна

---



