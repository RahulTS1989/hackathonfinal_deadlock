Here is a professional, hackathon-ready `README.md` file.

**Instructions:**

1. Create a file named `README.md` in your project folder.
2. Copy the text below and paste it in.
3. **Crucial Step:** Take a screenshot of your dashboard running and save it as `screenshot.png` in your folder so the image loads (or delete that line if you don't have one).

---

```markdown
# 🛡️ SafeGuard: The AI Safety Sentinel
> **Intelligent Automation for a Smarter & Safer Future**

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Framework](https://img.shields.io/badge/Framework-Streamlit-red)
![AI Model](https://img.shields.io/badge/AI-YOLOv8-green)
![Status](https://img.shields.io/badge/Status-Hackathon_Prototype-orange)

## 📖 Overview
**SafeGuard** is an intelligent Computer Vision system designed to automate safety compliance in high-risk industrial environments. By leveraging **YOLOv8** and **OpenCV**, it turns standard CCTV feeds into proactive safety officers that can detect hazards in real-time.

For this Hackathon demo, the system is trained to detect:
* **Safety Gear Compliance:** (Simulated)
* **Hazards:** (Simulated using objects like Cell Phones/Scissors for the demo)

## ⚠️ The Problem
Industrial accidents are often caused by:
1.  **Human Error:** Forgetting PPE (Personal Protective Equipment).
2.  **Delayed Response:** Manual monitoring is passive and slow.
3.  **Blind Spots:** Supervisors cannot be everywhere at once.

## 💡 The Solution
SafeGuard provides:
* **Real-Time Detection:** Instantly identifies violations via live camera feed.
* **Automated Alerts:** Sends SMS notifications to supervisors via **Twilio**.
* **Live Dashboard:** A centralized web interface for monitoring status and logs.

## ⚙️ Tech Stack
* **AI Engine:** [YOLOv8 (Ultralytics)](https://github.com/ultralytics/ultralytics) & OpenCV
* **Frontend:** Streamlit (Python)
* **Backend Logic:** Python 3.11
* **Notifications:** Twilio API (SMS)
* **Version Control:** GitHub

---

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/RahulJaiswal/SafeGuard-AI.git](https://github.com/RahulJaiswal/SafeGuard-AI.git)
cd SafeGuard-AI

```

### 2. Create a Virtual Environment

```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate

```

### 3. Install Dependencies

```bash
pip install -r requirements.txt

```

### 4. Configuration (Optional)

To enable SMS alerts, open `alert_system.py` and add your Twilio credentials:

```python
SID = 'YOUR_TWILIO_SID'
AUTH = 'YOUR_TWILIO_AUTH_TOKEN'

```

---

## 🏃‍♂️ How to Run the Demo

1. **Start the Application:**
```bash
streamlit run app.py

```


2. **Grant Permissions:** Allow the browser to access your webcam.
3. **Test the AI:**
* **SAFE STATE:** Sit in front of the camera. You will see a **Green Box** (Person detected).
* **HAZARD STATE:** Hold up a **Cell Phone** or **Scissors**. You will see a **Red Box** and the status will change to "HAZARD DETECTED".

## 🔮 Future Roadmap

* [ ] Train custom model on specific PPE (Hard Hats, Vests).
* [ ] Integrate with edge devices (Raspberry Pi/Jetson Nano).
* [ ] Add database storage for historical violation logs.
