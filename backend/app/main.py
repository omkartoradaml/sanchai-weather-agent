from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import os

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from app.weather import get_weather

# Load environment variables
load_dotenv()

app = FastAPI(title="Weather Agent API")

# -------------------------
# CORS (React → FastAPI)
# -------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # OK for internship task
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# LLM (OpenRouter)
# -------------------------
llm = ChatOpenAI(
    model="openai/gpt-4o-mini",
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1",
    temperature=0,
)

# -------------------------
# Prompt for city extraction
# -------------------------
city_prompt = ChatPromptTemplate.from_template(
    """
You are an assistant that extracts city names.

Return ONLY the city name.
If no city is found, return an empty string.

User query:
{query}
"""
)

city_chain = city_prompt | llm

# -------------------------
# Request schema
# -------------------------
class AskRequest(BaseModel):
    query: str


# -------------------------
# Routes
# -------------------------
@app.get("/")
def root():
    return {"message": "Weather Agent API running"}


@app.post("/ask")
def ask_weather(request: AskRequest):
    # 1️⃣ Extract city using LLM
    city_response = city_chain.invoke({"query": request.query})
    city = city_response.content.strip()

    if not city:
        return {"error": "Could not extract city from query"}

    # 2️⃣ Get weather using tool (OpenWeather API)
    weather = get_weather(city)

    if "error" in weather:
        return weather

    # 3️⃣ Structured response (frontend-friendly)
    return {
        "city": city,
        "weather": weather
    }


@app.get("/health")
def health():
    return {"status": "ok"}
