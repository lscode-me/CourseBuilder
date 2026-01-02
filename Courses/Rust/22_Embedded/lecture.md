# Встраиваемые и low-level системы
## Embedded Rust, no_std, ограничения среды

---

## 📋 Prerequisites

Перед началом этого модуля вы должны:

- Понимать системное программирование (см. модуль [17_System_Programming](../17_System_Programming/))
- Знать управление памятью (см. модуль [12_Memory_Management](../12_Memory_Management/))
- Иметь представление о embedded системах

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:

- Понимать, что такое embedded Rust
- Использовать no_std для ограниченных сред
- Работать с ограничениями embedded систем
- Применять Rust для микроконтроллеров
- Понимать различия между std и no_std

---

## 1. Embedded Rust

### 1.1 Что такое Embedded Rust

**Embedded Rust** — использование Rust для программирования микроконтроллеров и встраиваемых систем.

**Характеристики:**

- Ограниченные ресурсы
- Отсутствие ОС
- Прямой доступ к железу
- Реальное время

### 1.2 Преимущества Rust для embedded

**Почему Rust:**

- Безопасность памяти без GC
- Предсказуемое поведение
- Низкий overhead
- Мощная система типов

---

## 2. no_std

### 2.1 Что такое no_std

**no_std** — режим Rust без стандартной библиотеки.

**Ограничения:**

- Нет heap (нет Vec, String)
- Нет файловой системы
- Нет сетевых операций
- Только core библиотека

**Example: no_std программа**

```rust
#![no_std]
#![no_main]

use core::panic::PanicInfo;

#[panic_handler]
fn panic(_info: &PanicInfo) -> ! {
    loop {}
}

#[no_mangle]
pub extern "C" fn _start() -> ! {
    loop {}
}
```

### 2.2 Когда использовать no_std

**Используйте no_std для:**

- Микроконтроллеров
- Ядра ОС
- Bootloaders
- Реального времени

---

## 3. Ограничения среды

### 3.1 Ограниченная память

**Embedded системы имеют:**

- Ограниченную RAM
- Ограниченную flash память
- Нет heap (обычно)

### 3.2 Отсутствие ОС

**Нет:**

- Файловой системы
- Сетевого стека
- Многозадачности (обычно)
- Стандартной библиотеки

---

## 4. Примеры использования

### 4.1 Популярные платформы

**Примеры:**

- **STM32** — ARM микроконтроллеры

- **Arduino** — популярная платформа

- **ESP32** — Wi-Fi/Bluetooth микроконтроллеры

- **Raspberry Pi Pico** — RP2040

- **nRF52** — Bluetooth микроконтроллеры

### 4.2 Экосистема

**Популярные crates:**

- **embedded-hal** — аппаратная абстракция

- **cortex-m** — для ARM Cortex-M

- **nb** — неблокирующие операции

- **embedded-time** — работа со временем

- **heapless** — коллекции без heap

### 4.3 Пример: Простая embedded программа

**Example: Мигание LED**

```rust
// #![no_std]
// #![no_main]
//
// use cortex_m_rt::entry;
// use embedded_hal::digital::OutputPin;
//
// #[entry]
// fn main() -> ! {
//     let mut led = // Инициализация LED
//     
//     loop {
//         led.set_high();
//         delay(1000);
//         led.set_low();
//         delay(1000);
//     }
// }
```

### 4.4 Ограничения и решения

**Проблемы:**

- Нет heap → используйте статические массивы
- Нет стандартной библиотеки → используйте core
- Ограниченная память → оптимизируйте код

**Решения:**

- **heapless** — коллекции без heap

- **embedded-hal** — абстракция над железом

- **cortex-m** — поддержка ARM Cortex-M

---

## 5. Практические примеры

### 5.1 Пример: no_std программа

```rust
#![no_std]
#![no_main]

use core::panic::PanicInfo;

#[panic_handler]
fn panic(_info: &PanicInfo) -> ! {
    loop {}
}

#[no_mangle]
pub extern "C" fn _start() -> ! {
    // Инициализация
    loop {
        // Основной цикл
    }
}
```

### 5.2 Пример: Работа без heap

```rust
#![no_std]

use heapless::Vec;

fn main() {
    // Статический массив вместо Vec
    let mut buffer: Vec<u8, 100> = Vec::new();
    
    for i in 0..10 {
        buffer.push(i).unwrap();
    }
    
    // buffer имеет фиксированный размер
}
```

### 5.3 Пример: Работа с регистрами

```rust
// Концептуальный пример работы с регистрами
// use volatile_register::{RW, RO};

// struct Registers {
//     control: RW<u32>,
//     status: RO<u32>,
//     data: RW<u32>,
// }

// fn configure_device(regs: &mut Registers) {
//     // Запись в регистр управления
//     regs.control.write(0x01);
//     
//     // Чтение статуса
//     let status = regs.status.read();
// }
```

### 5.4 Пример: Прерывания

```rust
// #![no_std]
// use cortex_m::interrupt;

// #[interrupt]
// fn TIM2() {
//     // Обработчик прерывания таймера
// }
```

---

## 6. Реальное время

### 6.1 Требования real-time систем

**Характеристики:**

- Детерминированное время отклика
- Гарантированные временные ограничения
- Предсказуемое поведение

**Rust преимущества:**

- Нет GC пауз
- Предсказуемое управление памятью
- Низкий overhead

### 6.2 Пример: Real-time задача

```rust
// #![no_std]
// use cortex_m_rt::entry;

// #[entry]
// fn main() -> ! {
//     loop {
//         // Критическая задача с временными ограничениями
//         critical_task();
//         // Гарантированное время выполнения
//     }
// }
```

---

## 7. Популярные платформы детально

### 7.1 STM32

**Характеристики:**

- ARM Cortex-M микроконтроллеры
- Широкий выбор моделей
- Богатая экосистема

**Примеры использования:**

- Промышленная автоматизация
- IoT устройства
- Медицинские приборы

### 7.2 ESP32

**Характеристики:**

- Wi-Fi и Bluetooth
- Двойное ядро
- Низкая стоимость

**Примеры использования:**

- Умный дом
- IoT сетевое подключение
- Прототипирование

### 7.3 Raspberry Pi Pico

**Характеристики:**

- RP2040 чип
- Низкая стоимость
- Хорошая документация

**Примеры использования:**

- Образование
- Прототипирование
- Хобби проекты

---

## 8. Практические примеры

### 8.1 Пример: Чтение датчика

```rust
// #![no_std]
// use embedded_hal::adc::OneShot;

// fn read_sensor<ADC, PIN>(adc: &mut ADC, pin: &mut PIN) -> u16
// where
//     ADC: OneShot<ADC, u16, PIN>,
// {
//     adc.read(pin).unwrap()
// }
```

### 8.2 Пример: Управление мотором

```rust
// #![no_std]
// use embedded_hal::PwmPin;

// fn control_motor<PWM>(pwm: &mut PWM, speed: u8)
// where
//     PWM: PwmPin<Duty = u16>,
// {
//     let duty = (speed as u16) * 100;
//     pwm.set_duty(duty);
//     pwm.enable();
// }
```

### 8.3 Пример: Коммуникация по UART

```rust
// #![no_std]
// use embedded_hal::serial::{Read, Write};

// fn send_data<SERIAL>(serial: &mut SERIAL, data: &[u8])
// where
//     SERIAL: Write<u8>,
// {
//     for byte in data {
//         serial.write(*byte).unwrap();
//     }
// }
```

---

## 💡 Key Takeaways

- **Embedded Rust для микроконтроллеров:** Программирование встраиваемых систем

- **no_std без стандартной библиотеки:** Только core для ограниченных сред

- **Ограниченные ресурсы:** Мало памяти, нет ОС, нет heap

- **Rust безопасен для embedded:** Безопасность памяти без GC

- **Растущая экосистема:** embedded-hal, cortex-m и другие

---

## 🚀 Next Steps

**Related Modules:**

- [Кейсы системного Rust](../23_System_Cases/) — реальные примеры
- [System Programming](../17_System_Programming/) — основы системного программирования

**Practice Ideas:**

1. Изучите embedded-hal для аппаратной абстракции
2. Попробуйте создать простую no_std программу
3. Изучите примеры embedded проектов
4. Попробуйте программирование микроконтроллера

**Going Deeper:**

- Изучите конкретные платформы (STM32, ESP32)
- Почитайте о real-time системах
- Изучите примеры embedded проектов на Rust

---

## 📚 Additional Resources

**Documentation:**

- [Embedded Rust Book](https://docs.rust-embedded.org/book/) — книга по embedded Rust
- [The Embedded Rust Book](https://docs.rust-embedded.org/discovery/) — обучение

**Projects:**

- [embedded-hal](https://github.com/rust-embedded/embedded-hal) — аппаратная абстракция

---



