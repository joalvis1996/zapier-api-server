from flask import Blueprint, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()
gemini_bp = Blueprint('gemini_translate', __name__)


@gemini_bp.route("/translate-snippet", methods=["POST"])
def translate():
    user_input = request.json.get("text")
    prompt = f"다음 영어 뉴스를 자연스럽고 간결한 한국어로 번역해줘:\n\n{user_input}"

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={os.getenv('GEMINI_API_KEY')}"
    body = {
        "contents": [{"role": "user", "parts": [{"text": prompt}]}]
    }

    res = requests.post(url, json=body)
    try:
        translated = res.json()["candidates"][0]["content"]["parts"][0]["text"]
    except Exception:
        return jsonify({"error": "Failed to parse Gemini response"}), 500

    return jsonify({"translated": translated})

