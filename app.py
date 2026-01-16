import cv2
import math
import time
import cvzone
import streamlit as st
from ultralytics import YOLO
import numpy as np

# --- PAGE SETUP ---
st.set_page_config(page_title="SafeGuard AI", layout="wide")
st.title("🛡️ SafeGuard: Industrial Safety Monitor")

# Sidebar
st.sidebar.header("Control Panel")
confidence_threshold = st.sidebar.slider("Confidence Threshold", 0.0, 1.0, 0.5)
enable_alerts = st.sidebar.checkbox("Enable SMS Alerts", value=False)

# Load Model
@st.cache_resource
def load_model():
    return YOLO("yolov8n.pt") # Replace with "best.pt" if you train a custom model

model = load_model()

# Class Names (Standard COCO). 
# IF YOU TRAIN YOUR OWN MODEL: Change this list to ['Helmet', 'No Helmet', 'Person']
classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "couch", "potted plant", "bed",
              "dining table", "toilet", "tv", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"]

# --- APP LOGIC ---
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Live Camera Feed")
    frame_placeholder = st.empty()
    stop_button = st.button("Stop Camera")

with col2:
    st.subheader("Real-Time Logs")
    log_placeholder = st.empty()
    alert_count = 0

# Camera Loop
cap = cv2.VideoCapture(0)

while cap.isOpened() and not stop_button:
    success, img = cap.read()
    if not success:
        st.error("Camera not detected.")
        break

    # Detection
    results = model(img, stream=True)
    
    violation_detected = False

    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2 - x1, y2 - y1
            conf = math.ceil((box.conf[0] * 100)) / 100
            cls = int(box.cls[0])
            currentClass = classNames[cls]

            if conf > confidence_threshold:
                # --- HACKATHON LOGIC ---
                # Example: If 'person' is found, we assume it's a worker.
                # In a real trained model, you would check "if currentClass == 'No Helmet'"
                
                color = (0, 255, 0) # Green by default
                
                # SIMULATION FOR DEMO:
                # Let's say "Scissors" represents a "Hazard" or "No Helmet" for the demo
                if currentClass == "scissors" or currentClass == "cell phone": 
                    color = (0, 0, 255) # Red
                    violation_detected = True
                    cvzone.putTextRect(img, "VIOLATION!", (x1, y1-10), scale=1, thickness=1, colorR=(0,0,255))
                
                cvzone.cornerRect(img, (x1, y1, w, h), l=9, rt=5, colorR=color)
                cvzone.putTextRect(img, f'{currentClass} {conf}', (max(0, x1), max(35, y1)), scale=1, thickness=1, offset=5)

    # Status Updates
    if violation_detected:
        alert_count += 1
        log_placeholder.markdown(f"### ⚠️ Status: HAZARD DETECTED \n **Total Alerts:** {alert_count}")
        if enable_alerts and alert_count % 50 == 0: # Prevent spamming
             st.toast("SMS Alert Sent to Supervisor!") 
             # send_sms_alert("Safety Violation Detected on Camera 1") 
    else:
        log_placeholder.markdown(f"### ✅ Status: SAFE \n **Total Alerts:** {alert_count}")

    # Display in Streamlit
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    frame_placeholder.image(img, channels="RGB")

cap.release()
