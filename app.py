from flask import Flask, request, render_template
import os
import openai 

app = Flask(__name__)

# Configure OpenAI API
#  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
openai.api_key = "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"

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
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7,
        top_p=None,
        frequency_penalty=None,
        presence_penalty=None,
        log_level=None
    )

    chatbot_response = response.choices[0].text.strip()
    
    return render_template('chat.html', user_input=user_input, chatbot_response=chatbot_response)
