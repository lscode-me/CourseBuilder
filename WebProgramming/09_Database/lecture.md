# Взаимодействие с базами данных
## Работа с БД в веб-приложениях

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:
- Знать основы SQL
- Понимать архитектуру веб-приложений
- Иметь опыт работы с Python

**Recommended prior modules:**
- [Architecture](../08_Architecture/) — архитектура приложений
- [WSGI](../05_WSGI/) / [ASGI](../06_ASGI/) — интерфейсы

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:
- Работать с БД из веб-приложений
- Использовать ORM (SQLAlchemy)
- Понимать connection pooling
- Обрабатывать транзакции правильно
- Применять паттерны работы с БД в async приложениях

---

## 1. Подключение к базе данных

### 1.1 Прямое подключение (psycopg2)

```python
#!/usr/bin/env python3
"""Прямая работа с PostgreSQL."""

import psycopg2
from psycopg2.extras import RealDictCursor

# Подключение
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="myapp",
    user="app_user",
    password="secret"
)

# Курсор для выполнения запросов
cursor = conn.cursor(cursor_factory=RealDictCursor)

# SELECT
cursor.execute("SELECT id, name, email FROM users WHERE id = %s", (user_id,))
user = cursor.fetchone()  # {'id': 1, 'name': 'John', 'email': 'john@example.com'}

# INSERT
cursor.execute(
    "INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id",
    ("Jane", "jane@example.com")
)
new_id = cursor.fetchone()['id']
conn.commit()  # Важно!

# UPDATE
cursor.execute(
    "UPDATE users SET name = %s WHERE id = %s",
    ("Jane Doe", new_id)
)
conn.commit()

# Закрываем
cursor.close()
conn.close()
```

### 1.2 Context Manager

```python
import psycopg2
from contextlib import contextmanager

@contextmanager
def get_db_connection():
    """Context manager для подключения к БД."""
    conn = psycopg2.connect(
        host="localhost",
        database="myapp",
        user="app_user",
        password="secret"
    )
    try:
        yield conn
    finally:
        conn.close()

@contextmanager
def get_db_cursor(commit=False):
    """Context manager для курсора."""
    with get_db_connection() as conn:
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        try:
            yield cursor
            if commit:
                conn.commit()
        finally:
            cursor.close()

# Использование
with get_db_cursor() as cursor:
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

with get_db_cursor(commit=True) as cursor:
    cursor.execute("INSERT INTO users (name) VALUES (%s)", ("John",))
```

### 1.3 Connection Pool

```python
from psycopg2 import pool

# Создаём пул при старте приложения
connection_pool = pool.ThreadedConnectionPool(
    minconn=5,
    maxconn=20,
    host="localhost",
    database="myapp",
    user="app_user",
    password="secret"
)

def get_connection():
    """Получить соединение из пула."""
    return connection_pool.getconn()

def return_connection(conn):
    """Вернуть соединение в пул."""
    connection_pool.putconn(conn)

# Использование
conn = get_connection()
try:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
finally:
    return_connection(conn)

# При завершении приложения
connection_pool.closeall()
```

---

## 2. SQLAlchemy Core

### 2.1 Подключение и Engine

```python
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, select

# Создание engine (с пулом соединений)
engine = create_engine(
    "postgresql://user:pass@localhost/myapp",
    pool_size=5,
    max_overflow=10,
    pool_timeout=30,
    pool_recycle=1800,
    echo=True  # Логировать SQL
)

# Метаданные
metadata = MetaData()

# Определение таблицы
users = Table(
    'users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(100)),
    Column('email', String(200)),
)

# Создание таблиц
metadata.create_all(engine)
```

### 2.2 CRUD операции

```python
from sqlalchemy import select, insert, update, delete

# INSERT
with engine.connect() as conn:
    result = conn.execute(
        insert(users).values(name="John", email="john@example.com")
    )
    conn.commit()
    user_id = result.inserted_primary_key[0]

# SELECT
with engine.connect() as conn:
    # Один пользователь
    stmt = select(users).where(users.c.id == user_id)
    user = conn.execute(stmt).fetchone()
    
    # Все пользователи
    stmt = select(users).order_by(users.c.name)
    all_users = conn.execute(stmt).fetchall()
    
    # С фильтрацией
    stmt = select(users).where(users.c.email.like('%@example.com'))
    filtered = conn.execute(stmt).fetchall()

# UPDATE
with engine.connect() as conn:
    stmt = update(users).where(users.c.id == user_id).values(name="John Doe")
    conn.execute(stmt)
    conn.commit()

# DELETE
with engine.connect() as conn:
    stmt = delete(users).where(users.c.id == user_id)
    conn.execute(stmt)
    conn.commit()
```

---

## 3. SQLAlchemy ORM

### 3.1 Модели

```python
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(200), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationship
    orders = relationship("Order", back_populates="user")
    
    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}')>"
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }


class Order(Base):
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    total = Column(Integer, nullable=False)  # в копейках
    status = Column(String(50), default='pending')
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationship
    user = relationship("User", back_populates="orders")


# Создание engine и сессий
engine = create_engine("postgresql://user:pass@localhost/myapp")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Создание таблиц
Base.metadata.create_all(bind=engine)
```

### 3.2 CRUD с ORM

```python
from sqlalchemy.orm import Session

# CREATE
def create_user(db: Session, name: str, email: str) -> User:
    user = User(name=name, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)  # Получить сгенерированные значения (id, created_at)
    return user

# READ
def get_user(db: Session, user_id: int) -> User | None:
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100) -> list[User]:
    return db.query(User).offset(skip).limit(limit).all()

# UPDATE
def update_user(db: Session, user_id: int, **kwargs) -> User | None:
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        for key, value in kwargs.items():
            setattr(user, key, value)
        db.commit()
        db.refresh(user)
    return user

# DELETE
def delete_user(db: Session, user_id: int) -> bool:
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return True
    return False

# Использование
db = SessionLocal()
try:
    user = create_user(db, "John", "john@example.com")
    print(user)
finally:
    db.close()
```

### 3.3 Dependency Injection (FastAPI стиль)

```python
from contextlib import contextmanager

@contextmanager
def get_db():
    """Получить сессию БД."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Использование в обычном коде
with get_db() as db:
    users = get_users(db)

# В FastAPI
from fastapi import Depends, FastAPI

app = FastAPI()

def get_db_dependency():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/users")
def read_users(db: Session = Depends(get_db_dependency)):
    return get_users(db)
```

---

## 4. Транзакции

### 4.1 Базовые транзакции

```python
from sqlalchemy.orm import Session

def transfer_money(db: Session, from_user_id: int, to_user_id: int, amount: int):
    """Перевод денег между пользователями (атомарная операция)."""
    try:
        # Получаем пользователей
        from_user = db.query(User).filter(User.id == from_user_id).with_for_update().first()
        to_user = db.query(User).filter(User.id == to_user_id).with_for_update().first()
        
        if not from_user or not to_user:
            raise ValueError("User not found")
        
        if from_user.balance < amount:
            raise ValueError("Insufficient funds")
        
        # Выполняем перевод
        from_user.balance -= amount
        to_user.balance += amount
        
        # Создаём записи транзакций
        db.add(Transaction(user_id=from_user_id, amount=-amount))
        db.add(Transaction(user_id=to_user_id, amount=amount))
        
        db.commit()  # Всё или ничего
        
    except Exception as e:
        db.rollback()  # Откатываем при ошибке
        raise
```

### 4.2 Nested Transactions (Savepoints)

```python
def complex_operation(db: Session):
    """Операция с savepoints."""
    
    # Начинаем внешнюю транзакцию
    try:
        user = create_user(db, "John", "john@example.com")
        
        # Savepoint для вложенной операции
        savepoint = db.begin_nested()
        try:
            order = create_order(db, user.id, 1000)
            # Что-то может пойти не так
            process_payment(order)
            savepoint.commit()
        except PaymentError:
            savepoint.rollback()
            # User всё ещё создан, только order откатился
            user.status = 'payment_failed'
        
        db.commit()
        
    except Exception:
        db.rollback()
        raise
```

### 4.3 Уровни изоляции

```python
from sqlalchemy import create_engine

# Установка уровня изоляции для всего engine
engine = create_engine(
    "postgresql://user:pass@localhost/myapp",
    isolation_level="REPEATABLE READ"  # READ COMMITTED, SERIALIZABLE
)

# Для конкретной транзакции
with engine.connect().execution_options(isolation_level="SERIALIZABLE") as conn:
    # Эта транзакция выполнится с SERIALIZABLE
    pass
```

---

## 5. Async работа с БД

### 5.1 asyncpg (PostgreSQL)

```python
import asyncpg
import asyncio

async def main():
    # Подключение
    conn = await asyncpg.connect(
        host='localhost',
        database='myapp',
        user='user',
        password='pass'
    )
    
    # SELECT
    row = await conn.fetchrow(
        'SELECT id, name FROM users WHERE id = $1', 1
    )
    print(row['name'])
    
    # INSERT
    await conn.execute(
        'INSERT INTO users(name, email) VALUES($1, $2)',
        'Jane', 'jane@example.com'
    )
    
    # SELECT multiple
    rows = await conn.fetch('SELECT * FROM users')
    for row in rows:
        print(row)
    
    await conn.close()

asyncio.run(main())
```

### 5.2 asyncpg Connection Pool

```python
import asyncpg
from contextlib import asynccontextmanager

class Database:
    def __init__(self):
        self.pool = None
    
    async def connect(self, dsn: str):
        self.pool = await asyncpg.create_pool(
            dsn,
            min_size=5,
            max_size=20,
            command_timeout=60
        )
    
    async def disconnect(self):
        if self.pool:
            await self.pool.close()
    
    @asynccontextmanager
    async def connection(self):
        async with self.pool.acquire() as conn:
            yield conn
    
    @asynccontextmanager
    async def transaction(self):
        async with self.pool.acquire() as conn:
            async with conn.transaction():
                yield conn

# Использование
db = Database()

async def startup():
    await db.connect("postgresql://user:pass@localhost/myapp")

async def shutdown():
    await db.disconnect()

async def get_user(user_id: int):
    async with db.connection() as conn:
        return await conn.fetchrow(
            "SELECT * FROM users WHERE id = $1", user_id
        )

async def create_user_with_order(name: str, email: str, amount: int):
    async with db.transaction() as conn:
        user_id = await conn.fetchval(
            "INSERT INTO users(name, email) VALUES($1, $2) RETURNING id",
            name, email
        )
        await conn.execute(
            "INSERT INTO orders(user_id, total) VALUES($1, $2)",
            user_id, amount
        )
        return user_id
```

### 5.3 SQLAlchemy 2.0 Async

```python
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, select

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    email = Column(String(200))

# Async engine
async_engine = create_async_engine(
    "postgresql+asyncpg://user:pass@localhost/myapp",
    pool_size=5,
    max_overflow=10,
)

# Async session maker
async_session = async_sessionmaker(
    async_engine, 
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_async_db():
    async with async_session() as session:
        yield session

# CRUD
async def get_user(db: AsyncSession, user_id: int) -> User | None:
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalar_one_or_none()

async def create_user(db: AsyncSession, name: str, email: str) -> User:
    user = User(name=name, email=email)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

async def get_users(db: AsyncSession, skip: int = 0, limit: int = 100) -> list[User]:
    result = await db.execute(
        select(User).offset(skip).limit(limit)
    )
    return result.scalars().all()
```

---

## 6. Интеграция с веб-фреймворками

### 6.1 FastAPI + SQLAlchemy

```python
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

app = FastAPI()

# Pydantic schemas
class UserCreate(BaseModel):
    name: str
    email: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    
    class Config:
        from_attributes = True

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoints
@app.post("/users", response_model=UserResponse)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    # Проверка на дубликат
    if get_user_by_email(db, user.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    
    return create_user(db, user.name, user.email)

@app.get("/users/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.get("/users", response_model=list[UserResponse])
def read_users(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db)
):
    return get_users(db, skip=skip, limit=limit)
```

### 6.2 Flask + SQLAlchemy

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:pass@localhost/myapp'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user = User(name=data['name'], email=data['email'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'id': user.id, 'name': user.name})

@app.route('/users/<int:user_id>')
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify({'id': user.id, 'name': user.name, 'email': user.email})

@app.route('/users')
def list_users():
    users = User.query.all()
    return jsonify([{'id': u.id, 'name': u.name} for u in users])

# Создание таблиц
with app.app_context():
    db.create_all()
```

---

## 7. Оптимизация и паттерны

### 7.1 N+1 Problem

```python
# ❌ N+1 проблема
users = db.query(User).all()  # 1 запрос
for user in users:
    print(user.orders)  # N запросов!

# ✅ Eager loading с joinedload
from sqlalchemy.orm import joinedload

users = db.query(User).options(joinedload(User.orders)).all()  # 1 запрос
for user in users:
    print(user.orders)  # Без дополнительных запросов

# ✅ Или selectinload для больших наборов
from sqlalchemy.orm import selectinload

users = db.query(User).options(selectinload(User.orders)).all()  # 2 запроса
```

### 7.2 Пагинация

```python
from sqlalchemy import select, func

def paginate(db: Session, model, page: int = 1, per_page: int = 20):
    """Пагинация с подсчётом."""
    
    # Общее количество
    total = db.execute(select(func.count()).select_from(model)).scalar()
    
    # Данные страницы
    offset = (page - 1) * per_page
    items = db.query(model).offset(offset).limit(per_page).all()
    
    return {
        'items': items,
        'page': page,
        'per_page': per_page,
        'total': total,
        'pages': (total + per_page - 1) // per_page
    }

# Использование
result = paginate(db, User, page=2, per_page=10)
```

### 7.3 Bulk Operations

```python
# ❌ Медленно — N запросов
for data in users_data:
    db.add(User(**data))
db.commit()

# ✅ Быстро — bulk insert
db.execute(
    User.__table__.insert(),
    users_data
)
db.commit()

# ✅ Или через bulk_save_objects
users = [User(**data) for data in users_data]
db.bulk_save_objects(users)
db.commit()

# ✅ Bulk update
db.execute(
    User.__table__.update().where(User.id.in_(ids)).values(status='active')
)
db.commit()
```

### 7.4 Индексы

```python
from sqlalchemy import Index

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    email = Column(String(200), unique=True, index=True)  # Простой индекс
    name = Column(String(100))
    status = Column(String(50))
    created_at = Column(DateTime)
    
    # Составной индекс
    __table_args__ = (
        Index('idx_user_status_created', 'status', 'created_at'),
    )
```

---

## 8. Миграции (Alembic)

### 8.1 Настройка

```bash
# Установка
pip install alembic

# Инициализация
alembic init alembic
```

```python
# alembic/env.py
from models import Base
target_metadata = Base.metadata

# alembic.ini
sqlalchemy.url = postgresql://user:pass@localhost/myapp
```

### 8.2 Создание и применение миграций

```bash
# Автогенерация миграции
alembic revision --autogenerate -m "add users table"

# Применить миграции
alembic upgrade head

# Откатить
alembic downgrade -1

# Показать текущую версию
alembic current

# Показать историю
alembic history
```

```python
# alembic/versions/xxx_add_users_table.py

def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('email', sa.String(200), nullable=False),
    )
    op.create_index('ix_users_email', 'users', ['email'], unique=True)

def downgrade():
    op.drop_index('ix_users_email', table_name='users')
    op.drop_table('users')
```

---

## 💡 Key Takeaways

- **Connection Pool** — обязателен для production (psycopg2 pool или SQLAlchemy)
- **ORM** — удобно для CRUD, но следите за N+1
- **Транзакции** — всегда используйте для связанных операций
- **Async** — используйте asyncpg или SQLAlchemy async для ASGI приложений
- **Eager loading** — решает N+1 проблему (joinedload, selectinload)
- **Миграции** — Alembic для версионирования схемы БД

---

## 🚀 Next Steps

**Practice Ideas:**
1. Создайте REST API с CRUD операциями
2. Реализуйте пагинацию и фильтрацию
3. Добавьте async работу с БД в FastAPI
4. Настройте Alembic миграции

**Going Deeper:**
- SQLAlchemy 2.0 documentation
- PostgreSQL performance tuning
- Database design patterns

---

## 📚 Additional Resources

**Documentation:**
- [SQLAlchemy](https://docs.sqlalchemy.org/)
- [asyncpg](https://magicstack.github.io/asyncpg/)
- [Alembic](https://alembic.sqlalchemy.org/)
- [psycopg2](https://www.psycopg.org/docs/)

**Books:**
- "High Performance PostgreSQL"
- "SQL Antipatterns" — Bill Karwin

---

