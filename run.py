#!/usr/bin/python
from cms import app
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

app.debug = True

# set a 'SECRET_KEY' to enable the Flask session cookies
app.config['SECRET_KEY'] = 'd1c27e62636803a422aa6fc9617fdd24e428d7e961f00491'

toolbar = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['DEBUG_TB_TEMPLATE_EDITOR_ENABLED'] = True

app.run(host='0.0.0.0')
