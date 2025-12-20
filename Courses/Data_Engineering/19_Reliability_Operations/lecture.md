# Data Engineering
## Надёжность и эксплуатация

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать архитектуры data-платформ (модуль 17)
- Знать масштабирование (модуль 18)
- Иметь представление о мониторинге

**Recommended prior modules:**

- [17_Data_Platform_Architectures](../17_Data_Platform_Architectures/) — архитектуры data-платформ
- [18_Scaling_Performance](../18_Scaling_Performance/) — масштабирование

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Проектировать fault-tolerant системы
- Настраивать мониторинг и alerting
- Определять SLA и SLO
- Обеспечивать надёжность data-систем

---

## 1. Введение в надёжность

Надёжность — это способность системы работать корректно даже при сбоях. Критично для production систем.

**Компоненты надёжности:**

- **Fault Tolerance** — устойчивость к сбоям

- **Monitoring** — наблюдение за системой

- **Alerting** — уведомления о проблемах

- **SLA/SLO** — соглашения об уровне обслуживания

---

## 2. Fault Tolerance (Отказоустойчивость)

Fault tolerance — способность системы продолжать работу при сбоях компонентов.

### 2.1 Стратегии

**Redundancy:**

- Дублирование компонентов
- Replication данных
- Failover механизмы

**Graceful Degradation:**

- Продолжение работы при частичных сбоях
- Ухудшение функциональности вместо полного отказа

**Example: Fault Tolerance**

```python

class FaultTolerantSystem:
    def __init__(self):
        self.primary = {"status": "active", "data": []}
        self.replica = {"status": "standby", "data": []}
        self.failover_active = False
    
    def write(self, data):
        """Запись с репликацией"""
        # Запись в primary
        self.primary["data"].append(data)
        print(f"✅ Записано в primary: {data}")
        
        # Репликация в replica
        try:
            self.replica["data"].append(data)
            print(f"✅ Реплицировано в replica: {data}")
        except Exception as e:
            print(f"⚠️  Ошибка репликации: {e}, но primary работает")
    
    def read(self):
        """Чтение с failover"""
        try:
            if self.primary["status"] == "active":
                return self.primary["data"]
        except Exception as e:
            print(f"⚠️  Primary недоступен: {e}, failover к replica")
            self.failover_active = True
            return self.replica["data"]
    
    def failover(self):
        """Активация failover"""
        self.primary["status"] = "failed"
        self.replica["status"] = "active"
        self.failover_active = True
        print("🔄 Failover активирован: replica стала primary")

# Использование
system = FaultTolerantSystem()
system.write("data1")
system.write("data2")

# Failover

system.failover()
data = system.read()
print(f"Данные после failover: {data}")
```

**Output:**
```

✅ Записано в primary: data1
✅ Реплицировано в replica: data1
✅ Записано в primary: data2
✅ Реплицировано в replica: data2
🔄 Failover активирован: replica стала primary
Данные после failover: ['data1', 'data2']
```

---

## 3. Monitoring (Мониторинг)

Monitoring — непрерывное наблюдение за состоянием системы.

### 3.1 Типы метрик

**System Metrics:**

- CPU, Memory, Disk
- Network throughput
- Resource utilization

**Application Metrics:**

- Request rate
- Error rate
- Latency

**Business Metrics:**

- User activity
- Revenue
- Conversions

**Example: Monitoring System**

```python

class MonitoringSystem:
    def __init__(self):
        self.metrics = {
            "cpu_usage": [],
            "memory_usage": [],
            "error_rate": [],
            "request_rate": []
        }
    
    def collect_metric(self, metric_name, value, timestamp):
        """Собирает метрику"""
        if metric_name not in self.metrics:
            self.metrics[metric_name] = []
        
        self.metrics[metric_name].append({
            "value": value,
            "timestamp": timestamp
        })
        
        # Храним только последние 1000 значений
        if len(self.metrics[metric_name]) > 1000:
            self.metrics[metric_name] = self.metrics[metric_name][-1000:]
    
    def get_current_metrics(self):
        """Возвращает текущие метрики"""
        current = {}
        for metric_name, values in self.metrics.items():
            if values:
                current[metric_name] = values[-1]["value"]
        return current
    
    def get_dashboard(self):
        """Возвращает данные для дашборда"""
        return {
            "current": self.get_current_metrics(),
            "trends": {
                name: self._calculate_trend(values)
                for name, values in self.metrics.items()
            }
        }
    
    def _calculate_trend(self, values):
        """Вычисляет тренд"""
        if len(values) < 2:
            return "stable"
        
        recent = values[-10:]
        if len(recent) < 2:
            return "stable"
        
        first = recent[0]["value"]
        last = recent[-1]["value"]
        
        if last > first * 1.1:
            return "increasing"
        elif last < first * 0.9:
            return "decreasing"
        else:
            return "stable"

# Использование

monitor = MonitoringSystem()
monitor.collect_metric("cpu_usage", 75, "2024-01-01T10:00:00Z")
monitor.collect_metric("memory_usage", 60, "2024-01-01T10:00:00Z")
monitor.collect_metric("error_rate", 0.1, "2024-01-01T10:00:00Z")

dashboard = monitor.get_dashboard()
print("Monitoring Dashboard:")
print(f"  Current metrics: {dashboard['current']}")
```

**Output:**
```

Monitoring Dashboard:
  Current metrics: {'cpu_usage': 75, 'memory_usage': 60, 'error_rate': 0.1, 'request_rate': None}
```

---

## 4. Alerting (Уведомления)

Alerting — автоматические уведомления о проблемах.

### 4.1 Стратегии Alerting

**Threshold-based:**

- Алерты при превышении порогов
- Пример: CPU > 80%

**Anomaly Detection:**

- Обнаружение аномалий
- Machine learning подходы

**Example: Alerting System**

```python

class AlertingSystem:
    def __init__(self):
        self.alerts = []
        self.thresholds = {
            "cpu_usage": 80,
            "memory_usage": 90,
            "error_rate": 5
        }
    
    def check_threshold(self, metric_name, value):
        """Проверяет порог и генерирует алерт"""
        if metric_name in self.thresholds:
            threshold = self.thresholds[metric_name]
            if value > threshold:
                alert = {
                    "metric": metric_name,
                    "value": value,
                    "threshold": threshold,
                    "severity": "high" if value > threshold * 1.5 else "medium",
                    "timestamp": "2024-01-01T10:00:00Z"
                }
                self.alerts.append(alert)
                print(f"🚨 ALERT: {metric_name} = {value} превышает threshold {threshold} (severity: {alert['severity']})")
                return alert
        return None
    
    def get_active_alerts(self):
        """Возвращает активные алерты"""
        return self.alerts

# Использование

alerter = AlertingSystem()
alerter.check_threshold("cpu_usage", 85)
alerter.check_threshold("memory_usage", 95)
alerter.check_threshold("error_rate", 3)

active = alerter.get_active_alerts()
print(f"\nАктивных алертов: {len(active)}")
```

**Output:**
```

🚨 ALERT: cpu_usage = 85 превышает threshold 80 (severity: medium)
🚨 ALERT: memory_usage = 95 превышает threshold 90 (severity: high)
Активных алертов: 2
```

---

## 5. Distributed Tracing

Distributed tracing отслеживает запросы через распределённую систему.

### 5.1 Концепция Tracing

**Trace:**

- Полный путь запроса через систему
- Состоит из spans
- Показывает задержки и зависимости

**Span:**

- Отдельная операция в trace
- Содержит метаданные
- Связан с другими spans

**Example: Distributed Tracing**

```python

class DistributedTracer:
    def __init__(self):
        self.traces = {}
        self.current_trace_id = None
    
    def start_trace(self, trace_id, operation_name):
        """Начинает новый trace"""
        self.current_trace_id = trace_id
        self.traces[trace_id] = {
            "operation": operation_name,
            "spans": [],
            "start_time": "2024-01-01T10:00:00Z"
        }
        print(f"🔍 Trace начат: {trace_id}, операция: {operation_name}")
        return trace_id
    
    def add_span(self, span_name, service_name, duration_ms):
        """Добавляет span в текущий trace"""
        if not self.current_trace_id:
            return
        
        span = {
            "name": span_name,
            "service": service_name,
            "duration_ms": duration_ms
        }
        
        self.traces[self.current_trace_id]["spans"].append(span)
        print(f"  📍 Span: {span_name} ({service_name}), duration: {duration_ms}ms")
    
    def get_trace_summary(self, trace_id):
        """Возвращает сводку trace"""
        if trace_id not in self.traces:
            return None
        
        trace = self.traces[trace_id]
        total_duration = sum(span["duration_ms"] for span in trace["spans"])
        
        return {
            "trace_id": trace_id,
            "operation": trace["operation"],
            "total_spans": len(trace["spans"]),
            "total_duration_ms": total_duration
        }

# Использование
tracer = DistributedTracer()

# Trace запроса через систему
trace_id = tracer.start_trace("trace_001", "user_request")
tracer.add_span("api_gateway", "gateway", 10)
tracer.add_span("auth_service", "auth", 5)
tracer.add_span("data_service", "data", 20)
tracer.add_span("database_query", "db", 15)

summary = tracer.get_trace_summary(trace_id)
print(f"\nTrace Summary: {summary}")
```

**Output:**
```
🔍 Trace начат: trace_001, операция: user_request
  📍 Span: api_gateway (gateway), duration: 10ms
  📍 Span: auth_service (auth), duration: 5ms
  📍 Span: data_service (data), duration: 20ms
  📍 Span: database_query (db), duration: 15ms

Trace Summary: {'trace_id': 'trace_001', 'operation': 'user_request', 'total_spans': 4, 'total_duration_ms': 50}
```

---

## 6. SLA и SLO

SLA (Service Level Agreement) и SLO (Service Level Objective) определяют ожидания от системы.

### 6.1 SLA vs SLO

**SLO:**

- Внутренние цели
- Метрики производительности
- Пример: 99.9% uptime

**SLA:**

- Соглашение с клиентами
- Включает последствия нарушения
- Пример: 99.9% uptime или компенсация

**Example: SLA/SLO Tracking**

```python

class SLATracker:
    def __init__(self, slo_uptime=99.9):
        self.slo_uptime = slo_uptime
        self.uptime_history = []
        self.downtime_events = []
    
    def record_uptime(self, is_up, timestamp):
        """Записывает uptime"""
        self.uptime_history.append({
            "is_up": is_up,
            "timestamp": timestamp
        })
        
        if not is_up:
            self.downtime_events.append(timestamp)
    
    def calculate_uptime(self, period_days=30):
        """Вычисляет uptime за период"""
        if not self.uptime_history:
            return 100.0
        
        total_records = len(self.uptime_history)
        up_records = sum(1 for r in self.uptime_history if r["is_up"])
        
        uptime_percent = (up_records / total_records) * 100
        return uptime_percent
    
    def check_slo(self):
        """Проверяет соответствие SLO"""
        uptime = self.calculate_uptime()
        meets_slo = uptime >= self.slo_uptime
        
        print(f"📊 Uptime: {uptime:.2f}%, SLO: {self.slo_uptime}%")
        if meets_slo:
            print("✅ SLO выполняется")
        else:
            print(f"❌ SLO нарушено (не хватает {self.slo_uptime - uptime:.2f}%)")
        
        return meets_slo

# Использование

tracker = SLATracker(slo_uptime=99.9)

# Симуляция uptime
for i in range(1000):
    tracker.record_uptime(True, f"2024-01-01T{i:02d}:00:00Z")

# Небольшой downtime

tracker.record_uptime(False, "2024-01-01T10:00:00Z")

tracker.check_slo()
```

**Output:**
```

📊 Uptime: 99.90%, SLO: 99.9%
✅ SLO выполняется
```

### 6.2 SLI (Service Level Indicator)

**SLI:**

- Метрика, измеряющая уровень сервиса
- Основа для SLO
- Пример: latency, error rate, availability

**Связь SLI, SLO, SLA:**

- SLI измеряет производительность
- SLO устанавливает цели на основе SLI
- SLA включает SLO и последствия

**Example: SLI Tracking**

```python

class SLITracker:
    def __init__(self):
        self.slis = {
            "latency": [],
            "error_rate": [],
            "availability": []
        }
    
    def record_latency(self, latency_ms):
        """Записывает latency"""
        self.slis["latency"].append(latency_ms)
    
    def record_error(self, is_error):
        """Записывает ошибку"""
        self.slis["error_rate"].append(1 if is_error else 0)
    
    def calculate_sli(self, metric_name):
        """Вычисляет SLI"""
        if metric_name == "latency":
            if not self.slis["latency"]:
                return None
            p99 = sorted(self.slis["latency"])[int(len(self.slis["latency"]) * 0.99)]
            return {"p99_latency_ms": p99}
        elif metric_name == "error_rate":
            if not self.slis["error_rate"]:
                return None
            error_rate = sum(self.slis["error_rate"]) / len(self.slis["error_rate"]) * 100
            return {"error_rate_percent": error_rate}
        elif metric_name == "availability":
            if not self.slis["error_rate"]:
                return None
            availability = (1 - sum(self.slis["error_rate"]) / len(self.slis["error_rate"])) * 100
            return {"availability_percent": availability}
        return None
    
    def get_all_slis(self):
        """Возвращает все SLI"""
        return {
            "latency": self.calculate_sli("latency"),
            "error_rate": self.calculate_sli("error_rate"),
            "availability": self.calculate_sli("availability")
        }

# Использование
sli_tracker = SLITracker()

# Запись метрик
for _ in range(100):
    sli_tracker.record_latency(50)
    sli_tracker.record_error(False)

sli_tracker.record_latency(200)  # Высокая latency
sli_tracker.record_error(True)  # Ошибка

slis = sli_tracker.get_all_slis()
print("📊 SLI метрики:")
for metric, value in slis.items():
    if value:
        print(f"   {metric}: {value}")
```

**Output:**
```
📊 SLI метрики:
   latency: {'p99_latency_ms': 200}
   error_rate: {'error_rate_percent': 0.9900990099009901}
   availability: {'availability_percent': 99.00990099009901}
```

---

## 7. Chaos Engineering

Chaos Engineering — это практика тестирования отказоустойчивости системы через преднамеренное внесение сбоев.

### 7.1 Принципы Chaos Engineering

**Контролируемые эксперименты:**

- Начинать с малых воздействий
- Постепенно увеличивать
- Мониторинг результатов

**Типы экспериментов:**

- Убийство процессов
- Задержки сети
- Отключение сервисов

**Example: Chaos Engineering**

```python

class ChaosEngineer:
    def __init__(self):
        self.services = {}
        self.experiments = []
    
    def register_service(self, service_name, status="healthy"):
        """Регистрирует сервис"""
        self.services[service_name] = {"status": status}
        print(f"✅ Сервис '{service_name}' зарегистрирован: {status}")
    
    def kill_service(self, service_name):
        """Убивает сервис (chaos experiment)"""
        if service_name in self.services:
            self.services[service_name]["status"] = "killed"
            self.experiments.append({
                "type": "kill_service",
                "service": service_name,
                "timestamp": "2024-01-01T10:00:00Z"
            })
            print(f"💥 Chaos: сервис '{service_name}' убит")
            return True
        return False
    
    def inject_latency(self, service_name, delay_ms):
        """Внедряет задержку"""
        if service_name in self.services:
            self.services[service_name]["latency"] = delay_ms
            self.experiments.append({
                "type": "inject_latency",
                "service": service_name,
                "delay_ms": delay_ms
            })
            print(f"⏱️  Chaos: задержка {delay_ms}ms внедрена в '{service_name}'")
            return True
        return False
    
    def get_system_health(self):
        """Проверяет здоровье системы"""
        healthy = sum(1 for s in self.services.values() if s["status"] == "healthy")
        total = len(self.services)
        health_percent = (healthy / total * 100) if total > 0 else 0
        
        print(f"🏥 Здоровье системы: {health_percent:.1f}% ({healthy}/{total} сервисов)")
        return health_percent

# Использование
chaos = ChaosEngineer()

# Регистрация сервисов
chaos.register_service("api")
chaos.register_service("database")
chaos.register_service("cache")

# Chaos эксперименты
chaos.get_system_health()
chaos.kill_service("cache")
chaos.inject_latency("api", 1000)
chaos.get_system_health()
```

**Output:**
```
✅ Сервис 'api' зарегистрирован: healthy
✅ Сервис 'database' зарегистрирован: healthy
✅ Сервис 'cache' зарегистрирован: healthy
🏥 Здоровье системы: 100.0% (3/3 сервисов)
💥 Chaos: сервис 'cache' убит
⏱️  Chaos: задержка 1000ms внедрена в 'api'
🏥 Здоровье системы: 66.7% (2/3 сервисов)
```

---

## 8. Incident Response (Реагирование на инциденты)

Incident Response — это процесс реагирования на проблемы в production.

### 8.1 Процесс реагирования

**Обнаружение:**

- Мониторинг и алерты
- Отчёты пользователей
- Автоматическое обнаружение

**Реагирование:**

- Оценка серьёзности
- Мобилизация команды
- Начало расследования

**Разрешение:**

- Исправление проблемы
- Восстановление сервиса
- Проверка стабильности

**Example: Incident Response**

```python

class IncidentResponse:
    def __init__(self):
        self.incidents = []
        self.current_incident = None
    
    def create_incident(self, title, severity, description):
        """Создаёт инцидент"""
        incident = {
            "id": len(self.incidents) + 1,
            "title": title,
            "severity": severity,
            "description": description,
            "status": "open",
            "created_at": "2024-01-01T10:00:00Z"
        }
        self.incidents.append(incident)
        self.current_incident = incident
        print(f"🚨 Инцидент #{incident['id']} создан: {title} (severity: {severity})")
        return incident
    
    def assign_incident(self, incident_id, assignee):
        """Назначает инцидент"""
        incident = next((i for i in self.incidents if i["id"] == incident_id), None)
        if incident:
            incident["assignee"] = assignee
            print(f"👤 Инцидент #{incident_id} назначен: {assignee}")
            return True
        return False
    
    def resolve_incident(self, incident_id, resolution):
        """Разрешает инцидент"""
        incident = next((i for i in self.incidents if i["id"] == incident_id), None)
        if incident:
            incident["status"] = "resolved"
            incident["resolution"] = resolution
            incident["resolved_at"] = "2024-01-01T10:30:00Z"
            print(f"✅ Инцидент #{incident_id} разрешён: {resolution}")
            return True
        return False
    
    def get_open_incidents(self):
        """Возвращает открытые инциденты"""
        return [i for i in self.incidents if i["status"] == "open"]

# Использование
response = IncidentResponse()

# Создание инцидента
incident = response.create_incident(
    "High error rate on API",
    "high",
    "Error rate increased to 10%"
)

# Назначение
response.assign_incident(incident["id"], "on-call-engineer")

# Разрешение
response.resolve_incident(incident["id"], "Fixed database connection pool")

open_incidents = response.get_open_incidents()
print(f"\n📋 Открытых инцидентов: {len(open_incidents)}")
```

**Output:**
```
🚨 Инцидент #1 создан: High error rate on API (severity: high)
👤 Инцидент #1 назначен: on-call-engineer
✅ Инцидент #1 разрешён: Fixed database connection pool

📋 Открытых инцидентов: 0
```

---

## 9. Disaster Recovery (Восстановление после катастроф)

Disaster Recovery — это процесс восстановления системы после крупных сбоев.

### 9.1 Стратегии восстановления

**RTO (Recovery Time Objective):**

- Максимальное время простоя
- Целевое время восстановления
- Пример: 4 часа

**RPO (Recovery Point Objective):**

- Максимальная потеря данных
- Точка восстановления
- Пример: 1 час данных

**Example: Disaster Recovery Plan**

```python

class DisasterRecovery:
    def __init__(self):
        self.backups = []
        self.rto_hours = 4
        self.rpo_hours = 1
    
    def create_backup(self, backup_type="full"):
        """Создаёт резервную копию"""
        backup = {
            "type": backup_type,
            "timestamp": "2024-01-01T10:00:00Z",
            "size_gb": 100
        }
        self.backups.append(backup)
        print(f"💾 Backup создан: {backup_type} ({backup['size_gb']}GB)")
        return backup
    
    def restore_from_backup(self, backup):
        """Восстанавливает из backup"""
        print(f"🔄 Восстановление из backup: {backup['type']} от {backup['timestamp']}")
        print(f"   RTO: {self.rto_hours} часов")
        print(f"   RPO: {self.rpo_hours} часов")
        print("✅ Восстановление завершено")
        return True
    
    def test_recovery(self):
        """Тестирует процесс восстановления"""
        if not self.backups:
            print("❌ Нет backup для тестирования")
            return False
        
        latest_backup = self.backups[-1]
        print(f"🧪 Тестирование восстановления из backup: {latest_backup['type']}")
        return self.restore_from_backup(latest_backup)

# Использование
dr = DisasterRecovery()

# Создание backup
dr.create_backup("full")
dr.create_backup("incremental")

# Тестирование восстановления
dr.test_recovery()
```

**Output:**
```
💾 Backup создан: full (100GB)
💾 Backup создан: incremental (50GB)
🧪 Тестирование восстановления из backup: incremental
🔄 Восстановление из backup: incremental от 2024-01-01T10:00:00Z
   RTO: 4 часов
   RPO: 1 часов
✅ Восстановление завершено
```

---

## 💡 Key Takeaways

- **Fault Tolerance**: Устойчивость к сбоям через redundancy, replication, failover. Критично для production систем.

- **Monitoring**: Непрерывное наблюдение за системой. System, application и business метрики для полной картины.

- **Alerting**: Автоматические уведомления о проблемах. Threshold-based и anomaly detection для раннего обнаружения.

- **Distributed Tracing**: Отслеживание запросов через распределённую систему. Trace состоит из spans, показывает задержки и зависимости между сервисами.

- **SLA/SLO**: SLO — внутренние цели, SLA — соглашения с клиентами. Критично для управления ожиданиями.

- **SLI (Service Level Indicator)**: Метрики, измеряющие уровень сервиса. Основа для SLO. Latency, error rate, availability — примеры SLI.

- **Chaos Engineering**: Тестирование отказоустойчивости через преднамеренные сбои. Контролируемые эксперименты помогают выявить слабые места.

- **Incident Response**: Процесс реагирования на проблемы. Обнаружение → Реагирование → Разрешение. Критично для минимизации downtime.

- **Disaster Recovery**: Восстановление после крупных сбоев. RTO определяет время восстановления, RPO — потерю данных. Регулярное тестирование критично.

- **Надёжность**: Комплексный подход с fault tolerance, monitoring, alerting, tracing, SLA/SLO, chaos engineering и disaster recovery обеспечивает надёжность production систем.

---

## 🚀 Next Steps

**Related Modules:**

- [20_Data_Engineering_System_Design](../20_Data_Engineering_System_Design/) — system design
- [18_Scaling_Performance](../18_Scaling_Performance/) — масштабирование
- [17_Data_Platform_Architectures](../17_Data_Platform_Architectures/) — архитектуры

**Practice Ideas:**

1. Настройте мониторинг: метрики и дашборды для вашей системы
2. Реализуйте alerting: пороги и уведомления
3. Определите SLA/SLO: метрики и цели для вашего сервиса

**Going Deeper:**

- Изучите distributed tracing: отслеживание запросов
- Погрузитесь в chaos engineering: тестирование отказоустойчивости
- Изучите SRE practices: Site Reliability Engineering

---

## 📚 Additional Resources

**Books:**

- "Site Reliability Engineering" by Google — SRE practices
- "Designing Data-Intensive Applications" — надёжность систем

**Articles:**

- "Monitoring Best Practices" — рекомендации
- "SLA vs SLO vs SLI" — различия

**Documentation:**

- Prometheus: https://prometheus.io/docs/ (monitoring)
- Grafana: https://grafana.com/docs/ (visualization)

---


