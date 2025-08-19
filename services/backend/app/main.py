from fastapi import FastAPI

app = FastAPI(title="SnapCal Backend Service")

@app.get("/")
def read_root():
    return {"status": "Backend service is running!"}