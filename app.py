import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

# Sample Data
data = pd.DataFrame({
    'Year': [2015, 2016, 2017, 2018, 2019],
    'HIV': [3.1, 2.9, 2.8, 2.6, 2.5],
    'TB': [2.4, 2.3, 2.1, 2.0, 1.8],
    'HBV': [1.1, 1.0, 1.0, 0.9, 0.9],
    'HCV': [0.6, 0.6, 0.5, 0.5, 0.4],
})

app = dash.Dash(__name__)
fig = px.line(data, x='Year', y=['HIV', 'TB', 'HBV', 'HCV'], title="Disease Prevalence Trends")

app.layout = html.Div([
    html.H1("Epidemiological Trends Dashboard"),
    dcc.Graph(figure=fig)
])

server = app.server  # For Render deployment

if __name__ == '__main__':
    app.run_server(debug=True)
