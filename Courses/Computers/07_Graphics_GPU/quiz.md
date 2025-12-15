# Графические системы и GPU - Quiz

Проверьте свои знания по теме "От текстовых терминалов к массивно-параллельным вычислениям".

---

## Question 1: Текстовые терминалы

Что характеризовало текстовые терминалы 1960-1980-х годов?

A) Графический интерфейс с окнами

B) 80x25 символов, ASCII таблица, псевдографика

C) Цветная графика высокого разрешения

D) 3D графика

---

## Question 2: Framebuffer

Что такое framebuffer?

A) Область памяти, представляющая экран

B) Устройство для вывода звука

C) Файловая система

D) Тип процессора

---

## Question 3: CPU vs GPU

Какое основное отличие архитектуры GPU от CPU?

A) GPU имеет тысячи простых ядер, CPU — несколько мощных ядер

B) GPU имеет больше кэша

C) GPU не может выполнять вычисления

D) GPU работает медленнее CPU

---

## Question 4: SIMD

Что означает SIMD архитектура GPU?

A) Single Instruction, Multiple Devices

B) Single Instruction, Multiple Data — одна инструкция для тысяч элементов одновременно

C) Sequential Instruction, Multiple Data

D) Simple Instruction, Multiple Devices

---

## Question 5: CUDA Cores

Что такое CUDA Core в архитектуре GPU?

A) Интерфейс программирования

B) Тип памяти

C) Графический процессор

D) Простое вычислительное ядро в GPU

---

## Question 6: Warp

Что такое warp в архитектуре NVIDIA GPU?

A) Группа из 32 потоков, выполняющих одну инструкцию

B) Тип памяти

C) Протокол передачи данных

D) Графический API

---

## Question 7: Rendering Pipeline

Какой порядок этапов в графическом pipeline?

A) Display → Fragment Processing → Rasterization → Vertex Processing

B) 3D Model → Vertex Processing → Rasterization → Fragment Processing → Display

C) Vertex Processing → Display → Rasterization → Fragment Processing

D) Fragment Processing → Vertex Processing → Rasterization → Display

---

## Question 8: GPGPU

Что означает GPGPU?

A) General Purpose GPU — использование GPU для общих вычислений

B) Graphics Processing GPU

C) General Programming GPU

D) Graphics Performance GPU

---

## Question 9: CUDA Kernel

Что такое kernel в контексте CUDA?

A) Ядро операционной системы

B) Функция, выполняемая на GPU

C) Тип памяти GPU

D) Графический процессор

---

## Question 10: VRAM

Что такое VRAM?

A) Видеопамять на видеокарте с высоким bandwidth

B) Оперативная память компьютера

C) Виртуальная память

D) Кэш процессора

---

## Question 11: GDDR vs HBM

В чём различие между GDDR6 и HBM памятью?

A) GDDR6 быстрее HBM

B) HBM — stacked memory с очень высоким bandwidth, используется в datacenter GPUs

C) GDDR6 используется только в CPU

D) HBM используется только в CPU

---

## Question 12: Unified Memory

Что такое Unified Memory в контексте Apple Silicon?

A) Объединение CPU и GPU памяти в одну систему

B) Протокол передачи данных

C) Увеличение объёма памяти

D) Тип файловой системы

---

## Question 13: Ray Tracing

В чём основное отличие ray tracing от rasterization?

A) Ray tracing быстрее

B) Ray tracing симулирует физику света, rasterization — проекция треугольников

C) Rasterization более реалистичен

D) Нет различий

---

## Question 14: RT Cores

Для чего используются RT Cores в NVIDIA RTX?

A) Для обработки текста

B) Для сетевых операций

C) Для hardware-accelerated ray-triangle intersection

D) Для работы с памятью

---

## Question 15: Tensor Cores

Для чего используются Tensor Cores?

A) Для графики

B) Для matrix operations в deep learning

C) Для работы с файлами

D) Для сетевых операций

---

## Question 16: DLSS

Что такое DLSS?

A) Deep Learning Super Sampling — AI upscaling для повышения производительности

B) DirectX Library

C) Display Library System

D) Data Link System

---

## Question 17: GPU Performance

Во сколько раз GPU может быть быстрее CPU для параллельных задач?

A) В 2 раза

B) В 10 раз

C) До 100 раз (пример: 10,000 GFLOPS vs 100 GFLOPS)

D) GPU всегда медленнее CPU

---

## Question 18: OpenGL vs DirectX

В чём различие между OpenGL и DirectX?

A) OpenGL только для Windows

B) OpenGL — cross-platform, DirectX — Microsoft/Windows

C) DirectX только для Linux

D) Нет различий

---

## Question 19: Vulkan

Что такое Vulkan?

A) Старая версия OpenGL

B) Современная low-level API, преемник OpenGL

C) Графический процессор

D) Тип памяти

---

## Question 20: GPU Trade-off

Какое trade-off характерно для GPU?

A) GPU всегда быстрее CPU

B) GPU быстры для последовательных задач

C) GPU быстры для параллельных задач, но медленны для последовательных

D) GPU не могут выполнять вычисления

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | B | Текстовые терминалы характеризовались 80x25 символами, ASCII таблицей и псевдографикой. |
| 2 | A | Framebuffer — это область памяти, представляющая экран. |
| 3 | A | GPU имеет тысячи простых ядер, оптимизированных для параллельных задач, в то время как CPU имеет несколько мощных ядер. |
| 4 | B | SIMD означает Single Instruction, Multiple Data — одна инструкция выполняется для тысяч элементов одновременно. |
| 5 | D | CUDA Core — это простое вычислительное ядро в GPU. |
| 6 | A | Warp — это группа из 32 потоков, выполняющих одну инструкцию в архитектуре NVIDIA GPU. |
| 7 | B | Правильный порядок: 3D Model → Vertex Processing → Rasterization → Fragment Processing → Display. |
| 8 | A | GPGPU означает General Purpose GPU — использование GPU для общих вычислений, не только графики. |
| 9 | B | Kernel в CUDA — это функция, выполняемая на GPU. |
| 10 | A | VRAM — это видеопамять на видеокарте с очень высоким bandwidth. |
| 11 | B | HBM — это stacked memory с очень высоким bandwidth, используется в datacenter GPUs, в то время как GDDR6 используется в gaming GPUs. |
| 12 | A | Unified Memory объединяет CPU и GPU память в одну систему, что упрощает программирование. |
| 13 | B | Ray tracing симулирует физику света для реалистичных отражений, в то время как rasterization — это проекция треугольников на экран. |
| 14 | C | RT Cores используются для hardware-accelerated ray-triangle intersection в NVIDIA RTX. |
| 15 | B | Tensor Cores специализированы для matrix operations в deep learning. |
| 16 | A | DLSS — это Deep Learning Super Sampling, AI upscaling для повышения производительности при сохранении качества. |
| 17 | C | GPU может быть до 100 раз быстрее CPU для параллельных задач (пример: 10,000 GFLOPS vs 100 GFLOPS). |
| 18 | B | OpenGL — cross-platform open standard, DirectX — Microsoft, в основном для Windows/Xbox. |
| 19 | B | Vulkan — это современная low-level API, преемник OpenGL. |
| 20 | C | GPU быстры для параллельных задач, но медленны для последовательных задач. |

---

## Scoring Guide

- **18-20 правильных ответов (90-100%):** 🏆 Отлично! Вы отлично усвоили материал. Переходите к следующему модулю.

- **14-17 правильных ответов (70-89%):** ✅ Хорошо! Хороший результат! Повторите темы, в которых ошиблись.

- **10-13 правильных ответов (50-69%):** ⚠️ Удовлетворительно. Рекомендуется перечитать соответствующие разделы лекции.

- **Менее 10 правильных ответов (<50%):** 📚 Нужно повторить. Внимательно перечитайте лекцию и попробуйте ещё раз.

---

