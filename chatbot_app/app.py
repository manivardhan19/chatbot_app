from flask import Flask, render_template, request, jsonify
from chatbot_logic import get_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get', methods=['POST'])
def get_bot_response():
    user_msg = request.form['msg']
    bot_resp = get_response(user_msg)
    return jsonify({'response': bot_resp})

if __name__ == '__main__':
    app.run(debug=True)
