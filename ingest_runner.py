from jarvis_core.vector_store import store_chunks
from jarvis_core.chunker import chunk_text

from pdf2image import convert_from_path
import pytesseract
import os

# 🔧 Set paths
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
POPPLER_PATH = r"C:\Users\LENOVO\Desktop\Jarvis_Web\Jarvis_Assets\poppler-25.12.0\Library\bin"


# 🔥 OCR FUNCTION (for PDFs)
def extract_text_from_pdf(pdf_path):
    print("📄 Extracting text from PDF...")

    images = convert_from_path(pdf_path, poppler_path=POPPLER_PATH)

    text = ""
    for i, img in enumerate(images):
        print(f"➡️ Processing page {i+1}")
        text += pytesseract.image_to_string(img)

    return text


# 🚀 MAIN INGESTION
print("🚀 Starting ingestion...")

file_name = "Jarvis_Assets/gateReply.txt"   # 🔁 CHANGE THIS to your file (e.g., "nptel.pdf")

# 🔀 Handle TXT or PDF automatically
if file_name.endswith(".txt"):
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            text = f.read()
        print("✅ TXT file loaded")
    except Exception as e:
        print("❌ Error reading TXT file:", e)
        exit()

elif file_name.endswith(".pdf"):
    try:
        text = extract_text_from_pdf(file_name)
        print("✅ PDF text extracted")
    except Exception as e:
        print("❌ Error processing PDF:", e)
        exit()

else:
    print("❌ Unsupported file type")
    exit()


# 🧠 Chunking
if not text.strip():
    print("❌ No text extracted! (OCR failed or empty file)")
    exit()

chunks = chunk_text(text)
print(f"✅ Total chunks: {len(chunks)}")

# 📦 Prepare metadata
filenames = [file_name] * len(chunks)

# 💾 Store in DB
store_chunks(chunks, filenames)

print("🎉 Ingestion complete")