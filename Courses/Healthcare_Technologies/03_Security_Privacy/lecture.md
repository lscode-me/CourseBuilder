# Безопасность и Конфиденциальность в Healthcare

---

## Введение

Безопасность медицинских данных — критически важный аспект Healthcare IT. Утечка медицинских данных может привести к серьёзным последствиям для пациентов и огромным штрафам для организаций.

---

## 1. HIPAA — Health Insurance Portability and Accountability Act

### 1.1 Что такое HIPAA?

Американский закон, регулирующий защиту медицинских данных.

**Основные компоненты:**
- **Privacy Rule** — конфиденциальность PHI
- **Security Rule** — технические меры защиты
- **Breach Notification Rule** — уведомление о нарушениях

### 1.2 Protected Health Information (PHI)

PHI — любая информация, которая может идентифицировать пациента:

**18 идентификаторов:**
1. Имя
2. Адрес (улица, город, zip-code)
3. Даты (рождения, визитов, смерти)
4. Телефон
5. Email
6. SSN (Social Security Number)
7. Medical Record Number
8. Health Plan Number
9. Account Number
10. Certificate/License Number
11. Vehicle ID
12. Device Serial Number
13. URL
14. IP Address
15. Biometric identifiers
16. Фото лица
17. Любой уникальный идентификатор

### 1.3 De-identification

Удаление PHI для использования данных в исследованиях.

**Методы:**
1. **Safe Harbor** — удалить все 18 идентификаторов
2. **Expert Determination** — эксперт подтверждает, что риск минимален

```python
def deidentify_patient_data(patient):
    """Простая де-идентификация"""
    return {
        'age_group': calculate_age_group(patient['dob']),
        'gender': patient['gender'],
        'diagnosis': patient['diagnosis'],
        'zip_3': patient['zip'][:3],  # Только первые 3 цифры
        # Все имена, даты, номера удалены
    }
```

---

## 2. GDPR в Healthcare

### 2.1 Основные Принципы

**GDPR** (General Data Protection Regulation) — европейский закон о защите данных.

**Ключевые права:**
- **Right to Access** — пациент может запросить свои данные
- **Right to Erasure** ("Right to be Forgotten")
- **Right to Portability** — перенос данных
- **Right to Rectification** — исправление ошибок

### 2.2 Consent Management

```python
class ConsentManager:
    def __init__(self):
        self.consents = {}
    
    def record_consent(self, patient_id, purpose, granted=True):
        """Записать согласие пациента"""
        self.consents[patient_id] = {
            'purpose': purpose,
            'granted': granted,
            'timestamp': datetime.now(),
            'version': '1.0'
        }
    
    def can_process_data(self, patient_id, purpose):
        """Проверить разрешение на обработку"""
        consent = self.consents.get(patient_id)
        return consent and consent['granted'] and consent['purpose'] == purpose
```

---

## 3. Технические Меры Безопасности

### 3.1 Encryption

**At Rest:**
```python
from cryptography.fernet import Fernet

# Генерация ключа
key = Fernet.generate_key()
cipher = Fernet(key)

# Шифрование PHI
encrypted_ssn = cipher.encrypt(b"123-45-6789")

# Дешифрование
decrypted_ssn = cipher.decrypt(encrypted_ssn)
```

**In Transit:**
```
- TLS 1.2+ для всех соединений
- VPN для remote access
- Encrypted email (S/MIME, PGP)
```

### 3.2 Access Control

**RBAC (Role-Based Access Control):**
```python
class AccessControl:
    roles = {
        'doctor': ['read_patient', 'write_patient', 'prescribe'],
        'nurse': ['read_patient', 'update_vitals'],
        'admin': ['read_patient', 'manage_users'],
        'billing': ['read_patient_billing']
    }
    
    def has_permission(self, user_role, permission):
        return permission in self.roles.get(user_role, [])
```

**Принцип наименьших привилегий:**
- Давать только минимальные необходимые права
- Регулярный review доступов

### 3.3 Audit Logging

```python
class AuditLog:
    def log_access(self, user_id, patient_id, action, timestamp):
        """Логировать доступ к медицинским данным"""
        log_entry = {
            'user_id': user_id,
            'patient_id': patient_id,
            'action': action,  # 'read', 'write', 'delete'
            'timestamp': timestamp,
            'ip_address': get_client_ip(),
            'success': True
        }
        self.save_to_audit_db(log_entry)
    
    def detect_suspicious_activity(self):
        """Обнаружение подозрительной активности"""
        # Например: доступ к большому количеству записей
        # Доступ в необычное время
        # Доступ к собственной записи медработником
        pass
```

**Что логировать:**
- Кто (user_id)
- Что (action)
- Когда (timestamp)
- К чему (resource_id)
- Откуда (IP address)
- Результат (success/failure)

---

## 4. Безопасность Приложений

### 4.1 Authentication

```python
from flask import Flask, request
from werkzeug.security import check_password_hash
import jwt

def authenticate_user(username, password):
    user = get_user_from_db(username)
    
    if not user or not check_password_hash(user['password_hash'], password):
        return None
    
    # Многофакторная аутентификация
    if not verify_2fa(user, request.form['otp']):
        return None
    
    # Генерация JWT токена
    token = jwt.encode({
        'user_id': user['id'],
        'role': user['role'],
        'exp': datetime.utcnow() + timedelta(hours=1)
    }, SECRET_KEY)
    
    return token
```

**Требования:**
- Strong passwords (минимум 12 символов)
- Multi-factor authentication (MFA)
- Session timeout (15 минут inactivity)
- Account lockout после 5 неудачных попыток

### 4.2 Защита от OWASP Top 10

```python
# SQL Injection Prevention
from sqlalchemy import text

# BAD
query = f"SELECT * FROM patients WHERE id = {patient_id}"  # НЕ ДЕЛАЙТЕ ТАК!

# GOOD
query = text("SELECT * FROM patients WHERE id = :id")
result = db.execute(query, {"id": patient_id})


# XSS Prevention
from markupsafe import escape

user_input = request.form['note']
safe_note = escape(user_input)  # Экранирование HTML


# CSRF Protection
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect(app)
```

---

## 5. Incident Response

### 5.1 Breach Response Plan

**Шаги при утечке данных:**
1. **Identify** — обнаружить и оценить масштаб
2. **Contain** — остановить утечку
3. **Assess** — оценить затронутые данные и пациентов
4. **Notify** — уведомить:
   - Пациентов (если затронуто >500 человек)
   - HHS (Department of Health and Human Services)
   - Media (если >500 в одном штате)
5. **Remediate** — исправить уязвимость
6. **Review** — post-mortem анализ

### 5.2 Breach Notification Timeline

```
Обнаружение → 60 дней → Уведомление пациентов
              ↓
          Немедленно → Уведомление HHS (если >500)
```

---

## 6. Compliance Checklist

### 6.1 HIPAA Compliance

- [ ] PHI encrypted at rest and in transit
- [ ] Access control (RBAC) implemented
- [ ] Audit logging enabled
- [ ] Regular security assessments
- [ ] Incident response plan
- [ ] Business Associate Agreements (BAA) signed
- [ ] Employee training on HIPAA
- [ ] Physical security (locked server rooms)

### 6.2 GDPR Compliance

- [ ] Consent management system
- [ ] Data portability feature
- [ ] Right to erasure implemented
- [ ] Data processing agreement
- [ ] Privacy policy updated
- [ ] DPO (Data Protection Officer) appointed
- [ ] Data breach notification process

---

## Резюме

- ✅ HIPAA требования и PHI защита
- ✅ GDPR права пациентов
- ✅ Encryption (at rest & in transit)
- ✅ Access control и audit logging
- ✅ Безопасность приложений (auth, OWASP)
- ✅ Incident response и breach notification

---

## 🚀 Следующие Шаги

**Связанные модули:**
- [Medical Terminology](../01_Terminology/) — базовая терминология и стандарты
- [EHR Systems](../02_EHR_Systems/) — архитектура EHR систем
- [Medical Imaging](../04_Medical_Imaging/) — DICOM и защита изображений

**Идеи для практики:**
1. **De-identification Service** — удаление 18 HIPAA идентификаторов, сохранение агрегированных данных
2. **Audit Logger** — логирование доступа к PHI, поиск по логам, alerts для аномалий
3. **RBAC System** — роли (Doctor, Nurse, Admin, Billing) и permissions
4. **Encryption Service** — encrypt/decrypt функции, key management, field-level encryption
5. **Breach Detection** — анализ audit logs, обнаружение аномалий, автоматические alerts

---

## 📚 Дополнительные Ресурсы

**HIPAA:**
- [HHS HIPAA](https://www.hhs.gov/hipaa/index.html) — официальный сайт HIPAA
- [HIPAA Security Rule](https://www.hhs.gov/hipaa/for-professionals/security/index.html) — технические требования

**GDPR:**
- [GDPR Official](https://gdpr.eu/) — полный текст GDPR

**Security:**
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) — основные уязвимости веб-приложений
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework) — framework для кибербезопасности

