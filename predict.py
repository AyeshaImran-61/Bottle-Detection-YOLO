from ultralytics import YOLO

# Load your trained model
model = YOLO("runs/detect/runs/bottle_detection_exp1/weights/best.pt")

# Run prediction on an image
results = model.predict(
    source="bottle 3.jpg",   
    conf=0.25,
    save=True,
    show=False
)

print("Prediction completed successfully!")