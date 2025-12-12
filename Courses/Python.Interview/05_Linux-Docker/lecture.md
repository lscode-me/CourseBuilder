# Linux и Docker для Python-разработчика

## Что нужно знать для интервью

На интервью могут проверить базовые навыки работы с Linux и Docker. Это особенно важно для позиций Backend, Infrastructure и DevOps. Ожидается уверенное владение командной строкой.

---

## 🔑 Ключевые команды Linux

### Навигация и файлы

```bash
ls -la          # Список файлов с правами и скрытыми
cd /path        # Сменить директорию
pwd             # Текущая директория
mkdir -p dir    # Создать директорию (с родителями)
rm -rf dir      # Удалить рекурсивно (осторожно!)
cp -r src dst   # Копировать рекурсивно
mv src dst      # Переместить/переименовать
cat file        # Показать содержимое
less file       # Постраничный просмотр
head -n 10 file # Первые 10 строк
tail -f file    # Последние строки (follow)
```

### Права доступа

```bash
chmod 755 file  # rwxr-xr-x
chmod +x file   # Добавить право выполнения
chown user:group file  # Сменить владельца

# Формат: rwx rwx rwx = user group others
# r=4, w=2, x=1
# 755 = rwxr-xr-x
# 644 = rw-r--r--
```

### Управление сервисами (systemctl)

```bash
sudo systemctl start nginx    # Запустить
sudo systemctl stop nginx     # Остановить
sudo systemctl restart nginx  # Перезапустить
sudo systemctl status nginx   # Статус
sudo systemctl enable nginx   # Автозапуск при загрузке
```

### Диагностика

```bash
df -h           # Использование дисков
du -sh /path    # Размер директории
free -h         # Использование памяти
top / htop      # Процессы
ps aux          # Список процессов
kill -9 PID     # Завершить процесс
```

### Пакетные менеджеры

```bash
# Debian/Ubuntu
sudo apt update && sudo apt install package

# CentOS/RHEL
sudo yum install package

# Fedora/RHEL 8+
sudo dnf install package
```

---

## 🐳 Docker основы

### Ключевые команды

```bash
docker build -t myapp .       # Собрать образ
docker run -d -p 8080:80 myapp  # Запустить контейнер
docker ps                     # Запущенные контейнеры
docker ps -a                  # Все контейнеры
docker stop container_id      # Остановить
docker rm container_id        # Удалить контейнер
docker images                 # Список образов
docker rmi image_id           # Удалить образ
docker logs container_id      # Логи контейнера
docker exec -it container bash  # Зайти в контейнер
```

### Базовый Dockerfile

```dockerfile
FROM python:3.11

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "main.py"]
```

---

## 💻 Задача: Оптимизация Dockerfile

### Неоптимальный Dockerfile

```dockerfile
FROM python:3.11

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "main.py"]
```

### Оптимизированный Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Сначала копируем только requirements
COPY requirements.txt .

# Устанавливаем зависимости (кэшируется если requirements не изменился)
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Теперь копируем код
COPY . .

# Не-root пользователь
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

CMD ["python", "main.py"]
```

**Оптимизации:**
1. **python:3.11-slim** — меньший базовый образ
2. **COPY requirements.txt первым** — кэширование слоёв
3. **Объединение RUN** — меньше слоёв
4. **--no-cache-dir** — не хранить pip cache
5. **Non-root user** — безопасность
6. **.dockerignore** — исключить `.git`, `__pycache__`, `.env`

---

## ❓ Типичные вопросы на интервью

### Q: Как диагностировать "Permission denied"?

**A:**
```bash
ls -la file      # Проверить права
whoami           # Текущий пользователь
groups           # Группы пользователя
chmod +x file    # Дать право выполнения
sudo command     # Выполнить от root
```

### Q: Как проверить что занимает диск?

**A:**
```bash
df -h            # Общее использование
du -sh /*        # Размер директорий в корне
du -sh * | sort -hr | head  # Топ больших директорий
```

### Q: Разница между apt, yum, dnf?

**A:**
| apt | yum | dnf |
|-----|-----|-----|
| Debian/Ubuntu | CentOS/RHEL 7 | Fedora/RHEL 8+ |
| .deb пакеты | .rpm пакеты | .rpm пакеты |
| dpkg низкоуровневый | rpm низкоуровневый | rpm низкоуровневый |

### Q: Зачем .dockerignore?

**A:**
> "Исключает файлы из build context. Ускоряет сборку и уменьшает образ. Обычно исключают `.git`, `__pycache__`, `.env`, `node_modules`, `venv`."

---

## 📚 Дополнительные материалы

- [Docker Documentation](https://docs.docker.com/)
- [Linux Command Line Basics](https://ubuntu.com/tutorials/command-line-for-beginners)
- "The Docker Book" by James Turnbull

---

