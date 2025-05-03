import ast
from pathlib import Path

import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

raw_data = Path("data/raw")
restaurants_path = raw_data / "restaurantes_parcial.csv"

df = pd.read_csv(restaurants_path)

df_reduced = df.drop(
    columns=[
        "business_status",
        "icon",
        "icon_background_color",
        "opening_hours",
        "photos",
        "plus_code",
        "reference",
        "scope",
        "permanently_closed",
        "icon_mask_base_uri",
    ]
)

df_transformed = df_reduced.rename(columns={"vicinity": "address"})
df_transformed.drop_duplicates(inplace=True, subset="place_id")

df_transformed["geometry"] = df_transformed["geometry"].apply(ast.literal_eval)

df_transformed["latitude"] = df_transformed["geometry"].apply(
    lambda g: g["location"]["lat"]
)
df_transformed["longitude"] = df_transformed["geometry"].apply(
    lambda g: g["location"]["lng"]
)
df_transformed.drop(columns=["geometry"], inplace=True)

# Crie a engine
engine = create_engine("postgresql://nelson:senha_segura@localhost:5432/tastefinder")

# Carregue o DataFrame
df_transformed.to_sql(
    name="restaurants",
    con=engine,
    schema="tastefinder",
    if_exists="append",
    index=False,
    dtype={"types": sqlalchemy.types.JSON},
)
