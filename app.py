
from flask import Flask, request, jsonify
from flask_cors import CORS
import pytesseract
from PIL import Image
import io
import openai
import os

app = Flask(__name__)
CORS(app)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/solve", methods=["POST"])
def solve_mcq():
    if "image" not in request.files:
        return jsonify({"error": "No image provided"}), 400

    image = Image.open(request.files["image"].stream)
    text = pytesseract.image_to_string(image)

    prompt = f"একটি MCQ প্রশ্ন সলভ করো এবং সঠিক উত্তর বলো:
{text}

উত্তর:"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "তুমি একজন বুদ্ধিমান AI যে MCQ প্রশ্নের সঠিক উত্তর বলে।"},
                {"role": "user", "content": prompt},
            ],
        )
        answer = response["choices"][0]["message"]["content"]
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
