# Графические системы и GPU
## От текстовых терминалов к массивно-параллельным вычислениям

---

## 📋 Prerequisites

- Понимание архитектуры процессоров
- Знание концепций параллелизма
- Базовое представление о памяти

**Recommended prior modules:**
- [04_ProcessorArchitectures](../04_ProcessorArchitectures/)
- [06_ParallelComputing](../06_ParallelComputing/)

---

## 🎯 Learning Objectives

После завершения этого модуля вы сможете:
- Объяснять эволюцию графических систем
- Понимать архитектуру GPU и её отличия от CPU
- Анализировать использование GPU для общих вычислений (GPGPU)
- Различать типы графической памяти и их применение

---

## 1. Эволюция графических систем

### 1.1 Текстовые терминалы (1960-е - 1980-е)

**Character mode:**
- 80x25 символов
- ASCII таблица
- Псевдографика для "рисования"

### 1.2 Bitmap графика

**Framebuffer** — область памяти, представляющая экран:
```
Экран 640x480, 8-bit color → 307,200 bytes
```

**Ранние системы:**
- Xerox Alto (1973)
- Apple II (1977)
- IBM PC with CGA/EGA/VGA

### 1.3 Графические ускорители

**1990-е:** 2D accelerators
- BitBlt (Bit Block Transfer)
- Hardware line drawing
- Sprite support

**Конец 1990-х:** 3D accelerators
- 3dfx Voodoo (1996)
- NVIDIA Riva 128 (1997)
- ATI Rage (1996)

---

## 2. Архитектура GPU

### 2.1 CPU vs GPU Philosophy

**CPU:**
- Несколько мощных ядер (4-64)
- Сложные инструкции
- Большие кэши
- Low latency, high throughput per thread
- Оптимизирован для последовательных задач

**GPU:**
- Тысячи простых ядер (2000-10000+)
- Простые инструкции
- Маленькие кэши
- High latency, massive throughput
- Оптимизирован для параллельных задач

### 2.2 SIMD архитектура

**Single Instruction, Multiple Data:**

CPU выполняет одну инструкцию для одного элемента:
```c
for (int i = 0; i < 1000; i++)
    result[i] = a[i] + b[i];
```

GPU выполняет одну инструкцию для тысяч элементов одновременно:
```
result[0..1000] = a[0..1000] + b[0..1000]  // параллельно!
```

### 2.3 Современная GPU архитектура

**NVIDIA Ampere/Ada (пример):**
```
GPU
├── Streaming Multiprocessors (SM) x 128
│   ├── CUDA Cores x 64
│   ├── Tensor Cores
│   ├── RT Cores (ray tracing)
│   └── Shared Memory
├── L2 Cache
└── VRAM (GDDR6/HBM)
```

**Каждый SM:**
- 64-128 CUDA cores
- Shared memory (~100 KB)
- Warp scheduler

**Warp** — группа из 32 потоков, выполняющих одну инструкцию.

---

## 3. Графический pipeline

### 3.1 Rendering Pipeline

```
3D Model → Vertex Processing → Rasterization → Fragment Processing → Display
```

**Vertex Shader:**
- Трансформация 3D координат
- Освещение

**Rasterization:**
- Конвертация треугольников в пиксели

**Fragment/Pixel Shader:**
- Текстурирование
- Lighting calculations
- Effects

### 3.2 APIs

**OpenGL (1992):** Cross-platform, open standard

**DirectX (1995):** Microsoft, Windows/Xbox

**Vulkan (2016):** Современная low-level API, преемник OpenGL

**Metal (2014):** Apple

---

## 4. GPGPU - General Purpose GPU Computing

### 4.1 Идея

**Проблема:** GPU мощны, но используются только для графики.

**Решение:** Использовать GPU для общих вычислений.

### 4.2 CUDA (2007)

**NVIDIA CUDA** — платформа для программирования GPU:

```c
__global__ void add(int *a, int *b, int *c) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    c[i] = a[i] + b[i];
}

// Host code
add<<<numBlocks, threadsPerBlock>>>(d_a, d_b, d_c);
```

**Концепции:**
- **Kernel** — функция, выполняемая на GPU
- **Thread** — один экземпляр kernel
- **Block** — группа threads (до 1024)
- **Grid** — набор blocks

### 4.3 Применения GPGPU

**Machine Learning:**
- Matrix multiplication
- Convolutions
- Training neural networks

**Scientific Computing:**
- Molecular dynamics
- Weather simulation
- Computational fluid dynamics

**Cryptocurrency:**
- Bitcoin mining
- Ethereum (до proof-of-stake)

**Video Processing:**
- Encoding/decoding
- Effects, filters

**Example Performance:**
- CPU: 100 GFLOPS
- GPU: 10,000 GFLOPS (100x!)

---

## 5. Графическая память

### 5.1 VRAM vs System RAM

**VRAM (Video RAM):**
- Находится на видеокарте
- High bandwidth (до 1 TB/s!)
- Доступна GPU напрямую
- Изолирована от CPU

**Типы:**
- **GDDR6:** 16-24 Gbps per pin (gaming GPUs)
- **HBM2/3** (High Bandwidth Memory): stacked memory, до 2 TB/s (datacenter GPUs)

### 5.2 Unified Memory (Apple Silicon, AMD APU)

**Идея:** CPU и GPU разделяют одну память

**Преимущества:**
- Нет копирования CPU ↔ GPU
- Упрощение программирования

**Недостатки:**
- Меньше bandwidth для GPU
- Конкуренция за память

---

## 6. Ray Tracing

### 6.1 Rasterization vs Ray Tracing

**Rasterization (традиционный):**
- Проекция треугольников на экран
- Fast (~60+ FPS)
- Приближения для освещения

**Ray Tracing:**
- Симуляция физики света
- Каждый луч отслеживается от камеры
- Реалистичные отражения, тени, глобальное освещение
- Very slow без hardware support

### 6.2 RT Cores

**NVIDIA RTX (2018):**
- Dedicated RT cores
- Hardware-accelerated ray-triangle intersection
- BVH (Bounding Volume Hierarchy) traversal

**Производительность:**
- Software ray tracing: ~1 FPS
- Hardware RT cores: 30-60 FPS

---

## 7. AI и Tensor Cores

### 7.1 Tensor Cores

**Специализированные блоки для matrix operations:**

```
D = A × B + C
```

Одна инструкция выполняет умножение 4x4 матриц.

**Использование:**
- Deep learning (training, inference)
- DLSS (AI upscaling)

### 7.2 DLSS (Deep Learning Super Sampling)

**Идея:**
- Рендерить в низком разрешении (1080p)
- AI upscaling до 4K
- Performance boost + качество

---

## 💡 Key Takeaways

- **GPU эволюционировали** от простых 2D accelerators к массивно-параллельным процессорам
- **Архитектура GPU** оптимизирована для параллельных задач — тысячи простых ядер vs десятки сложных в CPU
- **GPGPU** расширила применение GPU за пределы графики — ML, научные вычисления
- **Специализированные блоки** (RT cores, Tensor cores) ускоряют конкретные задачи на порядки
- **Trade-off:** GPU быстры для параллельных задач, но медленны для последовательных

---

## 🚀 Next Steps

- [08_IO_Subsystems](../08_IO_Subsystems/) — Как GPU подключается к системе
- [15_LanguagesArchitectures](../15_LanguagesArchitectures/) — Языки для GPU программирования

---

## 📚 Additional Resources

- **CUDA Programming Guide** — NVIDIA
- **"Programming Massively Parallel Processors"** — Hwu, Kirk, Hajj
- **"Real-Time Rendering"** — Akenine-Möller

---
