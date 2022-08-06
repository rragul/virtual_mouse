import cv2
import mediapipe as mp
import pyautogui

cam = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
index_y = 0
while True:
    _, frame = cam.read()
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)
                # print(x, y)
                if id == 8:
                    cv2.circle(frame, (x,y), 10, (0,255,255))
                    index_x = screen_width / frame_width * x
                    index_y = screen_height / frame_height * y
                    pyautogui.moveTo(index_x, index_y)
                if id == 4:
                    cv2.circle(frame, (x,y), 10, (0,255,255))
                    tump_x = screen_width / frame_width * x
                    tump_y = screen_height / frame_height * y
                    # print(abs(index_y-tump_y))
                    if abs(index_y-tump_y) < 60:
                        pyautogui.click()
                        pyautogui.sleep(1)

    cv2.imshow('Virtual Mouse',frame)
    cv2.waitKey(1)

