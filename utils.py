from docx import Document


def extract_text_from_docx(file_path):
    """Извлекает текст из .docx файла"""
    document = Document(file_path)
    full_text = "\n".join(paragraph.text for paragraph in document.paragraphs)
    return full_text