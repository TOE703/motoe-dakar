from dash import dcc, html
from create_graphs import app
from dakarcharts import create_graphs


# HTML
def create_page():
    app.layout = html.Div([
        html.Link(rel='stylesheet',
                  href='/static/styles.css'),
        html.H1('motoe'),
        html.H2('Dakar Stats'),
        html.P('Single click to add or remove a category.'
               ' Double click to show only that category or show all categories.'),
        html.H3('Entry Numbers'),
        dcc.Graph(figure=create_graphs.create_entry_numbers_graphs(),
                  id='entry-number-graph data-graph'),
        html.H3('Finisher Percentage'),
        dcc.Graph(figure=create_graphs.create_finisher_percent_graph(),
                  id='finisher-number-graph data-graph'),
        html.H3('Distance (km)'),
        dcc.Graph(figure=create_graphs.create_distance_graph(),
                  id='distance-graph data-graph'),
        html.H3('Length (days)'),
        dcc.Graph(figure=create_graphs.create_length_graph(),
                  id='length-graph data-graph')
    ])
    return app


create_page().run_server(debug=True)
