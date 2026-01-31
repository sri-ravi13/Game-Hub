import cv2
import mediapipe as mp
import pyautogui
import time

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.35)
mp_draw = mp.solutions.drawing_utils
pyautogui.FAILSAFE = False

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
if not ret:
    print("Failed to grab frame from camera. Exiting.")
    exit()
frame_height, frame_width, _ = frame.shape


class KEY_STATE:
    NEUTRAL = 0

    LEFT = 1
    RIGHT = 2

    ACCELERATE = 3
    BRAKE = 4

current_steering = KEY_STATE.NEUTRAL
current_throttle = KEY_STATE.NEUTRAL


last_action_time = {
    'nitro': 0,
    'horn': 0
}
ACTION_COOLDOWN = 2 


def is_fist(hand_landmarks):

    try:
        index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
        index_mcp = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].y
        middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
        middle_mcp = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y
        return index_tip > index_mcp and middle_tip > middle_mcp
    except:
        return False

def is_thumbs_up(hand_landmarks):

    try:
        thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y
        thumb_ip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].y
        index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
        index_mcp = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP].y
        return thumb_tip < thumb_ip and index_tip > index_mcp
    except:
        return False


print("Starting Mr. Racer Controller v2 in 3 seconds...")
print("IMPORTANT: Click on the game to make it active!")
time.sleep(3)
print("Controller is LIVE. Press 'q' on the camera window to quit.")

try:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        new_steering = KEY_STATE.NEUTRAL
        new_throttle = KEY_STATE.NEUTRAL
        detected_gesture = "NONE"


        steer_boundary = frame_width / 3
        throttle_boundary = frame_height / 2

        if results.multi_hand_landmarks:
            hand_landmarks = results.multi_hand_landmarks[0]
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]
            cx, cy = int(wrist.x * frame_width), int(wrist.y * frame_height)
            cv2.circle(frame, (cx, cy), 10, (0, 255, 0), cv2.FILLED)


            if cx < steer_boundary:
                new_steering = KEY_STATE.LEFT
            elif cx > frame_width - steer_boundary:
                new_steering = KEY_STATE.RIGHT
            
            if cy < throttle_boundary:
                new_throttle = KEY_STATE.ACCELERATE
            else:
                new_throttle = KEY_STATE.BRAKE


            current_time = time.time()
            if is_fist(hand_landmarks):
                detected_gesture = "FIST (HORN)"
                if current_time - last_action_time['horn'] > ACTION_COOLDOWN:
                    print("Action: HORN!")
                    pyautogui.press('h')
                    last_action_time['horn'] = current_time
            elif is_thumbs_up(hand_landmarks):
                detected_gesture = "THUMBS UP (NITRO)"
                if current_time - last_action_time['nitro'] > ACTION_COOLDOWN:
                    print("Action: NITRO!")
                    pyautogui.press('space')
                    last_action_time['nitro'] = current_time

        if new_steering != current_steering:
            pyautogui.keyUp('left'); pyautogui.keyUp('right')
            if new_steering == KEY_STATE.LEFT: pyautogui.keyDown('left')
            elif new_steering == KEY_STATE.RIGHT: pyautogui.keyDown('right')
            current_steering = new_steering
        

        if new_throttle != current_throttle:
            pyautogui.keyUp('up'); pyautogui.keyUp('down')
            if new_throttle == KEY_STATE.ACCELERATE: pyautogui.keyDown('up')
            elif new_throttle == KEY_STATE.BRAKE: pyautogui.keyDown('down')
            current_throttle = new_throttle
        
        cv2.putText(frame, f"Gesture: {detected_gesture}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
        
        cv2.imshow('Mr. Racer Hand Controller', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): break
finally:
    print("Controller stopped. Releasing all keys.")
    pyautogui.keyUp('up'); pyautogui.keyUp('down'); pyautogui.guitool_code
print(browse(urls=['https://poki.com/en/g/subway-surfers', 'https://poki.com/en/g/mr-racer-car-racing']))