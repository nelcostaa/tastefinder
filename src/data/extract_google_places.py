import os
import time

import requests
from dotenv import load_dotenv

## OBTEM A API DE UM ARQUIVO DENTRO DE .env
## ARQUIVO NÃO SUBIDO PARA GIT POR SEGURANÇÃ
## OBTER API KEY NO GOOGLE CLOUD PLACES E SUBSTITUIR NA VAR API_KEY
load_dotenv()

api_key = os.getenv("GOOGLE_PLACES_API_KEY")  ## TROCAR AQUI PELA SUA API_KEY
location = "-25.4284,-49.2733"  ## LOCALIZAÇÃO DE CURITIBA

radius = 50_000  ## RAIO DA BUSCA EM METROS
type_of_place = "restaurant"  ## TIPO DE ESTABELECIMENTO A SER CONSIDERADO

params = {
    "location": location,
    "radius": radius,
    "type": type_of_place,
    "key": api_key,
}

response = requests.get(
    "https://maps.googleapis.com/maps/api/place/nearbysearch/json", params=params
)

dados = response.json()
restaurantes = dados.get("results", [])

while dados.get("next_page_token"):
    ## CADA REQUEST RETORNA NO MÁXIMO 20 VALORES
    ## E AO FINAL UM TOKEN PARA IR PARA PRÓXIMA PÁGINA
    token = dados.get("next_page_token")
    time.sleep(2)  ## GOOGLE PLACES PEDE UMA PEQUENA PAUSA ENTRE REQUESTS
    params["pagetoken"] = token  ## ATUALIZA OS PARÂMETROS COM O TOKEN

    ## REQUESTS ACESSANDO A PRÓXIMA PÁGINA
    response = requests.get(
        "https://maps.googleapis.com/maps/api/place/nearbysearch/json", params=params
    )
    dados = response.json()
    restaurantes.extend(dados.get("results", []))

for r in restaurantes:
    print(r["name"])

print(len(restaurantes))
print(dados.get("next_page_token"))
