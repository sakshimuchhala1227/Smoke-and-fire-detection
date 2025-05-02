<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
</head>
<body>

<h1>Smoke and Fire Detection</h1>

<h2>Introduction</h2>
<p>In many real-world scenarios, smoke is the earliest indicator of a fire, but if the smoke fumes are minimal or dispersed, they might not be detected in time by conventional fire alarm systems. This delay in detection can lead to major safety hazards.</p>
<p>To overcome this, our system provides a video-based smoke and fire detection mechanism that can recognize visual indicators before conventional systems react. By leveraging deep learning and computer vision, this project helps in early detection and prevention of potential fire incidents.</p>

<h2>Features</h2>
<ul>
    <li>🔥 Detects both smoke and fire in real-time from video streams</li>
    <li>🎥 Supports YouTube video input (including Shorts) and local video uploads</li>
    <li>✅ Bounding boxes drawn around detected areas for clear visualization</li>
    <li>💡 Simple UI using Streamlit for easy interaction</li>
    <li>🧠 Fine-tuned YOLOv8s model for accurate object detection</li>
</ul>

<h2>Demo Output</h2>
https://github.com/user-attachments/assets/8f26b648-312e-4525-a49d-db33a9cf475b

<h2>Model and Dataset</h2>
<p>This project uses a YOLOv8 model fine-tuned on a custom smoke and fire dataset. The dataset was collected and labeled using Roboflow.</p>
<p>To download and use the dataset directly, refer to the dataset.py file included in the repository:</p>
<pre><code>python dataset.py</code></pre>

<h2>Installation & Setup</h2>
<h3>1. Clone the Repository</h3>
<pre><code>git clone https://github.com/sakshimuchhala1227/Smoke-and-fire-detection.git
cd Smoke-and-fire-detection</code></pre>

<h3>2. Create a Virtual Environment</h3>
<pre><code>python -m venv myenv
source myenv/bin/activate  # On Windows use 'myenv\\Scripts\\activate'</code></pre>

<h3>3. Install Dependencies</h3>
<pre><code>pip install -r requirements.txt</code></pre>

<h3>4. Run the Streamlit App</h3>
<p>To run the Streamlit app:</p>
<pre><code>streamlit run app.py</code></pre>
<p>After running this, open your browser, and you will be able to interact with the UI.</p>

<h3>5. Save Outputs (Optional)</h3>
<p>If you want to save the output video with detections, you can run:</p>
<pre><code>python video.py</code></pre>
<p>This will process the video and save the output video with detections in the <code>output/</code> folder.</p>

<h2>Project Structure</h2>
<pre><code>├── app.py               # Main Streamlit app
├── dataset.py           # Code to download dataset
├── train.py             # Code to train the YOLOv8 model
├── video.py             # Code to process video and save output
├── requirements.txt     # Python dependencies
├── output/              # Folder containing output videos
└── run/                 # Folder containing best.pt (trained model)
</code></pre>

</body>
</html>
