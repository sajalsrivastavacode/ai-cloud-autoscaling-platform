from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Cloud Auto Scaling Platform Running"}

@app.get("/load")
def generate_load():
    cpu_load = random.randint(1,100)
    return {"cpu_load": cpu_load}

@app.get("/health")
def health():
    return {"status": "healthy"}