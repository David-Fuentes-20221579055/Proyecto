import dash
from dash import html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])


miVariable = dbc.Card(
    [
        dbc.CardHeader("Proyecto"),
        dbc.CardBody(
            [
                html.H5("¿Que desea realizar?", className="card-title"),#Titulo 2
                html.P(
                    "Selecciones una de las siguientes opciones",#Descripción
                    className="card-text",
                ),
                dbc.Button("Ingresar datos", color="primary"),
                html.Br(),html.Br(),
                dbc.Button("Consultar en linea", color="primary"),
            ]
        )
    ]
)

app.layout = dbc.Container(
    [  
        html.H1('Visualización de ensayos SPT'),#Titulo principal
        html.H3('Daniel Alexander Ruiz Hernández'),#Nombre
        html.H3('Henry David Fuentes Ortegón'),#Nombre
        html.Hr(),
        dbc.Row(
            [
                dbc.Col('Datos del proyecto', md=6 , style={'background-color':'blue'} ),#Columna para visualizar datos
                #dbc.Col('Datos del proyecto', md=6, style={'background-color':'red'}),
                dbc.Col(miVariable, md=12, style={'background-color':'green'}),
            ],
            align="center",
        )
    ],
    fluid=True
)



if __name__ == '__main__':
    app.run_server(debug=True)