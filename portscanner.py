from flask import Flask
from flask import render_template
import socket

app = Flask(__name__)

@app.route('/')
def hello():

    domain = '45.55.53.99'
    port = 20

    def check_port(domain, port):

        # Creating tuple
        request_tuple = (domain, port)

        # Create socket
        sock = socket.socket()

        # Set timeout to connection
        sock.settimeout(1)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Check if port is open
        result = sock.connect_ex(request_tuple) is 0

        # Close the socket
        sock.close()

        # Return result
        return result


    con = check_port(domain, port)

    return render_template('index.html', name=con)