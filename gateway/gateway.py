from fastapi import FastAPI
import httpx
import json

app = FastAPI()

with open('services_config.json') as f:
    services = json.load(f)['services']

@app.get("/gateway/{service_name}")
async def gateway(service_name: str):
    if service_name not in services:
        return {"error": f"El servicio de '{service_name}' no está registrado"}

    service_url = services[service_name]['url']
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(service_url)
            data = response.json()
        except httpx.RequestError:
            return {"error": f"El servicio de {service_name} no está disponible"}
    
    return {"respuesta": data}

@app.get("/orquestar")
async def orquestar():
    async with httpx.AsyncClient() as client:
        try:
            respuesta_a = await client.get(services['samuel']['url'])
            data_samuel = respuesta_a.json()
        except httpx.RequestError:
            data_samuel = "El servicio de Samuel no está disponible"

    return {"respuesta__samuel": data_samuel}
