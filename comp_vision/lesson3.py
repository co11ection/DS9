import cv2

img = cv2.imread("comp_vision/images2.jpeg")
gray =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_eye.xml"
)

faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
print(len(faces))

canvas = img.copy()

for (x, y, w, h) in faces:
    cv2.rectangle(canvas, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    roi_gray = gray[y:y+h, x: x+w]
    roi_color = canvas[y:y+h, x: x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    print(len(eyes))
    
    for ex, ey, ew, eh in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (255, 0, 0), 2)
    
    
    cv2.imwrite("faces_detected.jpg", canvas)
    