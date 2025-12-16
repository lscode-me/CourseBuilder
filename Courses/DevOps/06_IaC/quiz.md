# Infrastructure as Code - Quiz

Проверьте свои знания по IaC, Terraform и Ansible.

---

## Question 1: Определение IaC

Что такое Infrastructure as Code?

A) Управление инфраструктурой через машиночитаемые файлы конфигурации

B) Мониторинг серверов

C) Виртуализация

D) Документация по серверам в Word

---

## Question 2: Declarative vs Imperative

Чем отличается декларативный подход от императивного?

A) Декларативный быстрее

B) Декларативный описывает "что хотим", императивный — "как сделать"

C) Это одно и то же

D) Императивный не требует программирования

---

## Question 3: Terraform State

Для чего Terraform использует state файл?

A) Для отслеживания текущего состояния инфраструктуры

B) Для логирования

C) Для хранения паролей

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

A) Плагин для взаимодействия с API сервисов

B) Пароль для доступа

C) Облачный провайдер (AWS, GCP)

D) Тип виртуальной машины

---

## Question 6: Ansible

Какой протокол Ansible использует для подключения к серверам по умолчанию?

A) RDP

B) SSH

C) HTTP

D) FTP

---

## Question 7: Ansible Playbook

Что такое playbook в Ansible?

A) Набор задач (tasks) для выполнения на серверах

B) Лог выполнения

C) Тип виртуальной машины

D) Книга с документацией

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

A) Создание облачных ресурсов (EC2, RDS, S3)

B) Копирование файлов

C) Установка пакетов на серверы

D) Управление пользователями

---

## Question 10: Terraform Plan

Что делает команда `terraform plan`?

A) Показывает предварительный просмотр изменений без применения

B) Применяет изменения

C) Удаляет ресурсы

D) Создаёт новый проект

---

## Question 11: Idempotency

Что означает идемпотентность в контексте IaC?

A) Повторный запуск даёт тот же результат без дублирования

B) Каждый запуск создаёт новые ресурсы

C) Ресурсы удаляются после запуска

D) Код работает только один раз

---

## Question 12: Секреты в IaC

Как правильно хранить пароли в Terraform?

A) Использовать Secrets Manager или передавать через переменные с sensitive=true

B) Захардкодить в main.tf

C) В комментариях

D) Хранить в README

---

## Question 13: Terraform Modules

Для чего используются модули в Terraform?

A) Для усложнения кода

B) Для переиспользования и организации кода

C) Для логирования

D) Для backup

---

## Question 14: Ansible Inventory

Что содержит inventory в Ansible?

A) Список серверов и их группировку

B) Логи выполнения

C) Исходный код приложения

D) Docker images

---

## Question 15: State Locking

Для чего нужен state locking в Terraform?

A) Для шифрования

B) Для backup

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

A) Уровень доступа

B) Тип сервера

C) Переиспользуемый набор tasks, handlers, templates, variables

D) Пользователь системы

---

## Question 18: Terraform Data Source

Для чего используются data sources в Terraform?

A) Для backup

B) Для чтения информации о существующих ресурсах

C) Для логирования

D) Для создания ресурсов

---

## Question 19: Pulumi

Чем Pulumi отличается от Terraform?

A) Pulumi использует обычные языки программирования (Python, TypeScript)

B) Pulumi не имеет state

C) Terraform быстрее

D) Pulumi не поддерживает AWS

---

## Question 20: IaC Best Practices

Что из перечисленного является best practice для IaC?

A) Хранить state локально

B) Хардкодить всё в одном файле

C) Никогда не использовать переменные

D) Version control, remote state, модульность, code review

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | IaC — управление инфраструктурой через код/конфигурационные файлы |
| 2 | B | Declarative = "что хотим" (Terraform), Imperative = "как сделать" |
| 3 | A | State отслеживает, какие ресурсы существуют и их текущее состояние |
| 4 | B | Remote backend для team collaboration, locking, security |
| 5 | A | Provider — плагин для работы с API (AWS, GCP, Azure, etc.) |
| 6 | B | Ansible по умолчанию использует SSH для подключения |
| 7 | A | Playbook — YAML файл с набором задач для выполнения |
| 8 | C | Handlers выполняются по notify, в конце play |
| 9 | A | Terraform лучше для provisioning облачных ресурсов |
| 10 | A | terraform plan показывает что будет изменено, без применения |
| 11 | A | Идемпотентность — повторный запуск даёт тот же результат |
| 12 | A | Секреты через Secrets Manager или sensitive переменные |
| 13 | B | Модули для DRY и организации кода |
| 14 | A | Inventory содержит список серверов и их группы |
| 15 | C | Locking предотвращает race conditions при одновременной работе |
| 16 | C | terraform destroy удаляет все управляемые ресурсы |
| 17 | C | Role — структурированный набор tasks, handlers, templates |
| 18 | B | Data sources для чтения информации о существующих ресурсах |
| 19 | A | Pulumi использует Python, TypeScript, Go вместо HCL |
| 20 | D | Version control, remote state, модульность — key best practices |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы хорошо понимаете IaC. Переходите к GitOps. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Повторите Terraform state и Ansible playbooks. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте основы Terraform и Ansible. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Внимательно изучите все примеры из лекции. |

---

