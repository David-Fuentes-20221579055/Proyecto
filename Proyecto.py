import dash
from dash import html
import dash_bootstrap_components as dbc

#import fronted
from fronted.navegador.navegador import navegador
from fronted.izquierda.izquierda import izquierda
from fronted.derecha.derecha import derecha

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = dbc.Container( #Divisiones de la página
    [  
        dbc.Row(
            [
                dbc.Col(navegador, md=12 , style={'background-color':'Orange'} ),
                dbc.Col("  MAPA  Y PDF DE VISUALIZACIÓN, van en la parte izquierda, pero los trabajamos por separado en el momento ", md=8, style={'background-color':'moccasin'}),
                dbc.Col(derecha, md=4, style={'background-color':'navajowhite'}),
            ]
        ),
        
    ]
    
)



if __name__ == '__main__':
    app.run_server(debug=True)