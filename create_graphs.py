from dash import Dash
import plotly.express as px
import pandas as pd

app = Dash(__name__)

app.title = 'motoe'

df = pd.read_csv('data/dataset-all.csv')


# ENTRY NUMBERS
def create_entry_numbers_graphs():
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
    return entry_number_fig


# FINISHERS PERCENT
def create_finisher_percent_graph():
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
    return finisher_percent_fig


# DISTANCE
def create_distance_graph():
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
    return distance_fig


# LENGTH
def create_length_graph():
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
    return length_fig
