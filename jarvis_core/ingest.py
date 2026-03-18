import os
import fitz  # PyMuPDF
from odf import text, teletype
from odf.opendocument import load

def read_pdf(path):
    doc = fitz.open(path)
    return "\n".join(page.get_text() for page in doc)

def read_odf(path):
    doc = load(path)
    return teletype.extractText(doc)

def load_documents(folder="data"):
    docs = []
    filenames = []

    for file in os.listdir(folder):
        path = os.path.join(folder, file)

        if file.endswith(".txt"):
            with open(path, "r", encoding="utf-8") as f:
                docs.append(f.read())

        elif file.endswith(".pdf"):
            docs.append(read_pdf(path))

        elif file.endswith(".odt") or file.endswith(".ods"):
            docs.append(read_odf(path))

        else:
            continue
        
        filenames.append(file)

    return docs, filenames

