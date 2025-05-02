import streamlit as st
import cv2
import os
import tempfile
import subprocess
import uuid
from ultralytics import YOLO

# Load YOLO model
model = YOLO(r"F:\fire_smoke_detection\runs\detect\fire_smoke_yolov8s_12\weights\best.pt")

# Streamlit Interface
st.title("Fire and Smoke Detection in Videos")
st.write("Upload a video file or provide a YouTube URL to detect fire and smoke.")

# Function to download YouTube video using yt-dlp
def download_youtube_video(url):
    try:
        temp_dir = tempfile.gettempdir()
        unique_filename = f"{uuid.uuid4()}.mp4"  # Always download as .mp4 for compatibility
        output_path = os.path.join(temp_dir, unique_filename)

        # yt-dlp command to download video in .mp4 format
        command = [
            "yt-dlp",
            "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
            "-o", output_path,
            url
        ]

        # Running the yt-dlp command
        subprocess.run(command, check=True)
        return output_path
    except subprocess.CalledProcessError as e:
        st.error(f"yt-dlp failed to download the video: {e}")
        return None

video_path = None  

# Upload video
input_video = st.file_uploader("Upload a video", type=["mp4", "avi", "mov", "mkv", "webm", "wmv"])
youtube_url = st.text_input("Or enter a YouTube URL:")

# Process and display video
if input_video is not None:
    stframe = st.empty()
    # Save uploaded video to a temporary file
    temp_file_path = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    with open(temp_file_path.name, "wb") as f:
        f.write(input_video.read())

    video_path = temp_file_path.name
    st.write(f"Processing video: {video_path}")

elif youtube_url:
    video_path = download_youtube_video(youtube_url)
    if video_path:
        st.write(f"Downloaded video from YouTube: {video_path}")
    else:
        st.error("Failed to download video.")

else:
    st.warning("Please upload a video or provide a YouTube URL.")

# Function to process video and display with bounding boxes
def process_and_display(video_path):
    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS) or 25
    stframe = st.empty()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Run YOLO detection
        results = model(frame)[0]
        annotated = frame.copy()

        if results.boxes is not None and len(results.boxes) > 0:
            for box in results.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
                conf = float(box.conf[0])
                cls_id = int(box.cls[0])
                label = f"{model.names[cls_id]} {conf:.2f}"

                # Assign color: red for fire, grey for smoke
                if model.names[cls_id].lower() == "fire":
                    color = (0, 0, 255)   # Red in BGR
                elif model.names[cls_id].lower() == "smoke":
                    color = (255, 0, 0)  # Blue in BGR  # Grey in BGR
                else:
                    color = (0, 255, 0)   # Default: Green

                cv2.rectangle(annotated, (x1, y1), (x2, y2), color, 2)
                cv2.putText(annotated, label, (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        annotated_frame = cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)
        stframe.image(annotated_frame, channels="RGB", use_container_width=True)

    cap.release()



# Process and display the video if a valid path is available
if video_path:
    process_and_display(video_path)
