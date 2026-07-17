from ultralytics import YOLO

# Load pretrained YOLOv8 Nano model
model = YOLO("yolov8n.pt")

# Train the model
results = model.train(
    data="dataset/data.yaml",
    epochs=50,
    imgsz=640,
    batch=8,
    lr0=0.01,
    project="runs",
    name="bottle_detection_exp1",
    pretrained=True
)

# Evaluate model
metrics = model.val()

print(metrics)