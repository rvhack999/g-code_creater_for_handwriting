import random

class TextProcessor:
    SIZE_VARIATION_RANGE = (-5, 5)
    KERNING_VARIATION_RANGE = (-5, 5)
    LINE_SPACING_VARIATION_RANGE = (-5, 5)

    def wrap_text_to_pages(self, text_lines, page_width, page_height):
        """
        Деление текста на страницы с переносом слов и заданным ограничением по ширине и высоте страницы
        """
        pages = []
        current_page = []
        current_y = 0
        base_height_per_line = 50
        line_spacing = int(base_height_per_line * 1.5)

        words_in_progress = []  # Текущие слова на текущей строке
        word_buffer = ""       # Буфер для сборки слова

        def flush_words(words_list):
            nonlocal current_y
            while words_list:
                current_line = ''.join(words_list[:])  # Копия списка слов
                line_length = sum(len(word) * 50 for word in current_line)

                if current_y + line_spacing > page_height or line_length > page_width:
                    pages.append(current_page)
                    current_page = []
                    current_y = 0

                current_page.extend(current_line)
                current_y += line_spacing
                del words_list[:len(current_line)]

        for line in text_lines:
            for char in line:
                if char == ' ' or char == '\t':
                    # Завершаем сбор текущего слова и отправляем его в очередь
                    if word_buffer.strip():  # Избегаем добавления пустых слов
                        words_in_progress.append(word_buffer)
                    word_buffer = ""
                else:
                    word_buffer += char

            # Последняя проверка на наличие оставшихся слов
            if word_buffer.strip():
                words_in_progress.append(word_buffer)
                word_buffer = ""

            # Отправляем накопленные слова на обработку
            flush_words(words_in_progress)

        # Очистка остатков
        if word_buffer.strip():
            words_in_progress.append(word_buffer)
        flush_words(words_in_progress)

        if current_page:
            pages.append(current_page)

        return pages