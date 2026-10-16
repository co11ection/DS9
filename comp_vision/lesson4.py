# import cv2

# face_cascade = cv2.CascadeClassifier(
#     cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
# )

# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break
    
#     frame = cv2.flip(frame, 1)
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
#     faces = face_cascade.detectMultiScale(
#         gray, scaleFactor=1.1, minNeighbors=6
#     )
    
#     for x, y, w, h in faces:
#         cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
#     cv2.imshow("FACE", frame)
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break

# cap.release()
# cv2.destroyAllWindows()


import cv2
import numpy as np
import math


def count_fingers(hand_counter):
    hull = cv2.convexHull(hand_counter)
    
    area = cv2.contourArea(hand_counter)
    
    hull_area = cv2.contourArea(hull)
    
    solidity = area / hull_area if hull_area else 0
    
    if solidity > 0.95:
        return 0
    
    epsilon = 0.0015 * cv2.arcLength(hand_counter, True)
    
    approx = cv2.approxPolyDP(hand_counter, epsilon, True)
    
    if len(approx) < 4:
        return 0
    
    hull_idx = cv2.convexHull(approx, returnPoints=False)
    
    if hull_idx is None or len(hull_idx) < 3:
        return 0
    hull_idx = np.sort(hull_idx.flatten()).reshape(-1, 1)
    
    defects = cv2.convexityDefects(approx, hull_idx)
    count = 0
    if defects is not None:
        for i in range(defects.shape[0]):
            s, e, f, d = defects[i, 0] # получили индекс начала, конца, глубокой точки и глубины дефекта
            start = tuple(approx[s][0])
            
            end = tuple(approx[e][0])
            
            far = tuple(approx[f][0])
            
            a = math.dist(start, end)
            
            b = math.dist(start, far)
            
            c = math.dist(end, far)
            
            if b*c == 0:
                continue
            
            cos_angle = (b**2 + c**2 - a**2)/(2*b*c)
            
            cos_angle = max(-1, min(1.0, cos_angle))
            
            angle = math.degrees(math.acos(cos_angle)) 
            
            if angle <= 90 and d /256.0 > 15:
                count += 1
                
    return count


def find_hand(frame, lower, upper, min_area=3000):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    kernel = np.ones((7, 7), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    
    mask = cv2.GaussianBlur(mask, (5,5), 0)
    
    conturs, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )
    if not conturs:
        return None, mask
    
    hand = max(conturs, key=cv2.contourArea)
    
    if cv2.contourArea(hand)< min_area:
        return None, mask
    
    fingers = count_fingers(hand)
    
    tip = tuple(
        int(v) for v in hand[hand[:, :, 1].argmin()][0]
    )
    return (fingers, tip, hand), mask

lower = np.array([0, 30, 60], dtype=np.uint8)

upper = np.array([25, 180, 255], dtype=np.uint8)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Камера не включилась")
    raise SystemExit

while True:
    ret, frame = cap.read()
    
    if not ret:
        break
    
    frame = cv2.flip(frame, 1)
    
    result, mask = find_hand(frame, lower, upper)
    
    if result is not None:
        fingers, tip, hand = result
        
        cv2.drawContours(frame, [hand], -1, (0, 255, 0), 2)
        
        cv2.circle(frame, tip, 8, (0, 0, 255), -1)
        
        cv2.putText(
            frame,
            f'{fingers} fingers',
            (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.2,
            (0,255,0),
            3
        )     
    else:
        cv2.putText(
            frame,
            "hand does not found",
            (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.2,
            (0, 0, 255),
            3
        )
    
    cv2.imshow("Камера", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()

