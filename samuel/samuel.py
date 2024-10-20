from fastapi import FastAPI

app = FastAPI()

@app.get("/samuel")
async def servicio_a():
    return {"mensaje": "Respuesta desde el Servicio de Samuel en Python"}