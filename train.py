
from ultralytics import YOLO

# Load model
model = YOLO('yolov8m.pt')

# Train model
results = model.train(data='config.yaml', epochs=30, imgsz=640)
results = model.val() # validation

model.predict(source='./cars/24495494.jpg') # check by image