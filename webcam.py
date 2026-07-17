from ultralytics import YOLO
import cv2

# Load trained model
model = YOLO("runs/detect/runs/bottle_detection_exp1/weights/best.pt")

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Run detection
    results = model(frame, conf=0.25)

    # Draw detections
    annotated = results[0].plot()

    cv2.imshow("Bottle Detection", annotated)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()