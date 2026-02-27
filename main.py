from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to Pokémon Info Fetcher API"}

@app.get("/pokemon/{pokemon_name}")
def get_pokemon(pokemon_name: str):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    
    response = requests.get(url)
    
    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="Pokémon not found")
    
    data = response.json()
    
    return {
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"],
        "types": [t["type"]["name"] for t in data["types"]]
    }