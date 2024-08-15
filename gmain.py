from PIL import Image, ImageDraw, ImageFont

# Открытие изображения
image = Image.open('image_in.jpg')

# Создание объекта для рисования
draw = ImageDraw.Draw(image)

# Загрузка шрифта
font = ImageFont.truetype("consola.ttf", size=45)

# Определение текста, позиции и цвета
text = "Пример текста"
position = (50, 50)
color = (0, 0, 0)  # цвет

# Добавление текста на изображение
draw.text(position, text, fill=color, font=font)

# Сохранение изображения
image.save('output_image.jpg')
