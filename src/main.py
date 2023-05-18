from dash import html, dcc
from dash.dependencies import Input, Output
from src.pages.home import create_page_home
from src.pages.populations import populations_layout
from src.pages.monitoring import monitoring_layout
from src.helper_functions.helpers import load_custom_css
from src.pages.international_transactions import international_transactions_layout
import dash
import dash_bootstrap_components as dbc
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


cust_css = load_custom_css()

app = dash.Dash(__name__, suppress_callback_exceptions=False, external_stylesheets=[dbc.themes.BOOTSTRAP, cust_css])

server = app.server
app.config.suppress_callback_exceptions = False

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
], style={'background': '#261C67', 'height': '100vw', 'width': '100vw'})


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/populations':
        return populations_layout()
    elif pathname == '/international_transactions':
        return international_transactions_layout()
    elif pathname == '/monitoring':
        return monitoring_layout()
    else:
        return create_page_home()


if __name__ == '__main__':
    app.run_server(debug=False)
