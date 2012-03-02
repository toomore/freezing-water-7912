#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from fetch_data import grs_stock

from flask import Flask
app = Flask(__name__)

@app.route('/g')
def gg():
    g = grs_stock(2618)
    op = g.serial_price(6)
    return str(op)

@app.route('/')
def hello():
    return 'Hello World!!!!!!!!!!!!!'


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
