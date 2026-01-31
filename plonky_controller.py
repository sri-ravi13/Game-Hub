import cv2
import mediapipe as mp
import pyautogui
import time
import keyboard

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
SWIPE_THRESHOLD = frame_height * 0.15

LEFT_THRESHOLD = 0.35
RIGHT_THRESHOLD = 0.65
HORIZONTAL_COOLDOWN = 0.1
last_horizontal_time = 0

print("Starting in 3 seconds...")
print("IMPORTANT: Click on the Plonky game to make it the active window!")
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

    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]
        mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
        hand_x_norm = index_tip.x  # normalized [0,1]
        hand_y = int(index_tip.y * frame_height)
        hand_x = int(index_tip.x * frame_width)

        cv2.circle(frame, (hand_x, hand_y), 10, (0, 255, 0), cv2.FILLED)

        if current_time - last_horizontal_time > HORIZONTAL_COOLDOWN:
            if hand_x_norm < LEFT_THRESHOLD:
                if not keyboard.is_pressed('left'):
                    keyboard.press('left')
                last_horizontal_time = current_time
                cv2.putText(frame, 'Move LEFT', (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
            elif hand_x_norm > RIGHT_THRESHOLD:
                if not keyboard.is_pressed('right'):
                    keyboard.press('right')
                last_horizontal_time = current_time
                cv2.putText(frame, 'Move RIGHT', (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
            else:

                keyboard.release('left')
                keyboard.release('right')

        if not is_swiping:
            is_swiping = True
            swipe_start_pos = (hand_x, hand_y)
        else:
            dx = hand_x - swipe_start_pos[0]
            dy = hand_y - swipe_start_pos[1]

            action_performed_this_frame = False

            if current_time - last_action_time > ACTION_COOLDOWN:
                if abs(dy) > SWIPE_THRESHOLD:
                    if dy < 0:
                        pyautogui.press('up') 
                        cv2.putText(frame, 'JUMP', (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    else:
                        pyautogui.press('down')
                        cv2.putText(frame, 'DOWN', (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

                    action_performed_this_frame = True

            if action_performed_this_frame:
                is_swiping = False
                swipe_start_pos = None
                last_action_time = current_time

    else:
        is_swiping = False
        swipe_start_pos = None


    if is_swiping and swipe_start_pos:
        cv2.putText(frame, 'Swipe Up/Down...', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
    else:
        cv2.putText(frame, 'Hand Detected', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('Plonky Hand Controller', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("Controller stopped.")
