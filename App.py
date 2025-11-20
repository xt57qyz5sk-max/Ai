import streamlit as st

st.title("AI Product Visualizer")

st.write("Upload your product image and preview it using AI!")

uploaded = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded:
    st.image(uploaded, caption="Uploaded product", use_column_width=True)
    st.success("AI preview coming soon!")
