from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def predict():
    return {"mensaje": "Modelo en funcionamiento"}
