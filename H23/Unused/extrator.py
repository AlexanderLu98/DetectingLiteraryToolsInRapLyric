from docx import Document
from docx.enum.text import WD_COLOR_INDEX

def extract_highlighted_text(doc_path):
    doc = Document(doc_path)
    highlighted_text = []

    for para in doc.paragraphs:
        for run in para.runs:
            if run.font.highlight_color == WD_COLOR_INDEX.YELLOW:
                highlighted_text.append(run.text)

    return highlighted_text

# Use the function
highlighted_text = extract_highlighted_text('test.docx')
print(highlighted_text)
