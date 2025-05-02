# Smoke and Fire Detection 🚨🔥

## Introduction

In many real-world scenarios, **smoke is the earliest indicator of a fire**, but if the smoke fumes are minimal or dispersed, they might not be detected in time by conventional fire alarm systems. This delay in detection can lead to major safety hazards.

To overcome this, our system provides a **video-based smoke and fire detection mechanism** that can recognize visual indicators before conventional systems react. By leveraging deep learning and computer vision, this project helps in **early detection and prevention** of potential fire incidents.

## Features

- 🔥 Detects both **smoke** and **fire** in real-time from video streams
- 🎥 Supports YouTube video input (including Shorts) and local video uploads
- ✅ Bounding boxes drawn around detected areas for clear visualization
- 💡 Simple UI using **Streamlit** for easy interaction
- 🧠 Fine-tuned **YOLOv8s** model for accurate object detection

## Demo Output
https://github.com/sakshimuchhala1227/Smoke-and-fire-detection/blob/main/output/out_vehicle_fire.mp4


## Model and Dataset

This project uses a **YOLOv8 model fine-tuned on a custom smoke and fire dataset**. The dataset was collected and labeled using **Roboflow**.

To download and use the dataset directly, refer to the `dataset.py` file included in the repository:

```bash
python dataset.py
