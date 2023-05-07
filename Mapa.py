from dash import html
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import dash
import dash_core_components as dcc
import dash_html_components as html

# Define la latitud y longitud de la coordenada que quieres mostrar
latitud = 4.624335
longitud = -74.063644

# Crea la figura del mapa de Colombia y agrega la marca en la coordenada
fig = go.Figure(go.Scattermapbox(
    lat=[latitud],
    lon=[longitud],
    mode='markers',
    marker=go.scattermapbox.Marker(
        size=14
    ),
    text=['Tu ubicación']
))

fig.update_layout(
    mapbox=go.layout.Mapbox(
        accesstoken='tu_token_mapbox', # reemplaza con tu propio token de Mapbox
        center=go.layout.mapbox.Center(
            lat=4.5709,
            lon=-74.2973
        ),
        zoom=8
    )
)

# Crea la aplicación Dash
app = dash.Dash(__name__)

# Define la estructura de la página
app.layout = html.Div([
    dcc.Graph(id='mapa-colombia', figure=fig)
])

# Ejecuta la aplicación Dash
if __name__ == '__main__':
    app.run_server(debug=True)
