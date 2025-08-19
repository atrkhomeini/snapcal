from fastapi import FastAPI

app = FastAPI(title="SnapCal ML Inference Service")

@app.get("/")
def read_root():
    return {"status": "ML service is running!"}