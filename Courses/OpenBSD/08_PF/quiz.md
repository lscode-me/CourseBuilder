# Packet Filter (PF) - Quiz

Проверьте свои знания по файрволу PF в OpenBSD.

---

## Question 1: Конфигурация PF







В каком файле находится конфигурация PF?

A) /etc/iptables.conf

B) /etc/pf.conf

C) /etc/pf/rules.conf

D) /etc/firewall.conf

---

## Question 2: Включение PF







Какая команда включает PF?

A) pf enable

B) pfctl -e

C) pfctl -s

D) service pf start

---

## Question 3: Действие block







Что делает действие `block` по умолчанию?

A) Зависит от настройки block-policy

B) Логирует и пропускает

C) Отбрасывает пакет без уведомления

D) Отправляет RST отправителю

---

## Question 4: Ключевое слово quick







Что делает ключевое слово `quick` в правиле?

A) Включает быстрый режим PF

B) Немедленно применяет действие без проверки остальных правил

C) Добавляет правило в начало списка

D) Ускоряет обработку пакета

---

## Question 5: Stateful filtering







Что делает опция `keep state`?

A) Отслеживает состояние соединения

B) Сохраняет конфигурацию

C) Блокирует stateful пакеты

D) Включает persist режим

---

## Question 6: Таблицы







Какая команда добавляет IP в таблицу bruteforce?

A) pftable add bruteforce 192.168.1.1

B) pfctl -t bruteforce -a 192.168.1.1

C) pfctl -t bruteforce -T add 192.168.1.1

D) pfctl --table bruteforce --add 192.168.1.1

---

## Question 7: NAT







Какое ключевое слово используется для NAT исходящего трафика?

A) nat-to

B) snat

C) outbound-nat

D) masquerade

---

## Question 8: Port forwarding







Какое ключевое слово используется для перенаправления портов?

A) dnat

B) rdr-to

C) redirect

D) port-forward

---

## Question 9: Логирование







Какой интерфейс используется для просмотра логов PF?

A) firewall0

B) log0

C) pflog0

D) pf0

---

## Question 10: Просмотр правил







Какая команда показывает активные правила PF?

A) pf status

B) pfctl -sr

C) pfctl --rules

D) pfctl -l

---

## Question 11: Синтаксис проверка







Как проверить синтаксис pf.conf без применения?

A) pf test /etc/pf.conf

B) pfctl -c /etc/pf.conf

C) pfctl -nf /etc/pf.conf

D) pfctl -t /etc/pf.conf

---

## Question 12: Группа интерфейсов







Какой макрос обычно используется для внешнего интерфейса?

A) $wan

B) $external

C) $ext_if

D) $outside

---

## Question 13: Защита от SYN flood







Какая опция защищает от SYN flood атак?

A) anti-syn state

B) flood-protect

C) synproxy state

D) syn-protect state

---

## Question 14: scrub







Для чего используется директива scrub?

A) Удаление правил

B) Нормализация пакетов

C) Сброс состояний

D) Очистка логов

---

## Question 15: Просмотр состояний







Какая команда показывает таблицу состояний соединений?

A) pfctl -state

B) pfctl -st

C) pfctl -sc

D) pfctl -ss

---

## Question 16: anchor






Для чего используются anchors в PF?

A) Для блокировки трафика

B) Для защиты от спуфинга

C) Для подключения внешних наборов правил

D) Для якорной точки NAT

---

## Question 17: max-src-conn






Что ограничивает параметр max-src-conn?

A) Максимум источников

B) Максимум соединений с одного IP

C) Максимум подключений к порту

D) Максимум состояний

---

## Question 18: antispoof






Для чего используется директива antispoof?

A) Для блокировки ботов

B) Для блокировки пакетов с поддельными адресами

C) Для антиспам фильтрации

D) Для защиты от DDoS

---

## Question 19: pfctl -k






Что делает pfctl -k host?

A) Показывает состояния хоста

B) Блокирует хост

C) Проверяет хост

D) Удаляет состояния для указанного хоста

---

## Question 20: set skip






Что делает директива set skip on lo0?

A) Пропускает scrub

B) Пропускает логирование

C) Пропускает NAT

D) PF не фильтрует трафик на loopback

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | /etc/pf.conf — стандартный файл конфигурации PF |
| 2 | B | pfctl -e (enable) включает PF |
| 3 | A | Зависит от set block-policy (drop или return) |
| 4 | B | quick немедленно применяет действие без обработки остальных правил |
| 5 | A | keep state создаёт запись состояния для отслеживания соединения |
| 6 | C | pfctl -t bruteforce -T add IP — синтаксис добавления в таблицу |
| 7 | A | nat-to используется для Source NAT в OpenBSD |
| 8 | B | rdr-to (redirect to) — перенаправление входящего трафика |
| 9 | C | pflog0 — псевдоинтерфейс для логирования PF |
| 10 | B | pfctl -sr (show rules) показывает правила фильтрации |
| 11 | C | pfctl -nf (no-action, file) проверяет синтаксис без применения |
| 12 | C | $ext_if — общепринятый макрос для внешнего интерфейса |
| 13 | C | synproxy state проксирует TCP handshake для защиты от SYN flood |
| 14 | B | scrub нормализует пакеты (фрагментация, TTL, и т.д.) |
| 15 | D | pfctl -ss (show states) показывает таблицу состояний |
| 16 | C | anchors позволяют подключать внешние наборы правил |
| 17 | B | max-src-conn ограничивает число соединений с одного IP |
| 18 | B | antispoof блокирует пакеты с поддельными source адресами |
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

