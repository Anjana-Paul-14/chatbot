from flask import Flask, request, render_template
import os
import openai 

app = Flask(__name__)

# Configure OpenAI API

openai.api_key = " "

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form["message"]
    
    prompt=f"User: {user_input}\nChat: "
    chat_history = []
    response = openai.Completion.create(    # Call OpenAI API to generate a response
    engine="text-davinci-002",
    prompt=prompt,
    temperature=0.5
    max_tokens=60,
    frequency_penalty=0,
    stop=["\nUser: ", "\nChat:"],
    )

    chatbot_response = response.choices[0].text.strip()

    chat_history.append(f"User: {user_input}\nChat: {chatbot_response}")
    
    return render_template('chat.html', user_input=user_input, chatbot_response=chatbot_response)
