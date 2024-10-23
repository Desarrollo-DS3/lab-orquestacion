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
            
        try:
            respuesta_j = await client.get(services['juan']['url'])
            data_juan = respuesta_j.json()
        except httpx.RequestError:
            data_juan = "El servicio de Juan no está disponible"
            
        try:
            respuesta_john = await client.get(services['john']['url'])
            data_john = respuesta_john.json()
        except httpx.RequestError:
            data_samuel = "El servicio de John no está disponible"

        try:
            respuesta_duque = await client.get(services['duque']['url'])
            data_duque = respuesta_duque.json()
        except httpx.RequestError:
            data_duque = "El servicio de Duque no está disponible"
            
        try:
            respuesta_jr = await client.get(services['julian']['url'])
            data_julian = respuesta_jr.json()
        except httpx.RequestError:
            data_julian = "El servicio de Julian no está disponible"

        try:
            respuesta_sebastian = await client.get(services['sebastian']['url'])
            data_sebastian = respuesta_sebastian.json()
        except httpx.RequestError:
            data_sebastian = "El servicio de Sebastian no está disponible"

        return {
            "respuesta__samuel": data_samuel,
            "respuesta__juan": data_juan,
            "respuesta__john": data_john,
            "respuesta__duque": data_duque,
            "respuesta__julian": data_julian,
            "respuesta__sebastian": data_sebastian
        }
