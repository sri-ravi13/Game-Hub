import cv2
import mediapipe as mp
import pyautogui
import time
import math

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

pyautogui.FAILSAFE = False

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
if not ret:
    print("Failed to grab frame from camera. Exiting.")
    exit()
frame_height, frame_width, _ = frame.shape

is_swiping = False
swipe_start_pos = None
last_action_time = 0
ACTION_COOLDOWN = 0.5
SWIPE_THRESHOLD = frame_width * 0.10  

print("Starting in 3 seconds...")
print("IMPORTANT: Click on the Subway Surfers game to make it the active window!")
time.sleep(3)
print("Controller is LIVE. Press 'q' on the camera window to quit.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    current_time = time.time()
    action_performed_this_frame = False

    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]
        mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]
        cx, cy = int(wrist.x * frame_width), int(wrist.y * frame_height)
        cv2.circle(frame, (cx, cy), 10, (0, 255, 0), cv2.FILLED)

        if not is_swiping:

            is_swiping = True
            swipe_start_pos = (cx, cy)
            cv2.circle(frame, swipe_start_pos, 20, (255, 255, 0), cv2.FILLED) # Mark start point
        else:

            cv2.line(frame, swipe_start_pos, (cx, cy), (0, 255, 255), 4)

            dx = cx - swipe_start_pos[0]
            dy = cy - swipe_start_pos[1]


            if current_time - last_action_time > ACTION_COOLDOWN:

                if abs(dx) > abs(dy):
                    if abs(dx) > SWIPE_THRESHOLD:
                        if dx > 0:
                            print("Action: SWIPE RIGHT")
                            pyautogui.press('right')
                        else:
                            print("Action: SWIPE LEFT")
                            pyautogui.press('left')
                        action_performed_this_frame = True
                else: # More vertical movement
                    if abs(dy) > SWIPE_THRESHOLD:
                        if dy > 0:
                            print("Action: SWIPE DOWN")
                            pyautogui.press('down')
                        else:
                            print("Action: SWIPE UP")
                            pyautogui.press('up')
                        action_performed_this_frame = True
        

        if action_performed_this_frame:
            is_swiping = False
            swipe_start_pos = None
            last_action_time = current_time
    else:

        is_swiping = False
        swipe_start_pos = None

    if is_swiping and swipe_start_pos:
        cv2.putText(frame, 'Swiping...', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
    else:
        cv2.putText(frame, 'Waiting for swipe...', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('Subway Surfers Hand Controller', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("Controller stopped.")