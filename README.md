# YOLOv8 Project

This project utilizes YOLOv8 for vehicle detection on images.

## Project Structure

```
├── .venv/ # Virtual environment folder
├── cardetect_dataset/ # Dataset folder
├── cars/ # Directory for images to detect vehicles
├── config.yaml # Configuration file for YOLOv8
├── detect.py # Script for object detection on images
└── train.py # Script for training YOLOv8 model
```

## Getting Started

1. **Clone the repository:**

    ```bash
    git clone https://github.com/zulune/yolov8-car-detect.git
    cd yolov8-car-detect
    ```

2. **Setup virtual environment:**

    ```bash
    python -m venv .venv         # Create virtual environment
    source venv/bin/activate    # Activate virtual environment (Linux/Mac)
    .\venv\Scripts\activate     # Activate virtual environment (Windows)
    pip install -r requirements.txt   # Install dependencies
    ```

3. **Prepare Dataset:**

    Place your dataset in the `cardetect_dataset` folder. Ensure it follows the required structure. 
    - obj_Train_data (images and txt to train)
    - obj_Validation_data (images and txt to validation)
    #### from CVAT to export yolo 1.0 

4. **Configuration:**

    Update the `config.yaml` file with appropriate configuration settings for your project.

5. **Object Detection:**

    Use the `detect.py` script to perform object detection on images:

    ```bash
    python detect.py
    ```

6. **Training:**

    Use the `train.py` script to train your YOLOv8 model:

    ```bash
    python train.py
    ```

## License

This project is licensed under the [MIT License](LICENSE).

