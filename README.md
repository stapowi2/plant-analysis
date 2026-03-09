# Система сегментации и анализа проростков растений

Данный проект нужен для автоматического определения параметров растений (корней и листьев) по фотографиям. Система построена на базе нейросети YOLOv8

## Ссылки на ресурсы
* **Разметка данных в RoboFlow:** [https://app.roboflow.com/stapowis-workspace/plant_analysis/1](https://app.roboflow.com/stapowis-workspace/plant_analysis/1)
* **Репозиторий:** [https://github.com/stapowi2/plant-analysis.git](https://github.com/stapowi2/plant-analysis.git)

## Технологический стек
* **Модель:** YOLOv8 (Segmentation)
* **Backend:** FastAPI, Uvicorn
* **Бот:** pyTelegramBotAPI
* **Обработка изображений:** OpenCV, NumPy

## Инструкция по установке
1. Клонируйте репозиторий.
2. Установите необходимые зависимости:
   ```bash
   pip install ultralytics fastapi uvicorn pyTelegramBotAPI opencv-contrib-python requests python-multipart