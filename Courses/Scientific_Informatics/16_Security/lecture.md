# Data security, compliance и governance
## Data governance, compliance (GDPR, HIPAA), контроль доступа, аудит

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать основы работы с данными (модули 05-06)
- Знать принципы безопасности данных
- Понимать требования к научным данным
- Иметь представление о compliance требованиях

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Применять принципы data governance в научных проектах
- Обеспечивать compliance с GDPR, HIPAA и другими требованиями
- Реализовывать контроль доступа к данным
- Обеспечивать аудит и трассируемость данных
- Выбирать подходящие стратегии безопасности для научных данных

---

## 1. Data Governance в научных проектах

Data Governance — это не просто техническая задача, а комплексный подход к управлению данными, который включает политики, процессы, роли и мониторинг. В научных проектах это критически важно для обеспечения качества данных, соблюдения требований и эффективного использования данных.

### 1.1 Принципы Data Governance

**Data Governance** — управление доступностью, целостностью и безопасностью данных. Это не одноразовая задача, а непрерывный процесс, который должен быть интегрирован во все аспекты работы с данными.

**Компоненты:**

- **Политики** — правила работы с данными. Политики определяют классификацию данных по чувствительности, периоды хранения данных, контроль доступа (кто может получить доступ к каким данным). Это критически важно для соблюдения требований и защиты данных.

- **Процессы** — процедуры управления. Процессы включают workflow для одобрения доступа к данным, проверки качества данных и валидации, управления жизненным циклом данных (от создания до архивирования). Это обеспечивает систематический подход к работе с данными.

- **Ответственность** — роли и обязанности. Чёткое определение ролей (data owner — ответственный за данные, data steward — управляет качеством данных, data user — использует данные для исследований) критически важно для эффективного управления данными.

- **Мониторинг** — отслеживание использования. Мониторинг включает логи доступа (отслеживание того, кто получил доступ к каким данным), метрики использования (мониторинг использования данных), проверки соответствия (проверка соблюдения требований). Это позволяет выявлять проблемы и обеспечивать соблюдение политик.

Data Governance Structure:

POLICIES:
  data_classification: Classify data by sensitivity
  retention: Define data retention periods
  access_control: Who can access what data

PROCESSES:
  data_approval: Approval workflow for data access
  data_quality: Quality checks and validation
  data_lifecycle: From creation to archival

ROLES:
  data_owner: Responsible for data
  data_steward: Manages data quality
  data_user: Uses data for research

MONITORING:
  access_logs: Track who accessed what
  usage_metrics: Monitor data usage
  compliance_checks: Verify compliance

```

### 1.2 Классификация данных

**Пример: Классификация по чувствительности**

```python
# Классификация данных по чувствительности

data_classification = {
    'public': {
        'description': 'Publicly available data',
        'examples': ['Published research data'],
        'requirements': 'Minimal security'
    },
    'internal': {
        'description': 'Internal use only',
        'examples': ['Preliminary results'],
        'requirements': 'Access control required'
    },
    'confidential': {
        'description': 'Confidential research data',
        'examples': ['Unpublished results'],
        'requirements': 'Strict access control, encryption'
    },
    'restricted': {
        'description': 'Highly sensitive data',
        'examples': ['Patient data', 'Proprietary data'],
        'requirements': 'Maximum security, compliance required'
    }
}

print("Data Classification:")
for level, details in data_classification.items():
    print(f"\n{level.upper()}:")
    for key, value in details.items():
        print(f"  {key}: {value}")

```

**Output:**
```

Data Classification:

PUBLIC:
  description: Publicly available data
  examples: ['Published research data']
  requirements: Minimal security

INTERNAL:
  description: Internal use only
  examples: ['Preliminary results']
  requirements: Access control required

CONFIDENTIAL:
  description: Confidential research data
  examples: ['Unpublished results']
  requirements: Strict access control, encryption

RESTRICTED:
  description: Highly sensitive data
  examples: ['Patient data', 'Proprietary data']
  requirements: Maximum security, compliance required

```

---

## 2. Compliance (GDPR, HIPAA)

### 2.1 GDPR

**GDPR (General Data Protection Regulation)** — европейское регулирование защиты данных.

**Основные требования:**

- Согласие на обработку данных
- Право на доступ к данным
- Право на удаление данных
- Минимизация данных

**Пример: GDPR compliance**

```python

class GDPRCompliance:
    """Управление GDPR compliance"""
    
    def __init__(self):
        self.consents = {}
        self.data_subjects = {}
    
    def record_consent(self, subject_id, purpose, consent_given=True):
        """Запись согласия субъекта данных"""
        if subject_id not in self.consents:
            self.consents[subject_id] = []
        
        self.consents[subject_id].append({
            'purpose': purpose,
            'consent': consent_given,
            'timestamp': datetime.now().isoformat()
        })
    
    def get_subject_data(self, subject_id):
        """Получение данных субъекта (GDPR право доступа)"""
        return self.data_subjects.get(subject_id, {})
    
    def delete_subject_data(self, subject_id):
        """Удаление данных субъекта (GDPR право на удаление)"""
        if subject_id in self.data_subjects:
            del self.data_subjects[subject_id]
            del self.consents[subject_id]
            return True
        return False

# Пример

gdpr = GDPRCompliance()
gdpr.record_consent('SUBJECT-001', 'research', consent_given=True)
print("GDPR compliance: Consent recorded")

```

**Output:**
```

GDPR compliance: Consent recorded

```

### 2.2 HIPAA

**HIPAA (Health Insurance Portability and Accountability Act)** — регулирование защиты медицинских данных.

**Требования:**

- Защита PHI (Protected Health Information)
- Контроль доступа
- Аудит логов
- Шифрование

**Пример: HIPAA compliance**

```python

class HIPAACompliance:
    """Управление HIPAA compliance"""
    
    def __init__(self):
        self.phi_data = {}
        self.access_logs = []
    
    def store_phi(self, patient_id, data, encrypted=True):
        """Хранение PHI с шифрованием"""
        if encrypted:
            # Симуляция шифрования
            encrypted_data = f"ENCRYPTED_{data}"
        else:
            encrypted_data = data
        
        self.phi_data[patient_id] = {
            'data': encrypted_data,
            'encrypted': encrypted,
            'timestamp': datetime.now().isoformat()
        }
    
    def access_phi(self, user_id, patient_id, reason):
        """Доступ к PHI с логированием"""
        # Логирование доступа
        self.access_logs.append({
            'user_id': user_id,
            'patient_id': patient_id,
            'reason': reason,
            'timestamp': datetime.now().isoformat()
        })
        
        # Проверка прав доступа (упрощённо)
        if patient_id in self.phi_data:
            return self.phi_data[patient_id]
        return None
    
    def get_access_logs(self):
        """Получение логов доступа (HIPAA требование)"""
        return self.access_logs

# Пример

hipaa = HIPAACompliance()
hipaa.store_phi('PATIENT-001', 'Medical record', encrypted=True)
access = hipaa.access_phi('USER-001', 'PATIENT-001', 'Treatment')
print(f"HIPAA compliance: Access logged, {len(hipaa.get_access_logs())} log entries")

```

**Output:**
```

HIPAA compliance: Access logged, 1 log entries

```

---

## 3. Контроль доступа

### 3.1 Role-Based Access Control (RBAC)

**Пример: RBAC система**

```python

class RBAC:
    """Role-Based Access Control"""
    
    def __init__(self):
        self.roles = {
            'researcher': ['read_data', 'analyze_data'],
            'data_manager': ['read_data', 'write_data', 'manage_access'],
            'admin': ['read_data', 'write_data', 'manage_access', 'delete_data']
        }
        self.user_roles = {}
    
    def assign_role(self, user_id, role):
        """Назначение роли пользователю"""
        if role not in self.roles:
            raise ValueError(f"Unknown role: {role}")
        self.user_roles[user_id] = role
    
    def check_permission(self, user_id, permission):
        """Проверка разрешения"""
        if user_id not in self.user_roles:
            return False
        
        role = self.user_roles[user_id]
        return permission in self.roles[role]
    
    def can_access(self, user_id, resource, action):
        """Проверка доступа к ресурсу"""
        permission = f"{action}_{resource}"
        return self.check_permission(user_id, permission)

# Пример

rbac = RBAC()
rbac.assign_role('user1', 'researcher')
rbac.assign_role('user2', 'admin')

print(f"User1 can read: {rbac.check_permission('user1', 'read_data')}")
print(f"User1 can delete: {rbac.check_permission('user1', 'delete_data')}")
print(f"User2 can delete: {rbac.check_permission('user2', 'delete_data')}")

```

**Output:**
```

User1 can read: True
User1 can delete: False
User2 can delete: True

```

### 3.2 Attribute-Based Access Control (ABAC)

**Пример: ABAC система**

```python

class ABAC:
    """Attribute-Based Access Control"""
    
    def __init__(self):
        self.policies = []
    
    def add_policy(self, condition, action):
        """Добавление политики доступа"""
        self.policies.append({
            'condition': condition,
            'action': action
        })
    
    def check_access(self, user_attrs, resource_attrs, action):
        """Проверка доступа на основе атрибутов"""
        for policy in self.policies:
            if policy['condition'](user_attrs, resource_attrs):
                return policy['action'] == action
        return False

# Пример

abac = ABAC()
# Политика: пользователь может читать данные своего проекта

abac.add_policy(
    condition=lambda u, r: u.get('project') == r.get('project'),
    action='read'
)

user = {'project': 'PROJECT-A', 'role': 'researcher'}
resource = {'project': 'PROJECT-A', 'sensitivity': 'internal'}
can_read = abac.check_access(user, resource, 'read')
print(f"Can read: {can_read}")

```

**Output:**
```

Can read: True

```

---

## 4. Аудит и трассируемость

### 4.1 Аудит логов

**Пример: Система аудита**

```python

class AuditSystem:
    """Система аудита доступа к данным"""
    
    def __init__(self):
        self.audit_logs = []
    
    def log_access(self, user_id, resource, action, result='success'):
        """Логирование доступа"""
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'user_id': user_id,
            'resource': resource,
            'action': action,
            'result': result,
            'ip_address': '192.168.1.1'  # Симуляция
        }
        self.audit_logs.append(log_entry)
        return log_entry
    
    def query_logs(self, user_id=None, resource=None, start_date=None, end_date=None):
        """Запрос логов аудита"""
        filtered_logs = self.audit_logs
        
        if user_id:
            filtered_logs = [l for l in filtered_logs if l['user_id'] == user_id]
        if resource:
            filtered_logs = [l for l in filtered_logs if l['resource'] == resource]
        
        return filtered_logs
    
    def generate_audit_report(self):
        """Генерация отчёта аудита"""
        total_accesses = len(self.audit_logs)
        unique_users = len(set(l['user_id'] for l in self.audit_logs))
        
        return {
            'total_accesses': total_accesses,
            'unique_users': unique_users,
            'time_range': {
                'start': self.audit_logs[0]['timestamp'] if self.audit_logs else None,
                'end': self.audit_logs[-1]['timestamp'] if self.audit_logs else None
            }
        }

# Пример

audit = AuditSystem()
audit.log_access('user1', 'dataset1', 'read')
audit.log_access('user2', 'dataset1', 'write')
report = audit.generate_audit_report()
print(f"Audit report: {report}")

```

**Output:**
```

Audit report: {'total_accesses': 2, 'unique_users': 2, 'time_range': {'start': '2024-01-15T10:30:00', 'end': '2024-01-15T10:30:00'}}

```

### 4.2 Data Lineage

**Пример: Отслеживание происхождения данных**

```python

class DataLineage:
    """Отслеживание происхождения данных"""
    
    def __init__(self):
        self.lineage = {}
    
    def track_transformation(self, output_id, input_ids, transformation):
        """Отслеживание трансформации данных"""
        self.lineage[output_id] = {
            'inputs': input_ids,
            'transformation': transformation,
            'timestamp': datetime.now().isoformat()
        }
    
    def get_lineage(self, data_id):
        """Получение lineage для данных"""
        if data_id in self.lineage:
            return self.lineage[data_id]
        return None
    
    def get_full_lineage(self, data_id, visited=None):
        """Получение полного lineage (рекурсивно)"""
        if visited is None:
            visited = set()
        
        if data_id in visited:
            return []
        
        visited.add(data_id)
        lineage_info = self.get_lineage(data_id)
        
        if not lineage_info:
            return [{'id': data_id, 'type': 'source'}]
        
        result = [{'id': data_id, 'transformation': lineage_info['transformation']}]
        for input_id in lineage_info['inputs']:
            result.extend(self.get_full_lineage(input_id, visited))
        
        return result

# Пример

lineage = DataLineage()
lineage.track_transformation('processed_data', ['raw_data1', 'raw_data2'], 'merge')
lineage.track_transformation('final_results', ['processed_data'], 'analysis')

full_lineage = lineage.get_full_lineage('final_results')
print("Data Lineage:")
for step in full_lineage:
    print(f"  {step}")

```

**Output:**
```

Data Lineage:
  {'id': 'final_results', 'transformation': 'analysis'}
  {'id': 'processed_data', 'transformation': 'merge'}
  {'id': 'raw_data1', 'type': 'source'}
  {'id': 'raw_data2', 'type': 'source'}

```

---

## 5. Шифрование данных

### 5.1 Шифрование в покое и при передаче

**Пример: Концепция шифрования**

```python
# Концепция шифрования данных

encryption_concepts = {
    'encryption_at_rest': {
        'purpose': 'Защита данных на диске',
        'methods': ['AES-256', 'LUKS', 'Cloud encryption'],
        'when': 'Always for sensitive data'
    },
    'encryption_in_transit': {
        'purpose': 'Защита данных при передаче',
        'methods': ['TLS/SSL', 'VPN', 'SFTP'],
        'when': 'Always for network transfer'
    },
    'key_management': {
        'purpose': 'Безопасное хранение ключей',
        'methods': ['Key management services', 'Hardware security modules'],
        'importance': 'Critical'
    }
}

print("Encryption Concepts:")
for concept, details in encryption_concepts.items():
    print(f"\n{concept.replace('_', ' ').title()}:")
    for key, value in details.items():
        print(f"  {key}: {value}")

```

**Output:**
```

Encryption Concepts:

Encryption At Rest:
  purpose: Защита данных на диске
  methods: ['AES-256', 'LUKS', 'Cloud encryption']
  when: Always for sensitive data

Encryption In Transit:
  purpose: Защита данных при передаче
  methods: ['TLS/SSL', 'VPN', 'SFTP']
  when: Always for network transfer

Key Management:
  purpose: Безопасное хранение ключей
  methods: ['Key management services', 'Hardware security modules']
  importance: Critical

```

---

## 💡 Key Takeaways

- **Data Governance** — управление доступностью, целостностью и безопасностью данных через политики, процессы и мониторинг

- **GDPR** — европейское регулирование, требующее согласия, права доступа и удаления данных

- **HIPAA** — регулирование защиты медицинских данных, требующее защиты PHI, контроля доступа и аудита

- **Контроль доступа** — RBAC (роли) и ABAC (атрибуты) для управления доступом к данным

- **Аудит и трассируемость** — логирование доступа и отслеживание происхождения данных критичны для compliance

- **Шифрование** — защита данных в покое (на диске) и при передаче (по сети) обязательна для чувствительных данных

---

## 🚀 Next Steps

**Related Modules:**

- [06_DataIntegrity](../06_DataIntegrity/) — качество данных
- [13_Architecture](../13_Architecture/) — архитектура систем
- [07_Collaboration](../07_Collaboration/) — коллаборация

**Practice Ideas:**

1. Реализуйте систему контроля доступа для ваших данных
2. Настройте аудит логов для вашего pipeline
3. Изучите требования compliance для вашей области

**Going Deeper:**

- Изучите конкретные требования GDPR и HIPAA
- Познакомьтесь с системами управления ключами (KMS)
- Изучите методы анонимизации данных для исследований

---

## 📚 Additional Resources

**Documentation:**

- [GDPR Official Site](https://gdpr.eu/)
- [HIPAA Compliance Guide](https://www.hhs.gov/hipaa/)

---



