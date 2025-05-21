from flask import Flask
from routes.gemini_translate import gemini_bp

app = Flask(__name__)
app.register_blueprint(gemini_bp)

if __name__ == "__main__":
    app.run(debug=True)