#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
#import newrelic.agent
from flask import Flask, flash, url_for, render_template, request
from grs import stock
app = Flask(__name__)

@app.route('/grs/', defaults={'no':1201}, methods=['POST', 'GET'])
@app.route('/grs/<int:no>', methods=['POST', 'GET'])
def gg(no):
    if request.method == 'GET':
        g = stock(no)
        sno, name = g.info
        op = {}
        op['rawname'] = g.getRawRowsName
        op['raw'] = g.raw
        op['title'] = sno+name
        op['op'] = [g.MA(3), g.MA(6), g.MA(18)]
        return render_template('grs.htm', op = op)
    else:
        re = []
        for i in dir(request):
            re.append((i, getattr(request, i)))
        op = ''
        for v in re:
            op += "{}<br><br>".format(v)
        return str(op)

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
    app.run(host='0.0.0.0', port=port, debug=int(os.environ.get('FLASKDEBUG', 1)))
