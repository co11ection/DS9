#==================== Обработка картинок =============
# Цветовые пространства
# BGR - синий зеленый и красный
# HSV 
# H - HUE (тон, какой именно цвет(синий, зеленый или красный ...)) 0 - 179\  0 - 360
# S - Saturation(Нассыщенность - насколько чистый цыет, не серый) 0 - 255
# V - Value (яркость) 0-255


import cv2
import numpy as np

img = cv2.imread("comp_vision/images.jpeg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

print(hsv[100, 90])
print(hsv[10, 10])

lower = np.array([25, 40, 100]) # Нижняя граница цвета
upper = np.array([45, 150, 255]) # Верхняя граница цвета
mask = cv2.inRange(hsv, lower, upper)
# Маска - создает черно белое изображение, белыми отмечается пиксели попавшие вод диапазон который указали, а черными - все остальное
print("Форма", mask.shape)
cv2.imwrite("mask.jpg", mask)


noisy = img.copy()
rng = np.random.default_rng(42)
noise_mask = rng.random(noisy.shape[:2])
noisy[noise_mask< 0.02] = [255, 255, 255]
noisy[noise_mask> 0.98] = [0, 0, 0]


blur = cv2.GaussianBlur(noisy, (5, 5), 0)
median = cv2.medianBlur(noisy, 5)
cv2.imwrite('blure.jpg', blur)
cv2.imwrite('median.jpg', median) # чище убирает шумы


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges_soft = cv2.Canny(gray, 50, 150)
edgest_strict = cv2.Canny(gray, 100, 200)

cv2.imwrite("img6.jpg", edges_soft)
cv2.imwrite("img7.jpg", edgest_strict)



#---------------- пороговая обработка ------
for t in [80, 120, 160]:
    ret, thresh = cv2.threshold(gray, t, 255, cv2.THRESH_BINARY)
    count = cv2.countNonZero(thresh)
    print(f"Порог {t}, белые пиксели {count} из gray {gray.size}")
    
    
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower = np.array([0, 15, 100])
upper = np.array([30, 90, 255])
mask = cv2.inRange(hsv, lower, upper)


kernel = np.ones((5, 5), np.uint8)

oppened = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
clossed = cv2.morphologyEx(oppened, cv2.MORPH_CLOSE, kernel)
print(cv2.countNonZero(mask))
print(cv2.countNonZero(clossed))

counters, _ = cv2.findContours(
    clossed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)

largest = max(counters, key=cv2.contourArea)

print(largest)

x, y, w, h = cv2.boundingRect(largest)

print(x, y, w, h)

# cv2.imwrite("img8.jpg", counters)
M = cv2.moments(largest)
#m10 - расположение первого момента относительно оси y
# m00 - нулевой момент
#m01 - расположение первого момента относительно оси x
cx = int(M["m10"] / M["m00"])
cy = int(M['m01'] / M["m00"])

canvas = img.copy()
cv2.rectangle(canvas, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv2.imwrite('photo1.jpg', canvas)
