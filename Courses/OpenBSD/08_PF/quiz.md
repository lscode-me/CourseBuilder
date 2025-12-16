# Packet Filter (PF) - Quiz

Проверьте свои знания по файрволу PF в OpenBSD.

---

## Question 1: Конфигурация PF

В каком файле находится конфигурация PF?

A) /etc/pf.conf

B) /etc/iptables.conf

C) /etc/firewall.conf

D) /etc/pf/rules.conf

---

## Question 2: Включение PF

Какая команда включает PF?

A) service pf start

B) pf enable

C) pfctl -e

D) pfctl -s

---

## Question 3: Действие block

Что делает действие `block` по умолчанию?

A) Зависит от настройки block-policy

B) Отправляет RST отправителю

C) Логирует и пропускает

D) Отбрасывает пакет без уведомления

---

## Question 4: Ключевое слово quick

Что делает ключевое слово `quick` в правиле?

A) Немедленно применяет действие без проверки остальных правил

B) Ускоряет обработку пакета

C) Добавляет правило в начало списка

D) Включает быстрый режим PF

---

## Question 5: Stateful filtering

Что делает опция `keep state`?

A) Отслеживает состояние соединения

B) Включает persist режим

C) Блокирует stateful пакеты

D) Сохраняет конфигурацию

---

## Question 6: Таблицы

Какая команда добавляет IP в таблицу bruteforce?

A) pfctl -t bruteforce -T add 192.168.1.1

B) pfctl --table bruteforce --add 192.168.1.1

C) pftable add bruteforce 192.168.1.1

D) pfctl -t bruteforce -a 192.168.1.1

---

## Question 7: NAT

Какое ключевое слово используется для NAT исходящего трафика?

A) nat-to

B) masquerade

C) snat

D) outbound-nat

---

## Question 8: Port forwarding

Какое ключевое слово используется для перенаправления портов?

A) port-forward

B) redirect

C) dnat

D) rdr-to

---

## Question 9: Логирование

Какой интерфейс используется для просмотра логов PF?

A) firewall0

B) pflog0

C) log0

D) pf0

---

## Question 10: Просмотр правил

Какая команда показывает активные правила PF?

A) pfctl -l

B) pf status

C) pfctl -sr

D) pfctl --rules

---

## Question 11: Синтаксис проверка

Как проверить синтаксис pf.conf без применения?

A) pfctl -t /etc/pf.conf

B) pf test /etc/pf.conf

C) pfctl -c /etc/pf.conf

D) pfctl -nf /etc/pf.conf

---

## Question 12: Группа интерфейсов

Какой макрос обычно используется для внешнего интерфейса?

A) $external

B) $wan

C) $ext_if

D) $outside

---

## Question 13: Защита от SYN flood

Какая опция защищает от SYN flood атак?

A) flood-protect

B) synproxy state

C) anti-syn state

D) syn-protect state

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

A) pfctl -state

B) pfctl -st

C) pfctl -ss

D) pfctl -sc

---

## Question 16: anchor

Для чего используются anchors в PF?

A) Для блокировки трафика

B) Для якорной точки NAT

C) Для защиты от спуфинга

D) Для подключения внешних наборов правил

---

## Question 17: max-src-conn

Что ограничивает параметр max-src-conn?

A) Максимум соединений с одного IP

B) Максимум источников

C) Максимум подключений к порту

D) Максимум состояний

---

## Question 18: antispoof

Для чего используется директива antispoof?

A) Для защиты от DDoS

B) Для блокировки ботов

C) Для блокировки пакетов с поддельными адресами

D) Для антиспам фильтрации

---

## Question 19: pfctl -k

Что делает pfctl -k host?

A) Проверяет хост

B) Показывает состояния хоста

C) Блокирует хост

D) Удаляет состояния для указанного хоста

---

## Question 20: set skip

Что делает директива set skip on lo0?

A) Пропускает scrub

B) Пропускает NAT

C) Пропускает логирование

D) PF не фильтрует трафик на loopback

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | /etc/pf.conf — стандартный файл конфигурации PF |
| 2 | C | pfctl -e (enable) включает PF |
| 3 | A | Зависит от set block-policy (drop или return) |
| 4 | A | quick немедленно применяет действие без обработки остальных правил |
| 5 | A | keep state создаёт запись состояния для отслеживания соединения |
| 6 | A | pfctl -t bruteforce -T add IP — синтаксис добавления в таблицу |
| 7 | A | nat-to используется для Source NAT в OpenBSD |
| 8 | D | rdr-to (redirect to) — перенаправление входящего трафика |
| 9 | B | pflog0 — псевдоинтерфейс для логирования PF |
| 10 | C | pfctl -sr (show rules) показывает правила фильтрации |
| 11 | D | pfctl -nf (no-action, file) проверяет синтаксис без применения |
| 12 | C | $ext_if — общепринятый макрос для внешнего интерфейса |
| 13 | B | synproxy state проксирует TCP handshake для защиты от SYN flood |
| 14 | B | scrub нормализует пакеты (фрагментация, TTL, и т.д.) |
| 15 | C | pfctl -ss (show states) показывает таблицу состояний |
| 16 | D | anchors позволяют подключать внешние наборы правил |
| 17 | A | max-src-conn ограничивает число соединений с одного IP |
| 18 | C | antispoof блокирует пакеты с поддельными source адресами |
| 19 | D | pfctl -k удаляет состояния для указанного хоста |
| 20 | D | set skip отключает фильтрацию PF на указанном интерфейсе |

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

