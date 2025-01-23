import streamlit as st
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

# Streamlit UI
st.title("📸 Barcode Scanner App")
st.write("Click the button below to start scanning.")

# Function to scan barcode
def scan_barcode():
    cap = cv2.VideoCapture(0)  # Opens the webcam
    st.write("Scanning... (Press 'Q' to stop)")

    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to access webcam.")
            break

        decoded_objects = pyzbar.decode(frame)
        for obj in decoded_objects:
            barcode_data = obj.data.decode('utf-8')
            cap.release()
            cv2.destroyAllWindows()
            return barcode_data

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return None

# Streamlit button to start scanning
if st.button("Start Scanning"):
    result = scan_barcode()
    if result:
        st.success(f"✅ Scanned Barcode: {result}")
    else:
        st.error("⚠️ No barcode detected.")
