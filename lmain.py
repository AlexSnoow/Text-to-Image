import cv2
import numpy as np

# Выбор типа шрифта (например, Arial)
font = cv2.FONT_HERSHEY_SIMPLEX

# Выбор размера шрифта
size = 1

text_message = "Привет!"

# Создание изображения с размером 800x600 пикселей
image = np.zeros((600, 800, 3), dtype=np.uint8)

# Добавление текста на изображение в координатах (100, 50)
cv2.putText(image, text_message, (100, 50), font, size, (0, 255, 0))

# Сохранение изображения с текстом
cv2.imwrite("image_with_text.jpg", image)

print("Изображение сохранено в файле image_with_text.jpg")