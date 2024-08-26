from PIL import Image, ImageDraw, ImageFont
from color_utils import hex_to_rgba  # Предполагается, что hex_to_rgba определен в color_utils.py

def draw_button(
    text, font_path, font_size, text_color, button_color_hex, shadow_color,
    color1=(255, 153, 0), color2=(255, 69, 0)
):
    """
    Создает изображение кнопки с текстом, градиентом и тенями.

    :param text: Текст, который будет написан на кнопке.
    :param font_path: Путь к файлу шрифта.
    :param font_size: Размер шрифта для текста.
    :param text_color: Цвет текста в формате RGBA.
    :param button_color_hex: Цвет кнопки в формате HEX.
    :param shadow_color: Цвет тени в формате RGBA.
    :param color1: Первый цвет градиента.
    :param color2: Второй цвет градиента.
    :return: Изображение с кнопкой.
    """
    # Создаем объект шрифта
    font = ImageFont.truetype(font_path, size=font_size)
    
    # Создание объекта для расчета размера текста
    text_width, text_height = draw_text_size(text, font)
    
    # Вычисление размеров кнопки
    button_width = text_width + 50  # Добавляем отступ в 50 пикселей
    button_height = text_height + 50  # Добавляем отступ в 50 пикселей
    width, height = button_width, button_height

    # Создание изображения кнопки
    button_image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(button_image)

    # Создаем градиент
    gradient = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    gradient_draw = ImageDraw.Draw(gradient)

    transition_start = int(height * 0.2)
    transition_end = int(height * 0.8)

    for i in range(height):
        if i < transition_start:
            color = color1
        elif i > transition_end:
            color = color2
        else:
            ratio = (i - transition_start) / (transition_end - transition_start)
            r = int(color1[0] + (color2[0] - color1[0]) * ratio)
            g = int(color1[1] + (color2[1] - color1[1]) * ratio)
            b = int(color1[2] + (color2[2] - color1[2]) * ratio)
            color = (r, g, b)
        gradient_draw.line([(0, i), (width, i)], fill=color)

    button_color = hex_to_rgba(button_color_hex)
    button_with_gradient = Image.new("RGBA", (width, height), button_color)
    button_with_gradient.paste(gradient, (0, 0), gradient)

    # Создаем изображение для тени
    shadow_image = Image.new("RGBA", (width + 10, height + 10), (0, 0, 0, 0))
    shadow_draw = ImageDraw.Draw(shadow_image)
    shadow_draw.rectangle([10, 10, width + 10, height + 10], fill=shadow_color)
    
    # Вставляем градиентную кнопку на изображение с тенью
    shadow_image.paste(button_with_gradient, (10, 10), button_with_gradient)

    # Вставляем изображение с тенью на основное изображение кнопки
    button_image.paste(shadow_image, (0, 0), shadow_image)

    # Рисуем кнопку с градиентом
    button_image.paste(button_with_gradient, (0, 0), button_with_gradient)

    # Вычисление позиции текста
    text_position = (
        int((width - text_width) / 2),
        int((height - text_height) / 2),
    )
    draw.text(text_position, text, fill=text_color, font=font)

    return button_image

def draw_text_size(text, font):
    """
    Рассчитывает размер текста.

    :param text: Текст, который нужно измерить.
    :param font: Объект шрифта для текста.
    :return: Ширина и высота текста.
    """
    dummy_image = Image.new('RGBA', (1, 1))
    draw = ImageDraw.Draw(dummy_image)
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    return text_width, text_height
