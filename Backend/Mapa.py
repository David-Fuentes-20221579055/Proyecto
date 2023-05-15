import geopandas as gpd
import plotly.express as px


#importamos el archivo de departamentos
departamentos = gpd.read_file('data/Departamentos.zip')
departamentos_4326 = departamentos.to_crs(epsg=4326)

# Genera una figura a partir de los datos de geojson
fig = px.choropleth_mapbox(
    # departamentos_4326,
    geojson=departamentos_4326.geometry,
    locations=departamentos_4326.index
)

# agregamos el mapa
fig.update_layout(
    mapbox_style="open-street-map",
    mapbox_zoom=5,
    mapbox_center = {"lat": 4.6, "lon": -74},
)
