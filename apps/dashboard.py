
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd
import base64
import plotly.graph_objs as go



ds4a_image = base64.b64encode(open('./static/logo_0001_epm.png', 'rb').read())
LOGO = base64.b64encode(open('./static/Logo-Juancho-1.png', 'rb').read())
ds4aboth = base64.b64encode(open('./static/generic-ds4a-c1-logo.png', 'rb').read())


layout_dashboard = html.Div(className='row',  style = {'width': '100%'}, children=[  ### whole page

    #hidden div for trigger dashboard functions 

    html.Div(id = 'hidden-div-dashboard'),


    #LEFT PART
    html.Div(style={'backgroundColor': '#222629', 'width': '24.9%'}, 
    
    children=[
        #IMAGES OF CORRELATION AND EPM
        dbc.Row(children= [
            dbc.Col(style={'textAlign': 'center'},
                children=[  
                    html.Img(src='data:image/png;base64,{}'.format(LOGO.decode()), style = {'height': '90%','width': '90%'})

            ]), 
            dbc.Col(style={'textAlign': 'center'},
                children=[  
                    html.Img(src='data:image/png;base64,{}'.format(ds4a_image.decode()))

            ])
            
        ]),

        #SALTO DE LINEA
        html.Br(),
        #AUTOMATED DETECTION OF FAULTS IN WASTEWATER PIPES

        #NAMES OF PEOPLE IN THE GROUP
        dbc.Row(children=[
            dbc.Col(
                style={
                'textAlign': 'center',
                'text': '#37414B'},
                children=[ 

                    dbc.Col(children=[
                        html.H3("AUTOMATIC FAULT DETECTION IN SEWER SYSTEMS", 
                        style={
                        'color': '#61892F', 'margin-left': 10, 'font-family': 'Enriqueta', 'line-height': '1.25', 'margin': '0 0 10px', 'font-size': '20px', 'font-weight': 'bold' })]),

                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    dbc.Col(children=[
                        html.H4("Carolina Florez, Andres Florez, Johan  Lopez, Juan Jurado, Angel Racini, Yeis Taborda, Santiago Uribe", style={
                        'color': '#474B4F', 'margin-left': 20, 'font-family': 'Enriqueta', 'line-height': '1.25', 'margin': '0 0 10px', 'font-size': '20px', 'font-weight': 'bold', 'with':'90%'})]),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Img(src='data:image/png;base64,{}'.format(ds4aboth.decode())),
                    html.Br()
                ])
            ])
        ]),


    html.Div(style = {'width': '0.1%'}),  


    #RIGHT PART
    html.Div(style = {'width': '75%', 'backgroundColor': '#1A1A1D'}, children=[
                html.Div([#BOTON DE REGRESAR AL INICIO
                dbc.Row(html.Div(children = [
                    html.Button('Return to start', id='btn-nclicks-1', n_clicks=0, className="btn btn-dark",
                    style = {
                    'color':'#222629',
                    'text-transform': 'uppercase',
                    'padding': '20px',
                    'display': 'inline-block',
                    'border': 'none',
                    'transition': 'all 0.4s ease 0s',
                    'margin-left': '50px', 
                    'font-family': 'Enriqueta', 'line-height': '1.25', 
                    'font-size': '15px', 
                    'font-weight': 'bold', 'with':'60%'
                    }),
                    html.Div(id='return-to-index')
                ])),

                html.Div(children = [

                    html.Br(),
                    dbc.Row(style = {
                        'float': 'left',
                        'width': '100%'
                    }
                    , children = [
                        dbc.Col(style = {'width': '50%'}, children = [
                            dbc.Row(style = {'width': '100%'} , children=[
                                dbc.Col(style = {'height':'280px', 'width':'470px', }, children = [
                                    dcc.Graph(id = 'plot1', figure={'layout': go.Layout(
                                        paper_bgcolor = 'rgba(0,0,0,0)',
                                        plot_bgcolor = 'rgba(0,0,0,0)')}
                                    )
                                ])
                            ])
                        ]),

                        dbc.Col(style = {'textAlign': 'center','width': '50%'}, children= [
                        
                                html.Iframe(src="https://www.youtube.com/embed/7aofO9OcQ_8", 
                                height='280px', width='470px', style = {'border': '5px solid hsla(0,0%,100%,.5)', 'background-clip': 'padding-box'}),
                    
                        ]),

                ]),

                html.Br(),
                html.Br(),
                
                dbc.Row(style = {
                        'float': 'left',
                        'width': '100%'}
                , children = [
                    html.Br(),
                    dbc.Col(style = {'width': '50%', 'textAlign': 'center'}, children = [
                            html.Div(style={"maxHeight": "350px", "overflow": "scroll", 'float':'left', 'display':'inline', 'scrollbar-color': '#222629'}, 
                                id ='output-images')
                    ]),
                    html.Br(),
                    dbc.Col(style = {'width': '50%', 'textAlign': 'center'}, children= [
                                html.Div(style={"maxHeight": "350px", "overflow": "scroll", 'scrollbar-color': '#222629'},
                                id ='output-table')
                                #ELEMENTO DE VISUALIZACION
                    ]),

                ]),
            ])   
    ]),])
])