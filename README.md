# Smoke and Fire Detection

## Introduction

In many real-world scenarios, smoke is the earliest indicator of a fire, but if the smoke fumes are minimal or dispersed, they might not be detected in time by conventional fire alarm systems. This delay in detection can lead to major safety hazards.

To overcome this, our system provides a video-based smoke and fire detection mechanism that can recognize visual indicators before conventional systems react. By leveraging deep learning and computer vision, this project helps in early detection and prevention of potential fire incidents.

## Features

* 🔥 Detects both smoke and fire in real-time from video streams
* 🎥 Supports YouTube video input (including Shorts) and local video uploads
* ✅ Bounding boxes drawn around detected areas for clear visualization
* 💡 Simple UI using Streamlit for easy interaction
* 🧠 Fine-tuned YOLOv8s model for accurate object detection

## Demo Output
https://github.com/user-attachments/assets/4e3e94ca-bc82-4efb-a775-9f62fc8b8eaa

## Model and Dataset

This project uses a YOLOv8 model fine-tuned on a custom smoke and fire dataset. The dataset was collected and labeled using Roboflow.

To download and use the dataset directly, refer to the `dataset.py` file included in the repository:

```bash
python dataset.py
```

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/sakshimuchhala1227/Smoke-and-fire-detection.git
cd Smoke-and-fire-detection
```

### 2. Create a Virtual Environment

```bash
python -m venv myenv
source myenv/bin/activate  # On Windows use 'myenv\Scripts\activate'
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. How to Run

Install the required packages (if not already done):

```bash
pip install streamlit opencv-python ultralytics pytube yt-dlp
```

Save the script to a Python file, say `app.py`.

Run the Streamlit app:

```bash
streamlit run app.py
```

After running this, open your browser, and you will be able to interact with the UI.

### 5. Save Outputs (Optional)

If you want to save the output video with detections, you can run:

```bash
python video.py
```

This will process the video and save the output video with detections in the `output/` folder.

## Project Structure

```bash
├── app.py               # Main Streamlit app
├── dataset.py           # Code to download dataset
├── train.py             # Code to train the YOLOv8 model
├── video.py             # Code to process video and save output
├── requirements.txt     # Python dependencies
├── output/              # Folder containing output videos
└── run/                 # Folder containing best.pt (trained model)
```

