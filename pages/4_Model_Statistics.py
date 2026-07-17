import streamlit as st

st.set_page_config(page_title="Model Statistics", page_icon="📊")

st.title("📊 Model Statistics")
st.markdown("---")

st.subheader("🧠 Trained Model")

st.info("""
**Model:** YOLOv8 Nano (YOLOv8n)

**Task:** Custom Object Detection

**Classes:** 1

**Object:** Bottle
""")

st.markdown("---")

st.subheader("📈 Training Configuration")

col1, col2 = st.columns(2)

with col1:
    st.metric("Epochs", "50")
    st.metric("Image Size", "640 x 640")
    st.metric("Batch Size", "8")
    st.metric("Optimizer", "Auto")

with col2:
    st.metric("Framework", "Ultralytics YOLOv8")
    st.metric("Python", "3.11")
    st.metric("Device", "CPU")
    st.metric("Model Size", "YOLOv8n")

st.markdown("---")

st.subheader("🎯 Evaluation Metrics")

metric1, metric2 = st.columns(2)

with metric1:
    st.success("Precision")
    st.write("**0.575**")

    st.success("Recall")
    st.write("**0.414**")

with metric2:
    st.success("mAP@50")
    st.write("**0.464**")

    st.success("mAP@50-95")
    st.write("**0.271**")

st.markdown("---")

st.subheader("📋 Dataset Information")

st.write("""
- 📸 Total Images: **837**
- 🎯 Classes: **Bottle**
- 📁 Training Images
- 📁 Validation Images
- 📁 Test Images
""")

st.markdown("---")

st.subheader("💡 Model Performance Analysis")

st.success("""
### Strengths

✅ Detects bottles accurately in normal lighting.

✅ Works on different bottle shapes.

✅ Fast inference using YOLOv8 Nano.

✅ Lightweight model suitable for real-time applications.
""")

st.warning("""
### Limitations

• Performance decreases when bottles overlap.

• Small bottles are sometimes missed.

• Very dark or blurry images reduce detection accuracy.

• Transparent bottles are harder to detect.
""")

st.markdown("---")

st.subheader("🚀 Possible Improvements")

st.write("""
✔ Train for 100–200 epochs

✔ Collect more diverse images

✔ Use YOLOv8s or YOLOv8m

✔ Add more bottle types

✔ Train on GPU

✔ Apply stronger data augmentation
""")