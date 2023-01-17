from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)
server = app.server

df = pd.read_csv('dakar-stats-dataset.csv')

app.layout = html.Div([
    html.H1('Dakar Entry Numbers',
            style={'textAlign': 'center', 'margin': '0', 'font-family': 'sans-serif'}),
    dcc.Graph(id='my-graph',
              style={'height': '90vh'}),
    dcc.Checklist(
        id='my-checklist',
        options=df['category'].unique(),
        value=df['category'].unique(),
        style={'textAlign': 'center', 'font-family': 'sans-serif'}
    )
])


@app.callback(
    Output('my-graph', 'figure'),
    Input('my-checklist', 'value')
)
def update_graph(selected_categories):
    mask = df['category'].isin(selected_categories)
    fig = px.scatter(df[mask],
                     x='year',
                     y='entries',
                     color='category')
    fig.update_traces(mode='markers+lines')
    fig.update_xaxes(tickmode='linear',
                     tickangle=-45)
    fig.update_yaxes(tickmode='linear',
                     tick0=50,
                     dtick=50,
                     minor=dict(tick0=25, dtick=25, showgrid=True))
    fig.update_layout(
        xaxis_title="Year",
        yaxis_title="Entries"
    )
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
