import dash
from dash import html
import dash_bootstrap_components as dbc


derecha = dbc.Container(
    [
        html.H2('Datos del proyecto'),
        html.Hr(),
        html.Label('Nombre del proyecto'),
        dbc.Input(id='nombreProyecto', placeholder='Nombre del proyecto', type='text', value='Nombre'),
        html.Label('Localización'),
        dbc.Input(id='localizacion', placeholder='Localización', type='text', value='Ingerese la localización'),
        html.Label('Fecha inicicio:'),
        dbc.Input(value="Fecha", type="date"),
        html.Label('Fecha Fin:'),
        dbc.Input(value="Fecha", type="date"),
    ]
)