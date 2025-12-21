# От CLI к GUI, Touch, Voice и beyond

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать базовые концепции компьютерных систем
- Быть знакомы с историей развития компьютеров
- Знать основы операционных систем

**Recommended prior modules:**

- [01_EarlyComputers](../01_EarlyComputers/) — Ранние вычислительные машины
- [22_DevicesEvolution](../22_DevicesEvolution/) — Эволюция устройств

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Объяснять эволюцию интерфейсов от перфокарт к нейроинтерфейсам
- Понимать trade-offs между эффективностью и простотой использования
- Анализировать, почему разные типы интерфейсов сосуществуют
- Различать context-aware и adaptive интерфейсы
- Предвидеть будущие направления развития UI

---

## 1. Эпоха до интерактивности (1940-е - 1960-е)

### 1.1 Перфокарты и перфоленты

**Batch Processing** — программы подавались стопками перфокарт:
1. Программист пишет код на бумаге
2. Оператор переносит на перфокарты
3. Карты подаются в компьютер
4. Через часы/дни — результат на принтере

**Характеристики:**

- Нет интерактивности
- Feedback loop: часы или дни
- Одна ошибка → переделать всё

**Кто использовал:** IBM mainframes, ранние ЭВМ

### 1.2 Teletype терминалы (TTY)

**Конец 1960-х:** Первые интерактивные терминалы
- Печатающие машинки, подключённые к компьютеру
- Вводишь команду → сразу ответ (на бумаге!)
- Революция: feedback за секунды, а не часы

```

Login: bob
Password: ****
$ ls
file1.txt  file2.txt
$ cat file1.txt
Hello, World!
$
```

---

## 2. CLI - Command Line Interface (1970-е - настоящее время)

### 2.1 Рождение CLI

**UNIX shell (1971):** Thompson Shell, позже Bourne Shell (sh)

**Философия:**

- Текстовые команды
- Композиция через pipes: `cat file | grep "error" | wc -l`
- Скриптинг и автоматизация

**Примеры:**
```bash
# UNIX/Linux shells
sh, bash, zsh, fish

# DOS

COMMAND.COM

# Windows

cmd.exe, PowerShell
```

### 2.2 Преимущества CLI

**Эффективность для экспертов:**

- Быстрый ввод текста
- Композиция команд (pipes, redirection)
- Scripting — автоматизация задач
- Remote access (SSH)

**Мощность:**
```bash
# Одна строка заменяет GUI операции с тысячами файлов
find . -name "*.log" -mtime +7 -delete

# Композиция команд через pipes
cat access.log | grep "404" | awk '{print $1}' | sort | uniq -c | sort -rn | head -10
# Результат: топ-10 IP адресов с ошибками 404
```

**Пример: Автоматизация через CLI**

```bash
#!/bin/bash
# Автоматический backup с логированием
BACKUP_DIR="/backup/$(date +%Y%m%d)"
mkdir -p "$BACKUP_DIR"

# Копирование с прогрессом
rsync -av --progress /data/ "$BACKUP_DIR/" \
    | tee "$BACKUP_DIR/backup.log"

# Отправка уведомления
if [ $? -eq 0 ]; then
    echo "Backup successful" | mail -s "Backup OK" admin@example.com
else
    echo "Backup failed" | mail -s "Backup ERROR" admin@example.com
fi
```

**Низкие требования:**

- Работает через serial port
- Минимальный bandwidth
- Доступен на embedded системах

**Пример: Remote access через SSH**

```bash
# Подключение к удалённому серверу
ssh user@server.example.com

# Выполнение команды на удалённом сервере
ssh user@server "df -h | grep /dev/sda"

# Туннелирование (port forwarding)
ssh -L 8080:localhost:80 user@server
# Локальный порт 8080 → удалённый порт 80
```

### 2.3 Недостатки CLI

- **Кривая обучения:** Нужно знать команды

- **Не визуален:** Трудно работать с графикой, видео

- **Не подходит для discovery:** Нельзя "посмотреть, что есть"

- **Ошибки опасны:** `rm -rf /` удалит всё

---

## 3. TUI - Text User Interface (1980-е - 1990-е)

### 3.1 Псевдографические интерфейсы

**Идея:** Использовать текстовый терминал для "графики"

**Примеры:**

- **Norton Commander** (DOS, 1986)

- **Midnight Commander** (Unix, 1994)

- **Turbo Vision** (framework, Borland)

- **WordPerfect** (текстовый процессор)

**Возможности:**

- Меню, диалоги, кнопки из символов ASCII/псевдографики
- Использование ANSI escape codes для цвета
- Интерактивность: клавиши, мышь (в терминале!)

### 3.2 Преимущества TUI

- Работает в терминале (SSH, serial)
- Низкие требования к графике
- Keyboard-driven — быстрее мыши
- Более дружелюбен, чем чистый CLI

**Современные TUI:**

- `vim`, `emacs` (редакторы)
- `htop`, `top` (system monitoring)
- `tmux`, `screen` (terminal multiplexers)
- `ncurses` (библиотека для TUI)

---

## 4. GUI - Graphical User Interface (1970-е - настоящее время)

### 4.1 Пионеры: Xerox PARC

**Xerox Alto (1973):**

- Первый компьютер с GUI
- Bitmap display
- Mouse
- Windows, icons, menus

**Xerox Star (1981):**

- Коммерческий продукт
- Desktop metaphor: файлы как документы на столе
- WYSIWYG (What You See Is What You Get)

**Проблема:** Стоимость $16,000 — провал на рынке

### 4.2 Apple и массовый рынок

**Apple Lisa (1983):**

- GUI, вдохновлённый Xerox
- $10,000 — тоже провал

**Apple Macintosh (1984):**

- $2,500 — доступнее
- "Hello, I'm Macintosh" — дружелюбный
- Revolutionized desktop publishing

**Философия:**

- Визуальные метафоры (desktop, folders, trash)
- Point and click вместо команд
- Доступность для не-технических пользователей

### 4.3 Windows и PC

**Microsoft Windows (1985-):**

- Windows 1.0 — скептицизм
- Windows 3.0 (1990) — прорыв
- Windows 95 (1995) — доминирование

**Start Menu, Taskbar, Right-click:**
```

┌─────────────────────────────┐
│ [Start] [🗁] [⊞] [📁]       │ ← Taskbar
├─────────────────────────────┤
│  My Computer  Recycle Bin   │
│  [🖥️]         [🗑️]          │
│                             │
│  My Documents               │
│  [📁]                       │
└─────────────────────────────┘
```

### 4.4 WIMP парадигма

**WIMP: Windows, Icons, Menus, Pointer**

**Компоненты:**

- Windows: перекрывающиеся окна
- Icons: визуальное представление объектов
- Menus: иерархические списки команд
- Pointer: курсор мыши

**Trade-offs GUI vs CLI:**

| Aspect | CLI | GUI |
|--------|-----|-----|
| Обучение | Сложно | Легко |
| Эффективность (expert) | Высокая | Средняя |
| Discovery | Низкая | Высокая |
| Автоматизация | Отличная | Плохая |
| Remote | Отлично | Требует bandwidth |

---

## 5. Web-интерфейсы (1990-е - настоящее время)

### 5.1 От документов к приложениям

**1990-е: Статические страницы**
- HTML + CSS
- Гиперссылки
- Формы для ввода

**2000-е: AJAX (Asynchronous JavaScript and XML)**
- Gmail (2004), Google Maps (2005)
- Динамическое обновление без перезагрузки
- RIA (Rich Internet Applications)

**2010-е: Single Page Applications (SPA)**
- React, Angular, Vue.js
- Весь UI в браузере
- Backend — только API

**Современность: Progressive Web Apps (PWA)**
- Работают offline
- Push notifications
- Устанавливаются как native apps
- Blur между web и native

### 5.2 Responsive Design

**Проблема:** Один сайт, миллион размеров экранов (desktop, tablet, phone)

**Решение:** Responsive layouts

**Пример: Mobile-first responsive design**

```css

/* Mobile-first подход */
.container {
  width: 100%;
  padding: 10px;
}

/* Tablet */
@media (min-width: 768px) {
  .container {
    max-width: 750px;
    margin: 0 auto;
    padding: 20px;
  }
  .sidebar {
    display: block;
    width: 30%;
    float: left;
  }
  .content {
    width: 70%;
    float: right;
  }
}

/* Desktop */
@media (min-width: 1200px) {
  .container {
    max-width: 1170px;
  }
}
```

**Пример: Flexbox для responsive**

```css

/* Гибкая сетка с Flexbox */
.row {
  display: flex;
  flex-wrap: wrap;
}

.col {
  flex: 1;
  min-width: 300px; /* Минимальная ширина колонки */
}

/* На мобильных: одна колонка */
@media (max-width: 768px) {
  .col {
    flex: 100%;
  }
}
```

**Пример: Grid layout**

```css

/* CSS Grid для сложных layouts */
.container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
}

/* Адаптация под размер экрана */
@media (max-width: 768px) {
  .container {
    grid-template-columns: 1fr;
  }
}
```

Адаптация под размер экрана, ориентацию, input methods.

### 5.3 Web APIs и интерактивность

**Пример: Fetch API для AJAX**

```javascript

// Современный подход к AJAX
async function loadData() {
  try {
    const response = await fetch('/api/data');
    const data = await response.json();
    updateUI(data);
  } catch (error) {
    console.error('Error:', error);
  }
}

// Обновление UI без перезагрузки страницы
function updateUI(data) {
  const container = document.getElementById('content');
  container.innerHTML = data.map(item => 
    `<div class="item">${item.name}</div>`
  ).join('');
}
```

**Пример: WebSocket для real-time**

```javascript

// Real-time обновления через WebSocket
const socket = new WebSocket('ws://example.com/updates');

socket.onmessage = function(event) {
  const data = JSON.parse(event.data);
  // Обновление UI в реальном времени
  updateNotification(data);
};

// Отправка сообщения
socket.send(JSON.stringify({ type: 'subscribe', channel: 'news' }));
```

---

## 6. Touch и мультитач (2000-е - настоящее время)

### 6.1 Ранние сенсорные экраны

**1980-е - 1990-е:**

- Resistive touch screens
- Stylus-based (Palm Pilot, Newton)
- Single touch

**Ограничения:**

- Неточность
- Один палец
- Требуется стилус или сильное нажатие

### 6.2 iPhone и революция

**iPhone (2007):**

- Capacitive multitouch
- Finger gestures
- No stylus needed

**Новые паттерны взаимодействия:**

- **Tap:** Выбор

- **Swipe:** Навигация

- **Pinch-to-zoom:** Масштабирование

- **Long press:** Контекстное меню

**Философия:**

- Direct manipulation — объекты реагируют на пальцы
- Physics-based animations — инерция, bounce
- Minimalism — убрать всё лишнее

### 6.3 Touch UI design principles

**Fat Finger Problem:**

- Палец ~44x44 points (Apple HIG)
- Кнопки должны быть большими
- Расстояние между элементами

**Пример: Правильные размеры для touch**

```css

/* Минимальный размер кнопки для touch */
.touch-button {
  min-width: 44px;
  min-height: 44px;
  padding: 12px 24px;
  margin: 8px; /* Расстояние между кнопками */
}

/* Неправильно: слишком маленькие кнопки */
.small-button {
  width: 20px;
  height: 20px; /* Слишком мало для пальца! */
}
```

**No Hover:**

- Нет mouse-over состояний
- Tooltip'ы не работают
- Все действия должны быть видны

**Пример: Адаптация под touch**

```javascript

// Определение touch устройства
const isTouchDevice = 'ontouchstart' in window || 
                      navigator.maxTouchPoints > 0;

if (isTouchDevice) {
  // Показать все действия явно
  document.querySelectorAll('.hidden-on-desktop')
    .forEach(el => el.style.display = 'block');
  
  // Увеличить размеры элементов
  document.body.classList.add('touch-mode');
}
```

### 6.4 Gesture Recognition

**Пример: Обработка жестов в JavaScript**

```javascript

// Обработка swipe жеста
let touchStartX = 0;
let touchEndX = 0;

element.addEventListener('touchstart', (e) => {
  touchStartX = e.changedTouches[0].screenX;
});

element.addEventListener('touchend', (e) => {
  touchEndX = e.changedTouches[0].screenX;
  handleSwipe();
});

function handleSwipe() {
  const diff = touchStartX - touchEndX;
  if (Math.abs(diff) > 50) { // Минимальное расстояние
    if (diff > 0) {
      swipeLeft(); // Свайп влево
    } else {
      swipeRight(); // Свайп вправо
    }
  }
}
```

**Пример: Pinch-to-zoom**

```javascript

// Обработка pinch жеста
let initialDistance = 0;

element.addEventListener('touchstart', (e) => {
  if (e.touches.length === 2) {
    const touch1 = e.touches[0];
    const touch2 = e.touches[1];
    initialDistance = Math.hypot(
      touch2.clientX - touch1.clientX,
      touch2.clientY - touch1.clientY
    );
  }
});

element.addEventListener('touchmove', (e) => {
  if (e.touches.length === 2) {
    const touch1 = e.touches[0];
    const touch2 = e.touches[1];
    const currentDistance = Math.hypot(
      touch2.clientX - touch1.clientX,
      touch2.clientY - touch1.clientY
    );
    const scale = currentDistance / initialDistance;
    element.style.transform = `scale(${scale})`;
  }
});
```

---

## 7. Voice UI (2010-е - настоящее время)

### 7.1 Голосовые ассистенты

**Siri (2011):** Apple
**Google Assistant (2012)**
**Alexa (2014):** Amazon

**Capabilities:**

- Voice recognition (Speech-to-Text)
- Natural Language Understanding (NLU)
- Text-to-Speech (TTS)

**Use cases:**

- Hands-free: в машине, при готовке
- Accessibility: для людей с ограниченными возможностями
- Quick queries: "Какая погода?", "Поставь таймер"

### 7.2 Ограничения Voice UI

**Проблемы:**

- Accent и диалекты
- Шум в фоне
- Privacy concerns
- Slow для сложных задач
- Нет visual feedback — память пользователя

**Пример: Обработка ошибок распознавания**

```javascript

// Web Speech API
const recognition = new webkitSpeechRecognition();
recognition.lang = 'ru-RU';
recognition.continuous = false;

recognition.onresult = function(event) {
  const transcript = event.results[0][0].transcript;
  
  // Обработка неоднозначности
  if (transcript.includes('включи') || transcript.includes('включить')) {
    handleTurnOn();
  } else if (transcript.includes('выключи')) {
    handleTurnOff();
  } else {
    // Непонятная команда
    speak("Извините, я не понял. Повторите, пожалуйста.");
  }
};

recognition.onerror = function(event) {
  if (event.error === 'no-speech') {
    speak("Я не услышал команду. Попробуйте ещё раз.");
  } else if (event.error === 'network') {
    speak("Проблема с сетью. Проверьте подключение.");
  }
};
```

**Не заменяет другие UI:**
Voice дополняет, не заменяет touch/mouse/keyboard.

**Пример: Hybrid UI (Voice + Visual)**

```javascript

// Комбинация voice и visual feedback
function handleVoiceCommand(command) {
  // Выполнение команды
  executeCommand(command);
  
  // Visual feedback (важно!)
  showNotification(`Выполнено: ${command}`);
  highlightElement(command.target);
  
  // Подтверждение голосом
  speak(`Готово. ${command.result}`);
}
```

---

## 8. Визуальные и пространственные интерфейсы

### 8.1 Gesture Recognition

**Microsoft Kinect (2010):**

- Skeleton tracking
- Gestures без контроллеров
- Gaming, fitness

**Leap Motion:**

- Точное отслеживание пальцев
- 3D manipulation

**Проблемы:**

- Gorilla Arm Syndrome — усталость от поднятых рук
- Неточность
- Отсутствие тактильной обратной связи

### 8.2 AR (Augmented Reality)

**Определение:** Наложение цифровой информации на реальный мир

**Примеры:**

- Pokémon GO (2016)
- Google Glass (2013, провал)
- Snapchat/Instagram filters

**Apple ARKit, Google ARCore:**

- Plane detection
- Object tracking
- Occlusion

**Use cases:**

- Navigation (направления на улице)
- Furniture placement (IKEA app)
- Training и обучение

### 8.3 VR (Virtual Reality)

**Определение:** Полное погружение в виртуальный мир

**Устройства:**

- Oculus Rift (2016)
- HTC Vive
- PlayStation VR
- Meta Quest

**Challenges:**

- Motion sickness
- High hardware requirements
- Isolation от реального мира
- Social acceptance

### 8.4 Spatial Computing

**Apple Vision Pro (2024):**

- Mixed Reality — AR + VR
- Eye tracking + hand gestures
- Spatial audio
- Концепция: Apps живут в 3D пространстве вокруг пользователя

**Новая парадигма:**

- Не экраны, а пространство
- Взгляд + жесты вместо мыши
- Spatial memory — где оставил окна

---

## 9. Нейроинтерфейсы и будущее

### 9.1 Brain-Computer Interfaces (BCI)

**Neuralink, Kernel:**

- Прямое чтение сигналов мозга
- Пока: медицина (парализованные пациенты)
- Будущее: прямой контроль устройств мыслями

**Существующие:**

- EEG-based BCI (неинвазивные)
- Concentration games
- Basic control (двигать курсор)

### 9.2 Eye Tracking

**Технология:**

- Камера отслеживает зрачки
- Foveated rendering (VR)
- Accessibility

**Apple Vision Pro:**

- Взгляд как primary input
- Смотришь на кнопку → она активируется
- Pinch для подтверждения

### 9.3 Haptic Feedback

**Тактильная обратная связь:**

- Vibration motors
- Force feedback (game controllers)
- Ultrasonic haptics (ощущение без касания)

**Важность:**
Человек привык к физическим ощущениям. Их отсутствие делает UI менее интуитивным.

### 9.4 Ambient Computing

**Концепция:** UI исчезает — технологии вокруг, всегда доступны

**Признаки:**

- Voice ассистенты в каждой комнате
- Wearables (часы, очки)
- IoT — умный дом реагирует автоматически
- Context-aware — система знает, где ты и что делаешь

---

## 10. Accessibility и инклюзивный дизайн

### 10.1 Screen Readers

**Для незрячих:**

- JAWS, NVDA (Windows)
- VoiceOver (macOS/iOS)
- TalkBack (Android)

Читают контент вслух, навигация по структуре.

### 10.2 Voice Control

**Для людей с ограниченной подвижностью:**

- Полный контроль голосом
- "Click button", "Scroll down"

### 10.3 Адаптивные интерфейсы

**High contrast modes, Large text, Reduced motion**

**Пример: Поддержка accessibility в CSS**

```css

/* Уважение к пользовательским настройкам */
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}

@media (prefers-contrast: high) {
  .button {
    border: 2px solid;
    background: white;
    color: black;
  }
}

/* Увеличенный текст */
@media (prefers-font-size: large) {
  body {
    font-size: 1.2em;
  }
}
```

**Пример: Semantic HTML для screen readers**

```html

<!-- Правильно: semantic HTML -->
<nav aria-label="Main navigation">
  <ul>
    <li><a href="/">Home</a></li>
    <li><a href="/about">About</a></li>
  </ul>
</nav>

<main>
  <article>
    <h1>Article Title</h1>
    <p>Article content...</p>
  </article>
</main>

<!-- Неправильно: div soup -->
<div class="nav">
  <div class="link">Home</div>
  <div class="link">About</div>
</div>
```

**Пример: ARIA labels**

```html

<!-- Кнопка без видимого текста нуждается в label -->
<button aria-label="Close dialog">
  <span class="icon-close"></span>
</button>

<!-- Форма с описанием -->
<form>
  <label for="email">Email address</label>
  <input type="email" id="email" 
         aria-describedby="email-help">
  <span id="email-help">We'll never share your email</span>
</form>
```

**Важность:**
~15% населения имеют те или иные ограничения. Accessibility улучшает UX для всех.

### 10.4 Keyboard Navigation

**Пример: Поддержка клавиатурной навигации**

```javascript

// Обработка Tab navigation
document.addEventListener('keydown', (e) => {
  if (e.key === 'Tab') {
    // Убедиться, что фокус виден
    document.activeElement.style.outline = '2px solid blue';
  }
  
  // Escape для закрытия модальных окон
  if (e.key === 'Escape') {
    closeModal();
  }
  
  // Enter для активации кнопок
  if (e.key === 'Enter' && e.target.tagName === 'BUTTON') {
    e.target.click();
  }
});
```

**Пример: Focus management**

```javascript

// Управление фокусом для accessibility
function openModal() {
  modal.style.display = 'block';
  
  // Переместить фокус в модальное окно
  const firstInput = modal.querySelector('input');
  firstInput.focus();
  
  // Захватить фокус (trap focus)
  trapFocus(modal);
}

function closeModal() {
  modal.style.display = 'none';
  
  // Вернуть фокус на элемент, который открыл модальное окно
  previousFocusedElement.focus();
}
```

---

## 11. Производительность UI

### 11.1 Оптимизация рендеринга

**Проблема:** Медленный UI раздражает пользователей

**Решения:**

**1. Virtual Scrolling:**
```javascript

// Рендеринг только видимых элементов
function VirtualList({ items }) {
  const [startIndex, setStartIndex] = useState(0);
  const visibleItems = items.slice(startIndex, startIndex + 20);
  
  return (
    <div onScroll={handleScroll}>
      {visibleItems.map(item => <Item key={item.id} data={item} />)}
    </div>
  );
}
```

**2. Debouncing и Throttling:**
```javascript

// Debounce: выполнить после паузы
function debounce(func, wait) {
  let timeout;
  return function(...args) {
    clearTimeout(timeout);
    timeout = setTimeout(() => func.apply(this, args), wait);
  };
}

// Использование для поиска
const searchInput = document.getElementById('search');
searchInput.addEventListener('input', debounce(handleSearch, 300));
// Поиск выполнится только через 300ms после последнего ввода

// Throttle: выполнить не чаще чем раз в N ms
function throttle(func, limit) {
  let inThrottle;
  return function(...args) {
    if (!inThrottle) {
      func.apply(this, args);
      inThrottle = true;
      setTimeout(() => inThrottle = false, limit);
    }
  };
}
```

**3. Lazy Loading:**
```javascript

// Загрузка изображений по требованию
const images = document.querySelectorAll('img[data-src]');

const imageObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const img = entry.target;
      img.src = img.dataset.src;
      imageObserver.unobserve(img);
    }
  });
});

images.forEach(img => imageObserver.observe(img));
```

### 11.2 Измерение производительности

**Пример: Web Vitals**

```javascript

// Core Web Vitals
import { getCLS, getFID, getFCP, getLCP, getTTFB } from 'web-vitals';

getCLS(console.log); // Cumulative Layout Shift
getFID(console.log); // First Input Delay
getFCP(console.log); // First Contentful Paint
getLCP(console.log); // Largest Contentful Paint
getTTFB(console.log); // Time to First Byte

// Целевые значения:
// LCP < 2.5s
// FID < 100ms
// CLS < 0.1
```

---

## 💡 Key Takeaways

- **Эволюция UI** — от batch processing к интерактивности, от текста к графике, от desktop к mobile и beyond, каждый этап решал конкретные проблемы

- **CLI не умер** — остаётся самым эффективным для автоматизации, удалённого доступа и работы с большими объёмами данных благодаря композиции команд и scripting

- **Разные UI для разных контекстов** — нет "лучшего" интерфейса, есть подходящий для задачи: CLI для серверов, GUI для desktop, Touch для mobile, Voice для hands-free

- **Touch изменил парадигму** — direct manipulation, gestures, mobile-first design требуют новых подходов (fat finger problem, no hover, gestures)

- **Будущее — multimodal** — комбинация voice, touch, gestures, gaze в зависимости от контекста обеспечивает естественное взаимодействие

- **Accessibility критична** — инклюзивный дизайн делает технологии доступными для всех (~15% населения имеют ограничения) и улучшает UX для всех пользователей

---

## 🚀 Next Steps

После изучения эволюции UI рекомендуется:

- [26_ModernComputing](../26_ModernComputing/) — Как современные интерфейсы встраиваются в общую картину
- [27_FutureTrends](../27_FutureTrends/) — Будущие направления развития

---

## 📚 Additional Resources

### Книги

- **"The Design of Everyday Things"** — Don Norman

- **"GUI Bloopers"** — Jeff Johnson

- **"Designing Interfaces"** — Jenifer Tidwell

### Статьи и видео

- Apple Human Interface Guidelines
- Google Material Design
- Microsoft Fluent Design System

### Исторические

- Xerox PARC videos
- "Mother of All Demos" — Douglas Engelbart (1968)

---


