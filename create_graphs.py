import plotly.express as px
import pandas as pd

df = pd.read_csv('data/dataset-all.csv')
entry_number_columns = slice(1, 10)
finisher_percent_columns = slice(19, 28)
distance_columns = slice(28, 30)
length_columns = slice(30, 32)


def set_default_updates(figure):
    figure.update_traces(mode='markers+lines')
    figure.update_xaxes(tickmode='linear',
                        tickangle=-45,
                        rangeslider_visible=True)
    return figure


def create_base_figure(columns, has_trendline):
    if has_trendline:
        return px.scatter(df,
                          x=df['Year'],
                          y=df.columns[columns],
                          trendline='ols',
                          trendline_scope='overall')
    else:
        return px.scatter(df,
                          x=df['Year'],
                          y=df.columns[columns])


# ENTRY NUMBERS
def create_entry_numbers_graphs(base_figure):
    entry_number_fig = base_figure
    entry_number_fig = set_default_updates(entry_number_fig)
    entry_number_fig.update_yaxes(tickmode='linear',
                                  tick0=25,
                                  dtick=25)
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
def create_finisher_percent_graph(base_figure):
    finisher_percent_fig = base_figure
    finisher_percent_fig = set_default_updates(finisher_percent_fig)
    finisher_percent_fig.update_yaxes(tickmode='linear',
                                      tick0=5,
                                      dtick=5)
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
def create_distance_graph(base_figure):
    distance_fig = base_figure
    distance_fig = set_default_updates(distance_fig)
    distance_fig.update_yaxes(tickmode='linear',
                              tick0=500,
                              dtick=500)
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
def create_length_graph(base_figure):
    length_fig = base_figure
    length_fig = set_default_updates(length_fig)
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
