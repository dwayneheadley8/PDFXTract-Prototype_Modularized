import fitz  # PyMuPDF

def read_pdf_text(path):
    """
    Extract text from the first page of a PDF file.
    
    Args:
        path (str): Path to the PDF file
        
    Returns:
        str: Extracted text from the PDF, or empty string if error
    """
    try:
        doc = fitz.open(path)
        if len(doc) == 0:
            raise ValueError("PDF file is empty or corrupted")
        page = doc[0]
        text = page.get_text("text")
        doc.close()
        return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""
