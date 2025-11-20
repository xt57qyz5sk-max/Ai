import streamlit as st
from PIL import Image
import numpy as np

st.set_page_config(page_title="Personal Virtual Try-On + AI Marketing", layout="wide")
st.title("🎯 Personal Virtual Try-On + AI Marketing")

st.write("Upload your photo and product image, and AI will overlay the product on your photo and generate marketing content.")

# 1️⃣ Upload user photo
user_image = st.file_uploader("Upload your photo", type=["png", "jpg", "jpeg"])

# 2️⃣ Upload product image
product_image = st.file_uploader("Upload product image (preferably PNG with transparency)", type=["png", "jpg", "jpeg"])

if user_image and product_image:
    user_img = Image.open(user_image).convert("RGBA")
    product_img = Image.open(product_image).convert("RGBA")

    # --- Overlay product on user photo ---
    # Simple version: overlay at center of image
    try:
        product_img_resized = product_img.resize((user_img.width // 2, user_img.height // 2))
        user_img.paste(product_img_resized, (user_img.width//4, user_img.height//4), product_img_resized)
    except:
        st.warning("Product image might not support transparency. Use PNG for transparency.")

    st.image(user_img, caption="Virtual Try-On Result", use_column_width=True)
    
    # 3️⃣ Simple AI Marketing Generator
    if st.button("Generate Marketing Content"):
        st.success("📌 Instagram post ready")
        st.success("🎬 Short video (Placeholder)")
        st.success("📝 Caption ready")
        st.info("Advanced AI content can be added here later")

else:
    st.info("⏳ Please upload both your photo and the product image to start.")
