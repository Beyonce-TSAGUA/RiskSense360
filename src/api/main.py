from fastapi import FastAPI

app = FastAPI(title="RiskSense360 API")

@app.get("/")
def home():
    return {"message": "RiskSense360 API is running."}
