from flask import Flask, request, render_template
import os
import openai 
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy


load_dotenv()

# Configure OpenAI API
openai.api_key = os.environ["OPENAI_API_KEY"]

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chat_history.db'
db = SQLAlchemy(app)


class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_input = db.Column(db.String(255), nullable=False)
    chatbot_response = db.Column(db.String(255), nullable=False)
# Create the database tables
db.create_all()


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
    temperature=0.5,
    max_tokens=60,
    frequency_penalty=0,
    stop=["\nUser: ", "\nChat:"],
    )

    chatbot_response = response.choices[0].text.strip()

    # chat_history.append(f"User: {user_input}\nChat: {chatbot_response}")
    
    return render_template('chat.html', user_input=user_input, chatbot_response=chatbot_response)
