# Infrastructure as Code - Quiz

Проверьте свои знания по IaC, Terraform и Ansible.

---

## Question 1: Определение IaC







Что такое Infrastructure as Code?

A) Виртуализация

B) Мониторинг серверов

C) Документация по серверам в Word

D) Управление инфраструктурой через машиночитаемые файлы конфигурации

---

## Question 2: Declarative vs Imperative







Чем отличается декларативный подход от императивного?

A) Императивный не требует программирования

B) Это одно и то же

C) Декларативный быстрее

D) Декларативный описывает "что хотим", императивный — "как сделать"

---

## Question 3: Terraform State







Для чего Terraform использует state файл?

A) Для отслеживания текущего состояния инфраструктуры

B) Для хранения паролей

C) Для логирования

D) Для backup кода

---

## Question 4: Terraform Backend







Почему рекомендуется использовать remote backend для state?

A) Это бесплатно

B) Для командной работы, locking и безопасности

C) Так быстрее

D) Remote backend не нужен

---

## Question 5: Terraform Provider







Что такое provider в Terraform?

A) Тип виртуальной машины

B) Плагин для взаимодействия с API сервисов

C) Облачный провайдер (AWS, GCP)

D) Пароль для доступа

---

## Question 6: Ansible







Какой протокол Ansible использует для подключения к серверам по умолчанию?

A) HTTP

B) SSH

C) RDP

D) FTP

---

## Question 7: Ansible Playbook







Что такое playbook в Ansible?

A) Лог выполнения

B) Книга с документацией

C) Тип виртуальной машины

D) Набор задач (tasks) для выполнения на серверах

---

## Question 8: Ansible Handler







Когда выполняются handlers в Ansible?

A) В начале playbook

B) Каждую минуту

C) По notify от task, в конце play

D) Никогда

---

## Question 9: Terraform vs Ansible







Для чего лучше подходит Terraform?

A) Установка пакетов на серверы

B) Создание облачных ресурсов (EC2, RDS, S3)

C) Копирование файлов

D) Управление пользователями

---

## Question 10: Terraform Plan







Что делает команда `terraform plan`?

A) Создаёт новый проект

B) Применяет изменения

C) Показывает предварительный просмотр изменений без применения

D) Удаляет ресурсы

---

## Question 11: Idempotency







Что означает идемпотентность в контексте IaC?

A) Ресурсы удаляются после запуска

B) Повторный запуск даёт тот же результат без дублирования

C) Каждый запуск создаёт новые ресурсы

D) Код работает только один раз

---

## Question 12: Секреты в IaC







Как правильно хранить пароли в Terraform?

A) Захардкодить в main.tf

B) Хранить в README

C) В комментариях

D) Использовать Secrets Manager или передавать через переменные с sensitive=true

---

## Question 13: Terraform Modules







Для чего используются модули в Terraform?

A) Для усложнения кода

B) Для логирования

C) Для переиспользования и организации кода

D) Для backup

---

## Question 14: Ansible Inventory







Что содержит inventory в Ansible?

A) Логи выполнения

B) Список серверов и их группировку

C) Исходный код приложения

D) Docker images

---

## Question 15: State Locking







Для чего нужен state locking в Terraform?

A) Для backup

B) Для шифрования

C) Для предотвращения одновременных изменений несколькими пользователями

D) Для ускорения

---

## Question 16: Terraform Destroy







Что делает `terraform destroy`?

A) Форматирует код

B) Создаёт backup

C) Удаляет все ресурсы, описанные в конфигурации

D) Обновляет провайдеры

---

## Question 17: Ansible Role







Что такое role в Ansible?

A) Переиспользуемый набор tasks, handlers, templates, variables

B) Тип сервера

C) Пользователь системы

D) Уровень доступа

---

## Question 18: Terraform Data Source







Для чего используются data sources в Terraform?

A) Для backup

B) Для создания ресурсов

C) Для чтения информации о существующих ресурсах

D) Для логирования

---

## Question 19: Pulumi







Чем Pulumi отличается от Terraform?

A) Pulumi не имеет state

B) Pulumi не поддерживает AWS

C) Pulumi использует обычные языки программирования (Python, TypeScript)

D) Terraform быстрее

---

## Question 20: IaC Best Practices







Что из перечисленного является best practice для IaC?

A) Хранить state локально

B) Хардкодить всё в одном файле

C) Version control, remote state, модульность, code review

D) Никогда не использовать переменные

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | D | IaC — управление инфраструктурой через код/конфигурационные файлы |
| 2 | D | Declarative = "что хотим" (Terraform), Imperative = "как сделать" |
| 3 | A | State отслеживает, какие ресурсы существуют и их текущее состояние |
| 4 | B | Remote backend для team collaboration, locking, security |
| 5 | B | Provider — плагин для работы с API (AWS, GCP, Azure, etc.) |
| 6 | B | Ansible по умолчанию использует SSH для подключения |
| 7 | D | Playbook — YAML файл с набором задач для выполнения |
| 8 | C | Handlers выполняются по notify, в конце play |
| 9 | B | Terraform лучше для provisioning облачных ресурсов |
| 10 | C | terraform plan показывает что будет изменено, без применения |
| 11 | B | Идемпотентность — повторный запуск даёт тот же результат |
| 12 | D | Секреты через Secrets Manager или sensitive переменные |
| 13 | C | Модули для DRY и организации кода |
| 14 | B | Inventory содержит список серверов и их группы |
| 15 | C | Locking предотвращает race conditions при одновременной работе |
| 16 | C | terraform destroy удаляет все управляемые ресурсы |
| 17 | A | Role — структурированный набор tasks, handlers, templates |
| 18 | C | Data sources для чтения информации о существующих ресурсах |
| 19 | C | Pulumi использует Python, TypeScript, Go вместо HCL |
| 20 | C | Version control, remote state, модульность — key best practices |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы хорошо понимаете IaC. Переходите к GitOps. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Повторите Terraform state и Ansible playbooks. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте основы Terraform и Ansible. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Внимательно изучите все примеры из лекции. |

---

