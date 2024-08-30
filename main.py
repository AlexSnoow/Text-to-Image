import csv
import os
from PIL import Image
from button_drawer import draw_button  # Импортируем модуль для создания кнопок

# Определяем папки
input_folder = "IN"
output_folder = "OUT"
csv_file = "input.csv"

# Функция для обработки изображений
def process_image(file_path, output_path, text, font_path="arial.ttf"):
    try:
        # Открываем изображение
        image = Image.open(file_path)

        # Параметры для кнопки
        text_color = (255, 255, 255)
        button_color_hex = "#FE6E1F"
        shadow_color = (0, 0, 0, 128)
        font_size = 30

        # Вычисляем размеры изображения
        image_width, image_height = image.size

        # Рассчитываем положение кнопки (например, по центру внизу)
        button_position = ((image_width - 300) // 2, image_height - 150)

        # Генерируем кнопку
        button = draw_button(
            text=text,
            font_path=font_path,
            font_size=font_size,
            text_color=text_color,
            button_color_hex=button_color_hex,
            shadow_color=shadow_color
        )

        if button is None:
            print(f"Ошибка при создании кнопки для текста: {text}")
            return

        # Вставляем кнопку на изображение
        image.paste(button, button_position, button)

        # Сохраняем изображение с кнопкой
        image.save(output_path)
        print(f"Изображение сохранено как {output_path}")
    except Exception as e:
        print(f"Ошибка при обработке {file_path}: {e}")

# Основная функция для чтения CSV и обработки файлов
def main():
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    try:
        with open(csv_file, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')

            # Выводим заголовки для отладки
            headers = next(reader)
            print(f"Заголовки: {headers}")

            for row in reader:
                if not row:
                    continue

                # Проверка количества колонок в строке
                if len(row) < 5:
                    print(f"Недостаточно данных в строке: {row}")
                    continue

                art = row[0]  # Первый столбец (АРТ)
                print(f"Обрабатываем ART: {art}")

                # Проходим по каждой колонке, начиная со второй
                for i, column_value in enumerate(row[1:], start=0):
                    text = column_value  # Текст для кнопки из колонки

                    # Ищем соответствующее изображение с окончанием -{i}.jpg
                    image_file = os.path.join(input_folder, f"{art}-{i}.jpg")
                    output_image = os.path.join(output_folder, f"{art}-{i}.jpg")

                    if os.path.exists(image_file):
                        print(f"Обрабатываем файл: {image_file} с текстом: {text}")
                        process_image(image_file, output_image, text)
                    else:
                        print(f"Изображение {image_file} не найдено")
    except Exception as e:
        print(f"Ошибка при чтении CSV файла: {e}")

if __name__ == "__main__":
    main()
