# Hand Gesture Game Hub 🎮✋

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.5%2B-green)](https://opencv.org/)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-Latest-orange)](https://mediapipe.dev/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Latest-red)](https://streamlit.io/)
[![License](https://img.shields.io/badge/license-MIT-purple)](LICENSE)

> **Control your favorite games with a wave of your hand!**

A sophisticated computer vision-based system that transforms real-time hand movements into in-game commands. Play Subway Surfers, Mr. Racer, and Plonky using intuitive hand gestures instead of traditional keyboard controls.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Supported Games](#supported-games)
- [Demo](#demo)
- [Installation](#installation)
- [System Requirements](#system-requirements)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Gesture Controls](#gesture-controls)
- [Project Structure](#project-structure)
- [Technical Architecture](#technical-architecture)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)

---

## 🌟 Overview

The **Hand Gesture Game Hub** is an innovative Human-Computer Interaction (HCI) system that leverages advanced computer vision to translate physical hand movements into digital game commands. Built as a mini project for the Image Analysis and Computer Vision Laboratory course at MEPCO Schlenk Engineering College, this system demonstrates the practical application of MediaPipe's hand tracking technology in creating Natural User Interfaces (NUIs).

### Key Highlights

- 🎯 **Real-time Hand Tracking**: Utilizes MediaPipe to detect 21 hand landmarks with high accuracy
- 🚀 **Low Latency**: Optimized for responsive gameplay with minimal input lag
- 🎨 **Intuitive Interface**: Beautiful Streamlit-based UI for easy game selection
- 🎮 **Multiple Control Schemes**: Supports swipes, positional tracking, and gesture recognition
- ♿ **Accessibility**: Provides alternative control method for users with motor impairments
- 🏃 **Physical Activity**: Encourages movement and reduces sedentary gameplay

---

## ✨ Features

### Computer Vision & Gesture Recognition

- **High-Fidelity Hand Tracking**: Accurately identifies 21 key landmarks on the hand
- **Diverse Gesture Support**: From simple swipes to complex poses (fist, thumbs-up)
- **Robust Detection**: Works under various lighting conditions
- **Adaptive Logic**: Rule-based system optimized for each game

### User Interface

- **Centralized Game Hub**: Single interface to launch all game controllers
- **Custom Styling**: Frosted glass design with background image support
- **Game Instructions**: Built-in "How to Play" guides for each game
- **Visual Feedback**: Real-time gesture display on camera feed

### Performance

- **Real-time Processing**: Processes webcam input at 30+ FPS
- **Efficient Architecture**: Separate processes for UI and controllers
- **State Management**: Smart key press/release handling
- **Cooldown System**: Prevents duplicate actions from single gestures

---

## 🎮 Supported Games

### 1. Subway Surfers 🚇
*Endless runner game with swipe-based controls*

**Controls:**
- 👆 **Swipe Up**: Jump over obstacles
- 👇 **Swipe Down**: Roll under barriers
- 👈 **Swipe Left**: Move to left lane
- 👉 **Swipe Right**: Move to right lane

**Gameplay Style**: Fast-paced, reflex-based
**Difficulty**: Easy to Medium

---

### 2. Mr. Racer 🏎️
*Racing game with advanced positional and gesture controls*

**Positional Controls (Hold):**
- 🔺 **Hand in Top Half**: Accelerate
- 🔻 **Hand in Bottom Half**: Brake/Reverse
- ◀️ **Hand on Left Side**: Steer Left
- ▶️ **Hand on Right Side**: Steer Right

**Gesture Controls (Action):**
- 👍 **Thumbs Up**: Activate Nitro Boost
- ✊ **Fist**: Sound Horn

**Gameplay Style**: Strategic positioning with action gestures
**Difficulty**: Medium to Hard

---

### 3. Plonky 🦘
*Platform game with hybrid swipe and hold controls*

**Controls:**
- 👆 **Swipe Up**: Jump
- 👇 **Swipe Down**: Duck/Crouch
- ◀️ **Hold Left**: Move Left (continuous)
- ▶️ **Hold Right**: Move Right (continuous)
- 👍 **Thumbs Up**: Special Move

**Gameplay Style**: Platforming with continuous movement
**Difficulty**: Easy to Medium

---

## 🎬 Demo

### Main Interface
The Hand Gesture Game Hub features a sleek, modern interface with:
- Game selection cards with preview images
- Expandable "How to Play" instructions
- One-click controller launch
- "Coming Soon" section for future games

### Live Gameplay
Watch as hand movements translate into game actions:
- Visual hand skeleton overlay
- Real-time gesture detection feedback
- Smooth, responsive character control
- Minimal latency between gesture and action

---

## 🚀 Installation

### Prerequisites

Before installing, ensure you have:

- **Python 3.8 or higher**
- **Webcam** (built-in or external)
- **Windows/macOS/Linux** operating system
- **4GB RAM minimum** (8GB recommended)
- **Stable internet connection** (for initial setup)

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/hand-gesture-game-hub.git
cd hand-gesture-game-hub
```

### Step 2: Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Download Game Assets

Create an `assets` folder and add the following images:
- `subway.jpg` - Subway Surfers thumbnail
- `maxresdefault.jpeg` - Mr. Racer thumbnail
- `plonky.jpeg` - Plonky thumbnail
- `play.jpeg` - Background image

### Step 5: Verify Installation

```bash
python -c "import cv2, mediapipe, streamlit, pyautogui; print('All dependencies installed successfully!')"
```

---

## 📦 System Requirements

### Minimum Requirements

| Component | Specification |
|-----------|--------------|
| **OS** | Windows 10, macOS 10.14+, Ubuntu 18.04+ |
| **Python** | 3.8 or higher |
| **RAM** | 4GB |
| **Webcam** | 720p @ 30fps |
| **Processor** | Dual-core 2.0 GHz |
| **Storage** | 500MB free space |

### Recommended Requirements

| Component | Specification |
|-----------|--------------|
| **OS** | Windows 11, macOS 12+, Ubuntu 20.04+ |
| **Python** | 3.10+ |
| **RAM** | 8GB |
| **Webcam** | 1080p @ 60fps |
| **Processor** | Quad-core 2.5 GHz |
| **Storage** | 1GB free space |

### Required Python Packages

```txt
opencv-python>=4.5.0
mediapipe>=0.9.0
streamlit>=1.28.0
pyautogui>=0.9.53
keyboard>=0.13.5
Pillow>=10.0.0
```

---

## 💻 Usage

### Quick Start

1. **Launch the Game Hub**
```bash
streamlit run game_hub_streamlit.py
```

2. **Select Your Game**
   - Click on any game card in the web interface
   - Read the "How to Play" instructions
   - Click the "▶️ Play Now!" button

3. **Position Yourself**
   - Sit 2-3 feet from your webcam
   - Ensure good lighting (front/side lighting preferred)
   - Keep background relatively plain

4. **Make the Game Active**
   - **IMPORTANT**: Click on the game window after it loads
   - Wait for the "Controller is LIVE" message
   - Start playing with hand gestures!

5. **Exit**
   - Press `q` on the camera window to quit
   - Or close the game window directly

### Detailed Usage Guide

#### For Subway Surfers

```bash
# 1. Launch from hub or directly:
python subway_surfers_controller.py

# 2. Open Subway Surfers in browser
# 3. Click on game to make it active
# 4. Wait 3 seconds for controller initialization
# 5. Start swiping!
```

**Tips:**
- Make deliberate swipe motions
- Return hand to center between swipes
- Swipe threshold is 10% of screen width
- 0.5 second cooldown between actions

#### For Mr. Racer

```bash
# 1. Launch from hub or directly:
python mr_racer_controller.py

# 2. Open Mr. Racer game
# 3. Click on game window
# 4. Position hand for initial acceleration
# 5. Use gestures for special actions
```

**Tips:**
- Screen divided into 3 vertical zones for steering
- Top/bottom half controls acceleration/braking
- Hold gestures for continuous control
- Special actions have 2-second cooldown

#### For Plonky

```bash
# 1. Launch from hub or directly:
python plonky_controller.py

# 2. Open Plonky game
# 3. Click on game window
# 4. Use continuous holds and swipes
```

**Tips:**
- Left/right zones trigger continuous movement
- Vertical swipes must be 15% of screen height
- Horizontal cooldown is 0.1 seconds for responsiveness

---

## 🔧 How It Works

### System Architecture

```
┌─────────────────┐
│  Streamlit UI   │  (Game Hub Interface)
└────────┬────────┘
         │ Launches
         ▼
┌─────────────────┐
│ Game Controller │  (Separate Python Process)
└────────┬────────┘
         │
    ┌────┴────┬────────┬──────────┐
    ▼         ▼        ▼          ▼
┌───────┐ ┌────────┐ ┌──────┐ ┌──────────┐
│OpenCV │ │MediaPipe│ │Logic │ │PyAutoGUI │
└───────┘ └────────┘ └──────┘ └──────────┘
    │         │         │          │
    │         ▼         │          │
    │  ┌──────────┐    │          │
    │  │21 Hand   │    │          │
    │  │Landmarks │    │          │
    │  └────┬─────┘    │          │
    │       │          │          │
    ▼       ▼          ▼          ▼
┌───────────────────────────────────┐
│     Gesture Recognition Logic     │
└───────────────────────────────────┘
                 │
                 ▼
         ┌──────────────┐
         │Keyboard Input│
         │to Game Window│
         └──────────────┘
```

### Processing Pipeline

1. **Frame Capture**: OpenCV captures video from webcam at 30 FPS
2. **Hand Detection**: MediaPipe palm detector locates hand in frame
3. **Landmark Extraction**: 21 key points identified on detected hand
4. **Gesture Analysis**: Custom logic analyzes landmark positions/movements
5. **Action Mapping**: Recognized gestures mapped to keyboard commands
6. **Input Simulation**: PyAutoGUI sends keypresses to active game window
7. **Visual Feedback**: Annotated frame displayed with detection info

### MediaPipe Hand Landmarks

MediaPipe tracks 21 landmarks on each hand:

```
        8   12  16  20
        |   |   |   |
    4   |   |   |   |
    |   7   11  15  19
    |   |   |   |   |
    3   6   10  14  18
    |   |   |   |   |
    2   5   9   13  17
    |   |   |   |   |
    1   |   |   |   |
    |   |   |   |   |
    0   0   0   0   0  ← Wrist
```

**Key Landmarks Used:**
- **0**: WRIST - Base position tracking
- **4**: THUMB_TIP - Thumbs-up detection
- **8**: INDEX_FINGER_TIP - Swipe tracking
- **5-17**: Knuckles - Fist detection

---

## 🎯 Gesture Controls

### Swipe Gesture Detection

```python
# Simplified algorithm
1. Detect hand → Record start position
2. Track hand movement → Calculate displacement (dx, dy)
3. Compare displacement to threshold
4. Determine primary direction (horizontal vs vertical)
5. Trigger corresponding action
6. Apply cooldown period
7. Reset for next gesture
```

**Parameters:**
- `SWIPE_THRESHOLD`: 10-15% of screen dimension
- `ACTION_COOLDOWN`: 0.5 seconds
- Detection based on wrist position for stability

### Positional Control

```python
# Screen divided into zones
Left Zone   | Center Zone | Right Zone
  (33%)     |    (33%)    |   (33%)
```

- Hand position tracked continuously
- Zone changes trigger key down/up events
- Prevents key spam with state management

### Pose Recognition

```python
# Thumbs-up detection
if thumb_tip.y < thumb_ip.y AND index_tip.y > index_mcp.y:
    return THUMBS_UP

# Fist detection  
if all_finger_tips.y > corresponding_mcp.y:
    return FIST
```

- Based on relative landmark positions
- Resistant to hand rotation
- 2-second cooldown for action gestures

---

## 📁 Project Structure

```
hand-gesture-game-hub/
│
├── game_hub_streamlit.py          # Main Streamlit UI
├── subway_surfers_controller.py   # Subway Surfers controller
├── mr_racer_controller.py         # Mr. Racer controller
├── plonky_controller.py           # Plonky controller
│
├── assets/                         # Game assets
│   ├── subway.jpg
│   ├── maxresdefault.jpeg
│   ├── plonky.jpeg
│   └── play.jpeg
│
├── requirements.txt                # Python dependencies
├── README.md                       # This file
├── LICENSE                         # MIT License
│
├── docs/                           # Documentation
│   ├── ARCHITECTURE.md
│   ├── GESTURE_GUIDE.md
│   └── TROUBLESHOOTING.md
│
└── examples/                       # Example videos/images
    ├── demo_subway.gif
    ├── demo_racer.gif
    └── demo_plonky.gif
```

### File Descriptions

#### Core Application Files

**game_hub_streamlit.py**
- Main entry point of the application
- Streamlit-based web interface
- Custom CSS styling with frosted glass effects
- Game launcher with subprocess management
- Error handling and user feedback

**subway_surfers_controller.py**
- Swipe-based gesture recognition
- Wrist position tracking for stability
- Directional swipe detection (up/down/left/right)
- Visual feedback with trajectory lines

**mr_racer_controller.py**
- Hybrid control scheme
- Positional tracking for steering/throttle
- Pose recognition for special actions
- State-based key management

**plonky_controller.py**
- Continuous movement controls
- Combined swipe and hold mechanics
- Index finger tip tracking
- Dual cooldown system

---

## 🏗️ Technical Architecture

### Technology Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **UI** | Streamlit | Web-based interface |
| **Computer Vision** | OpenCV | Video I/O and processing |
| **Hand Tracking** | MediaPipe | Landmark detection |
| **Input Simulation** | PyAutoGUI, Keyboard | OS-level keyboard control |
| **Language** | Python 3.8+ | Core implementation |

### Design Patterns

#### 1. **Modular Architecture**
Each game has its own controller script, allowing for:
- Independent gesture logic
- Easy addition of new games
- Isolated debugging and testing

#### 2. **State Management**
```python
class KEY_STATE:
    NEUTRAL = 0
    LEFT = 1
    RIGHT = 2
    ACCELERATE = 3
    BRAKE = 4

current_steering = KEY_STATE.NEUTRAL
current_throttle = KEY_STATE.NEUTRAL
```

#### 3. **Event-Driven Processing**
```python
while cap.isOpened():
    frame = capture()
    landmarks = detect_hand(frame)
    gesture = recognize_gesture(landmarks)
    execute_action(gesture)
    display_feedback(frame)
```

### Key Algorithms

#### Swipe Detection Algorithm

```python
def detect_swipe(start_pos, current_pos, threshold):
    dx = current_pos.x - start_pos.x
    dy = current_pos.y - start_pos.y
    
    if abs(dx) > abs(dy):  # Horizontal swipe
        if abs(dx) > threshold:
            return 'RIGHT' if dx > 0 else 'LEFT'
    else:  # Vertical swipe
        if abs(dy) > threshold:
            return 'DOWN' if dy > 0 else 'UP'
    
    return None
```

#### Pose Recognition Algorithm

```python
def is_thumbs_up(landmarks):
    thumb_tip = landmarks[THUMB_TIP]
    thumb_ip = landmarks[THUMB_IP]
    index_tip = landmarks[INDEX_FINGER_TIP]
    index_mcp = landmarks[INDEX_FINGER_MCP]
    
    thumb_extended = thumb_tip.y < thumb_ip.y
    fingers_curled = index_tip.y > index_mcp.y
    
    return thumb_extended and fingers_curled
```

---

## ⚙️ Configuration

### Camera Settings

Edit controller files to adjust camera parameters:

```python
# In any controller file
cap = cv2.VideoCapture(0)  # Change 0 to 1, 2, etc. for different cameras

# Adjust MediaPipe confidence thresholds
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,  # Increase for fewer false positives
    min_tracking_confidence=0.5     # Increase for more stable tracking
)
```

### Gesture Sensitivity

**Swipe Threshold** (Subway Surfers & Plonky):
```python
# Make swipes easier (smaller value) or harder (larger value)
SWIPE_THRESHOLD = frame_width * 0.10  # Default: 10% of screen
```

**Cooldown Periods**:
```python
# Adjust time between repeated actions
ACTION_COOLDOWN = 0.5  # seconds (default)
```

**Zone Boundaries** (Mr. Racer):
```python
# Adjust steering sensitivity
steer_boundary = frame_width / 3  # Default: divide screen into thirds

# Adjust throttle sensitivity  
throttle_boundary = frame_height / 2  # Default: top/bottom half
```

### UI Customization

**Background Image**:
```python
# In game_hub_streamlit.py
background_image_path = "assets/play.jpeg"  # Change to your image
```

**Color Scheme**:
```css
/* In the st.markdown CSS section */
h1 { color: #D4AF37; }  /* Title color */
h2 { color: #f63366; }  /* Section headers */
.stButton>button { background-color: #5a4fcf; }  /* Button color */
```

---

## 🐛 Troubleshooting

### Common Issues and Solutions

#### 1. Camera Not Detected

**Error Message:**
```
Failed to grab frame from camera. Exiting.
```

**Solutions:**
- Check if camera is connected and working
- Try different camera index: `cv2.VideoCapture(1)` or `(2)`
- Close other applications using the camera
- Grant camera permissions to Python/Terminal
- Update camera drivers

#### 2. Hand Not Detected

**Symptoms:** No hand skeleton appears on screen

**Solutions:**
- Improve lighting conditions
- Move closer to camera (2-3 feet ideal)
- Ensure plain background
- Keep hand fully visible in frame
- Clean camera lens
- Lower detection confidence:
```python
min_detection_confidence=0.5  # Default: 0.7
```

#### 3. Gestures Not Triggering

**Symptoms:** Hand detected but no game response

**Solutions:**
- **CRITICAL**: Click on game window to make it active
- Increase gesture magnitude (swipe larger/faster)
- Check cooldown hasn't blocked action
- Verify game uses standard keyboard controls
- Disable PyAutoGUI failsafe:
```python
pyautogui.FAILSAFE = False
```

#### 4. High Latency/Lag

**Symptoms:** Delay between gesture and game action

**Solutions:**
- Close resource-heavy applications
- Reduce webcam resolution:
```python
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
```
- Lower MediaPipe tracking confidence
- Ensure Python is not running in debug mode

#### 5. Streamlit Won't Start

**Error Message:**
```
Port 8501 already in use
```

**Solutions:**
```bash
# Use different port
streamlit run game_hub_streamlit.py --server.port 8502

# Or kill existing Streamlit process
# Windows:
taskkill /F /IM streamlit.exe

# macOS/Linux:
pkill -f streamlit
```

#### 6. Import Errors

**Error Message:**
```
ModuleNotFoundError: No module named 'mediapipe'
```

**Solutions:**
```bash
# Reinstall dependencies
pip install --upgrade -r requirements.txt

# Or install individually
pip install opencv-python mediapipe streamlit pyautogui keyboard
```

#### 7. PyAutoGUI Not Working

**Symptoms:** Keypresses not reaching game

**Solutions:**
- Ensure game window is in focus (click it)
- Disable game's anti-cheat if present
- Try running with administrator privileges
- On macOS, grant Accessibility permissions:
  - System Preferences → Security & Privacy → Accessibility
  - Add Terminal/Python to allowed apps

### Debug Mode

Enable detailed logging:

```python
# Add to top of controller file
import logging
logging.basicConfig(level=logging.DEBUG)

# Add print statements for debugging
print(f"Hand position: ({cx}, {cy})")
print(f"Detected gesture: {gesture}")
print(f"Cooldown remaining: {cooldown_time}")
```

### Performance Optimization

```python
# Reduce processing load
hands = mp_hands.Hands(
    max_num_hands=1,           # Track only one hand
    model_complexity=0,         # Use lighter model (0 or 1)
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# Lower frame rate
time.sleep(0.03)  # ~33 FPS instead of max
```

---