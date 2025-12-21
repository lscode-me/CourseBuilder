# От текстовых терминалов к массивно-параллельным вычислениям

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

**Пример: BitBlt операция**

```c

// Копирование прямоугольной области экрана
BitBlt(
    hDestDC,      // Destination device context
    x, y,         // Destination coordinates
    width, height,// Size
    hSrcDC,       // Source device context
    srcX, srcY,   // Source coordinates
    SRCCOPY       // Operation: copy
);
```

**Преимущество:** Hardware-ускорение вместо медленного программного копирования пикселей.

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

// CPU: последовательное выполнение
for (int i = 0; i < 1000; i++) {
    result[i] = a[i] + b[i];
}
// Время: ~1000 циклов (если 1 операция = 1 цикл)
```

**CPU с SIMD (SSE/AVX):**
```c

// CPU с AVX-512: 16 элементов за раз
#include <immintrin.h>
for (int i = 0; i < 1000; i += 16) {
    __m512 va = _mm512_load_ps(&a[i]);
    __m512 vb = _mm512_load_ps(&b[i]);
    __m512 vresult = _mm512_add_ps(va, vb);
    _mm512_store_ps(&result[i], vresult);
}
// Время: ~63 цикла (1000/16)
```

GPU выполняет одну инструкцию для тысяч элементов одновременно:
```c

// GPU: параллельное выполнение
// Все 1000 элементов обрабатываются одновременно
result[0..1000] = a[0..1000] + b[0..1000];  // параллельно!
// Время: ~1 цикл (если достаточно ядер)
```

**Масштабирование:**

- CPU: 4-64 ядра → 4-64 операции параллельно
- GPU: 2000-10000 ядер → тысячи операций параллельно

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

**Пример: Warp execution**

```c

// 32 потока в warp выполняют одну инструкцию
__global__ void vectorAdd(float *a, float *b, float *c, int n) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < n) {
        c[i] = a[i] + b[i];  // Все 32 потока выполняют одновременно
    }
}
```

**Важно:** Если потоки в warp идут по разным путям (divergence), производительность падает:
```c

// Плохо: divergence в warp
if (threadIdx.x % 2 == 0) {
    result = a + b;  // 16 потоков
} else {
    result = a - b;  // 16 потоков
}
// Обе ветки выполняются последовательно → 2x медленнее
```

### 2.4 Memory Hierarchy в GPU

**Уровни памяти (от быстрого к медленному):**

```

Registers (per thread)     → ~1 cycle, ~256 KB per SM
Shared Memory (per block)   → ~5 cycles, ~100 KB per SM
L1/L2 Cache                 → ~50 cycles, несколько MB
Global Memory (VRAM)        → ~400 cycles, GB
```

**Пример: Использование shared memory**

```c

__global__ void matrixMultiply(float *A, float *B, float *C, int N) {
    __shared__ float tileA[16][16];  // Shared memory
    __shared__ float tileB[16][16];
    
    // Загрузить tile в shared memory (быстро)
    tileA[threadIdx.y][threadIdx.x] = A[...];
    tileB[threadIdx.y][threadIdx.x] = B[...];
    __syncthreads();  // Ждать загрузки всех
    
    // Вычисления с данными из shared memory
    float sum = 0;
    for (int k = 0; k < 16; k++) {
        sum += tileA[threadIdx.y][k] * tileB[k][threadIdx.x];
    }
    C[...] = sum;
}
```

**Оптимизация:** Использование shared memory может ускорить код в 10-100 раз по сравнению с прямым доступом к global memory.

---

## 3. Графический pipeline

### 3.1 Rendering Pipeline

```

3D Model → Vertex Processing → Rasterization → Fragment Processing → Display
```

**Детальный pipeline:**

```

1. Input Assembler      → Собирает вершины в примитивы (треугольники)
2. Vertex Shader       → Трансформация координат, освещение
3. Hull Shader         → Tessellation (разбиение на подтреугольники)
4. Domain Shader       → Обработка tessellated вершин
5. Geometry Shader     → Генерация новых примитивов
6. Rasterization       → Конвертация в пиксели
7. Fragment Shader     → Цвет каждого пикселя
8. Output Merger       → Blending, depth test, stencil test
```

**Vertex Shader (GLSL пример):**
```glsl

// Vertex shader
#version 330 core
layout (location = 0) in vec3 aPos;      // Позиция вершины
layout (location = 1) in vec2 aTexCoord; // Текстурные координаты

uniform mat4 model;      // Матрица модели
uniform mat4 view;       // Матрица вида
uniform mat4 projection; // Матрица проекции

out vec2 TexCoord;

void main() {
    // Трансформация в clip space
    gl_Position = projection * view * model * vec4(aPos, 1.0);
    TexCoord = aTexCoord;
}
```

**Fragment Shader (GLSL пример):**
```glsl

// Fragment shader
#version 330 core
in vec2 TexCoord;
out vec4 FragColor;

uniform sampler2D ourTexture;

void main() {
    // Текстурирование
    FragColor = texture(ourTexture, TexCoord);
}
```

**Rasterization:**

- Конвертация треугольников в пиксели
- Интерполяция атрибутов (цвет, текстура) между вершинами
- Z-buffer для определения видимости

**Fragment/Pixel Shader:**

- Текстурирование
- Lighting calculations (Phong, PBR)
- Effects (bloom, shadows, reflections)

### 3.2 Graphics APIs

**OpenGL (1992):** Cross-platform, open standard

**Пример: OpenGL инициализация**

```c

// Создание окна и контекста
GLFWwindow* window = glfwCreateWindow(800, 600, "OpenGL", NULL, NULL);
glfwMakeContextCurrent(window);

// Загрузка функций OpenGL
gladLoadGL();

// Создание шейдерной программы
unsigned int shaderProgram = glCreateProgram();
// ... компиляция vertex и fragment shaders
glLinkProgram(shaderProgram);
```

**DirectX (1995):** Microsoft, Windows/Xbox

**DirectX 12 особенности:**

- Low-level API (больше контроля)
- Multi-threaded command recording
- Explicit resource management

**Vulkan (2016):** Современная low-level API, преемник OpenGL

**Пример: Vulkan setup (упрощённо)**

```c

// Vulkan требует больше boilerplate, но даёт больше контроля
VkInstance instance;
VkInstanceCreateInfo createInfo = {};
vkCreateInstance(&createInfo, NULL, &instance);

VkDevice device;
VkDeviceCreateInfo deviceInfo = {};
vkCreateDevice(physicalDevice, &deviceInfo, NULL, &device);

// Command buffer для записи команд
VkCommandBuffer cmdBuffer;
vkAllocateCommandBuffers(device, &allocInfo, &cmdBuffer);
```

**Преимущества Vulkan:**

- Меньше overhead (нет driver overhead)
- Multi-threading friendly
- Лучшая производительность (10-30% быстрее OpenGL)

**Metal (2014):** Apple

**Пример: Metal shader (MSL)**

```metal

// Metal Shading Language
vertex VertexOut vertex_main(VertexIn in [[stage_in]]) {
    VertexOut out;
    out.position = projectionMatrix * modelViewMatrix * in.position;
    out.texCoord = in.texCoord;
    return out;
}

fragment float4 fragment_main(VertexOut in [[stage_in]],
                            texture2d<float> texture [[texture(0)]]) {
    constexpr sampler textureSampler;
    return texture.sample(textureSampler, in.texCoord);
}
```

**Сравнение API:**

| API | Платформа | Уровень | Производительность |
|-----|-----------|---------|-------------------|
| OpenGL | Cross-platform | High-level | Средняя |
| DirectX 11 | Windows/Xbox | High-level | Средняя |
| DirectX 12 | Windows/Xbox | Low-level | Высокая |
| Vulkan | Cross-platform | Low-level | Высокая |
| Metal | Apple | Low-level | Высокая |

---

## 4. GPGPU - General Purpose GPU Computing

### 4.1 Идея

**Проблема:** GPU мощны, но используются только для графики.

**Решение:** Использовать GPU для общих вычислений.

### 4.2 CUDA (2007)

**NVIDIA CUDA** — платформа для программирования GPU:

**Полный пример: Vector Addition**

```c
#include <cuda_runtime.h>
#include <stdio.h>

// Kernel функция (выполняется на GPU)
__global__ void vectorAdd(int *a, int *b, int *c, int n) {
    // Вычисляем индекс для этого потока
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    
    if (i < n) {
        c[i] = a[i] + b[i];
    }
}

int main() {
    int n = 10000;
    size_t size = n * sizeof(int);
    
    // Host (CPU) память
    int *h_a = (int*)malloc(size);
    int *h_b = (int*)malloc(size);
    int *h_c = (int*)malloc(size);
    
    // Инициализация
    for (int i = 0; i < n; i++) {
        h_a[i] = i;
        h_b[i] = i * 2;
    }
    
    // Device (GPU) память
    int *d_a, *d_b, *d_c;
    cudaMalloc(&d_a, size);
    cudaMalloc(&d_b, size);
    cudaMalloc(&d_c, size);
    
    // Копирование CPU → GPU
    cudaMemcpy(d_a, h_a, size, cudaMemcpyHostToDevice);
    cudaMemcpy(d_b, h_b, size, cudaMemcpyHostToDevice);
    
    // Запуск kernel
    int threadsPerBlock = 256;
    int blocksPerGrid = (n + threadsPerBlock - 1) / threadsPerBlock;
    vectorAdd<<<blocksPerGrid, threadsPerBlock>>>(d_a, d_b, d_c, n);
    
    // Копирование GPU → CPU
    cudaMemcpy(h_c, d_c, size, cudaMemcpyDeviceToHost);
    
    // Проверка результата
    printf("c[0] = %d, c[9999] = %d\n", h_c[0], h_c[9999]);
    
    // Освобождение памяти
    cudaFree(d_a);
    cudaFree(d_b);
    cudaFree(d_c);
    free(h_a);
    free(h_b);
    free(h_c);
    
    return 0;
}
```

**Концепции:**

- **Kernel** — функция, выполняемая на GPU (помечена `__global__`)

- **Thread** — один экземпляр kernel (имеет `threadIdx`)

- **Block** — группа threads (до 1024, имеет `blockIdx`)

- **Grid** — набор blocks (весь запуск kernel)

**Иерархия потоков:**
```

Grid (весь kernel launch)
  └── Block 0
      ├── Thread 0
      ├── Thread 1
      └── ...
  └── Block 1
      └── ...
```

**Вычисление индекса:**
```c

int globalIndex = blockIdx.x * blockDim.x + threadIdx.x;
// blockIdx.x    - номер блока в grid
// blockDim.x    - размер блока (количество threads)
// threadIdx.x   - номер thread в блоке
```

### 4.3 OpenCL (альтернатива CUDA)

**OpenCL** — открытый стандарт для GPGPU (работает на NVIDIA, AMD, Intel):

```c

// OpenCL kernel (похож на CUDA)
__kernel void vectorAdd(__global int *a, 
                        __global int *b, 
                        __global int *c) {
    int i = get_global_id(0);
    c[i] = a[i] + b[i];
}
```

**Преимущества OpenCL:**

- Работает на любых GPU/CPU
- Vendor-agnostic

**Недостатки:**

- Меньше оптимизаций для конкретных GPU
- Сложнее в использовании

### 4.4 Применения GPGPU

**Machine Learning:**

**Пример: Matrix Multiplication для нейросетей**

```c

// Упрощённый пример умножения матриц на GPU
__global__ void matrixMultiply(float *A, float *B, float *C, 
                                int M, int N, int K) {
    int row = blockIdx.y * blockDim.y + threadIdx.y;
    int col = blockIdx.x * blockDim.x + threadIdx.x;
    
    if (row < M && col < N) {
        float sum = 0.0f;
        for (int k = 0; k < K; k++) {
            sum += A[row * K + k] * B[k * N + col];
        }
        C[row * N + col] = sum;
    }
}
```

**Применения:**

- Matrix multiplication (основа нейросетей)
- Convolutions (CNNs)
- Training neural networks (backpropagation)
- Inference (предсказания)

**Scientific Computing:**

**Пример: Molecular Dynamics**

```c

// Вычисление сил между частицами
__global__ void computeForces(float3 *positions, 
                               float3 *forces, 
                               int n) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i >= n) return;
    
    float3 force = make_float3(0, 0, 0);
    for (int j = 0; j < n; j++) {
        if (i != j) {
            float3 r = positions[j] - positions[i];
            float dist = length(r);
            // Lennard-Jones potential
            float f = 4 * epsilon * (pow(sigma/dist, 12) - pow(sigma/dist, 6));
            force += f * normalize(r);
        }
    }
    forces[i] = force;
}
```

**Применения:**

- Molecular dynamics (симуляция атомов)
- Weather simulation (прогноз погоды)
- Computational fluid dynamics (аэродинамика)
- Quantum chemistry

**Cryptocurrency:**

- Bitcoin mining (SHA-256 hashing)
- Ethereum mining (до proof-of-stake, Ethash)
- Cryptocurrency wallets (подпись транзакций)

**Video Processing:**

**Пример: Video Encoding**

```c

// Упрощённый пример обработки кадра
__global__ void processFrame(uchar4 *input, uchar4 *output, 
                             int width, int height) {
    int x = blockIdx.x * blockDim.x + threadIdx.x;
    int y = blockIdx.y * blockDim.y + threadIdx.y;
    
    if (x < width && y < height) {
        int idx = y * width + x;
        uchar4 pixel = input[idx];
        
        // Применение фильтра (например, grayscale)
        unsigned char gray = 0.299f * pixel.x + 

                           0.587f * pixel.y + 
                           0.114f * pixel.z;
        output[idx] = make_uchar4(gray, gray, gray, pixel.w);
    }
}
```

**Применения:**

- Encoding/decoding (H.264, H.265, AV1)
- Effects, filters (blur, sharpen, color correction)
- Real-time video processing

**Example Performance:**

**Benchmark: Matrix Multiplication (1024x1024)**
- CPU (Intel i9): ~100 GFLOPS, ~10 ms
- GPU (NVIDIA RTX 4090): ~83,000 GFLOPS, ~0.1 ms
- **Ускорение: ~100x**

**Benchmark: Neural Network Training (ResNet-50)**
- CPU: ~10 hours
- GPU: ~10 minutes
- **Ускорение: ~60x**

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

**Пример: Unified Memory в CUDA**

```c

// Unified Memory автоматически управляется системой
__managed__ int *data;  // Доступна и CPU, и GPU

// Выделение unified memory
cudaMallocManaged(&data, n * sizeof(int));

// CPU может писать
for (int i = 0; i < n; i++) {
    data[i] = i;
}

// GPU может читать (без явного копирования!)
__global__ void process(int *data, int n) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < n) {
        data[i] *= 2;  // GPU изменяет данные
    }
}

// CPU может читать результат (без явного копирования!)
printf("%d\n", data[0]);
```

**Преимущества:**

- Нет копирования CPU ↔ GPU (автоматическая миграция страниц)
- Упрощение программирования (один указатель)
- Меньше ошибок (нет забытых копирований)

**Недостатки:**

- Меньше bandwidth для GPU (shared bus)
- Конкуренция за память
- Latency при миграции страниц

**Сравнение подходов:**

| Подход | Bandwidth | Сложность | Производительность |
|--------|-----------|-----------|-------------------|
| Separate Memory | Высокая (1 TB/s) | Высокая | Максимальная |
| Unified Memory | Средняя (50 GB/s) | Низкая | Хорошая |

### 5.3 Memory Management Best Practices

**1. Minimize Host-Device Transfers**

```c

// Плохо: много маленьких копирований
for (int i = 0; i < 1000; i++) {
    cudaMemcpy(d_data, h_data, size, cudaMemcpyHostToDevice);
    kernel<<<...>>>(d_data);
}

// Хорошо: одно большое копирование
cudaMemcpy(d_data, h_data, totalSize, cudaMemcpyHostToDevice);
for (int i = 0; i < 1000; i++) {
    kernel<<<...>>>(d_data);
}
```

**2. Использование Pinned Memory**

```c

// Pinned memory быстрее для Host-Device transfers
float *h_pinned;
cudaMallocHost(&h_pinned, size);  // Pinned (page-locked)
// ... копирование быстрее в 2-3 раза
cudaFreeHost(h_pinned);
```

**3. Memory Coalescing**

```c

// Хорошо: coalesced access (последовательные адреса)
__global__ void good(float *data) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    data[i] = ...;  // Все threads читают последовательно
}

// Плохо: uncoalesced access (случайные адреса)
__global__ void bad(float *data) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    data[random[i]] = ...;  // Случайные адреса → медленно
}
```

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

**Как работает RT Core:**
```

Ray → BVH Traversal → Triangle Intersection → Result
      (RT Core)        (RT Core)              (Shader)
```

**Пример: Ray Tracing в Vulkan/GLSL**

```glsl

// Ray tracing shader
#version 460
#extension GL_EXT_ray_tracing : require

layout(binding = 0) uniform accelerationStructureEXT topLevelAS;
layout(binding = 1, rgba8) uniform image2D image;

void main() {
    vec3 origin = ...;
    vec3 direction = ...;
    
    // Hardware-accelerated ray tracing
    rayQueryEXT rayQuery;
    rayQueryInitializeEXT(rayQuery, topLevelAS, 
                          gl_RayFlagsNoneEXT, 
                          0xFF, origin, 0.01, direction, 1000.0);
    
    while(rayQueryProceedEXT(rayQuery)) {
        // RT Core обрабатывает intersection
    }
    
    if (rayQueryGetIntersectionTypeEXT(rayQuery, true) != 
        gl_RayQueryCommittedIntersectionNoneEXT) {
        // Hit: вычисляем цвет
        vec3 color = ...;
        imageStore(image, ivec2(gl_LaunchIDEXT.xy), vec4(color, 1.0));
    }
}
```

**Производительность:**

- Software ray tracing: ~1 FPS (на CPU)
- Hardware RT cores: 30-60 FPS (на RTX GPU)
- **Ускорение: 30-60x**

**Применения:**

- Realistic lighting в играх
- Reflections, refractions
- Global illumination
- Path tracing для кино (offline rendering)

### 6.3 Hybrid Rendering

**Современный подход:** Комбинация rasterization + ray tracing

```

Base Pass (Rasterization)     → Быстро, 60+ FPS
  └── Ray Traced Reflections   → Медленно, но реалистично
  └── Ray Traced Shadows       → Точные тени
  └── Ray Traced GI            → Глобальное освещение
```

**Пример: Hybrid в игре**
- Rasterization: геометрия, текстуры, базовое освещение
- Ray Tracing: только отражения и тени (частично)
- Результат: 60 FPS с реалистичными эффектами

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

**Как работает DLSS:**
```

1. Render в низком разрешении (1080p) → быстро
2. Motion vectors (куда движутся объекты)
3. Tensor Core обрабатывает через нейросеть
4. Upscale до 4K с восстановлением деталей
5. Результат: качество близко к нативному 4K, но быстрее
```

**Производительность DLSS:**

- Native 4K: 30 FPS
- DLSS Quality (4K from 1440p): 60 FPS, качество ~95%
- DLSS Performance (4K from 1080p): 90 FPS, качество ~85%

**Другие AI upscaling технологии:**

- **AMD FSR** (FidelityFX Super Resolution): Software-based, работает на любых GPU

- **Intel XeSS**: AI upscaling для Intel Arc

- **NVIDIA DLSS**: Hardware-accelerated (требует Tensor Cores)

### 7.3 AI Inference на GPU

**Пример: Real-time Object Detection**

```python
# Использование GPU для AI inference

import tensorrt as trt
import pycuda.driver as cuda

# Загрузка оптимизированной модели

engine = load_engine("model.trt")

# Inference на GPU

context = engine.create_execution_context()
# ... обработка кадра за ~10ms (vs 100ms на CPU)

```

**Применения:**

- Real-time object detection (автономные автомобили)
- Speech recognition
- Image generation (Stable Diffusion)
- Language models (inference)

---

## 8. Оптимизация GPU кода

### 8.1 Профилирование

**Инструменты:**

- **NVIDIA Nsight Compute**: Детальный анализ kernel

- **NVIDIA Nsight Systems**: Timeline профилирование

- **AMD Radeon GPU Profiler**: Для AMD GPU

**Метрики производительности:**
```

Occupancy          → % использования SM (цель: >50%)
Memory Throughput  → Bandwidth использования (цель: >80%)
Instruction Throughput → Сколько инструкций выполняется
```

### 8.2 Common Optimizations

**1. Maximize Occupancy**

```c

// Плохо: мало threads per block
kernel<<<1000, 32>>>();  // 32 threads/block

// Хорошо: больше threads per block
kernel<<<125, 256>>>();  // 256 threads/block → лучше occupancy
```

**2. Avoid Divergence**

```c

// Плохо: divergence в warp
if (threadIdx.x < 16) {
    // 16 threads идут сюда
} else {
    // 16 threads идут сюда
}  // Обе ветки выполняются последовательно

// Хорошо: все threads идут одним путём
int value = array[threadIdx.x];  // Нет divergence
```

**3. Coalesced Memory Access**

```c

// Хорошо: последовательный доступ
int i = blockIdx.x * blockDim.x + threadIdx.x;
data[i] = ...;  // Coalesced

// Плохо: случайный доступ
int i = blockIdx.x * blockDim.x + threadIdx.x;
data[random[i]] = ...;  // Uncoalesced → медленно
```

**4. Использование Shared Memory**

```c

// Кэширование данных в shared memory
__shared__ float cache[256];
cache[threadIdx.x] = global_data[blockIdx.x * 256 + threadIdx.x];
__syncthreads();
// Использование cache вместо global_data → быстрее
```

### 8.3 Performance Tips

**DO:**

- ✅ Использовать shared memory для часто используемых данных
- ✅ Максимизировать occupancy (threads per block)
- ✅ Обеспечить coalesced memory access
- ✅ Минимизировать Host-Device transfers

**DON'T:**

- ❌ Слишком маленькие или большие block sizes
- ❌ Divergence в warps
- ❌ Частые синхронизации (`__syncthreads()`)
- ❌ Копирование данных туда-сюда без необходимости

---

## 💡 Key Takeaways

- **GPU эволюционировали** от простых 2D accelerators к массивно-параллельным процессорам с тысячами ядер

- **Архитектура GPU** оптимизирована для параллельных задач — тысячи простых ядер vs десятки сложных в CPU, trade-off: быстры для параллелизма, медленны для последовательных задач

- **GPGPU** расширила применение GPU за пределы графики — ML, научные вычисления, криптовалюты, обработка видео с ускорением в 10-100x

- **Специализированные блоки** (RT cores для ray tracing, Tensor cores для AI) ускоряют конкретные задачи на порядки (30-100x)

- **Memory hierarchy** критична для производительности — правильное использование shared memory, coalesced access и минимизация transfers могут ускорить код в 10-100 раз

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


