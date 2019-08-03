def load(app):
    from views import base

    app.register_blueprint(base)
