import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from config import csv_path

df = pd.read_csv(csv_path)

app = dash.Dash()

fig = px.scatter(
    df,
    x="GDP",
    y="Life expectancy",
    size="Population",
    color="continent",
    hover_name="Country",
    log_x=True,
    size_max=60,
)

app.layout = html.Div([dcc.Graph(id="life-exp-vs-gdp", figure=fig)])


if __name__ == "__main__":
    app.run_server(debug=True)