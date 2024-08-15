import cv2
import numpy as np

# Выбор типа шрифта и размера
font = cv2.FONT_HERSHEY_SIMPLEX
size = 1.5

text_message = "Привет!"

image = np.zeros((600, 800, 3), dtype=np.uint8)
cv2.putText(image, text_message.encode('utf-8').decode(), (100, 50), font, size, (0, 255, 0))
cv2.imwrite("image_with_text.jpg", image)

print("Изображение сохранено в файле image_with_text.jpg")