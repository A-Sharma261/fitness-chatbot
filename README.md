# Fitness Chatbot

A simple AI-powered fitness chatbot that gives beginner-friendly fitness guidance using the Gemini API.

Users can ask questions about workouts, exercise explanations, cardio, mobility, recovery, and general fitness habits. The chatbot is designed to be friendly, practical, and easy to use.

## Features

- AI-powered fitness chatbot
- Gemini API integration
- FastAPI backend
- Simple HTML, CSS, and JavaScript frontend
- Conversation history for follow-up questions
- Fitness-focused chatbot instructions
- Basic safety checks for health or injury-related messages
- Beginner-friendly responses

## Tech Stack

### Backend

- Python
- FastAPI
- Uvicorn
- Pydantic
- python-dotenv
- Google GenAI SDK

### Frontend

- HTML
- CSS
- JavaScript

### AI Model

- Gemini 2.5 Flash Lite

## Project Structure

```text
fitness-chatbot/
├── backend/
│   ├── app/
│   │   ├── chatbot.py
│   │   ├── config.py
│   │   ├── main.py
│   │   ├── prompt.py
│   │   ├── safety.py
│   │   └── schemas.py
│   └── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── .gitignore
└── README.md


How It Works
User types a message
→ Frontend sends the message to the backend
→ Backend checks for basic safety concerns
→ Backend sends the message and conversation history to Gemini
→ Gemini generates a fitness-focused response
→ Backend sends the response back to the frontend
→ Frontend displays the chatbot's answer
Getting Started
1. Clone the Repository
git clone YOUR_REPOSITORY_URL
cd fitness-chatbot
2. Set Up the Backend

Go into the backend folder:

cd backend

Create a virtual environment:

python -m venv .venv

Activate the virtual environment.

For Windows:

.venv\Scripts\activate

For Mac/Linux:

source .venv/bin/activate

Install the required packages:

pip install -r requirements.txt
3. Add Your Gemini API Key

Inside the backend folder, create a file called:

.env

Add your Gemini API key:

GEMINI_API_KEY=your_gemini_api_key_here

Do not share your API key or upload the .env file to GitHub.

4. Run the Backend

From inside the backend folder, run:

uvicorn app.main:app --reload

If it works, the backend will run at:

http://127.0.0.1:8000

You can test the backend by opening:

http://127.0.0.1:8000

You should see a message saying the backend is running.

You can also test the chatbot API at:

http://127.0.0.1:8000/docs
5. Run the Frontend

Keep the backend running.

Open this file in your browser:

frontend/index.html

Now you can type a fitness question and chat with the bot.

Example Questions

Try asking:

Give me a beginner 3-day gym workout plan.
Explain progressive overload in simple terms.
What is a good warm-up before leg day?
Can you make me a home workout with no equipment?
How much rest should I take between sets?
What is the difference between strength training and hypertrophy training?
Safety Note

This chatbot gives general fitness information only.

It does not:

diagnose medical conditions
treat injuries
replace a doctor
replace a physiotherapist
replace a dietitian
provide medical advice
recommend steroids or performance-enhancing drugs
give extreme rapid weight-loss advice

If you have pain, an injury, a medical condition, or any health concern, speak with a qualified health professional.

Current Limitations

This is an early version of the project.

Current limitations include:

no user accounts
no database
no saved chat history after refreshing the page
no deployed online version yet
basic keyword-based safety checks
simple frontend design
Future Improvements

Possible future improvements include:

reset chat button
improved frontend design
loading animation
workout plan form
user profile inputs
persistent chat history
custom fitness knowledge base
better safety filtering
test suite
online deployment
Development Notes

If the chatbot is not responding, check that:

the backend is running
the Gemini API key is inside backend/.env
the backend URL is http://127.0.0.1:8000
the frontend is sending requests to /chat
dependencies were installed with pip install -r requirements.txt

Before pushing to GitHub, make sure .env is not being committed.

Disclaimer

This project is for general fitness education and learning purposes only. It is not a medical tool and should not be used as a replacement for professional health advice.