# this is the "web_app/__init__.py" file...

import os

from dotenv import load_dotenv
from flask import Flask

from web_app.routes.home_routes import home_routes
from web_app.routes.rps_routes import rps_routes
from web_app.routes.stocks_routes import stocks_routes

load_dotenv()

# set this to something else on production!!!
SECRET_KEY = os.getenv("SECRET_KEY", default="super secret")


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = SECRET_KEY  # needed for flash messaging

    app.register_blueprint(home_routes)
    app.register_blueprint(rps_routes)
    app.register_blueprint(stocks_routes)
    return app


if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
