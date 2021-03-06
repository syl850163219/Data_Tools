import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import datetime as dt

import pandas as pd
import pathlib

import modular.mkt_behavior as mkt_b
import modular.config as conf

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

def create_mkt_pattern_playbook_page():
    today=dt.datetime.today()
    gauge=create_mkt_pattern_playbook_gauge("123")
    
    container = html.Div([
            dbc.Row([
                dbc.Col([
                    create_mkt_pattern_playbook_card("股份制银行负债结构"+today.strftime("%Y-%m-%d"))
                ]),
            ]),
            dbc.Row([
                dbc.Col([
                    create_mkt_pattern_playbook_card("股份制银行负债结构"+today.strftime("%Y-%m-%d"))
                ]),
            ]),
            dbc.Row([
                dbc.Col([
                    create_mkt_pattern_playbook_card("股份制银行负债结构"+today.strftime("%Y-%m-%d"))
                ]),
            ]),
            dbc.Row([
                dbc.Col([
                    create_mkt_pattern_playbook_card("股份制银行负债结构"+today.strftime("%Y-%m-%d"))
                ]),
            ]),
            dbc.Row([
                dbc.Col([
                    create_mkt_pattern_playbook_card("股份制银行负债结构"+today.strftime("%Y-%m-%d"))
                ]),
            ]),
            dbc.Row([
                dbc.Col([
                    create_mkt_pattern_playbook_card("股份制银行负债结构"+today.strftime("%Y-%m-%d"))
                ]),
            ]),
            dbc.Row([
                dbc.Col([
                    create_mkt_pattern_playbook_card("股份制银行负债结构"+today.strftime("%Y-%m-%d"))
                ]),
            ]),
            dbc.Row([
                dbc.Col([
                    create_mkt_pattern_playbook_card("股份制银行负债结构"+today.strftime("%Y-%m-%d"))
                ]),
            ]),
            dbc.Row([
                dbc.Col([
                    create_mkt_pattern_playbook_card("股份制银行负债结构"+today.strftime("%Y-%m-%d"))
                ]),
            ]),
        ])

    page=dbc.Container([gauge,container])
    
    return page


def create_mkt_pattern_playbook_card(title):
    title=title
    card = html.Div([
        dbc.CardHeader(html.H6(title)),
        dbc.CardBody([
            dbc.Alert(
                            "Something's gone wrong! Give us a moment, but try loading this page again if problem persists.",
                            id="no-data-alert-",
                            color="warning",
                            style={"display": "none"},
                                ),
            dbc.Row([
            ]),
            dcc.Graph(id='xxx',figure=mkt_b.fig_bank_debt_resource()),
        ])
    ])
    return card

def create_mkt_pattern_playbook_gauge(title):
    title=title
    
    GAUGE = html.Div([
        dbc.CardHeader(html.H6(title)),
        dbc.Alert(
             "Not enough data to render these plots, please adjust the filters",
            id="no-data-alert",
            color="warning",
            style={"display": "none"},
        ),
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    dcc.Graph(id='x1'),
                ]),
                dbc.Col([
                    dcc.Graph(id='x2'),
                ]),
                dbc.Col([
                    dcc.Graph(id='x3'),
                ]),
            ])
        ])
    ])
    
    return GAUGE
    
