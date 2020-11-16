
from dash import Dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import base64


ds4a_image = base64.b64encode(open('./static/logo_0001_epm.png', 'rb').read())
LOGO = base64.b64encode(open('./static/Logo-Juancho-1.png', 'rb').read())
ds4aboth = base64.b64encode(open('./static/generic-ds4a-c1-logo.png', 'rb').read())

layout_index = html.Div(className='row', style = {'width': '100%'}, children=[  ### whole page

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
    html.Div(style = {'width': '75%', 'backgroundColor': '#1A1A1D'},

                children=[

                #ROW FOR VIDEO
                
                dbc.Row(style = {'width': '100%'}, children= [
                    dbc.Col(style={'textAlign': 'center'},
                        children=[
                            html.Br(),  
                            dbc.Col(children=[
                                html.H1("Sewers Rover", 
                                style={'color': '#61892F', 'margin-left': 10, 'font-family': 'Enriqueta', 'line-height': '1.25', 'margin': '0 0 10px', 'font-size': '35px', 'font-weight': 'bold' })]),
                            html.Br(),
                            dbc.Col(children=[
                                html.H1("Using artificial vision, more specifically the use of convolutional neural networks and the YOLO algorithm, we created a model capable of detecting structural flaws (holes, specifically) in the sewers of the city of Medellin, Colombia. This model would allow the automation of this process for Empresas Publicas de Medellin (EPM)", 
                                style={'color': '#474B4F', 'margin-left': 10, 'font-family': 'Enriqueta', 'line-height': '1.25', 'margin': '0 0 10px', 'font-size': '20px', 'font-weight': 'bold' })])
                            ]), 
                            
                            dbc.Col(style={'textAlign': 'center', 'with':'60%'},
                                children=[
                                    html.Br(),
                                    html.Iframe(src="https://www.youtube.com/embed/akZQXlQQjj8", height='300px', width='500px', 
                                        style = {'border': '5px solid hsla(0,0%,100%,.5)', 'background-clip': 'padding-box'}),  
                            ])   
                ]), 

                #ROW FOR DRAG AND DROP
                html.Div(style = {'align-items': 'center','justify-content': 'center', 'display': 'flex'}, children = [
                dbc.Col(style = {'align-items': 'center','justify-content': 'center', 'display': 'flex', 'with':'100%', 'height':'300px'},
                    children =[

                        dcc.Upload(
                        id='upload-image',
                        children=html.Div([
                            html.A(html.H5('Click here and select the images to start the App', 
                            style = {'color': '#61892F', 'margin-top': '10px',
                                        'margin-right':'10px',
                                        'margin-bottom':'10px',
                                        'margin-left':'10px'}))
                        ]),
                        style={
                            'borderStyle': 'dashed',
                            'borderRadius': '10px',
                            'textAlign': 'center',
                            'border-color' : '#6B6E70'
                        },multiple=True),
                        #OBJETO DE CARGA UNO
                        html.Div(id="hidden_div_for_redirect_callback"),
                    ]
                ) 

            ])])
])
