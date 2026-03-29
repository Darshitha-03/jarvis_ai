from flask import Flask, request, jsonify, render_template
import os

from jarvis_core.generator import jarvis_answer
from jarvis_core.uploader import process_uploaded_file

app = Flask(__name__)

UPLOAD_FOLDER = "data"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    question = data["message"]

    result = jarvis_answer(question)
    return jsonify(result)


@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    process_uploaded_file(filepath)

    return jsonify({"message": f"{file.filename} uploaded and processed successfully"})


if __name__ == "__main__":
    app.run(debug=True)