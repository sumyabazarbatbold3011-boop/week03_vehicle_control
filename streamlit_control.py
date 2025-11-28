import streamlit as st
import requests

SERVER_URL = "http://127.0.0.1:5000"  # Flask server URL

st.title("🚗 Vehicle Control Panel")

speed = st.slider("Speed", 0, 255, 0)

def send_command(direction, speed):
    url = f"{SERVER_URL}/move"
    payload = {"direction": direction, "speed": speed}
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            st.success(f"✅ Command sent: {direction} at speed {speed}")
        else:
            st.error(f"❌ Error: {response.text}")
    except Exception as e:
        st.error(f"❌ Failed to send command: {e}")

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Forward"):
        send_command("forward", speed)
with col2:
    if st.button("Stop"):
        send_command("stop", 0)
with col3:
    if st.button("Backward"):
        send_command("backward", speed)

col1, col2 = st.columns(2)
with col1:
    if st.button("Left"):
        send_command("left", speed)
with col2:
    if st.button("Right"):
        send_command("right", speed)
