# final script 
import cv2
import os
from ultralytics import YOLO

# Load YOLO model
model = YOLO(r"F:\fire_smoke_detection\runs\detect\fire_smoke_yolov8s_12\weights\best.pt")

# Input can be a single video or a folder of videos
input_path = r"F:\fire_smoke_detection\input\ethanol_truck.mp4" # Change this to video or folder path
output_folder = r"F:\fire_smoke_detection\output"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Supported video extensions
video_extensions = ['.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv', '.webm']

# Determine whether input_path is a file or a folder
video_files = []

if os.path.isdir(input_path):
    for filename in os.listdir(input_path):
        ext = os.path.splitext(filename)[1].lower()
        if ext in video_extensions:
            video_files.append(os.path.join(input_path, filename))
elif os.path.isfile(input_path):
    ext = os.path.splitext(input_path)[1].lower()
    if ext in video_extensions:
        video_files.append(input_path)
    else:
        print(" Unsupported file type.")
        exit()
else:
    print("Invalid input path.")
    exit()

# Process all video files
for video_file in video_files:
    filename = os.path.basename(video_file)
    print(f" Processing: {filename}")
    output_path = os.path.join(output_folder, f"out_{filename}")

    cap = cv2.VideoCapture(video_file)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps == 0:
        fps = 25  # Fallback in case FPS is zero

    ext = os.path.splitext(video_file)[1].lower()

    # Choose correct codec based on extension
    if ext == '.webm':
        fourcc = cv2.VideoWriter_fourcc(*'VP80')  # VP8 for .webm
    elif ext == '.avi':
        fourcc = cv2.VideoWriter_fourcc(*'XVID')  # MPEG-4 for .avi
    elif ext == '.mov':
        fourcc = cv2.VideoWriter_fourcc(*'avc1')  # H.264 for .mov
    elif ext == '.mkv':
        fourcc = cv2.VideoWriter_fourcc(*'X264')  # H.264 for .mkv
    elif ext == '.flv':
        fourcc = cv2.VideoWriter_fourcc(*'FLV1')  # Flash Video
    elif ext == '.wmv':
        fourcc = cv2.VideoWriter_fourcc(*'WMV1')  # Windows Media Video
    else:
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Default for .mp4 and unknowns

    out_writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))


    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Run YOLO detection
        results = model(frame, imgsz=416,task="detect")[0]
        annotated_frame = results.plot()

        # Write annotated frame
        out_writer.write(annotated_frame)

        # Show preview (press 'q' to quit preview)
        cv2.imshow("Detection", annotated_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out_writer.release()
    print(f"Saved: {output_path}")

cv2.destroyAllWindows()
print("All videos processed successfully.")
