from src.templates.monitoring.monitoring_features import page_layout
from dash import html
from dash import dcc
def page_template(prefix):
    content = make_storages(prefix) + page_layout(prefix)
    layout = html.Div(id=f'{prefix}page', children=content, style={'background': '#261C67'})
    return layout

def make_storages(prefix):
    content = [
        dcc.Store(id=f'{prefix}monitoring-data', storage_type='memory')
    ]
    return content