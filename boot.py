from flask import Flask

import loader

app = Flask(__name__)
app.config.from_object('config')

loader.load(app)
