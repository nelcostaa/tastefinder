import os
import time
from pathlib import Path

import pandas as pd
import requests
from dotenv import load_dotenv

## OBTEM A API DE UM ARQUIVO DENTRO DE .env
## ARQUIVO NÃO SUBIDO PARA GIT POR SEGURANÇÃ
## OBTER API KEY NO GOOGLE CLOUD PLACES E SUBSTITUIR NA VAR API_KEY
load_dotenv()


def make_request(key: str, location: str, radius: int, type: str) -> object:
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

    if dados.get("next_page_token"):
        get_next_page(dados, restaurantes, params)

    return restaurantes


def get_next_page(dados, restaurantes: list, params: dict):
    while dados.get("next_page_token"):
        ## CADA REQUEST RETORNA NO MÁXIMO 20 VALORES
        ## E AO FINAL UM TOKEN PARA IR PARA PRÓXIMA PÁGINA
        token = dados.get("next_page_token")
        time.sleep(2)  ## GOOGLE PLACES PEDE UMA PEQUENA PAUSA ENTRE REQUESTS
        params["pagetoken"] = token  ## ATUALIZA OS PARÂMETROS COM O TOKEN

        ## REQUESTS ACESSANDO A PRÓXIMA PÁGINA
        response = requests.get(
            "https://maps.googleapis.com/maps/api/place/nearbysearch/json",
            params=params,
        )
        dados = response.json()
        restaurantes.extend(dados.get("results", []))


for r in restaurantes:
    print(r["name"])

data_path = Path("data")
processed_data = data_path / "processed" / "curitiba_bairros_offsets_2025-05.csv"
df = pd.read_csv(processed_data)

api_key = os.getenv("GOOGLE_PLACES_API_KEY")  ## TROCAR AQUI PELA SUA API_KEY
radius = 1500  ## RAIO DA BUSCA EM METROS
type_of_place = "restaurant"  ## TIPO DE ESTABELECIMENTO A SER CONSIDERADO

for location in df["coord_grouped"]:
    pass
