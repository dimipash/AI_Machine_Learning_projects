import torch
import cv2
import numpy as np

model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

def detect_objects(image_path):    
    image = cv2.imread(image_path)
    results = model(image)
    results.show()

def detect_from_webcam():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        results = model(frame)

        rendered_img = np.array(results.render()[0])
        cv2.imshow('Webcam Object Detection', rendered_img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

print("Choose an option:\n1. Detect objects in an image\n2. Detect objects from webcam")
choice = input("Enter 1 or 2: ")

if choice == '1':
    image_path = input("Enter the path to the image: ")
    detect_objects(image_path)
elif choice == '2':
    detect_from_webcam()
else:
    print("Invalid choice. Please enter 1 or 2.")

