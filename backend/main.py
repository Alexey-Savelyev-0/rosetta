from flask import Flask, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = "your-api-key"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=data['messages']
    )
    return jsonify(response['choices'][0]['message']['content'])


def create_chat_response(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response['choices'][0]['message']['content']



if __name__ == '__main__':
    app.run(debug=True)