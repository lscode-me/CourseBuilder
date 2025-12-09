# Медицинская Визуализация и Диагностика

---

## Введение

Медицинская визуализация — это использование различных технологий для создания изображений внутренних структур тела. В этом модуле мы рассмотрим основные типы изображений и стандарт DICOM.

---

## 1. Типы Медицинских Изображений

### 1.1 X-ray (Рентген)

**Принцип:** Рентгеновские лучи проходят через тело, поглощение зависит от плотности ткани.

**Применение:**
- Переломы костей
- Заболевания лёгких
- Стоматология

**Характеристики:**
- 2D изображение
- Низкая доза радиации
- Быстро и дёшево

### 1.2 CT (Computed Tomography)

**Принцип:** Множество X-ray снимков под разными углами, компьютерная реконструкция в 3D.

**Применение:**
- Травмы
- Опухоли
- Сосудистые заболевания

**Характеристики:**
- 3D изображение (серия срезов)
- Высокая доза радиации
- Детализированное изображение

### 1.3 MRI (Magnetic Resonance Imaging)

**Принцип:** Магнитное поле и радиоволны создают изображение мягких тканей.

**Применение:**
- Мозг и нервная система
- Суставы и мышцы
- Внутренние органы

**Характеристики:**
- Отличная детализация мягких тканей
- Нет радиации
- Долго (30-60 минут)
- Дорого

### 1.4 Ultrasound (УЗИ)

**Принцип:** Ультразвуковые волны отражаются от тканей.

**Применение:**
- Беременность
- Сердце (эхокардиография)
- Абдоминальные органы

**Характеристики:**
- Реальное время
- Безопасно (нет радиации)
- Portable
- Зависит от оператора

### 1.5 PET (Positron Emission Tomography)

**Принцип:** Радиоактивный индикатор показывает метаболическую активность.

**Применение:**
- Онкология (обнаружение опухолей)
- Неврология
- Кардиология

**Характеристики:**
- Функциональная информация
- Часто комбинируется с CT (PET/CT)

---

## 2. DICOM — Digital Imaging and Communications in Medicine

### 2.1 Что такое DICOM?

DICOM — стандарт для хранения и передачи медицинских изображений.

**DICOM файл содержит:**
- **Pixel Data** — само изображение
- **Metadata** — информация о пациенте, исследовании, оборудовании

### 2.2 Структура DICOM

```
DICOM File
├── File Meta Information (преамбула)
├── Data Set
│   ├── Patient Module
│   │   ├── Patient Name
│   │   ├── Patient ID
│   │   ├── Patient Birth Date
│   │   └── Patient Sex
│   ├── Study Module
│   │   ├── Study Date
│   │   ├── Study Time
│   │   └── Study Description
│   ├── Series Module
│   │   ├── Modality (CT, MRI, X-ray)
│   │   ├── Series Number
│   │   └── Series Description
│   ├── Image Module
│   │   ├── Image Number
│   │   ├── Rows
│   │   ├── Columns
│   │   └── Pixel Spacing
│   └── Pixel Data
│       └── Image (массив пикселей)
```

### 2.3 DICOM Tags

DICOM использует теги (group, element) для идентификации полей:

```
(0010,0010) → Patient Name
(0010,0020) → Patient ID
(0010,0030) → Patient Birth Date
(0008,0060) → Modality
(0020,000D) → Study Instance UID
(0020,000E) → Series Instance UID
(7FE0,0010) → Pixel Data
```

### 2.4 Чтение DICOM в Python

```python
import pydicom
import numpy as np
import matplotlib.pyplot as plt

# Чтение DICOM файла
ds = pydicom.dcmread("image.dcm")

# Метаданные
print(f"Patient: {ds.PatientName}")
print(f"Modality: {ds.Modality}")
print(f"Study Date: {ds.StudyDate}")

# Изображение
image = ds.pixel_array  # NumPy array

# Windowing (для CT)
if 'WindowCenter' in ds:
    center = ds.WindowCenter
    width = ds.WindowWidth
    
    # Применить windowing
    img_min = center - width / 2
    img_max = center + width / 2
    image = np.clip(image, img_min, img_max)

# Визуализация
plt.imshow(image, cmap='gray')
plt.title(f"{ds.Modality} - {ds.StudyDescription}")
plt.show()
```

### 2.5 Создание DICOM

```python
from pydicom.dataset import Dataset, FileDataset
import datetime

# Создать Dataset
file_meta = Dataset()
file_meta.MediaStorageSOPClassUID = '1.2.840.10008.5.1.4.1.1.2'  # CT Image
file_meta.MediaStorageSOPInstanceUID = generate_uid()
file_meta.TransferSyntaxUID = pydicom.uid.ExplicitVRLittleEndian

ds = FileDataset("output.dcm", {}, file_meta=file_meta, preamble=b"\0" * 128)

# Patient Information
ds.PatientName = "Doe^John"
ds.PatientID = "123456"
ds.PatientBirthDate = "19800101"
ds.PatientSex = "M"

# Study/Series Information
ds.StudyDate = datetime.date.today().strftime('%Y%m%d')
ds.Modality = "CT"
ds.SeriesNumber = 1
ds.InstanceNumber = 1

# Image Information
ds.Rows = 512
ds.Columns = 512
ds.SamplesPerPixel = 1
ds.PhotometricInterpretation = "MONOCHROME2"
ds.BitsAllocated = 16
ds.BitsStored = 16
ds.HighBit = 15
ds.PixelRepresentation = 0

# Pixel Data
image = np.random.randint(0, 65535, (512, 512), dtype=np.uint16)
ds.PixelData = image.tobytes()

# Сохранить
ds.save_as("output.dcm")
```

---

## 3. PACS — Picture Archiving and Communication System

### 3.1 Что такое PACS?

PACS — система для хранения, получения и распространения медицинских изображений.

**Компоненты:**
```
Modality (CT, MRI) → PACS Server → Viewer (Radiologist Workstation)
                          ↓
                    Archive Storage
```

### 3.2 DICOM Networking

**DICOM Services:**
- **C-STORE** — отправить изображение
- **C-FIND** — поиск изображений
- **C-MOVE** — запросить изображение
- **C-GET** — получить изображение

```python
from pynetdicom import AE, evt
from pynetdicom.sop_class import StudyRootQueryRetrieveInformationModelFind

# DICOM Query (C-FIND)
ae = AE()
ae.add_requested_context(StudyRootQueryRetrieveInformationModelFind)

# Создать dataset для запроса
ds = Dataset()
ds.QueryRetrieveLevel = 'STUDY'
ds.PatientName = 'Doe^John'
ds.StudyDate = '20230101'

# Выполнить запрос
assoc = ae.associate('pacs.hospital.org', 11112)
if assoc.is_established:
    responses = assoc.send_c_find(ds, StudyRootQueryRetrieveInformationModelFind)
    
    for (status, identifier) in responses:
        if status and identifier:
            print(f"Study: {identifier.StudyDescription}")
    
    assoc.release()
```

---

## 4. Обработка Медицинских Изображений

### 4.1 Windowing (для CT)

CT изображения имеют широкий динамический диапазон. Windowing позволяет выбрать диапазон для визуализации.

```python
def apply_windowing(image, center, width):
    """
    Window Center — середина окна (HU)
    Window Width — ширина окна (HU)
    """
    img_min = center - width / 2
    img_max = center + width / 2
    
    windowed = np.clip(image, img_min, img_max)
    windowed = (windowed - img_min) / (img_max - img_min) * 255
    
    return windowed.astype(np.uint8)

# Примеры window settings
# Lung: center=-600, width=1500
# Soft tissue: center=40, width=400
# Bone: center=400, width=1800
```

### 4.2 Сегментация

```python
from skimage import filters, morphology

def segment_lungs(ct_image):
    """Простая сегментация лёгких"""
    # Thresholding
    threshold = filters.threshold_otsu(ct_image)
    binary = ct_image < threshold
    
    # Morphological operations
    binary = morphology.remove_small_objects(binary, min_size=1000)
    binary = morphology.binary_closing(binary, morphology.disk(5))
    
    return binary
```

### 4.3 3D Reconstruction

```python
import numpy as np
from skimage import measure

def reconstruct_3d(dicom_files):
    """3D реконструкция из серии DICOM"""
    slices = [pydicom.dcmread(f) for f in dicom_files]
    slices.sort(key=lambda x: float(x.ImagePositionPatient[2]))
    
    # Создать 3D volume
    volume = np.stack([s.pixel_array for s in slices])
    
    # Создать mesh (например, для костей)
    verts, faces, _, _ = measure.marching_cubes(volume, level=200)
    
    return verts, faces
```

---

## 5. AI в Медицинской Визуализации

### 5.1 Применение

- **Detection** — обнаружение патологий (опухоли, переломы)
- **Segmentation** — выделение органов, опухолей
- **Classification** — классификация заболеваний
- **Registration** — совмещение изображений

### 5.2 Пример: Классификация X-ray

```python
import tensorflow as tf
from tensorflow import keras

# Загрузить предобученную модель
model = keras.applications.DenseNet121(weights='imagenet', include_top=False)

# Добавить classification head
x = keras.layers.GlobalAveragePooling2D()(model.output)
x = keras.layers.Dense(512, activation='relu')(x)
output = keras.layers.Dense(2, activation='softmax')(x)  # Normal vs Pneumonia

model = keras.Model(inputs=model.input, outputs=output)

# Training
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
# model.fit(train_data, train_labels, epochs=10)

# Prediction
prediction = model.predict(xray_image)
print(f"Pneumonia probability: {prediction[0][1]:.2%}")
```

---

## Резюме

- ✅ Типы медицинских изображений (X-ray, CT, MRI, Ultrasound, PET)
- ✅ DICOM стандарт и структура
- ✅ Чтение и создание DICOM в Python
- ✅ PACS системы и DICOM networking
- ✅ Обработка изображений (windowing, segmentation)
- ✅ AI в медицинской визуализации

---

## 🚀 Следующие Шаги

**Связанные модули:**
- [Medical Terminology](../01_Terminology/) — HL7, FHIR, стандарты обмена данными
- [EHR Systems](../02_EHR_Systems/) — интеграция изображений в EHR
- [Security & Privacy](../03_Security_Privacy/) — защита медицинских изображений

**Идеи для практики:**
1. **DICOM Viewer** — чтение DICOM, отображение изображения, метаданные, windowing controls
2. **Metadata Extractor** — извлечение Patient info, Study, Series из серии DICOM файлов
3. **DICOM Anonymizer** — де-идентификация DICOM: удаление Patient Name, ID, DOB
4. **3D Reconstruction** — создание 3D модели из CT серии с визуализацией
5. **Basic Segmentation** — thresholding, morphological operations, overlay на изображение

---

## 📚 Дополнительные Ресурсы

**DICOM:**
- [DICOM Standard](https://www.dicomstandard.org/) — официальный стандарт DICOM
- [pydicom Documentation](https://pydicom.github.io/) — Python библиотека для DICOM
- [DICOM Library](https://www.dicomlibrary.com/) — примеры DICOM файлов

**Viewers:**
- [OHIF Viewer](https://ohif.org/) — open source DICOM viewer (web)
- [3D Slicer](https://www.slicer.org/) — powerful 3D visualization
- [Weasis](https://nroduit.github.io/en/) — standalone DICOM viewer

**Datasets:**
- [The Cancer Imaging Archive](https://www.cancerimagingarchive.net/) — публичные медицинские изображения
- [NIH Chest X-ray Dataset](https://www.nih.gov/news-events/news-releases/nih-clinical-center-provides-one-largest-publicly-available-chest-x-ray-datasets-scientific-community) — большой датасет для AI

**AI/ML:**
- [Medical Segmentation Decathlon](http://medicaldecathlon.com/) — соревнования по сегментации

