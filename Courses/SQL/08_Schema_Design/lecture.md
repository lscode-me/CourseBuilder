# Проектирование схемы данных
## Первичные ключи, внешние ключи, нормализация, денормализация

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать структуру таблиц и связи между ними
- Знать базовый синтаксис CREATE TABLE
- Иметь представление о типах данных

**Recommended prior modules:**

- [01_Intro](../01_Intro/) — Введение в SQL и реляционные базы данных
- [03_Data_Types](../03_Data_Types/) — Типы данных и NULL

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Создавать первичные ключи для уникальной идентификации строк
- Использовать внешние ключи для связей между таблицами
- Применять нормализацию для устранения избыточности данных
- Понимать, когда денормализация оправдана
- Проектировать эффективные схемы баз данных

---

## 1. Первичные ключи (Primary Keys)

### 1.1 Что такое первичный ключ

**Первичный ключ (Primary Key)** — столбец или набор столбцов, который уникально идентифицирует каждую строку в таблице.

**Требования:**

- ✅ Уникальность — каждая строка имеет уникальное значение
- ✅ NOT NULL — не может быть NULL
- ✅ Неизменяемость — значение не должно меняться

**Пример:**

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);
```

### 1.2 Составные первичные ключи

**Первичный ключ может состоять из нескольких столбцов:**

```sql
CREATE TABLE order_items (
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    PRIMARY KEY (order_id, product_id)
);
```

### 1.3 Автоинкремент

**SERIAL (PostgreSQL) / AUTO_INCREMENT (MySQL):**

```sql
-- PostgreSQL
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);

-- MySQL
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100)
);
```

---

## 2. Внешние ключи (Foreign Keys)

### 2.1 Что такое внешний ключ

**Внешний ключ (Foreign Key)** — столбец, который ссылается на первичный ключ другой таблицы.

**Пример:**

```sql
CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    amount DECIMAL(10, 2),
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

### 2.2 ON DELETE и ON UPDATE

**Поведение при удалении/обновлении:**

```sql
CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id)
        ON DELETE CASCADE    -- Удалить заказы при удалении пользователя
        ON UPDATE CASCADE    -- Обновить при изменении id пользователя
);
```

**Варианты:**

- **CASCADE** — каскадное удаление/обновление

- **RESTRICT** — запретить удаление/обновление

- **SET NULL** — установить NULL

- **NO ACTION** — ничего не делать (по умолчанию)

### 2.3 Преимущества внешних ключей

**Целостность данных:**

- ✅ Предотвращает "осиротевшие" записи
- ✅ Гарантирует существование связанных данных
- ✅ Автоматическая валидация

---

## 3. Нормализация

### 3.1 Что такое нормализация

**Нормализация** — процесс организации данных для устранения избыточности и аномалий.

**Цели:**

- Устранение дублирования данных
- Предотвращение аномалий обновления
- Упрощение структуры данных

### 3.2 Первая нормальная форма (1NF)

**Требования:**

- Каждая ячейка содержит атомарное значение
- Нет повторяющихся групп
- Все строки уникальны

**❌ Не в 1NF:**

```sql
CREATE TABLE users (
    id INTEGER,
    name VARCHAR(100),
    phones VARCHAR(200)  -- "123-456, 789-012" (не атомарно)
);
```

**✅ В 1NF:**

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE user_phones (
    user_id INTEGER,
    phone VARCHAR(20),
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

### 3.3 Вторая нормальная форма (2NF)

**Требования:**

- В 1NF
- Все неключевые атрибуты полностью зависят от первичного ключа

**❌ Не в 2NF:**

```sql
CREATE TABLE order_items (
    order_id INTEGER,
    product_id INTEGER,
    product_name VARCHAR(100),  -- Зависит только от product_id
    quantity INTEGER,
    PRIMARY KEY (order_id, product_id)
);
```

**✅ В 2NF:**

```sql
CREATE TABLE products (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE order_items (
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);
```

### 3.4 Третья нормальная форма (3NF)

**Требования:**

- В 2NF
- Нет транзитивных зависимостей (неключевые атрибуты не зависят от других неключевых атрибутов)

**❌ Не в 3NF:**

```sql
CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    user_country VARCHAR(100),  -- Зависит от user_id, не от order_id
    amount DECIMAL(10, 2)
);
```

**✅ В 3NF:**

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    country VARCHAR(100)
);

CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    amount DECIMAL(10, 2),
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

---

## 4. Денормализация

### 4.1 Когда денормализация оправдана

**Денормализация** — намеренное нарушение нормализации для улучшения производительности.

**Когда использовать:**

- ✅ Частые JOIN замедляют запросы
- ✅ Чтение важнее записи (OLAP системы)
- ✅ Данные редко изменяются
- ✅ Производительность критична

**Пример:**

```sql
-- Денормализованная таблица для быстрых отчётов
CREATE TABLE user_stats (
    user_id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    total_orders INTEGER,      -- Денормализация
    total_spent DECIMAL(10, 2), -- Денормализация
    last_order_date DATE        -- Денормализация
);
```

### 4.2 Компромиссы денормализации

**Преимущества:**

- ✅ Быстрее чтение (меньше JOIN)
- ✅ Проще запросы

**Недостатки:**

- ❌ Избыточность данных
- ❌ Сложнее обновления
- ❌ Риск несогласованности

---

## 5. Практические примеры

### 5.1 Проектирование интернет-магазина

**Нормализованная схема:**

```sql
-- Пользователи
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE
);

-- Категории товаров
CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);

-- Товары
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10, 2),
    category_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

-- Заказы
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Позиции заказа
CREATE TABLE order_items (
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    price DECIMAL(10, 2),  -- Цена на момент заказа
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);
```

### 5.2 Индексы для производительности

```sql
-- Индексы для внешних ключей
CREATE INDEX idx_orders_user_id ON orders(user_id);
CREATE INDEX idx_order_items_order_id ON order_items(order_id);
CREATE INDEX idx_order_items_product_id ON order_items(product_id);
```

### 5.3 Проектирование блога

**Схема для блога:**

```sql
-- Пользователи
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Посты
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    author_id INTEGER NOT NULL,
    title VARCHAR(200) NOT NULL,
    content TEXT,
    published_at TIMESTAMP,
    FOREIGN KEY (author_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Комментарии
CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    post_id INTEGER NOT NULL,
    author_id INTEGER NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE,
    FOREIGN KEY (author_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Теги
CREATE TABLE tags (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);

-- Связь многие-ко-многим: посты и теги
CREATE TABLE post_tags (
    post_id INTEGER,
    tag_id INTEGER,
    PRIMARY KEY (post_id, tag_id),
    FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE,
    FOREIGN KEY (tag_id) REFERENCES tags(id) ON DELETE CASCADE
);
```

---

## 6. BCNF (Boyce-Codd Normal Form)

### 6.1 Что такое BCNF

**BCNF** — усиленная версия 3NF, устраняет все аномалии.

**Требования:**

- В 3NF
- Каждая детерминанта (левая часть функциональной зависимости) — потенциальный ключ

### 6.2 Пример нарушения BCNF

**❌ Не в BCNF:**

```sql
CREATE TABLE course_instructors (
    course_id INTEGER,
    instructor_id INTEGER,
    instructor_department VARCHAR(100),  -- Зависит от instructor_id
    PRIMARY KEY (course_id, instructor_id)
);
```

**Проблема:** `instructor_department` зависит от `instructor_id`, но `instructor_id` не является ключом.

**✅ В BCNF:**

```sql
CREATE TABLE instructors (
    id INTEGER PRIMARY KEY,
    department VARCHAR(100)
);

CREATE TABLE course_instructors (
    course_id INTEGER,
    instructor_id INTEGER,
    PRIMARY KEY (course_id, instructor_id),
    FOREIGN KEY (instructor_id) REFERENCES instructors(id)
);
```

---

## 7. Триггеры для поддержания денормализованных данных

### 7.1 Автоматическое обновление денормализованных полей

**Пример: поддержание total_orders в user_stats:**

```sql
-- Таблица с денормализованными данными
CREATE TABLE user_stats (
    user_id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    total_orders INTEGER DEFAULT 0,
    total_spent DECIMAL(10, 2) DEFAULT 0
);

-- Триггер для обновления статистики
CREATE OR REPLACE FUNCTION update_user_stats()
RETURNS TRIGGER AS $$
BEGIN
    IF TG_OP = 'INSERT' THEN
        UPDATE user_stats
        SET 
            total_orders = total_orders + 1,
            total_spent = total_spent + NEW.amount
        WHERE user_id = NEW.user_id;
        RETURN NEW;
    ELSIF TG_OP = 'UPDATE' THEN
        UPDATE user_stats
        SET total_spent = total_spent - OLD.amount + NEW.amount
        WHERE user_id = NEW.user_id;
        RETURN NEW;
    ELSIF TG_OP = 'DELETE' THEN
        UPDATE user_stats
        SET 
            total_orders = total_orders - 1,
            total_spent = total_spent - OLD.amount
        WHERE user_id = OLD.user_id;
        RETURN OLD;
    END IF;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER orders_stats_trigger
AFTER INSERT OR UPDATE OR DELETE ON orders
FOR EACH ROW
EXECUTE FUNCTION update_user_stats();
```

---

## 8. Выбор первичного ключа

### 8.1 Натуральные ключи vs Суррогатные ключи

**Натуральный ключ** — имеет бизнес-значение:

```sql
-- Email как натуральный ключ
CREATE TABLE users (
    email VARCHAR(100) PRIMARY KEY,
    name VARCHAR(100)
);
```

**Суррогатный ключ** — искусственный идентификатор:

```sql
-- ID как суррогатный ключ
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(100) UNIQUE,
    name VARCHAR(100)
);
```

### 8.2 Когда использовать каждый тип

**Натуральные ключи:**

- ✅ Естественный уникальный идентификатор (email, ISBN)
- ✅ Меньше JOIN (можно использовать напрямую)
- ❌ Могут измениться
- ❌ Могут быть составными и сложными

**Суррогатные ключи:**

- ✅ Стабильны (не меняются)
- ✅ Простые (один столбец)
- ✅ Быстрые (обычно INTEGER)
- ❌ Требуют дополнительный JOIN для бизнес-логики

---

## 9. Ограничения (Constraints)

### 9.1 CHECK ограничения

**Проверка значений:**

```sql
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    amount DECIMAL(10, 2) CHECK (amount > 0),
    status VARCHAR(20) CHECK (status IN ('pending', 'completed', 'cancelled')),
    order_date DATE CHECK (order_date <= CURRENT_DATE)
);
```

### 9.2 UNIQUE ограничения

**Уникальность значений:**

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(100) UNIQUE NOT NULL,
    username VARCHAR(50) UNIQUE NOT NULL
);
```

### 9.3 NOT NULL ограничения

**Обязательные поля:**

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    age INTEGER  -- Может быть NULL
);
```

---

## 10. Практические рекомендации

### 10.1 Именование

**Соглашения:**

- ✅ Таблицы: множественное число (users, orders)
- ✅ Столбцы: snake_case (user_id, order_date)
- ✅ Индексы: idx_<table>_<column>
- ✅ Внешние ключи: <referenced_table>_id

### 10.2 Документация схемы

**Комментарии к таблицам и столбцам:**

```sql
COMMENT ON TABLE users IS 'Пользователи системы';
COMMENT ON COLUMN users.email IS 'Email адрес пользователя (уникальный)';
COMMENT ON COLUMN users.created_at IS 'Дата регистрации';
```

### 10.3 Версионирование схемы

**Миграции:**

```sql
-- Миграция: добавление столбца
ALTER TABLE users ADD COLUMN phone VARCHAR(20);

-- Миграция: изменение типа
ALTER TABLE users ALTER COLUMN age TYPE INTEGER;

-- Миграция: удаление столбца
ALTER TABLE users DROP COLUMN old_column;
```

---

## 💡 Key Takeaways

- **Первичные ключи** — уникально идентифицируют строки, должны быть NOT NULL и уникальны

- **Внешние ключи** — обеспечивают целостность данных и связи между таблицами

- **Нормализация** — устраняет избыточность, но может замедлить запросы

- **Денормализация** — улучшает производительность чтения, но усложняет обновления

- **Компромисс** — баланс между нормализацией и производительностью

---

## 🚀 Next Steps

**Related Modules:**

- [09_Indexes](../09_Indexes/) — Индексы для производительности
- [10_Query_Plans](../10_Query_Plans/) — Планы выполнения запросов

**Practice Ideas:**

1. Спроектируйте схему для блога (посты, комментарии, теги)
2. Попрактикуйтесь с нормализацией и денормализацией
3. Создайте внешние ключи с разными ON DELETE/UPDATE стратегиями
4. Сравните производительность нормализованной и денормализованной схем

**Going Deeper:**

- Изучите BCNF (Boyce-Codd Normal Form)
- Изучите паттерны проектирования для разных типов приложений
- Изучите использование триггеров для поддержания денормализованных данных

---

## 📚 Additional Resources

**Documentation:**

- [PostgreSQL Constraints](https://www.postgresql.org/docs/current/ddl-constraints.html) — ограничения
- [Database Normalization](https://www.postgresql.org/docs/current/database-design.html) — нормализация

---


