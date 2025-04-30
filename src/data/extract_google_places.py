import logging
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


def make_request(key: str, location: str, radius: int, type: str) -> list:
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
    resultados = dados.get("results", [])

    if dados.get("next_page_token"):
        get_next_page(dados, resultados, params)

    return resultados


def get_next_page(dados, resultados: list, params: dict):
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
        resultados.extend(dados.get("results", []))


data_path = Path("data")
processed_data = data_path / "processed" / "curitiba_bairros_offsets_2025-05.csv"
df = pd.read_csv(processed_data)

api_key = os.getenv("GOOGLE_PLACES_API_KEY")  ## TROCAR AQUI PELA SUA CHAVE DE API
radius = 1000  ## RAIO DA BUSCA EM METROS
type_of_place = "restaurant"  ## TIPO DE ESTABELECIMENTO A SER CONSIDERADO

# Configure logging simples
logging.basicConfig(level=logging.INFO)

restaurantes = []

for idx, location in enumerate(df["combined_coordinates"]):
    try:
        logging.info(f"Requesting location {idx+1}/{len(df)}: {location}")

        resultados = make_request(api_key, location, radius, type_of_place)
        restaurantes.extend(resultados)

        # Salvar incrementalmente após cada request
        pd.DataFrame(restaurantes).to_csv(
            data_path / "processed" / "restaurantes_parcial.csv", index=False
        )

        # pausa para evitar rate-limiting severo
        time.sleep(2)

    except requests.exceptions.RequestException as e:
        logging.error(f"Request falhou para {location}: {e}")
        continue
