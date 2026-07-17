import streamlit as st
from ultralytics import YOLO
import os

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="Bottle Detection AI",
    page_icon="🍾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------------------------
# LOAD MODEL
# -------------------------------------------------
MODEL_PATH = "weights/best.pt"

@st.cache_resource
def load_model():
    if not os.path.exists(MODEL_PATH):
        st.error("❌ Model not found!")
        st.stop()
    return YOLO(MODEL_PATH)

model = load_model()

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------
st.sidebar.title("🍾 Bottle Detection AI")
st.sidebar.success("Navigation")

st.sidebar.markdown("---")

st.sidebar.header("🧠 Model")

st.sidebar.write("• YOLOv8n")
st.sidebar.write("• PyTorch")
st.sidebar.write("• Streamlit")
st.sidebar.write("• OpenCV")

st.sidebar.markdown("---")

st.sidebar.info(
"""
Choose a page from the sidebar above.

If you don't see pages,

Press **R** or click **Always rerun**.
"""
)

# -------------------------------------------------
# TITLE
# -------------------------------------------------
st.title("🍾 Bottle Detection AI Dashboard")

st.write(
"""
Welcome to the professional Bottle Detection System.

This application uses a custom-trained **YOLOv8** model for real-time bottle detection.
"""
)

st.markdown("---")

# -------------------------------------------------
# METRICS
# -------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Model", "YOLOv8n")

with col2:
    st.metric("Classes", "1")

with col3:
    st.metric("Dataset", "837 Images")

with col4:
    st.metric("Framework", "PyTorch")

st.markdown("---")

# -------------------------------------------------
# FEATURES
# -------------------------------------------------

left, right = st.columns([2,1])

with left:

    st.subheader("✨ Features")

    st.success("✔ Image Detection")

    st.success("✔ Video Detection")

    st.success("✔ Webcam Detection")

    st.success("✔ Confidence Threshold")

    st.success("✔ Download Results")

    st.success("✔ Detection Statistics")

    st.success("✔ Professional Dashboard")

with right:

    st.subheader("📌 Project Information")

    st.info(
"""
**Developer**

Ayesha Imran

---

**University**

University of Faisalabad

---

**Project**

Bottle Detection using YOLOv8

---

**Framework**

PyTorch + Streamlit
"""
)

st.markdown("---")

st.success("✅ Model Loaded Successfully")

st.caption("Use the pages in the left sidebar to perform Image, Video and Webcam Detection.")