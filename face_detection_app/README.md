# Face Detection Application

This project is a simple yet powerful face detection application built in Python using the OpenCV library. It can detect faces in both static images and real-time video streams from a webcam.

## Features

*   **Image-Based Face Detection:** Detect faces in an image file and display the result with bounding boxes around the detected faces.
*   **Real-Time Webcam Face Detection:** Capture video from a webcam and perform real-time face detection, displaying the video feed with bounding boxes around the detected faces.

## Dependencies

The project relies on the following Python library:

*   `opencv-python`: A comprehensive library for computer vision tasks.


## Usage

1.  **Run the main script:**

    ```bash
    uv run main.py
    ```

2.  **Choose an option:**

    The script will prompt you to choose between two modes:

    *   **Detect faces from an image (1):** If you choose this option, you will be asked to provide the path to the image file you want to process.
    *   **Detect faces from webcam (2):** This option will open a window displaying the video feed from your webcam with real-time face detection.


## How It Works

The application uses a pre-trained Haar Cascade classifier from OpenCV to detect faces. The `haarcascade_frontalface_default.xml` file contains the pre-trained model for detecting frontal faces.

The script loads this classifier and then applies it to either a static image or each frame of a video stream. When a face is detected, a green rectangle is drawn around it to indicate the location of the face.


