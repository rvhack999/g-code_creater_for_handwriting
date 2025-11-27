from xml.etree.ElementTree import Element, SubElement
from lxml import etree


class VectorRenderer:
    def __init__(self, canvas_size=(800, 600)):
        self.canvas_size = canvas_size
        self.root = Element('svg', xmlns="http://www.w3.org/2000/svg",
                          version="1.1", width=f"{canvas_size[0]}px", height=f"{canvas_size[1]}px")

    def add_rectangle(self, x, y, w, h, stroke_color="black"):
        rect = SubElement(self.root, 'rect', {
            'x': str(x),
            'y': str(y),
            'width': str(w),
            'height': str(h),
            'stroke': stroke_color,
            'fill': 'none',
            'stroke-width': '1'
        })

    def save_as_svg(self, filename):
        tree = etree.ElementTree(self.root)
        with open(filename, 'wb') as f:
            tree.write(f, encoding='utf-8', xml_declaration=True)

    def render_text_on_canvas(self, text_lines):
        """
        Рендеринг текста на холсте с указанием размера холста
        """
        base_width_per_char = 50
        base_height_per_line = 50
        line_spacing = int(base_height_per_line * 1.5)

        y_position = 0
        for line in text_lines:
            x_position = 0
            for char in line:
                if char == '\t':  # Обрабатываем табуляцию
                    x_position += 200  # Значительное смещение для табуляции
                    continue

                # Простая демонстрационная фигура (прямоугольник)
                self.add_rectangle(x_position, y_position, base_width_per_char, base_height_per_line)

                x_position += base_width_per_char

            # Переходим на следующую строку с возможным изменением расстояния
            y_position += line_spacing