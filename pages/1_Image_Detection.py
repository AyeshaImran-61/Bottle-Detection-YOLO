import streamlit as st
from ultralytics import YOLO
from PIL import Image
import tempfile
import os
import cv2

st.set_page_config(page_title="Image Detection", page_icon="🖼️", layout="wide")

MODEL_PATH = "weights/best.pt"

@st.cache_resource
def load_model():
    return YOLO(MODEL_PATH)

model = load_model()

st.title("🖼️ Image Detection")
st.write("Upload an image and detect bottles using your trained YOLOv8 model.")

confidence = st.slider(
    "Confidence Threshold",
    0.10,
    1.00,
    0.25,
    0.05
)

uploaded_file = st.file_uploader(
    "Choose an Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    image = Image.open(uploaded_file)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original Image")
        st.image(image, width=500)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
        image.save(tmp.name)

        results = model.predict(
            source=tmp.name,
            conf=confidence,
            save=False
        )

    result = results[0]

    plotted = result.plot()

    plotted = cv2.cvtColor(plotted, cv2.COLOR_BGR2RGB)

    with col2:
        st.subheader("Detection Result")
        st.image(plotted, width=500)

    st.markdown("---")

    st.subheader("Detection Statistics")

    total = len(result.boxes)

    if total == 0:
        st.warning("No bottles detected.")
    else:

        st.success(f"Total Bottles Detected : {total}")

        for i, box in enumerate(result.boxes):

            conf = float(box.conf)

            st.write(
                f"Bottle {i+1} : {conf:.2%} confidence"
            )

    result_image = Image.fromarray(plotted)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as output:

        result_image.save(output.name)

        with open(output.name, "rb") as file:

            st.download_button(
                "📥 Download Result",
                data=file,
                file_name="bottle_detection.png",
                mime="image/png"
            )

    os.remove(tmp.name)
    os.remove(output.name)