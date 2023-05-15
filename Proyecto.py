#Se importan las librerias necesarias para la aplicación
import dash #Para construir aplicaciones web con Dash
from dash import html, dcc #Para crear los componentes HTML y Dash 
import dash_bootstrap_components as dbc #Para agregar estilos
import geopandas as gpd #Para trabajar datos geoespaciales
import plotly.express as px #generar la visualización de datos

#importar el fronted y Backend 
from fronted.navegador.navegador import navegador
from fronted.izquierda.izquierda import izquierda
from fronted.derecha.derecha import derecha
from Backend.Mapa import fig
#Se crea una instancia de la aplicación Dash y se agrega el estilo Bootstrap
app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = dbc.Container( #Divisiones de la página, define la estructura de la aplicación
    [  
        dbc.Row(
            [
                dbc.Col(navegador, md=12 , style={'background-color':'Orange'} ),
                dbc.Col( 
                dcc.Graph(figure=fig,
                 style={'width': '100%', "height": "600px"}),),
                dbc.Col(derecha, md=4, style={'background-color':'navajowhite'}),
                dbc.Col(" La página web permitirá a los usuarios visualizar ensayos de SPT (Standard Penetration Test) de diferentes localizaciones y almacenar archivos en formato PDF con información sobre los ensayos. ", md=8, style={'background-color':'moccasin'}),
            ]
        ),
        
    ],
    fluid=True
    
)

#Se inicia el servidor de la aplicación.

if __name__ == '__main__':
    app.run_server(debug=True)