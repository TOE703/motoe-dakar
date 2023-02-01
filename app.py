from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

app = Dash(__name__)
app.title = 'motoe'

df = pd.read_csv('data/dataset-all.csv')

# ENTRY NUMBERS
entrants_columns = df.columns[1:10]
entry_number_fig = px.scatter(df,
                              x=df['Year'],
                              y=entrants_columns,
                              trendline='ols',
                              trendline_scope='overall')
entry_number_fig.update_traces(mode='markers+lines')
entry_number_fig.update_xaxes(tickmode='linear',
                              tickangle=-45,
                              rangeslider_visible=True)
entry_number_fig.update_yaxes(tickmode='linear',
                              tick0=50,
                              dtick=50,
                              minor=dict(tick0=25, dtick=25, showgrid=True))
entry_number_fig.update_layout(
    xaxis_title='Year',
    yaxis_title='Entries',
    legend_title_text='Category',
    legend=dict(
        orientation='h'
    )
)

# FINISHERS NUMBERS
finisher_percent_columns = df.columns[19:28]
finisher_percent_fig = px.scatter(df,
                                  x=df['Year'],
                                  y=finisher_percent_columns,
                                  trendline='ols',
                                  trendline_scope='overall')
finisher_percent_fig.update_traces(mode='markers+lines')
finisher_percent_fig.update_xaxes(tickmode='linear',
                                  tickangle=-45,
                                  rangeslider_visible=True)
finisher_percent_fig.update_yaxes(tickmode='linear',
                                  tick0=10,
                                  dtick=10,
                                  minor=dict(tick0=5, dtick=5, showgrid=True))
finisher_percent_fig.update_layout(
    xaxis_title='Year',
    yaxis_title='Finisher Percentage',
    legend_title_text='Category',
    legend=dict(
        orientation='h'
    )
)

# DISTANCE
distance_columns = df.columns[28:30]
distance_fig = px.scatter(df,
                          x=df['Year'],
                          y=distance_columns,
                          trendline='ols',
                          trendline_scope='overall')
distance_fig.update_traces(mode='markers+lines')
distance_fig.update_xaxes(tickmode='linear',
                          tickangle=-45,
                          rangeslider_visible=True)
distance_fig.update_yaxes(tickmode='linear',
                          tick0=1000,
                          dtick=1000,
                          minor=dict(tick0=500, dtick=500, showgrid=True))
distance_fig.update_layout(
    xaxis_title='Year',
    yaxis_title='Distance (km)',
    legend_title_text='Category',
    legend=dict(
        orientation='h'
    )
)

# LENGTH
length_columns = df.columns[30:32]
length_fig = px.scatter(df,
                        x=df['Year'],
                        y=length_columns,
                        trendline='ols',
                        trendline_scope='overall')
length_fig.update_traces(mode='markers+lines')
length_fig.update_xaxes(tickmode='linear',
                        tickangle=-45,
                        rangeslider_visible=True)
length_fig.update_yaxes(tickmode='linear',
                        tick0=1,
                        dtick=1)
length_fig.update_layout(
    xaxis_title='Year',
    yaxis_title='Length (days)',
    legend_title_text='Category',
    legend=dict(
        orientation='h'
    )
)

# HTML
app.layout = html.Div([
    html.H1('Dakar Stats'),
    html.P('Single click to add or remove a category. Double click to show only that category or show all categories.'),
    html.H2('Entry Numbers'),
    dcc.Graph(figure=entry_number_fig,
              id='entry-number-graph data-graph'),
    html.H2('Finisher Percentage'),
    dcc.Graph(figure=finisher_percent_fig,
              id='finisher-number-graph data-graph'),
    html.H2('Distance (km)'),
    dcc.Graph(figure=distance_fig,
              id='distance-graph data-graph'),
    html.H2('Length (days)'),
    dcc.Graph(figure=length_fig,
              id='length-graph data-graph')
])

app.run_server(debug=True)
