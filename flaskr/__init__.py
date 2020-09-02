import os

from flask import Flask

#note activate virtual env with "source venv/bin/activate"

def create_app(test_config = None):
    #create and configure app
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        #remember to change this
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )

    if test_config is None:
        #load the instance config, if exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        #load the test config if passed in
        app.config.from_mapping(test_config)

    #ensure instance folder exists
    try:
        os.mkdir(app.instance_path)
    except OSError:
        pass

    #page that says hello
    @app.route('/hello')
    def hello():
        return "Hello Ben! Please keep being cute"

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    return app

