import streamlit as st
from ultralytics import YOLO
import tempfile
import os
import cv2

st.set_page_config(
    page_title="Video Detection",
    page_icon="🎥",
    layout="wide"
)

MODEL_PATH = "weights/best.pt"

@st.cache_resource
def load_model():
    return YOLO(MODEL_PATH)

model = load_model()

st.title("🎥 Video Bottle Detection")

st.write(
    "Upload a video and detect bottles frame by frame using the trained YOLOv8 model."
)

confidence = st.slider(
    "Confidence Threshold",
    0.10,
    1.00,
    0.25,
    0.05
)

video_file = st.file_uploader(
    "Upload Video",
    type=["mp4", "avi", "mov", "mkv"]
)

if video_file is not None:

    input_video = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    input_video.write(video_file.read())
    input_video.close()

    cap = cv2.VideoCapture(input_video.name)

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    output_path = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4").name

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")

    writer = cv2.VideoWriter(
        output_path,
        fourcc,
        fps,
        (width, height)
    )

    progress = st.progress(0)

    frame_text = st.empty()

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    current = 0

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        results = model.predict(
            frame,
            conf=confidence,
            verbose=False
        )

        annotated = results[0].plot()

        writer.write(annotated)

        current += 1

        progress.progress(min(current / frame_count, 1.0))

        frame_text.text(
            f"Processing Frame {current} / {frame_count}"
        )

    cap.release()
    writer.release()

    st.success("✅ Video Detection Completed")

    st.video(output_path)

    with open(output_path, "rb") as f:

        st.download_button(
            "📥 Download Processed Video",
            data=f,
            file_name="bottle_detection_video.mp4",
            mime="video/mp4"
        )

    os.remove(input_video.name)