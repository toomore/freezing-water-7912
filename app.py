#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
#import newrelic.agent
from fetch_data import grs_stock
from flask import Flask, flash, url_for
app = Flask(__name__)

#@newrelic.agent.wsgi_application()
@app.route('/g/<int:no>')
def gg(no):
    a = grs_stock(no)
    return "%s<br><br>%s<br><br>%s" % (a.MA(3), a.MA(6), a.MA(18))


#@newrelic.agent.wsgi_application()
@app.route('/')
def hello():
    app.logger.debug('A value for debugging')
    app.logger.warning('A warning occurred (%d apples)', 42)
    app.logger.error('An error occurred')
    img = url_for('static', filename='img/test1.png')
    return 'Hello World!!!!!!!!!!!!!<br><img src="%s">' % img


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port,debug=True)
