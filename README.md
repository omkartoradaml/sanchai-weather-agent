# AI Weather Assistant

This project is a simple full-stack weather assistant built as part of an internship-style assignment.  
Users can ask weather-related questions in natural language, and the system responds with real-time weather details for the requested city.

The objective of this project is to demonstrate full-stack development skills along with a basic understanding of Agentic AI concepts using LangChain.

---

## Project Overview

- Accepts natural language weather queries from users
- Extracts city names from the user input using an LLM
- Fetches real-time weather data from an external API
- Displays weather details in a structured and user-friendly format
- Implements a clean frontend and a modular backend

---

## Key Features

- Natural language weather queries
- City extraction using LangChain
- Real-time weather information
- Structured JSON response from backend
- React-based frontend interface
- Glass-style card UI
- Interactive map background using OpenStreetMap
- FastAPI backend with Swagger documentation

---

## Technology Stack

### Frontend
- React (Vite)
- JavaScript
- CSS
- Leaflet
- OpenStreetMap

### Backend
- Python
- FastAPI
- LangChain
- OpenRouter (LLM integration)
- OpenWeather API

---

## High-Level Working Flow

- User enters a weather-related question in the frontend
- The query is sent to the FastAPI backend
- LangChain with an LLM extracts the city name from the query
- Backend calls the OpenWeather API using the extracted city
- Weather data is returned in a structured format
- Frontend displays the temperature and weather condition

This project follows a simple Agent and Tool interaction pattern.

---

## Running the Project Locally

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload


Backend will be available at:

http://127.0.0.1:8000

Swagger documentation:

http://127.0.0.1:8000/docs


Frontend Setup
cd frontend
npm install
npm run dev


Frontend will be available at:

http://localhost:5173


Author

Omkar Toradmal

B.Tech – Computer Engineering

Notes

This project is developed for learning and internship evaluation purposes

Sensitive data such as API keys are managed using environment variables

The focus of this project is on clarity, correctness, and practical implementation
