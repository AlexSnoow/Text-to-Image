from PIL import Image, ImageDraw, ImageFont

# Создание нового изображения с прозрачным фоном (800x600 пикселей)
image = Image.new("RGBA", (800, 600), (0, 0, 0, 0))  # прозрачный фон

# Создание объекта для рисования
draw = ImageDraw.Draw(image)

# Загрузка шрифта
font = ImageFont.truetype("arial.ttf", size=30)

# Определение текста
text = "Текст на прозрачном фоне"

# Вычисление размера текста
text_bbox = draw.textbbox((0, 0), text, font=font)
text_width = text_bbox[2] - text_bbox[0]  # Ширина текста
text_height = text_bbox[3] - text_bbox[1]  # Высота текста

# Определение отступов и положения прямоугольника
padding = 20  # отступы вокруг текста
rect_start = (50, 50)
rect_end = (rect_start[0] + text_width + 2 * padding, rect_start[1] + text_height + 2 * padding)

# Рисование оранжевого прямоугольника, чуть больше текста
orange_color = (255, 165, 0, 255)  # оранжевый цвет с полной непрозрачностью
draw.rectangle([rect_start, rect_end], fill=orange_color)

# Определение позиции текста внутри прямоугольника
text_position = (rect_start[0] + padding, rect_start[1] + padding)
text_color = (0, 0, 0)  # черный цвет текста

# Добавление текста на изображение
draw.text(text_position, text, fill=text_color, font=font)

# Сохранение изображения в формате PNG
image.save('output_image_with_transparent_background.png')

# Для просмотра изображения
image.show()
