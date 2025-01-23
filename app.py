import streamlit as st
from pyzbar.pyzbar import decode
from PIL import Image
import requests
from io import BytesIO

st.title("📸 Web-Based Barcode Scanner")

st.write("Upload an image containing a barcode to scan.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)

    # Convert image to bytes
    img_bytes = BytesIO()
    image.save(img_bytes, format="PNG")
    
    # Decode barcode from the image
    results = decode(image)
    
    if results:
        for result in results:
            st.success(f"✅ Barcode Detected: {result.data.decode('utf-8')}")
    else:
        st.error("⚠️ No barcode found. Please upload a clearer image.")
