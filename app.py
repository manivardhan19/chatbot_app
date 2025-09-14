from flask import Flask, request
from chatbot_logic import get_response

app = Flask(__name__)

@app.route("/")
def home():
    
    with open("index.html", encoding="utf-8") as f:
        return f.read()

@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')
    return get_response(user_text)

if __name__ == "__main__":
    app.run(debug=True)
