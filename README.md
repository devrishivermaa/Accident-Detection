# Real-Time Accident Detection Using IoT with Jetson Nano and YOLOv8n

This repository contains the implementation of a **real-time accident detection system** using the YOLOv8n model deployed on a Jetson Nano. The project integrates computer vision, IoT, and Flask to detect accidents from live video feeds and send alerts with relevant data.

---

## Project Structure

```
├── dataset/                         # Contains the annotated dataset for training
├── Model_codes/
│   ├── data.yaml                    # Dataset configuration file for YOLOv8
│   ├── Jetsonnano.py                # Script for deployment on Jetson Nano
│   ├── model_infer.ipynb            # Inference notebook
│   └── Model_train.ipynb            # YOLOv8n training notebook
├── Models/
│   ├── generalized.pt               # Trained model for generalized use cases
│   └── yolov8n.pt                   # Fine-tuned YOLOv8n model
├── Plots/                           # Contains training and validation plots
├── results_imgs/                    # Images showcasing detection results
├── Test_videos/
│   ├── acc_ved.mp4                  # Video demonstrating accident detection
│   ├── cr.mp4                       # Test video 1
│   ├── output_video.mp4             # Video with detection outputs
│   ├── Project Demo.mp4             # Project demonstration video
│   └── Work_report.pdf              # Report detailing project workflow
```

---

## Features

1. **Accident Detection**
   - Detects accidents in real-time using the YOLOv8n model.
   - Processes live video streams or pre-recorded videos.

2. **Flask Server Integration**
   - Displays accident detection results on a web server.
   - Sends alerts with snapshots and accident details.

3. **Jetson Nano Optimization**
   - Optimized for deployment on Jetson Nano 2GB.
   - Lightweight YOLOv8n model ensures fast inference.

4. **Annotated Dataset**
   - Custom dataset annotated using **Roboflow**.

---

## Dataset

The dataset used for this project was created and annotated with the help of [Roboflow](https://roboflow.com/). Roboflow provides an intuitive interface for annotation and dataset augmentation. 

Steps to use the dataset:
1. Download the dataset by exporting it from Roboflow in YOLO format.
2. Place the dataset in the `dataset/` directory.
3. Update the `data.yaml` file to reflect the paths and class names.

---

## Getting Started

### Prerequisites
- Python 3.8+
- Jetson Nano with JetPack SDK
- Required Libraries: `torch`, `ultralytics`, `Flask`, `opencv-python`

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/realtime-accident-detection.git
   cd realtime-accident-detection
   ```

2. Download the pretrained YOLOv8n model and place it in the `Models/` directory:
   - `generalized.pt`: General-purpose model.
   - `yolov8n.pt`: Fine-tuned model for accident detection.

---

## How to Run

### 1. Train the Model
- Navigate to `Model_codes/` and open `Model_train.ipynb` to train the YOLOv8n model on your dataset.

### 2. Perform Inference
- Use `model_infer.ipynb` to test the trained model on new videos or images.

### 3. Deploy on Jetson Nano
- Run `Jetsonnano.py` to deploy the model on Jetson Nano for real-time inference.

### 4. Start Flask Server
- Use the Flask server to display results and monitor accident detections:
   ```bash
   python app.py
   ```

---

## Results

- **Detection Accuracy**: The fine-tuned YOLOv8n model achieved high accuracy with fast inference times on Jetson Nano.
- **Inference Demo**: Check `Test_videos/` for demo videos showcasing accident detection in various scenarios.

---

## Future Improvements

- Expand the dataset with more diverse accident scenarios.
- Implement edge computing for multi-camera setups.
- Enhance alert system with IoT hardware for real-time notifications.

---

## Acknowledgments

- YOLOv8 framework by [Ultralytics](https://github.com/ultralytics).
- **[Roboflow](https://roboflow.com/)** for dataset annotation and augmentation tools.

---

Feel free to adjust any section or add more details!
