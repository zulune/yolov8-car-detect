import glob
import os
import cv2
from ultralytics import YOLO

# Path to all images
IMG_PATH = './cars/*.jpg' 

model = YOLO('./runs/detect/train/weights/best.pt') # load trained model

results = model.predict(IMG_PATH, save=True)

