import math
from pathlib import Path

import geopandas as gpd
from shapely.geometry import Point

path = Path("data/raw/DIVISA_DE_BAIRROS/")
shp_path = path / "DIVISA_DE_BAIRROS.shp"

gdf = gpd.read_file(shp_path)

gdf["centroid"] = gdf.geometry.centroid
print(gdf[["NOME", "geometry", "centroid"]].head())


def offset_points(point: Point, distance: float, angle_deg: float) -> Point:
    """
    Gera um novo Point deslocado do original:
      - point: Point em CRS métrico (x, y em metros)
      - distance: deslocamento em metros
      - angle_deg: ângulo em graus (0=leste, 90=norte)
    """
    rad = math.radians(angle_deg)

    distance_x = distance * math.cos(rad)
    distance_y = distance * math.sin(rad)

    point_x = point.x + distance_x
    point_y = point.y + distance_y

    return Point(point_x, point_y)


for centro in gdf["centroid"]:
    pontos = [offset_points(centro, 3000, ang) for ang in (0, 120, 240)]


print(pontos)
