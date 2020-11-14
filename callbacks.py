#System Dependencies
import base64

#Dash dependencies
import dash
import dash_table
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go

import pandas as pd
import numpy as np
import cv2

#AZURE BUCKETS
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

from yolov3 import Create_Yolov3
from utils import detect_image, Load_Yolo_model

from app import app
from apps import dashboard, index

yolo = Create_Yolov3(input_size= 416, CLASSES="./model_data/license_plate_names.txt")
yolo.load_weights("./checkpoints/yolov3_custom") # use keras weights

connect_str = "DefaultEndpointsProtocol=https;AccountName=epmnprgdevilabdiag;AccountKey=9TtF46i87zM7ZR52hCOvC2L8PFrKM7yslk4DdYSt7DNmlrXF+iUpbHtqJXnGdAAWA/gnzOjNrwTzfqTQpy2xWQ==;EndpointSuffix=core.windows.net"

#IMAGE UPLOAD
@app.callback(Output("hidden_div_for_redirect_callback", "children"),
              [Input('upload-image', 'contents')],
              [State('upload-image', 'filename'),
               State('upload-image', 'last_modified')])
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        #Conect to BLOB STORAGE
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)
        container_client = blob_service_client.get_container_client("pruebasds4")

        #ELIMINAR TODAS LAS IMAGENES EN EL CONTENEDOR DE BLOB STORAGE SI LAS HAY

        my_blobs = container_client.list_blobs()

        #BATCH SIZE LIMITATIONS ON DELETE

        blobs_list = [b.name for b in my_blobs]
        blobs_length = len(blobs_list)

        if blobs_length >= 256:

            start=0
            end=256

            while end <= blobs_length:
                container_client.delete_blobs(*blobs_list[start:end])
                start = start + 256
                end = end + 256
                if start < blobs_length and end > blobs_length:
                    container_client.delete_blobs(*blobs_list[start:blobs_length])
        else:
            container_client.delete_blobs(*blobs_list)


        #SUBIR TODAS LAS IMAGENES AL CONTENEDOR
  
        for image , name, _ in zip(list_of_contents, list_of_names, list_of_dates):
            if 'jpg' in name:
                #decoding image
                _ , content_string = image.split(',')
                #decoded = base64.b64decode(content_string)
                container_client.upload_blob(name=name, data=content_string)
                
        return dcc.Location(pathname="/dashboard", id="url")
            
                


#BOTON DE REGRESAR AL INICIO
@app.callback(Output('return-to-index', 'children'),
              [Input('btn-nclicks-1', 'n_clicks')])
def displayClick(btn1):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'btn-nclicks-1' in changed_id:
        return dcc.Location(pathname="/", id="url")



#This function generates all the image list after pass in the model
def generate_thumbnail(image):
    return html.Img(
            src=image,
            style = {
                'height': '50%',
                'width': '50%',
                'float': 'center',
                'position': 'relative',
                'padding-top': '10px',
                'padding-right': '10px'
            }
        )

def generate_table(dataframe):
    return dash_table.DataTable(
            id='table-uploading',
            data= dataframe.to_dict('records'),
            columns=[{"name": i, "id": i} for i in dataframe.columns],
            sort_action='native', 
            style_as_list_view=True,
            style_table= {'margin-left':'15px'},
            style_header={'backgroundColor': '#222629', 'color':'#61892F', 'font-family': 'Enriqueta', 'line-height': '1.25', 'margin': '0 0 10px', 'font-size': '15px', 'font-weight': 'bold', 'textAlign': 'left'},
            style_cell={
                'backgroundColor': '#1A1A1D',
                'color': '#474B4F', 'font-family': 'Enriqueta', 'line-height': '1.25', 'margin': '0 0 10px', 'font-size': '13px', 'font-weight': 'bold', 'textAlign': 'center'},
            style_data_conditional=[
            {
                'if': {
                    'filter_query': '{taken} = 1',
                    'column_id': 'taken',
                },
                'backgroundColor': 'dodgerblue',
                'color': 'white'
            }, 
            {
                'if': {
                    'filter_query': '{taken} = 1', # comparing columns to each other
                    'column_id': 'order_id'
                },
                'backgroundColor': '#3D9970'
            }]
        )


def change_classname(x):
    #Change class_names
    if x == 0:
        return 'RA'
    elif x== 1:
        return 'HU'
    else:
        return 'DE'



#CALLBACK FOR THE MODEL INPUTS AND OUTPUTS
@app.callback([Output("output-images", "children"), Output("output-table", "children"), Output("plot1", "figure")],
              [Input('hidden-div-dashboard', 'content')])
def update_dashboard(generate_dashboard):
    #Download all the images from blob storage and processing with deeplearning model
    images_div = []
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    container_client = blob_service_client.get_container_client("pruebasds4")
    my_blobs = container_client.list_blobs()

    #Column name list
    column_names = ['id', 'x1', 'y1', 'x2' , 'y2', 'Score', 'Class']
    #row list
    rows = []
    names = []
    images = []

    for blob in my_blobs:
        image_downloaded = container_client.download_blob(blob.name).readall()
        decoded_data = base64.b64decode( image_downloaded )
        np_data = np.fromstring(decoded_data,np.uint8)
        img = cv2.imdecode(np_data,cv2.IMREAD_UNCHANGED)

        #INGRESARLAS AL MODELO 

        prediction = detect_image(yolo, img, "./IMAGES/HU8_detect.jpg", input_size= 416, show=True, CLASSES="./model_data/license_plate_names.txt", rectangle_colors=(255,0,0))
        if prediction[1][0]: 
            
            for box_stats in prediction[1]:
                box_stats['id'] = blob.name
                rows.append(box_stats) 
            
            #CAST TO BASE64 
            retval, buffer_img = cv2.imencode('.jpg', prediction[0])
            data = base64.b64encode(buffer_img)
            images_div.append('data:image/png;base64,{}'.format(data.decode()))

    
    #Create empty dataframe
    df = pd.DataFrame(rows, columns = column_names)
    
    df['Class'] = df['Class'].apply(lambda x: change_classname(x))
    children = [generate_thumbnail(data) for data in images_div]
    df2 = df.groupby(['Class']).size().reset_index(name='counts')

    #GENERATE PLOTS 

    colors = ['#61892F', '#6B6E70', '#86C232']

    ploty1 = go.Figure(data = [go.Pie(
                labels = df2['Class'], values = df2['counts'], hole=.5
            )])
        
    ploty1.update_layout(height= 350, width = 470, paper_bgcolor = 'rgba(0,0,0,0)', plot_bgcolor = 'rgba(0,0,0,0)', 
    font=dict(family = "Enriqueta, Times New Roman", size=16 , color='rgb(97,137,47)'),  title="Faillure Distribution",  title_x = 0.5)
    ploty1.update_traces(marker = dict(colors=colors))

    table = generate_table(df)
    return children, table, ploty1


#GENERATE LABELED IMAGES FROM THE MODEL
