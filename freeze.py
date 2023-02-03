from flask_frozen import Freezer
from routes import flask_app

freezer = Freezer(flask_app)

if __name__ == '__main__':
    freezer.freeze()
