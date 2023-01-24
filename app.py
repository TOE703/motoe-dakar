from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv('dataset-all.csv')

fig = px.scatter(df,
                 x=df['Year'],
                 y=df.columns[1:10])
fig.update_traces(mode='markers+lines')
fig.update_xaxes(tickmode='linear',
                 tickangle=-45,
                 rangeslider_visible=True)
fig.update_yaxes(tickmode='linear',
                 tick0=50,
                 dtick=50,
                 minor=dict(tick0=25, dtick=25, showgrid=True))
fig.update_layout(
    xaxis_title='Year',
    yaxis_title='Entries',
    legend_title_text='Click to add or remove categories',
    legend=dict(
        orientation='h'
    )
)

app.layout = html.Div([
    html.H1('Dakar Entry Numbers'),
    dcc.Graph(figure=fig,
              id='entry-number-graph')
])

app.run_server(debug=True)
