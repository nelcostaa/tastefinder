import math
from pathlib import Path

import geopandas as gpd
from shapely.geometry import Point

data_path = Path("data")

shp_path = data_path / "raw" / "DIVISA_DE_BAIRROS_SIRGAS" / "DIVISA_DE_BAIRROS.shp"

gdf = gpd.read_file(shp_path)

gdf["centroid"] = gdf.geometry.centroid


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


gdf["offset_points"] = gdf["centroid"].apply(
    lambda c: [offset_points(c, 1000, ang) for ang in (0, 120, 240)]
)


gdf_offsets = gdf.explode("offset_points")
gdf_offsets = gdf_offsets.set_geometry("offset_points")

gdf_offsets.crs = gdf.crs
gdf_offsets = gdf_offsets.to_crs(epsg=4326)

gdf_offsets["longitude"] = gdf_offsets["offset_points"].geometry.x
gdf_offsets["latitude"] = gdf_offsets["offset_points"].geometry.y

processed_path = data_path / "processed" / "curitiba_bairros_offsets_2025-05.csv"
gdf_offsets.to_csv(processed_path, index=False)
