import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import re

st.title("📸 Barcode Scanner (Google ZXing API)")

st.write("Upload an image containing a barcode to scan.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)

    # Convert image to bytes
    img_bytes = BytesIO()
    image.save(img_bytes, format="PNG")
    
    # Send image to Google's ZXing API for barcode recognition
    files = {"file": img_bytes.getvalue()}
    response = requests.post("https://zxing.org/w/decode", files=files)

    if response.status_code == 200:
        html_text = response.text

        # Extract barcode number using regex
        match = re.search(r'<td>Raw text</td><td><pre>(.*?)</pre></td>', html_text)
        
        if match:
            barcode_data = match.group(1)
            st.success(f"✅ Barcode Detected: {barcode_data}")
        else:
            st.error("⚠️ No barcode found. Please try again with a clearer image.")
    else:
        st.error("⚠️ Failed to scan barcode. Please try again.")
