from fastapi import FastAPI
from app.main import detect_disease

app = FastAPI(title="Plant Disease MCP API")


@app.get("/")
def root():
    return {"message": "Plant Disease MCP API running......."}


@app.post("/analyze")
async def analyze(bucket: str, key: str):
    result = await detect_disease(bucket, key)
    return {"status": "success", "result": result}
