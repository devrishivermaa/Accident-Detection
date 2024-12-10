import cv2
import os
from ultralytics import YOLO
from datetime import datetime
from flask import Flask, render_template_string, send_from_directory, url_for
import threading
import time

# Initialize the Flask app
app = Flask(_name_)

# Directory containing the accident images
image_dir = '/home/group8/Pictures/accident_images'

# Camera coordinates
latitude = 26.835668
longitude = 75.651536

# HTML template for displaying images with improved styling and auto-refresh
html_template = """
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Accident Alert</title>
    <style>
    body {
        font-family: 'Arial', sans-serif;
        background-color: #222222;
        color: #fff;
        text-align: center;
        margin: 0;
        padding: 0;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
    }
    h1 {
        font-size: 50px;
        color: #e74c3c;
        margin-bottom: 20px;
    }
    h2 {
        font-size: 30px;
        color: #f39c12;
    }
    h3 {
        font-size: 24px;
        color: #7f8c8d;
        margin-top: 10px;
    }
    .gallery {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
        gap: 20px;
        padding: 20px;
        max-width: 90%;
        margin: 0 auto;
    }
    .gallery div {
        position: relative;
        overflow: hidden;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        background-color: #333;
        padding: 10px;
        text-align: center;
    }
    .gallery img {
        width: 100%;
        height: auto;
        max-height: 200px;
        object-fit: cover;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .gallery div:hover img {
        transform: scale(1.1);
        box-shadow: 0 6px 16px rgba(0, 0, 0, 0.3);
    }
    .button {
        margin-top: 10px;
        padding: 8px 12px;
        background-color: #3498db;
        color: #fff;
        text-decoration: none;
        border-radius: 5px;
        font-size: 16px;
        display: inline-block;
    }
    .button:hover {
        background-color: #2980b9;
    }
    .footer {
        position: fixed;
        bottom: 10px;
        color: #7f8c8d;
        font-size: 14px;
    }
    </style>
    <meta http-equiv="refresh" content="5">  <!-- Auto-refresh every 5 seconds -->
</head>
<body>
    <h1>🚨 Accident Alert! 🚨</h1>
    <h2>Real-Time Accident Detection</h2>
    <h3>Server Room</h3>
    
    <div class="gallery">
        {% for image in images %}
            <div>
                <img src="{{ url_for('serve_image', filename=image) }}" alt="{{ image }}">
                <p>{{ image }}</p>
                <a href="https://www.google.com/maps/place/200+ft+Ajmer+Bus+Stop/@26.8887935,75.7370937,17z/data=!4m6!3m5!1s0x396db5f0cb6ed4f5:0x4512fa0fbd8a156c!8m2!3d26.8884228!4d75.7367772!16s%2Fg%2F11jznwx928?entry=ttu&g_ep=EgoyMDI0MTExMy4xIKXMDSoASAFQAw%3D%3D" target="_blank" class="button">Accident Location</a>
                
            </div>
        {% endfor %}
    </div>
    
    <div class="footer">
        <p>&copy; 2024 Rajasthan Police - All Rights Reserved</p>
    </div>
</body>
</html>
"""

# Route to display the images
@app.route('/')
def display_images():
    images = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]
    return render_template_string(html_template, images=sorted(images, reverse=True))

# Route to serve the images
@app.route('/images/<filename>')
def serve_image(filename):
    return send_from_directory(image_dir, filename)

# Route to display the map with the camera location
@app.route('/location')
def show_location():
    return render_template_string(map_template, latitude=latitude, longitude=longitude)

# Function to run the Flask app
def run_flask_server():
    app.run(host='0.0.0.0', port=5000)

# Function to capture accident image
def capture_accident_image():
    model = YOLO('generalized.pt')
    output_dir = image_dir

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        cap = cv2.VideoCapture(0)
        frame_count = 0

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to grab frame")
                break

            frame_count += 1

            if frame_count % 5 == 0:
                results = model.predict(frame)

                for result in results:
                    if any(box.cls == 1 for box in result.boxes):  # Customize for accident class
                        print("Accident detected!")
                        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                        image_filename = f'{output_dir}/accident_{timestamp}.jpg'

                        cv2.imwrite(image_filename, frame)
                        print(f"Image saved: {image_filename}")
                        
                        # Optionally, wait a bit before checking for the next accident
                        time.sleep(2)

    except KeyboardInterrupt:
        print("Program interrupted by user")

# Main function to run both tasks
def main():
    # Start the Flask server in a separate thread
    flask_thread = threading.Thread(target=run_flask_server)
    flask_thread.daemon = True  # Allows the server to stop when the program exits
    flask_thread.start()

    # Start capturing accident images continuously
    capture_accident_image()

if _name_ == '_main_':
    main()