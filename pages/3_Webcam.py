import streamlit as st
import cv2
from ultralytics import YOLO

st.set_page_config(page_title="Webcam Detection", layout="wide")

st.title("📷 Live Webcam Bottle Detection")

MODEL_PATH = "runs/detect/runs/bottle_detection_exp1/weights/best.pt"

@st.cache_resource
def load_model():
    return YOLO(MODEL_PATH)

model = load_model()

st.info("Press **Start Webcam** to begin live detection. Press **Stop Webcam** to stop.")

run = st.checkbox("▶ Start Webcam")

frame_placeholder = st.empty()

if run:
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    if not cap.isOpened():
        st.error("Could not open webcam.")
        st.stop()

    while run:
        ret, frame = cap.read()

        if not ret:
            st.error("Failed to read frame.")
            break

        results = model(frame, conf=0.25)

        annotated_frame = results[0].plot()

        annotated_frame = cv2.cvtColor(
            annotated_frame,
            cv2.COLOR_BGR2RGB
        )

        frame_placeholder.image(
            annotated_frame,
            channels="RGB"
        )

        run = st.checkbox("▶ Start Webcam", value=True)

    cap.release()