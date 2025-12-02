# Packet Filter (PF) - Quiz

Проверьте свои знания по файрволу PF в OpenBSD.

---

## Question 1: Конфигурация PF

В каком файле находится конфигурация PF?

A) /etc/firewall.conf

B) /etc/pf.conf

C) /etc/iptables.conf

D) /etc/pf/rules.conf

---

## Question 2: Включение PF

Какая команда включает PF?

A) pfctl -s

B) pfctl -e

C) pf enable

D) service pf start

---

## Question 3: Действие block

Что делает действие `block` по умолчанию?

A) Отбрасывает пакет без уведомления

B) Отправляет RST отправителю

C) Логирует и пропускает

D) Зависит от настройки block-policy

---

## Question 4: Ключевое слово quick

Что делает ключевое слово `quick` в правиле?

A) Ускоряет обработку пакета

B) Немедленно применяет действие без проверки остальных правил

C) Добавляет правило в начало списка

D) Включает быстрый режим PF

---

## Question 5: Stateful filtering

Что делает опция `keep state`?

A) Сохраняет конфигурацию

B) Отслеживает состояние соединения

C) Блокирует stateful пакеты

D) Включает persist режим

---

## Question 6: Таблицы

Какая команда добавляет IP в таблицу bruteforce?

A) pfctl -t bruteforce -a 192.168.1.1

B) pfctl -t bruteforce -T add 192.168.1.1

C) pftable add bruteforce 192.168.1.1

D) pfctl --table bruteforce --add 192.168.1.1

---

## Question 7: NAT

Какое ключевое слово используется для NAT исходящего трафика?

A) snat

B) masquerade

C) nat-to

D) outbound-nat

---

## Question 8: Port forwarding

Какое ключевое слово используется для перенаправления портов?

A) port-forward

B) dnat

C) rdr-to

D) redirect

---

## Question 9: Логирование

Какой интерфейс используется для просмотра логов PF?

A) log0

B) pf0

C) pflog0

D) firewall0

---

## Question 10: Просмотр правил

Какая команда показывает активные правила PF?

A) pfctl -l

B) pfctl -sr

C) pfctl --rules

D) pf status

---

## Question 11: Синтаксис проверка

Как проверить синтаксис pf.conf без применения?

A) pfctl -c /etc/pf.conf

B) pfctl -nf /etc/pf.conf

C) pfctl -t /etc/pf.conf

D) pf test /etc/pf.conf

---

## Question 12: Группа интерфейсов

Какой макрос обычно используется для внешнего интерфейса?

A) $external

B) $ext_if

C) $outside

D) $wan

---

## Question 13: Защита от SYN flood

Какая опция защищает от SYN flood атак?

A) syn-protect state

B) synproxy state

C) flood-protect

D) anti-syn state

---

## Question 14: scrub

Для чего используется директива scrub?

A) Очистка логов

B) Нормализация пакетов

C) Удаление правил

D) Сброс состояний

---

## Question 15: Просмотр состояний

Какая команда показывает таблицу состояний соединений?

A) pfctl -st

B) pfctl -ss

C) pfctl -sc

D) pfctl -state

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | /etc/pf.conf — стандартный файл конфигурации PF |
| 2 | B | pfctl -e (enable) включает PF |
| 3 | D | Зависит от set block-policy (drop или return) |
| 4 | B | quick немедленно применяет действие без обработки остальных правил |
| 5 | B | keep state создаёт запись состояния для отслеживания соединения |
| 6 | B | pfctl -t bruteforce -T add IP — синтаксис добавления в таблицу |
| 7 | C | nat-to используется для Source NAT в OpenBSD |
| 8 | C | rdr-to (redirect to) — перенаправление входящего трафика |
| 9 | C | pflog0 — псевдоинтерфейс для логирования PF |
| 10 | B | pfctl -sr (show rules) показывает правила фильтрации |
| 11 | B | pfctl -nf (no-action, file) проверяет синтаксис без применения |
| 12 | B | $ext_if — общепринятый макрос для внешнего интерфейса |
| 13 | B | synproxy state проксирует TCP handshake для защиты от SYN flood |
| 14 | B | scrub нормализует пакеты (фрагментация, TTL, и т.д.) |
| 15 | B | pfctl -ss (show states) показывает таблицу состояний |

---

## Scoring Guide

Подсчитайте количество правильных ответов:

| Результат | Оценка | Рекомендации |
|-----------|--------|--------------|
| **14-15 правильных (93-100%)** | 🏆 Отлично! | Вы хорошо знаете PF. |
| **11-13 правильных (73-87%)** | ✅ Хорошо | Повторите NAT и таблицы. |
| **8-10 правильных (53-67%)** | ⚠️ Удовлетворительно | Рекомендуется практика с реальными конфигурациями. |
| **Менее 8 правильных (<53%)** | 📚 Нужно повторить | Изучите PF User's Guide и man pf.conf. |

---

