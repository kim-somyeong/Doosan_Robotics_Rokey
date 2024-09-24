from ultralytics import YOLO

model = YOLO('yolov8n.pt')

model.predict(source='https://youtu.be/LNwODJXcvt4',show=True)