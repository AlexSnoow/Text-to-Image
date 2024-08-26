from PIL import Image
from button_drawer import draw_button

def main():
    # Входные данные
    input_image_path = "IN/1973128773-0.jpg"
    output_image_path = "OUT/1973128773-0_with_button.jpg"  # Изменено на формат JPG
    
    # Параметры кнопки
    text = "Мощный проц Core i5"
    font_path = "arial.ttf"
    font_size = 30
    text_color = (255, 255, 255)  # Белый
    button_color_hex = "#FE6E1F"  # Оранжевый
    shadow_color = (0, 0, 0, 128)  # Черный с прозрачностью
    color1 = (255, 153, 0)  # Светло-оранжевый
    color2 = (255, 69, 0)   # Красный

    # Создание кнопки
    button_image = draw_button(
        text,
        font_path,
        font_size,
        text_color,
        button_color_hex,
        shadow_color,
        color1,
        color2
    )

    # Открытие основного изображения
    base_image = Image.open(input_image_path).convert("RGBA")

    # Расположение кнопки
    image_width, image_height = base_image.size
    button_width, button_height = button_image.size
    button_position = (
        (image_width - button_width) // 2,
        image_height - button_height - 50  # Отступ от нижнего края
    )

    # Вставка кнопки на основное изображение
    base_image.paste(button_image, button_position, button_image)

    # Сохранение результата в формате JPG
    base_image = base_image.convert("RGB")  # Преобразование в RGB перед сохранением в JPG
    base_image.save(output_image_path, "JPEG")

if __name__ == "__main__":
    main()
