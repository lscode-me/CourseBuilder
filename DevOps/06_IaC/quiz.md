# Infrastructure as Code - Quiz

Проверьте свои знания по IaC, Terraform и Ansible.

---

## Question 1: Определение IaC

Что такое Infrastructure as Code?

A) Документация по серверам в Word

B) Управление инфраструктурой через машиночитаемые файлы конфигурации

C) Мониторинг серверов

D) Виртуализация

---

## Question 2: Declarative vs Imperative

Чем отличается декларативный подход от императивного?

A) Декларативный описывает "что хотим", императивный — "как сделать"

B) Это одно и то же

C) Декларативный быстрее

D) Императивный не требует программирования

---

## Question 3: Terraform State

Для чего Terraform использует state файл?

A) Для хранения паролей

B) Для отслеживания текущего состояния инфраструктуры

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

A) Облачный провайдер (AWS, GCP)

B) Плагин для взаимодействия с API сервисов

C) Тип виртуальной машины

D) Пароль для доступа

---

## Question 6: Ansible

Какой протокол Ansible использует для подключения к серверам по умолчанию?

A) HTTP

B) SSH

C) FTP

D) RDP

---

## Question 7: Ansible Playbook

Что такое playbook в Ansible?

A) Книга с документацией

B) Набор задач (tasks) для выполнения на серверах

C) Лог выполнения

D) Тип виртуальной машины

---

## Question 8: Ansible Handler

Когда выполняются handlers в Ansible?

A) В начале playbook

B) По notify от task, в конце play

C) Каждую минуту

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

A) Применяет изменения

B) Показывает предварительный просмотр изменений без применения

C) Удаляет ресурсы

D) Создаёт новый проект

---

## Question 11: Idempotency

Что означает идемпотентность в контексте IaC?

A) Каждый запуск создаёт новые ресурсы

B) Повторный запуск даёт тот же результат без дублирования

C) Код работает только один раз

D) Ресурсы удаляются после запуска

---

## Question 12: Секреты в IaC

Как правильно хранить пароли в Terraform?

A) Захардкодить в main.tf

B) Использовать Secrets Manager или передавать через переменные с sensitive=true

C) Хранить в README

D) В комментариях

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

A) Исходный код приложения

B) Список серверов и их группировку

C) Логи выполнения

D) Docker images

---

## Question 15: State Locking

Для чего нужен state locking в Terraform?

A) Для шифрования

B) Для предотвращения одновременных изменений несколькими пользователями

C) Для ускорения

D) Для backup

---

## Question 16: Terraform Destroy

Что делает `terraform destroy`?

A) Форматирует код

B) Удаляет все ресурсы, описанные в конфигурации

C) Создаёт backup

D) Обновляет провайдеры

---

## Question 17: Ansible Role

Что такое role в Ansible?

A) Пользователь системы

B) Переиспользуемый набор tasks, handlers, templates, variables

C) Тип сервера

D) Уровень доступа

---

## Question 18: Terraform Data Source

Для чего используются data sources в Terraform?

A) Для создания ресурсов

B) Для чтения информации о существующих ресурсах

C) Для логирования

D) Для backup

---

## Question 19: Pulumi

Чем Pulumi отличается от Terraform?

A) Pulumi не поддерживает AWS

B) Pulumi использует обычные языки программирования (Python, TypeScript)

C) Terraform быстрее

D) Pulumi не имеет state

---

## Question 20: IaC Best Practices

Что из перечисленного является best practice для IaC?

A) Хранить state локально

B) Version control, remote state, модульность, code review

C) Никогда не использовать переменные

D) Хардкодить всё в одном файле

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | IaC — управление инфраструктурой через код/конфигурационные файлы |
| 2 | A | Declarative = "что хотим" (Terraform), Imperative = "как сделать" |
| 3 | B | State отслеживает, какие ресурсы существуют и их текущее состояние |
| 4 | B | Remote backend для team collaboration, locking, security |
| 5 | B | Provider — плагин для работы с API (AWS, GCP, Azure, etc.) |
| 6 | B | Ansible по умолчанию использует SSH для подключения |
| 7 | B | Playbook — YAML файл с набором задач для выполнения |
| 8 | B | Handlers выполняются по notify, в конце play |
| 9 | B | Terraform лучше для provisioning облачных ресурсов |
| 10 | B | terraform plan показывает что будет изменено, без применения |
| 11 | B | Идемпотентность — повторный запуск даёт тот же результат |
| 12 | B | Секреты через Secrets Manager или sensitive переменные |
| 13 | B | Модули для DRY и организации кода |
| 14 | B | Inventory содержит список серверов и их группы |
| 15 | B | Locking предотвращает race conditions при одновременной работе |
| 16 | B | terraform destroy удаляет все управляемые ресурсы |
| 17 | B | Role — структурированный набор tasks, handlers, templates |
| 18 | B | Data sources для чтения информации о существующих ресурсах |
| 19 | B | Pulumi использует Python, TypeScript, Go вместо HCL |
| 20 | B | Version control, remote state, модульность — key best practices |

---

## Scoring Guide

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **18-20 правильных (90-100%)** | 🏆 Отлично! | Вы хорошо понимаете IaC. Переходите к GitOps. |
| **14-17 правильных (70-89%)** | ✅ Хорошо | Повторите Terraform state и Ansible playbooks. |
| **10-13 правильных (50-69%)** | ⚠️ Удовлетворительно | Перечитайте основы Terraform и Ansible. |
| **Менее 10 правильных (<50%)** | 📚 Нужно повторить | Внимательно изучите все примеры из лекции. |

---

