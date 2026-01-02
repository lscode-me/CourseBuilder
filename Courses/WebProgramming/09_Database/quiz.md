# Взаимодействие с базами данных - Quiz

Проверьте свои знания по теме работы с базами данных в веб-приложениях.

---

## Question 1: Connection Pool

Зачем нужен connection pool при работе с базой данных в веб-приложении?

A) Для автоматического backup данных

B) Для кэширования SQL запросов

C) Для переиспользования соединений и избежания накладных расходов на создание новых

D) Для шифрования соединений с базой данных

---

## Question 2: Context Manager

Какой результат выполнения кода?

```python
with get_db_cursor(commit=True) as cursor:
    cursor.execute("INSERT INTO users (name) VALUES (%s)", ("John",))
# После выхода из with блока
```

A) Данные будут сохранены, так как commit=True вызовет commit автоматически

B) Данные НЕ будут сохранены, так как нет явного commit

C) Возникнет ошибка, так как cursor нельзя использовать в context manager

D) Данные будут сохранены в отдельной транзакции

---

## Question 3: SQLAlchemy Engine

Что делает параметр `pool_recycle=1800` при создании SQLAlchemy engine?

A) Закрывает и пересоздаёт соединения старше 1800 секунд

B) Устанавливает timeout для SQL запросов в 1800 мс

C) Ограничивает максимальное количество запросов до 1800

D) Перезапускает базу данных каждые 1800 секунд

---

## Question 4: ORM vs Core

Какое утверждение о SQLAlchemy верно?

A) SQLAlchemy Core требует больше памяти чем ORM

B) ORM и Core нельзя использовать вместе в одном проекте

C) SQLAlchemy ORM не поддерживает relationships между таблицами

D) SQLAlchemy Core быстрее, но менее удобен для CRUD операций

---

## Question 5: Session Management

Что произойдёт, если забыть вызвать `db.commit()` после INSERT в SQLAlchemy ORM?

A) Данные автоматически сохранятся при закрытии сессии

B) Данные будут потеряны при закрытии сессии

C) Возникнет ошибка TransactionError

D) Данные сохранятся в temporary table

---

## Question 6: Refresh After Commit

Зачем вызывать `db.refresh(user)` после `db.commit()`?

A) Для получения сгенерированных значений (id, created_at) из базы данных

B) Для синхронизации с другими сессиями

C) Для очистки кэша сессии

D) Для проверки, что данные действительно сохранены

---

## Question 7: with_for_update

Что делает `query.with_for_update()` в SQLAlchemy?

A) Блокирует выбранные строки для предотвращения concurrent modifications

B) Создаёт триггер на UPDATE

C) Включает оптимистическую блокировку

D) Автоматически выполняет UPDATE после SELECT

---

## Question 8: Savepoints

Что произойдёт с пользователем при откате savepoint?

```python
user = create_user(db, "John", "john@example.com")
savepoint = db.begin_nested()
try:
    order = create_order(db, user.id, 1000)
    raise PaymentError("Failed")
except PaymentError:
    savepoint.rollback()
db.commit()
```

A) Возникнет ошибка, так как нельзя commit после rollback

B) Пользователь будет удалён вместе с заказом

C) Пользователь останется, только заказ будет откачен

D) И пользователь, и заказ будут сохранены

---

## Question 9: Isolation Levels

Какой уровень изоляции по умолчанию в PostgreSQL?

A) REPEATABLE READ

B) READ UNCOMMITTED

C) SERIALIZABLE

D) READ COMMITTED

---

## Question 10: asyncpg Placeholders

Какой синтаксис placeholders использует asyncpg?

A) `%s` — как в psycopg2

B) `$1, $2, $3` — нумерованные

C) `:name` — именованные

D) `?` — как в sqlite3

---

## Question 11: Async Session

Какой класс используется для async сессий в SQLAlchemy 2.0?

A) AioSession

B) AsyncDbSession

C) Session с параметром async=True

D) AsyncSession

---

## Question 12: FastAPI Dependency

Что делает `yield` в FastAPI dependency для базы данных?

```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

A) Возвращает значение и завершает функцию

B) Создаёт генератор, который никогда не закрывает соединение

C) Вызывает ошибку, так как yield нельзя использовать в dependency

D) Возвращает значение, затем выполняет cleanup код в finally после завершения запроса

---

## Question 13: N+1 Problem

Что такое N+1 problem?

A) Ограничение на количество соединений в пуле

B) Проблема, когда для N записей выполняется N+1 запрос к базе

C) Ошибка при использовании более 1 базы данных

D) Проблема с индексами при большом количестве записей

---

## Question 14: Eager Loading

Какой метод загрузки предпочтительнее для большого количества связанных записей?

A) selectinload — для больших наборов данных

B) subqueryload — устаревший метод

C) lazyload — для любых объёмов данных

D) joinedload — всегда лучше

---

## Question 15: Bulk Operations

Какой способ вставки 10,000 записей наиболее эффективен?

A) Цикл с `db.add()` для каждой записи

B) Использование stored procedure

C) Отдельная транзакция для каждой записи

D) `db.bulk_save_objects()` или `insert().values()`

---

## Question 16: Flask-SQLAlchemy

Как Flask-SQLAlchemy управляет сессиями?

A) Не поддерживает управление сессиями

B) Использует глобальную сессию для всех запросов

C) Требует ручного создания и закрытия сессий

D) Автоматически создаёт scoped session привязанную к request context

---

## Question 17: Alembic

Что делает команда `alembic upgrade head`?

A) Применяет все непримененные миграции до последней версии

B) Создаёт новую миграцию

C) Откатывает последнюю миграцию

D) Показывает текущую версию базы данных

---

## Question 18: Alembic Autogenerate

Что НЕ может автоматически обнаружить `alembic revision --autogenerate`?

A) Добавление новой таблицы

B) Переименование столбца

C) Добавление нового столбца

D) Изменение типа столбца

---

## Question 19: Index

Какой индекс создаётся в этом коде?

```python
class User(Base):
    __tablename__ = 'users'
    email = Column(String(200), unique=True, index=True)
    __table_args__ = (
        Index('idx_user_status_created', 'status', 'created_at'),
    )
```

A) Три индекса: unique на email, простой на email, составной на status+created_at

B) Только один составной индекс на status и created_at

C) Два индекса: простой на email и составной на status+created_at

D) Индексы не создаются, только constraints

---

## Question 20: Pydantic Integration

Что делает `from_attributes = True` в Pydantic модели для SQLAlchemy?

A) Позволяет создавать SQLAlchemy объекты из Pydantic

B) Включает автоматическую сериализацию в JSON

C) Позволяет Pydantic читать атрибуты из ORM объектов (не только dict)

D) Добавляет валидацию атрибутов SQLAlchemy модели

---

## Question 21: Async Engine

Какой URL драйвер используется для async PostgreSQL в SQLAlchemy?

A) `postgresql+psycopg2://`

B) `postgresql+asyncpg://`

C) `postgresql://`

D) `async+postgresql://`

---

## Question 22: expire_on_commit

Что делает `expire_on_commit=False` в async_sessionmaker?

A) Предотвращает истечение атрибутов объекта после commit

B) Позволяет использовать сессию после commit

C) Отключает автоматический commit

D) Отключает проверку на дубликаты

---

## Question 23: Result Proxy

Как получить список объектов из async SQLAlchemy запроса?

```python
result = await db.execute(select(User))
# Как получить список User объектов?
```

A) `result.fetchall()`

B) `result.scalars().all()`

C) `result.all()`

D) `await result.all()`

---

## Question 24: Transaction Rollback

Когда автоматически вызывается rollback в SQLAlchemy?

A) При таймауте соединения

B) При закрытии сессии без commit

C) При возникновении исключения в with блоке сессии

D) Оба варианта A и B верны

---

## Question 25: Connection Pool Parameters

Что означают параметры `pool_size=5, max_overflow=10`?

A) Минимум 5 соединений, максимум 10 соединений

B) Пул из 5 соединений с очередью на 10 ожидающих запросов

C) 5 постоянных соединений + до 10 дополнительных при нагрузке

D) 5 соединений на чтение, 10 на запись

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | C | Connection pool переиспользует соединения, избегая накладных расходов на TCP handshake и аутентификацию |
| 2 | A | При commit=True context manager автоматически вызывает conn.commit() перед закрытием |
| 3 | A | pool_recycle закрывает соединения старше указанного времени для избежания stale connections |
| 4 | D | SQLAlchemy Core работает с SQL напрямую и быстрее, ORM добавляет абстракцию и удобство |
| 5 | B | Без commit() изменения остаются только в памяти сессии и теряются при её закрытии |
| 6 | A | refresh() синхронизирует объект с базой, получая auto-generated значения (id, default values) |
| 7 | A | with_for_update() добавляет FOR UPDATE к SELECT, блокируя строки для других транзакций |
| 8 | C | Savepoint позволяет откатить только часть транзакции; пользователь уже в основной транзакции |
| 9 | D | PostgreSQL по умолчанию использует READ COMMITTED |
| 10 | B | asyncpg использует нумерованные placeholders: $1, $2, $3... |
| 11 | D | AsyncSession — специальный класс для async операций в SQLAlchemy 2.0 |
| 12 | D | yield возвращает db, затем после завершения request-а выполняется finally блок с close() |
| 13 | B | N+1: 1 запрос для списка, затем N запросов для связанных данных каждой записи |
| 14 | A | selectinload делает 2 запроса (основной + IN query) и эффективнее для больших наборов |
| 15 | D | Bulk операции значительно быстрее, так как минимизируют roundtrips к базе |
| 16 | D | Flask-SQLAlchemy создаёт scoped session, автоматически привязанную к request lifecycle |
| 17 | A | upgrade head применяет все миграции до последней (head) версии |
| 18 | B | Autogenerate не может обнаружить переименование — видит как drop + create нового столбца |
| 19 | C | index=True создаёт простой индекс, Index() создаёт составной; unique создаёт constraint |
| 20 | C | from_attributes позволяет Pydantic читать данные из ORM объектов через getattr |
| 21 | B | postgresql+asyncpg:// указывает использовать asyncpg драйвер для async операций |
| 22 | A | expire_on_commit=False предотвращает "detached instance" ошибки после commit в async коде |
| 23 | B | scalars() возвращает только первый элемент каждой строки (сам объект), all() собирает в список |
| 24 | D | Rollback вызывается и при исключении в транзакции, и при закрытии сессии без commit |
| 25 | C | pool_size — постоянные соединения, max_overflow — дополнительные при пиковой нагрузке |

---

## Scoring Guide

Подсчитайте количество правильных ответов:

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **23-25 правильных (90-100%)** | 🏆 Отлично! | Вы отлично усвоили материал. Готовы к production-разработке с БД. |
| **18-22 правильных (70-89%)** | ✅ Хорошо | Хороший результат! Повторите темы async работы и оптимизации. |
| **13-17 правильных (50-69%)** | ⚠️ Удовлетворительно | Рекомендуется перечитать разделы о транзакциях и session management. |
| **Менее 13 правильных (<50%)** | 📚 Нужно повторить | Внимательно перечитайте лекцию, особенно примеры кода. |

---



