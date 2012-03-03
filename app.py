#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
#import newrelic.agent
from fetch_data import grs_stock
from flask import Flask
app = Flask(__name__)

#@newrelic.agent.wsgi_application()
@app.route('/g/<int:no>')
def gg(no):
    g = grs_stock(no)
    op = g.serial_price(6)
    return str(g.row_data)


#@newrelic.agent.wsgi_application()
@app.route('/')
def hello():
    return 'Hello World!!!!!!!!!!!!!'


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port,debug=True)
