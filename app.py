from flask import Flask, request, jsonify, render_template
from jarvis_core.generator import jarvis_answer

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    question = data["message"]

    print("USER QUERY:", question)

    result = jarvis_answer(question)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
