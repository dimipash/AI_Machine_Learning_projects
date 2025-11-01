# Object Detection with YOLOv5

This project is an object detection application that utilizes the powerful and real-time object detection capabilities of the YOLOv5 model. This repository is structured to perform inference on images to detect a wide variety of objects.

## Features

*   **State-of-the-art Object Detection:** Leverages the YOLOv5 model, which is known for its high accuracy and speed.
*   **Pre-trained on COCO:** The model is pre-trained on the large-scale COCO dataset, enabling it to detect 80 different object classes.
*   **Extensible:** The project can be extended to train on custom datasets for specific use cases.
*   **Easy to Use:** Simple and straightforward scripts to run inference on your own images.

## Installation

1.  **Clone this repository.**   

2.  **Install dependencies:**
    This project relies on the dependencies listed in the `yolov5/requirements.txt` file. It is recommended to use a virtual environment.
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r yolov5/requirements.txt
    ```

## Usage

To run object detection on an image, you can use the `detect.py` script provided by YOLOv5. The `main.py` script is a placeholder for custom logic.

```bash
python yolov5/detect.py --source test_image.png --weights yolov5s.pt
```

This command will download the `yolov5s.pt` weights if they are not already present and run detection on the `test_image.png`. The results will be saved in the `yolov5/runs/detect/exp` directory.

## Dependencies

The main dependencies for this project are:

*   Python 3.8 or later
*   PyTorch
*   OpenCV
*   NumPy
*   Matplotlib

For a complete list of dependencies, please refer to the `yolov5/requirements.txt` file.

## Project Structure

```
.
├── main.py
├── test_image.png
├── README.md
├── .gitignore
└── yolov5/
    ├── detect.py
    ├── models/
    ├── data/
    ├── utils/
    └── requirements.txt
```

*   `main.py`: Main script for custom application logic.
*   `test_image.png`: A sample image for testing the object detection.
*   `README.md`: This file.
*   `.gitignore`: Specifies which files and directories to ignore in version control.
*   `yolov5/`: Submodule containing the YOLOv5 implementation.
    *   `detect.py`: Script to run inference.
    *   `models/`: Contains model definitions.
    *   `data/`: Contains dataset configurations.
    *   `utils/`: Utility functions.
    *   `requirements.txt`: Dependencies for YOLOv5.