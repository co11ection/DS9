# =========== Computer Vision =========
# Облать, которая учит программы ПОНИМАТЬ изображение и видео
# находить на них обьекты, лица, текст, движение

# OpenCV - pip3/pip install opencv-python
# python -m venv venv
# . venv/bin/activate
# RGB (RED- BLUE - GREEN) - 0 - 255 BGR (интенсивность синего, зеленый, крассный каналы)


import cv2
import numpy as np

img = np.zeros((300, 400, 3), dtype=np.uint8)
img[:,:] = (235, 205, 135)
img[200: 300,:] = (80, 150, 60)
cv2.circle(img, (340, 60), 35, (80, 220,255), -1)
cv2.rectangle(img, (120, 150), (260, 250), (60, 90, 160), -1)
cv2.imwrite("img1.jpg", img)


loaded = cv2.imread('img1.jpg')
print("Форма", loaded.shape)
print("Тип данных", loaded.dtype)
print("Пиксель (10,10)", loaded[10,10])



img = cv2.imread("comp_vision/images.jpeg")

h, w = img.shape[:2]
print(h)
print(w)

half = cv2.resize(img, (w//2, h//2))
print(half.shape)

cy, cx = h//2, w//2

# img[y1: y2, x1:x2]

crop = img[cy-50: cy+50, cx-50: cx+50]
print(crop.shape)
cv2.imwrite("img2.jpg", crop)


flip_img = cv2.flip(img, -1)
# 0 - по вертикали
# 1 - по горизонтали
# -1 - выполняет оба разворота
cv2.imwrite("img3.jpg", flip_img)

# rotate - 90, 180, 270

rotate_img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imwrite("img4.jpg", rotate_img)


gray_photo = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("img5.jpg", gray_photo)


import time

cap = cv2.VideoCapture(0)
fps = 30
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(width, height, fps)
fourcc = cv2.VideoWriter_fourcc(*"avc1") #mp4v
writer = cv2.VideoWriter("output.mp4", fourcc, fps, (width, height))


print("Камера открыта", cap.isOpened())
time.sleep(1)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    frame = cv2.flip(frame, 1)
    writer.write(frame)
    cv2.imshow("Камера", frame)
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord('q'):
        break
    elif key == ord("s"):
        cv2.imwrite('photo.jpg', frame)
        print('Фото сохранено')

cap.release()
writer.release()
cv2.destroyAllWindows()

import os
print(os.path.abspath("output.mp4"), os.path.exists("output.mp4") and os.path.getsize("output.mp4"))