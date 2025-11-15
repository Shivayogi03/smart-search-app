# core/extractor.py

import os
from io import BytesIO

# PDF extraction
try:
    import pdfplumber
except ImportError:
    pdfplumber = None

# DOCX extraction
try:
    import docx
except ImportError:
    docx = None


def extract_text(file):
    """
    Extract text from uploaded files: PDF, DOCX, TXT.
    Returns a clean string of text.
    """
    filename = file.name.lower()

    # Handle TXT files
    if filename.endswith(".txt"):
        content = file.read().decode("utf-8", errors="ignore")
        return content

    # Handle PDF files
    elif filename.endswith(".pdf"):
        if pdfplumber is None:
            raise ImportError("pdfplumber is required to extract PDF text. Install with pip install pdfplumber")
        
        text = ""
        file.seek(0)  # Reset file pointer
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text

    # Handle DOCX files
    elif filename.endswith(".docx"):
        if docx is None:
            raise ImportError("python-docx is required to extract DOCX text. Install with pip install python-docx")
        
        file.seek(0)
        doc = docx.Document(file)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text

    else:
        raise ValueError("Unsupported file type. Please upload TXT, PDF, or DOCX.")
