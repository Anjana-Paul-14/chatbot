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
    user_input = request.form['user_input']
    
    # Call OpenAI API to generate a response
    response = openai.Completion.create(
    engine="davinci",
    prompt=user_input,
    max_tokens=20,
    n=1,
    stop=None,
    temperature=0.2
    )

    chatbot_response = response.choices[0].text.strip()
    
    return render_template('chat.html', user_input=user_input, chatbot_response=chatbot_response)
