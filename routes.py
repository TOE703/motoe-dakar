from flask import Flask, render_template
import create_graphs

flask_app = Flask(__name__, template_folder='templates', static_folder='static')


@flask_app.route('/')
def index():
    rt = render_template('base.html',
                         entry=create_graphs.create_entry_numbers_graphs().to_html(),
                         finisher=create_graphs.create_finisher_percent_graph().to_html(),
                         distance=create_graphs.create_distance_graph().to_html(),
                         length=create_graphs.create_length_graph().to_html())
    return rt
