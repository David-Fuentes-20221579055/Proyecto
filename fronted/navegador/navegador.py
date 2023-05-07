from dash import html
import dash_bootstrap_components as dbc

#Importar componentes gráficos
from .textocentral import textocentral
from .visualizacion import visualizacion
from .usuario import usuario

navegador = dbc.Container(
    [
        html.H1('Visualización de ensayos SPT'),#Titulo principal
        html.H3('Daniel Alexander Ruiz Hernández'),#Nombre
        html.H3('Henry David Fuentes Ortegón'),#Nombre
        dbc.Container([
            dbc.Row([
                dbc.Col(visualizacion, md=3),
                dbc.Col(textocentral, md=6),
                dbc.Col(usuario, md=3),
            ])
        ])

    ]
)