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

    csv_fields = ("port", "protocol", "tcp/udp", "description")
    read_csv = csv.DictReader(csv_file, csv_fields)
    json_csv = json.dumps([row for row in read_csv])

    return Response(json_csv, mimetype='application/json')