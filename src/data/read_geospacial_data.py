from pathlib import Path

import geopandas as gpd

path = Path("data/raw/DIVISA_DE_BAIRROS/")
shp_path = path / "DIVISA_DE_BAIRROS.shp"

gdf = gpd.read_file(shp_path)

gdf["centroid"] = gdf.geometry.centroid
print(gdf[["NOME", "geometry", "centroid"]].head())
