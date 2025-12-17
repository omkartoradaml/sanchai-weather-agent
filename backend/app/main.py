from fastapi import FastAPI
from dotenv import load_dotenv
import os

from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType

from app.tools import weather_tool

# Load environment variables
load_dotenv()

app = FastAPI()

# Initialize LLM (OpenRouter via LangChain)
llm = ChatOpenAI(
    model=os.getenv("OPENROUTER_MODEL"),
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1"
)

# Initialize Agent
agent = initialize_agent(
    tools=[weather_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# --------------------
# Health Check
# --------------------
@app.get("/health")
def health():
    return {"status": "ok"}

# --------------------
# LLM Test Endpoint
# --------------------
@app.get("/llm-test")
def llm_test():
    response = llm.invoke("Say hello in one short sentence")
    return {"response": response.content}

# --------------------
# Agent Endpoint (MAIN FEATURE)
# --------------------
@app.get("/ask")
def ask(query: str):
    """
    Accepts natural language query.
    If weather-related, agent uses weather tool.
    """
    answer = agent.run(query)
    return {"answer": answer}
