# Хэши и контрольные суммы
## MD5, SHA и проверка целостности данных

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать бинарные данные (модуль 02_NumberSystems)
- Иметь опыт работы в командной строке

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Объяснить разницу между хэшами и шифрованием
- Вычислять контрольные суммы файлов
- Проверять целостность скачанных файлов
- Использовать хэши для дедупликации и сравнения

---

## 1. Что такое хэш-функция

### 1.1 Определение

**Хэш-функция** — преобразует данные произвольного размера в строку фиксированной длины.

```
Input: "Hello"           → MD5:  8b1a9953c4611296a827abf8c47804d7
Input: "Hello World"     → MD5:  b10a8db164e0754105b7a99be72e3fe5
Input: "Hello Worl"      → MD5:  e99c029231c55e55de1dc04a2f1c5e24
```

### 1.2 Свойства хэш-функций

1. **Детерминированность**: Один вход → один выход
2. **Быстрота**: Быстрое вычисление
3. **Лавинный эффект**: Малое изменение входа → большое изменение выхода
4. **Необратимость**: Нельзя восстановить вход по хэшу
5. **Устойчивость к коллизиям**: Трудно найти два входа с одинаковым хэшем

### 1.3 Хэш vs Шифрование

| Хэш | Шифрование |
|-----|------------|
| Необратимый | Обратимый |
| Фиксированная длина | Зависит от входа |
| Нет ключа | Требует ключ |
| Проверка целостности | Защита данных |

---

## 2. Популярные алгоритмы

### 2.1 MD5 (устаревший)

- **Длина**: 128 бит (32 hex символа)
- **Скорость**: Очень быстрый
- **Безопасность**: Скомпрометирован, не для криптографии

```bash
echo -n "Hello" | md5sum
# 8b1a9953c4611296a827abf8c47804d7  -
```

### 2.2 SHA-1 (устаревший)

- **Длина**: 160 бит (40 hex символов)
- **Безопасность**: Скомпрометирован, используется в Git

```bash
echo -n "Hello" | sha1sum
# f7ff9e8b7bb2e09b70935a5d785e0cc5d9d0abf0  -
```

### 2.3 SHA-256 (рекомендуется)

- **Длина**: 256 бит (64 hex символа)
- **Безопасность**: Криптографически стойкий

```bash
echo -n "Hello" | sha256sum
# 185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969  -
```

### 2.4 SHA-512

- **Длина**: 512 бит (128 hex символов)
- **Безопасность**: Более стойкий, медленнее

```bash
echo -n "Hello" | sha512sum
```

### 2.5 Сравнение

| Алгоритм | Длина | Скорость | Безопасность |
|----------|-------|----------|--------------|
| MD5 | 128 бит | Быстрый | Скомпрометирован |
| SHA-1 | 160 бит | Быстрый | Скомпрометирован |
| SHA-256 | 256 бит | Средний | Стойкий |
| SHA-512 | 512 бит | Медленнее | Стойкий |
| BLAKE3 | 256+ бит | Очень быстрый | Стойкий |

---

## 3. Командная строка

### 3.1 Вычисление хэшей

```bash
# MD5
md5sum file.txt
# SHA-256
sha256sum file.txt
# SHA-512
sha512sum file.txt

# Несколько файлов
sha256sum *.txt

# Из строки (без перевода строки!)
echo -n "text" | sha256sum
```

### 3.2 Проверка хэшей

```bash
# Создать файл с хэшами
sha256sum *.iso > checksums.sha256

# Проверить
sha256sum -c checksums.sha256
# file1.iso: OK
# file2.iso: FAILED
```

### 3.3 macOS

```bash
# На macOS используйте shasum
shasum -a 256 file.txt
shasum -a 512 file.txt

# MD5
md5 file.txt
# или
md5 -q file.txt  # Только хэш
```

---

## 4. Практические применения

### 4.1 Проверка загрузок

```bash
# Скачали Ubuntu ISO, хотим проверить
# 1. Скачать файл с хэшами с официального сайта
wget https://releases.ubuntu.com/22.04/SHA256SUMS

# 2. Проверить
sha256sum -c SHA256SUMS 2>/dev/null | grep ubuntu-22.04-desktop-amd64.iso
# ubuntu-22.04-desktop-amd64.iso: OK
```

### 4.2 Сравнение файлов

```bash
# Быстрое сравнение без побайтового чтения
if [ "$(md5sum file1)" == "$(md5sum file2)" ]; then
    echo "Files are identical"
fi
```

### 4.3 Дедупликация

```bash
# Найти дубликаты по хэшу
find . -type f -exec md5sum {} \; | sort | uniq -d -w32
```

### 4.4 Кэширование

```python
import hashlib

def cache_key(data):
    """Генерирует ключ кэша для данных."""
    return hashlib.sha256(data.encode()).hexdigest()[:16]
```

---

## 5. Python и хэши

### 5.1 hashlib

```python
import hashlib

# Из строки
text = "Hello, World!"
md5_hash = hashlib.md5(text.encode()).hexdigest()
sha256_hash = hashlib.sha256(text.encode()).hexdigest()

print(f"MD5: {md5_hash}")
print(f"SHA-256: {sha256_hash}")
```

### 5.2 Хэш файла

```python
import hashlib

def file_hash(filepath, algorithm='sha256'):
    """Вычисляет хэш файла."""
    h = hashlib.new(algorithm)
    
    with open(filepath, 'rb') as f:
        # Читаем блоками для больших файлов
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    
    return h.hexdigest()

# Использование
print(file_hash('large_file.iso'))
print(file_hash('file.txt', 'md5'))
```

### 5.3 Сравнение файлов

```python
def files_equal(file1, file2):
    """Сравнивает файлы по SHA-256."""
    return file_hash(file1) == file_hash(file2)
```

---

## 6. Безопасность

### 6.1 НЕ используйте для

❌ Хранение паролей напрямую
❌ MD5/SHA-1 для безопасности

### 6.2 Для паролей

```python
# Используйте bcrypt, argon2 или scrypt
import bcrypt

password = b"secret_password"
hashed = bcrypt.hashpw(password, bcrypt.gensalt())

# Проверка
if bcrypt.checkpw(password, hashed):
    print("Password correct!")
```

---

## 💡 Key Takeaways

- **Хэш необратим**: Нельзя восстановить данные из хэша.

- **SHA-256 — современный стандарт**: MD5 и SHA-1 скомпрометированы.

- **Проверяйте загрузки**: Всегда сверяйте хэш с официальным.

- **Для паролей — специальные алгоритмы**: bcrypt, argon2, не SHA-256.

---

## 📚 Additional Resources

- [SHA-2 Wikipedia](https://en.wikipedia.org/wiki/SHA-2)
- [hashlib Python docs](https://docs.python.org/3/library/hashlib.html)
- [bcrypt](https://github.com/pyca/bcrypt/)

---


