from fastapi import FastAPI
from agent import Agent05
app = FastAPI(title="Code-Review-QA")
agent = Agent05()

@app.post("/execute")
async def execute(payload: dict):
    return agent.execute(payload)
