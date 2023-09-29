import pandas as pd
import plotly.graph_objects as go
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output

airline_data =  pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv', 
                            encoding = "ISO-8859-1",
                            dtype={'Div1Airport': str, 'Div1TailNum': str, 
                                   'Div2Airport': str, 'Div2TailNum': str})

# Create a dash application layout
app = dash.Dash(__name__)

# Get the layout of the application and adjust it.
# Create an outer division using html.Div and add title to the dashboard using html.H1 component
# Add a html.Div and core input text component
# Finally, add graph component.
app.layout = html.Div(children=[html.H1("Airline Performance Dashboard",
                                        style = {'align': "center", "color": '#503036', "font-size": 40}),
                                html.Div(["Input Year", dcc.Input(),], 
                                style={}),
                                html.Br(),
                                html.Br(),
                                html.Div(),
                                ])
