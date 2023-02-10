from dash import Dash, dcc, html, Output, Input, ctx
import plotly.express as px
import create_graphs

my_app = Dash(__name__)

my_app.title = 'motoe'


# HTML
def build_app():
    my_app.layout = html.Div([
        html.Link(rel='stylesheet',
                  href='/static/styles.css'),
        html.H1('motoe'),
        html.H2('Dakar Stats'),
        html.P('Single click to add or remove a category.'
               ' Double click to show only that category or reshow all categories.'),
        html.P('The \'Selected\' button will show a trendline for only the selected categories'),
        html.H3('Entry Numbers'),
        html.Button('Selected', id='entry-selected-button', n_clicks=0),
        html.Button('Reset', id='entry-reset-button', n_clicks=0),
        dcc.Graph(figure=create_graphs.create_entry_numbers_graphs(
            create_graphs.create_base_figure(create_graphs.entry_number_columns, True)),
            id='entry-number-graph'),
        html.H3('Finisher Percentage'),
        dcc.Graph(figure=create_graphs.create_finisher_percent_graph(
            create_graphs.create_base_figure(create_graphs.finisher_percent_columns, True)),
            id='finisher-number-graph'),
        html.H3('Distance (km)'),
        dcc.Graph(figure=create_graphs.create_distance_graph(
            create_graphs.create_base_figure(create_graphs.distance_columns, True)),
            id='distance-graph'),
        html.H3('Length (days)'),
        dcc.Graph(figure=create_graphs.create_length_graph(
            create_graphs.create_base_figure(create_graphs.length_columns, True)),
            id='length-graph')
    ])
    return my_app


@my_app.callback(
    Output('entry-number-graph', 'figure'),
    Input('entry-number-graph', 'figure'),
    Input('entry-selected-button', 'n_clicks'),
    Input('entry-reset-button', 'n_clicks')
)
def update_entry_graph(graph_x, entry_selected_button, entry_reset_button):
    temp_columns = []
    for v in graph_x['data']:
        if v['name'] == 'Overall Trendline':
            continue
        if 'visible' in v and v['visible'] == True:
            temp_columns.append(create_graphs.df.columns.get_loc(v['name']))
    if 'entry-reset-button' == ctx.triggered_id or not temp_columns:
        return create_graphs.create_entry_numbers_graphs(create_graphs.create_base_figure(slice(1, 10), True))
    elif 'entry-selected-button' == ctx.triggered_id:
        return create_graphs.create_entry_numbers_graphs(create_graphs.create_base_figure(temp_columns, True))


build_app().run_server()
