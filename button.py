from PIL import Image, ImageDraw, ImageFont

def hex_to_rgba(hex_color, alpha=255):
    # Убираем символ #
    hex_color = hex_color.lstrip('#')
    # Преобразуем HEX в RGB
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return (r, g, b, alpha)

def draw_button(draw, position, size, text, font, text_color, button_color, shadow_color):
    x, y = position
    width, height = size
    
    # Рисуем тень
    shadow_offset = (10, 10)
    shadow_rect_start = (x + shadow_offset[0], y + shadow_offset[1])
    shadow_rect_end = (x + width + shadow_offset[0], y + height + shadow_offset[1])
    draw.rectangle([shadow_rect_start, shadow_rect_end], fill=shadow_color)
    
    # Создание градиента
    gradient = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    gradient_draw = ImageDraw.Draw(gradient)
    
    color1 = (255, 165, 0)  # Первый цвет градиента
    color2 = (255, 69, 0)   # Второй цвет градиента
    transition_start = int(height * 0.2)  # Начало перехода
    transition_end = int(height * 0.8)    # Конец перехода
    
    for i in range(height):
        if i < transition_start:
            color = color1
        elif i > transition_end:
            color = color2
        else:
            # Интерполяция цвета между color1 и color2
            ratio = (i - transition_start) / (transition_end - transition_start)
            r = int(color1[0] + (color2[0] - color1[0]) * ratio)
            g = int(color1[1] + (color2[1] - color1[1]) * ratio)
            b = int(color1[2] + (color2[2] - color1[2]) * ratio)
            color = (r, g, b)
        
        gradient_draw.line([(0, i), (width, i)], fill=color)
    
    # Наложение градиента на кнопку
    button_with_gradient = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    button_with_gradient.paste(gradient, (0, 0), gradient)
    
    # Наложение основной кнопки
    button_with_gradient = Image.new('RGBA', (width, height), button_color)
    button_with_gradient.paste(gradient, (0, 0), gradient)
    
    image.paste(button_with_gradient, (x, y), button_with_gradient)

    # Добавляем текст на кнопку
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]  # Ширина текста
    text_height = text_bbox[3] - text_bbox[1]  # Высота текста
    text_position = (x + (width - text_width) / 2, y + (height - text_height) / 2)
    
    draw.text(text_position, text, fill=text_color, font=font)

# Создание нового изображения с прозрачным фоном (800x600 пикселей)
image = Image.new("RGBA", (800, 600), (0, 0, 0, 0))  # прозрачный фон

# Создание объекта для рисования
draw = ImageDraw.Draw(image)

# Загрузка шрифта
font = ImageFont.truetype("arial.ttf", size=30)

# Определение кнопки
button_position = (50, 50)
button_size = (300, 100)
button_text = "Нажми меня"
text_color = (255, 255, 255)  # белый цвет текста
button_color_hex = "#FE6E1F"
button_color = hex_to_rgba(button_color_hex)  # Преобразование HEX в RGBA
shadow_color = (0, 0, 0, 128)  # цвет тени (полупрозрачный черный)

# Рисование кнопки
draw_button(draw, button_position, button_size, button_text, font, text_color, button_color, shadow_color)

# Сохранение изображения в формате PNG
image.save('output_image_with_3d_button.png')

# Для просмотра изображения
# image.show()
