from flask import Flask
from routes.gemini_translate import gemini_bp

app = Flask(__name__)
app.register_blueprint(gemini_bp)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))  # Render가 지정한 포트 환경변수 사용
    app.run(host="0.0.0.0", port=port, debug=True)