# color_utils.py

def hex_to_rgba(hex_color, alpha=255):
    """
    Преобразует цвет в формате HEX в формат RGBA.
    
    :param hex_color: Цвет в формате HEX (например, '#FE6E1F').
    :param alpha: Значение альфа-канала (прозрачности), по умолчанию 255 (непрозрачный).
    :return: Кортеж (r, g, b, alpha), представляющий цвет в формате RGBA.
    """
    hex_color = hex_color.lstrip("#")
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return (r, g, b, alpha)
