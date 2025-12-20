# Графические системы и GPU - Quiz

Проверьте свои знания по теме "От текстовых терминалов к массивно-параллельным вычислениям".

---

## Question 1: Текстовые терминалы

Что характеризовало текстовые терминалы 1960-1980-х годов?

A) 80x25 символов, ASCII таблица, псевдографика

B) 3D графика

C) Цветная графика высокого разрешения

D) Графический интерфейс с окнами

---

## Question 2: Framebuffer

Что такое framebuffer?

A) Файловая система

B) Область памяти, представляющая экран

C) Устройство для вывода звука

D) Тип процессора

---

## Question 3: CPU vs GPU

Какое основное отличие архитектуры GPU от CPU?

A) GPU имеет больше кэша

B) GPU не может выполнять вычисления

C) GPU имеет тысячи простых ядер, CPU — несколько мощных ядер

D) GPU работает медленнее CPU

---

## Question 4: SIMD

Что означает SIMD архитектура GPU?

A) Single Instruction, Multiple Devices

B) Sequential Instruction, Multiple Data

C) Single Instruction, Multiple Data — одна инструкция для тысяч элементов одновременно

D) Simple Instruction, Multiple Devices

---

## Question 5: CUDA Cores

Что такое CUDA Core в архитектуре GPU?

A) Простое вычислительное ядро в GPU

B) Графический процессор

C) Тип памяти

D) Интерфейс программирования

---

## Question 6: Warp

Что такое warp в архитектуре NVIDIA GPU?

A) Протокол передачи данных

B) Графический API

C) Тип памяти

D) Группа из 32 потоков, выполняющих одну инструкцию

---

## Question 7: Rendering Pipeline

Какой порядок этапов в графическом pipeline?

A) Fragment Processing → Vertex Processing → Rasterization → Display

B) Display → Fragment Processing → Rasterization → Vertex Processing

C) Vertex Processing → Display → Rasterization → Fragment Processing

D) 3D Model → Vertex Processing → Rasterization → Fragment Processing → Display

---

## Question 8: GPGPU

Что означает GPGPU?

A) General Purpose GPU — использование GPU для общих вычислений

B) Graphics Processing GPU

C) Graphics Performance GPU

D) General Programming GPU

---

## Question 9: CUDA Kernel

Что такое kernel в контексте CUDA?

A) Графический процессор

B) Тип памяти GPU

C) Функция, выполняемая на GPU

D) Ядро операционной системы

---

## Question 10: VRAM

Что такое VRAM?

A) Виртуальная память

B) Оперативная память компьютера

C) Кэш процессора

D) Видеопамять на видеокарте с высоким bandwidth

---

## Question 11: GDDR vs HBM

В чём различие между GDDR6 и HBM памятью?

A) GDDR6 быстрее HBM

B) HBM используется только в CPU

C) GDDR6 используется только в CPU

D) HBM — stacked memory с очень высоким bandwidth, используется в datacenter GPUs

---

## Question 12: Unified Memory

Что такое Unified Memory в контексте Apple Silicon?

A) Объединение CPU и GPU памяти в одну систему

B) Увеличение объёма памяти

C) Протокол передачи данных

D) Тип файловой системы

---

## Question 13: Ray Tracing

В чём основное отличие ray tracing от rasterization?

A) Rasterization более реалистичен

B) Ray tracing симулирует физику света, rasterization — проекция треугольников

C) Ray tracing быстрее

D) Нет различий

---

## Question 14: RT Cores

Для чего используются RT Cores в NVIDIA RTX?

A) Для сетевых операций

B) Для hardware-accelerated ray-triangle intersection

C) Для работы с памятью

D) Для обработки текста

---

## Question 15: Tensor Cores

Для чего используются Tensor Cores?

A) Для графики

B) Для сетевых операций

C) Для matrix operations в deep learning

D) Для работы с файлами

---

## Question 16: DLSS

Что такое DLSS?

A) Data Link System

B) Deep Learning Super Sampling — AI upscaling для повышения производительности

C) DirectX Library

D) Display Library System

---

## Question 17: GPU Performance

Во сколько раз GPU может быть быстрее CPU для параллельных задач?

A) В 10 раз

B) GPU всегда медленнее CPU

C) До 100 раз (пример: 10,000 GFLOPS vs 100 GFLOPS)

D) В 2 раза

---

## Question 18: OpenGL vs DirectX

В чём различие между OpenGL и DirectX?

A) Нет различий

B) OpenGL — cross-platform, DirectX — Microsoft/Windows

C) OpenGL только для Windows

D) DirectX только для Linux

---

## Question 19: Vulkan

Что такое Vulkan?

A) Тип памяти

B) Старая версия OpenGL

C) Графический процессор

D) Современная low-level API, преемник OpenGL

---

## Question 20: GPU Trade-off

Какое trade-off характерно для GPU?

A) GPU всегда быстрее CPU

B) GPU быстры для параллельных задач, но медленны для последовательных

C) GPU быстры для последовательных задач

D) GPU не могут выполнять вычисления

---

## Question 21: Warp Divergence

Что происходит при divergence в warp (32 потока идут разными путями)?

A) Обе ветки выполняются параллельно

B) Обе ветки выполняются последовательно, что снижает производительность

C) GPU автоматически оптимизирует divergence

D) Divergence не влияет на производительность

---

## Question 22: Shared Memory

Зачем используется shared memory в CUDA?

A) Для хранения глобальных переменных

B) Для связи между разными GPU

C) Для хранения результатов kernel

D) Для быстрого доступа к данным, используемым несколькими threads в блоке

---

## Question 23: Memory Coalescing

Что такое coalesced memory access?

A) Последовательный доступ к памяти, который позволяет GPU читать данные эффективно

B) Использование unified memory

C) Копирование данных между CPU и GPU

D) Случайный доступ к памяти

---

## Question 24: Vulkan vs OpenGL

В чём основное преимущество Vulkan перед OpenGL?

A) Vulkan работает только на Windows

B) Vulkan имеет меньше overhead и лучшую производительность

C) Vulkan не требует драйверов

D) Vulkan проще в использовании

---

## Question 25: Vertex Shader

Что делает vertex shader в графическом pipeline?

A) Управляет памятью GPU

B) Рендерит текстуры

C) Обрабатывает пиксели

D) Трансформирует 3D координаты вершин и вычисляет освещение

---

## Question 26: Fragment Shader

Что делает fragment shader (pixel shader)?

A) Копирует данные в память

B) Обрабатывает вершины

C) Управляет rasterization

D) Вычисляет цвет каждого пикселя (текстурирование, освещение, эффекты)

---

## Question 27: OpenCL

Что такое OpenCL?

A) Открытый стандарт для GPGPU, работающий на разных GPU/CPU

B) Тип памяти GPU

C) Язык программирования для GPU

D) Графический API только для NVIDIA

---

## Question 28: Unified Memory Trade-off

Какое trade-off у unified memory (CPU и GPU разделяют память)?

A) Unified memory медленнее всегда

B) Больше bandwidth, но сложнее программирование

C) Нет trade-off, это всегда лучше

D) Упрощение программирования, но меньший bandwidth для GPU

---

## Question 29: DLSS Performance

Какой прирост производительности даёт DLSS при upscaling с 1440p до 4K?

A) ~10x прирост FPS

B) Нет прироста, только улучшение качества

C) DLSS замедляет рендеринг

D) ~2x прирост FPS при сохранении ~95% качества

---

## Question 30: RT Cores Performance

Во сколько раз RT Cores ускоряют ray tracing по сравнению с software ray tracing?

A) В 5 раз

B) RT Cores не ускоряют ray tracing

C) В 2 раза

D) В 30-60 раз (с ~1 FPS до 30-60 FPS)

---

---

## Answer Key

| # | Answer | Explanation |
|---|--------|-------------|
| 1 | A | Текстовые терминалы характеризовались 80x25 символами, ASCII таблицей и псевдографикой. |
| 2 | B | Framebuffer — это область памяти, представляющая экран. |
| 3 | C | GPU имеет тысячи простых ядер, оптимизированных для параллельных задач, в то время как CPU имеет несколько мощных ядер. |
| 4 | C | SIMD означает Single Instruction, Multiple Data — одна инструкция выполняется для тысяч элементов одновременно. |
| 5 | A | CUDA Core — это простое вычислительное ядро в GPU. |
| 6 | D | Warp — это группа из 32 потоков, выполняющих одну инструкцию в архитектуре NVIDIA GPU. |
| 7 | D | Правильный порядок: 3D Model → Vertex Processing → Rasterization → Fragment Processing → Display. |
| 8 | A | GPGPU означает General Purpose GPU — использование GPU для общих вычислений, не только графики. |
| 9 | C | Kernel в CUDA — это функция, выполняемая на GPU. |
| 10 | D | VRAM — это видеопамять на видеокарте с очень высоким bandwidth. |
| 11 | D | HBM — это stacked memory с очень высоким bandwidth, используется в datacenter GPUs, в то время как GDDR6 используется в gaming GPUs. |
| 12 | A | Unified Memory объединяет CPU и GPU память в одну систему, что упрощает программирование. |
| 13 | B | Ray tracing симулирует физику света для реалистичных отражений, в то время как rasterization — это проекция треугольников на экран. |
| 14 | B | RT Cores используются для hardware-accelerated ray-triangle intersection в NVIDIA RTX. |
| 15 | C | Tensor Cores специализированы для matrix operations в deep learning. |
| 16 | B | DLSS — это Deep Learning Super Sampling, AI upscaling для повышения производительности при сохранении качества. |
| 17 | C | GPU может быть до 100 раз быстрее CPU для параллельных задач (пример: 10,000 GFLOPS vs 100 GFLOPS). |
| 18 | B | OpenGL — cross-platform open standard, DirectX — Microsoft, в основном для Windows/Xbox. |
| 19 | D | Vulkan — это современная low-level API, преемник OpenGL. |
| 20 | B | GPU быстры для параллельных задач, но медленны для последовательных задач. |
| 21 | B | При divergence в warp обе ветки выполняются последовательно, что снижает производительность в 2 раза. |
| 22 | D | Shared memory используется для быстрого доступа к данным, используемым несколькими threads в блоке, что может ускорить код в 10-100 раз. |
| 23 | A | Coalesced memory access — это последовательный доступ к памяти, который позволяет GPU читать данные эффективно за один транзакцию. |
| 24 | B | Vulkan имеет меньше overhead (нет driver overhead) и лучшую производительность (10-30% быстрее OpenGL), но требует больше boilerplate кода. |
| 25 | D | Vertex shader трансформирует 3D координаты вершин (model → view → projection) и вычисляет освещение на уровне вершин. |
| 26 | D | Fragment shader (pixel shader) вычисляет цвет каждого пикселя, включая текстурирование, освещение и эффекты. |
| 27 | A | OpenCL — это открытый стандарт для GPGPU, который работает на разных GPU (NVIDIA, AMD, Intel) и CPU, в отличие от CUDA (только NVIDIA). |
| 28 | D | Unified memory упрощает программирование (нет явных копирований), но даёт меньший bandwidth для GPU по сравнению с отдельной VRAM. |
| 29 | D | DLSS даёт ~2x прирост FPS при upscaling с 1440p до 4K, сохраняя ~95% качества нативного 4K рендеринга. |
| 30 | D | RT Cores ускоряют ray tracing в 30-60 раз, позволяя достичь 30-60 FPS вместо ~1 FPS на software ray tracing. |

---

## Scoring Guide

- **27-30 правильных ответов (90-100%):** 🏆 Отлично! Вы отлично усвоили материал. Переходите к следующему модулю.

- **21-26 правильных ответов (70-89%):** ✅ Хорошо! Хороший результат! Повторите темы, в которых ошиблись.

- **15-20 правильных ответов (50-69%):** ⚠️ Удовлетворительно. Рекомендуется перечитать соответствующие разделы лекции.

- **Менее 15 правильных ответов (<50%):** 📚 Нужно повторить. Внимательно перечитайте лекцию и попробуйте ещё раз.

---

