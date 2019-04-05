from flask import Flask, render_template
from flask import request, jsonify, Response
from checkPort import check_port, check_range

import csv
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/check-port')
def checkPort():

    # Get request data
    domain = request.args.get('domain')
    port = int(request.args.get('port'))

    # Check if port is open
    isOpen = check_port(domain, port)

    return Response(str(isOpen), mimetype='text/plain')


@app.route('/check-ports')
def checkPorts():

    # Get request data
    domain = request.args.get('domain')
    port_start = int(request.args.get('port_start'))
    port_end = int(request.args.get('port_end'))

    # Check if range of port is open
    ports_list = check_range(domain, port_start, port_end)

    return Response(json.dumps(ports_list), mimetype='application/json')


@app.route('/ports-info')
def portsInfo():

    csv_file = open('portMap/main-ports.csv', 'r')
    csv_lines = csv_file.readlines()

    dic = {}
    for x in csv_lines:
        x = x.split(',')
        dic.update(
            {
                x[0]: {
                    "protocol": x[1],
                    "tcp/udp": x[2],
                    "description": x[3]
                }
            }
        )

    return Response(json.dumps(dic), mimetype='text/plain')