import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ About Bottle Detection AI")

st.markdown("---")

left, right = st.columns([2,1])

with left:

    st.header("📌 Project Overview")

    st.write("""
This project is a custom Object Detection System developed using the YOLOv8
deep learning model.

The system detects bottles from images, videos, and live webcam streams using
a model trained on a custom Roboflow dataset.

The application is built with Streamlit and OpenCV to provide a simple and
professional user interface.
""")

    st.header("🎯 Features")

    st.success("✔ Image Detection")

    st.success("✔ Video Detection")

    st.success("✔ Webcam Detection")

    st.success("✔ Download Detection Results")

    st.success("✔ Adjustable Confidence Threshold")

    st.success("✔ Professional Dashboard")

with right:

    st.header("👩‍💻 Developer")

    st.info("""
**Name**

Ayesha Imran

---

**University**

University of Faisalabad

---

**Degree**

Bachelor of Artificial Intelligence

---

**Project**

Bottle Detection using YOLOv8
""")

st.markdown("---")

st.header("📊 Training Results")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Precision", "0.575")

with c2:
    st.metric("Recall", "0.414")

with c3:
    st.metric("mAP50", "0.464")

with c4:
    st.metric("mAP50-95", "0.271")

st.markdown("---")

st.header("📦 Dataset")

st.write("""
- Total Images: **837**
- Classes: **1**
- Object: **Bottle**
- Annotation Tool: **Roboflow**
""")

st.markdown("---")

st.header("🛠 Technologies Used")

tech1, tech2, tech3, tech4 = st.columns(4)

tech1.info("🐍 Python")
tech2.info("🔥 PyTorch")
tech3.info("🎯 YOLOv8")
tech4.info("🎈 Streamlit")

st.markdown("---")

st.header("🚀 Future Improvements")

st.write("""
- Multi-object detection
- GPU acceleration
- Real-time analytics dashboard
- Object counting
- Detection history
- Cloud deployment
- Mobile support
""")

st.markdown("---")

st.success("Bottle Detection AI • Portfolio Project • 2026")