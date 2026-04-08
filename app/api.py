from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.env import OpsGuardEnv
from app.models import Action

app = FastAPI(title="OpsGuardEnv")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

env = OpsGuardEnv(seed=42)


@app.get("/reset")
def reset(difficulty: str | None = None):
    obs, reward, done, info = env.reset(difficulty=difficulty)
    return {
        "observation": obs.model_dump(),
        "reward": reward,
        "done": done,
        "info": info,
    }


@app.post("/step")
def step(action: Action):
    obs, reward, done, info = env.step(action)
    return {
        "observation": obs.model_dump(),
        "reward": reward,
        "done": done,
        "info": info,
    }


@app.get("/state")
def state():
    return env.state().model_dump()