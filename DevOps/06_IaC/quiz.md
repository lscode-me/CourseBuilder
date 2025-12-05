# Infrastructure as Code - Quiz

Проверьте свои знания по IaC, Terraform и Ansible.

---

## Question 1: Определение IaC


Что такое Infrastructure as Code?

A) Виртуализация

B) Документация по серверам в Word

C) Мониторинг серверов

D) Управление инфраструктурой через машиночитаемые файлы конфигурации

---

## Question 2: Declarative vs Imperative


Чем отличается декларативный подход от императивного?

A) Это одно и то же

B) Декларативный быстрее

C) Декларативный описывает "что хотим", императивный — "как сделать"

D) Императивный не требует программирования

---

## Question 3: Terraform State


Для чего Terraform использует state файл?

A) Для логирования

B) Для отслеживания текущего состояния инфраструктуры

C) Для хранения паролей

D) Для backup кода

---

## Question 4: Terraform Backend


Почему рекомендуется использовать remote backend для state?

A) Так быстрее

B) Для командной работы, locking и безопасности

C) Remote backend не нужен

D) Это бесплатно

---

## Question 5: Terraform Provider


Что такое provider в Terraform?

A) Пароль для доступа

B) Тип виртуальной машины

C) Плагин для взаимодействия с API сервисов

D) Облачный провайдер (AWS, GCP)

---

## Question 6: Ansible


Какой протокол Ansible использует для подключения к серверам по умолчанию?

A) RDP

B) HTTP

C) SSH

D) FTP

---

## Question 7: Ansible Playbook


Что такое playbook в Ansible?

A) Книга с документацией

B) Тип виртуальной машины

C) Лог выполнения

D) Набор задач (tasks) для выполнения на серверах

---

## Question 8: Ansible Handler


Когда выполняются handlers в Ansible?

A) Никогда

B) Каждую минуту

C) В начале playbook

D) По notify от task, в конце play

---

## Question 9: Terraform vs Ansible


Для чего лучше подходит Terraform?

A) Управление пользователями

B) Создание облачных ресурсов (EC2, RDS, S3)

C) Копирование файлов

D) Установка пакетов на серверы

---

## Question 10: Terraform Plan


Что делает команда `terraform plan`?

A) Удаляет ресурсы

B) Применяет изменения

C) Создаёт новый проект

D) Показывает предварительный просмотр изменений без применения

---

## Question 11: Idempotency


Что означает идемпотентность в контексте IaC?

A) Каждый запуск создаёт новые ресурсы

B) Код работает только один раз

C) Ресурсы удаляются после запуска

D) Повторный запуск даёт тот же результат без дублирования

---

## Question 12: Секреты в IaC


Как правильно хранить пароли в Terraform?

A) Хранить в README

B) Захардкодить в main.tf

C) Использовать Secrets Manager или передавать через переменные с sensitive=true

D) В комментариях

---

## Question 13: Terraform Modules


Для чего используются модули в Terraform?

A) Для логирования

B) Для усложнения кода

C) Для переиспользования и организации кода

D) Для backup

---

## Question 14: Ansible Inventory


Что содержит inventory в Ansible?

A) Docker images

B) Логи выполнения

C) Список серверов и их группировку

D) Исходный код приложения

---

## Question 15: State Locking


Для чего нужен state locking в Terraform?

A) Для шифрования

B) Для предотвращения одновременных изменений несколькими пользователями

C) Для backup

D) Для ускорения

---

## Question 16: Terraform Destroy


Что делает `terraform destroy`?

A) Форматирует код

B) Обновляет провайдеры

C) Удаляет все ресурсы, описанные в конфигурации

D) Создаёт backup

---

## Question 17: Ansible Role


Что такое role в Ansible?

A) Пользователь системы

B) Тип сервера

C) Уровень доступа

D) Переиспользуемый набор tasks, handlers, templates, variables

---

## Question 18: Terraform Data Source


Для чего используются data sources в Terraform?

A) Для логирования

B) Для чтения информации о существующих ресурсах

C) Для backup

D) Для создания ресурсов

---

## Question 19: Pulumi


Чем Pulumi отличается от Terraform?

A) Pulumi не поддерживает AWS

B) Pulumi использует обычные языки программирования (Python, TypeScript)

C) Pulumi не имеет state

D) Terraform быстрее

---

## Question 20: IaC Best Practices


Что из перечисленного является best practice для IaC?

A) Хардкодить всё в одном файле

B) Version control, remote state, модульность, code review

C) Хранить state локально

D) Никогда не использовать переменные

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | D | IaC — управление инфраструктурой через код/конфигурационные файлы |
| 2 | C | Declarative = "что хотим" (Terraform), Imperative = "как сделать" |
| 3 | B | State отслеживает, какие ресурсы существуют и их текущее состояние |
| 4 | B | Remote backend для team collaboration, locking, security |
| 5 | C | Provider — плагин для работы с API (AWS, GCP, Azure, etc.) |
| 6 | C | Ansible по умолчанию использует SSH для подключения |
| 7 | D | Playbook — YAML файл с набором задач для выполнения |
| 8 | D | Handlers выполняются по notify, в конце play |
| 9 | B | Terraform лучше для provisioning облачных ресурсов |
| 10 | D | terraform plan показывает что будет изменено, без применения |
| 11 | D | Идемпотентность — повторный запуск даёт тот же результат |
| 12 | C | Секреты через Secrets Manager или sensitive переменные |
| 13 | C | Модули для DRY и организации кода |
| 14 | C | Inventory содержит список серверов и их группы |
| 15 | B | Locking предотвращает race conditions при одновременной работе |
| 16 | C | terraform destroy удаляет все управляемые ресурсы |
| 17 | D | Role — структурированный набор tasks, handlers, templates |
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

