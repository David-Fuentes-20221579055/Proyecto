import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

# Definir los datos de prueba (en lugar de cargar datos reales de una base de datos)
datos_ensayos = pd.DataFrame({
    'Localización': ['A', 'B', 'C'],
    'Profundidad (m)': [0, 1, 2],
    'Resistencia (kg/cm2)': [50, 100, 150],
    'Fecha': ['01-01-2022', '02-01-2022', '03-01-2022']
})

# Crear la aplicación Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Definir el contenido de la página
app.layout = dbc.Container([
    html.H1('Visualización de ensayos de SPT'),
    html.Hr(),
    dbc.Row([
        # Sección de mapa interactivo
        dbc.Col([
            html.H2('Mapa interactivo'),
            dcc.Graph(id='mapa')
        ], md=6),
        # Sección de información del ensayo seleccionado
        dbc.Col([
            html.H2('Información del ensayo'),
            html.Div(id='info-ensayo')
        ], md=6)
    ]),
    html.Hr(),
    # Sección de almacenamiento de archivos PDF
    html.H2('Almacenamiento de archivos PDF'),
    dbc.Form([
        dbc.FormGroup([
            dbc.Label('Localización'),
            dbc.Input(type='text', placeholder='Ingrese la localización del ensayo')
        ]),
        dbc.FormGroup([
            dbc.Label('Profundidad (m)'),
            dbc.Input(type='number', placeholder='Ingrese la profundidad del ensayo')
        ]),
        dbc.FormGroup([
            dbc.Label('Resistencia (kg/cm2)'),
            dbc.Input(type='number', placeholder='Ingrese la resistencia del ensayo')
        ]),
        dbc.FormGroup([
            dbc.Label('Fecha'),
            dbc.Input(type='date', placeholder='Ingrese la fecha del ensayo')
        ]),
        dbc.Button('Generar PDF', color='primary', block=True)
    ])
])

# Definir la lógica de la aplicación
@app.callback(
    dash.dependencies.Output('mapa', 'figure'),
    [dash.dependencies.Input('mapa', 'clickData')])
def actualizar_mapa(clickData):
    if clickData is not None:
        # Obtener la localización seleccionada en el mapa y mostrar los datos del ensayo correspondiente
        localizacion = clickData['points'][0]['location']
        ensayo = datos_ensayos[datos_ensayos['Localización'] == localizacion].iloc[0]
        return px.scatter_mapbox(
            datos_ensayos, lat='Latitud', lon='Longitud', hover_data=['Localización', 'Profundidad (m)', 'Resistencia (kg/cm2)', 'Fecha']
        ).update_traces(marker=dict(size=10))
    else:
        # Mostrar el mapa sin ningún punto seleccionado
        return px.scatter_mapbox(
            datos_ensayos, lat='Latitud', lon='Longitud', hover_data=['Localización', 'Profundidad (m)', 'Resistencia (kg/cm)'])
