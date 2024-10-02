import cv2
import numpy as np
import random
cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

window_width = 640
window_height = 480

def add_disco_lights(frame):
    for _ in range(5):  
        x1 = random.randint(0, window_width)
        y1 = random.randint(0, window_height)
        x2 = x1 + random.randint(20, 100)
        y2 = y1 + random.randint(20, 100)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, -1)
while True:
    
    ret, frame = cap.read()
    
    if not ret:
        print("Failed to grab frame")
        break

    frame = cv2.resize(frame, (window_width, window_height))

    frame = cv2.flip(frame, 1)

    frame_with_effects = frame.copy()

    add_disco_lights(frame_with_effects)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    font = cv2.FONT_HERSHEY_SIMPLEX
    text = "Happy Birthday"
    font_scale = 1.7
    font_color = (255, 255, 255)
    font_thickness = 5
    text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
    text_x = (frame.shape[1] - text_size[0]) // 2
    text_y = (frame.shape[0] + text_size[1]) // 2
    cv2.putText(frame_with_effects, text, (text_x, text_y), font, font_scale, font_color, font_thickness)

    for (x, y, w, h) in faces:
        
        face_region = frame[y:y+h, x:x+w]
        frame_with_effects[y:y+h, x:x+w] = face_region
    
    
    cv2.imshow('Birthday Party ', frame_with_effects)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
