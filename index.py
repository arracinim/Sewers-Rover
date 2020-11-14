import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import dashboard, index
import callbacks


app.config.suppress_callback_exceptions = True

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == "/dashboard":
        return dashboard.layout_dashboard

    else:
        return index.layout_index

if __name__ == '__main__':
    app.run_server(debug=True)

