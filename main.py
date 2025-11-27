from text_processor import TextProcessor
from vector_renderer import VectorRenderer
from utils import extract_text_from_docx
from concurrent.futures import ThreadPoolExecutor, as_completed
import os


DOCS_FOLDER = 'docs'  # Переменная, указывающая на папку с документами
INPUT_FILE = 'lesson.docx'  # Название исходного файла
    

def main():
    canvas_size = (800, 600)
    input_file = os.path.join(DOCS_FOLDER, INPUT_FILE)  # Добавлен путь к папке docs
    output_prefix = "output"
    
    # Извлечение текста из .docx файла
    extracted_text = extract_text_from_docx(input_file)

    # Обработчик текста
    processor = TextProcessor()
    processed_text = processor.wrap_text_to_pages(extracted_text.split("\n"), canvas_size[0], canvas_size[1])

    # Многопоточная обработка
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = {executor.submit(render_page, page_lines, idx, canvas_size, output_prefix): idx for idx, page_lines in enumerate(processed_text)}
        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Ошибка при обработке страницы {futures[future]}: {e}")

def render_page(page_lines, index, canvas_size, output_prefix):
    renderer = VectorRenderer(canvas_size)
    renderer.render_text_on_canvas(page_lines)
    output_filename = f'{output_prefix}_page_{index+1}.svg'
    renderer.save_as_svg(output_filename)

if __name__ == "__main__":
    main()