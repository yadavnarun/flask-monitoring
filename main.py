from flask import Flask, Response
from datetime import datetime
import prometheus_client
from prometheus_client import Counter

app = Flask(__name__)

graphs = {}
graphs['t'] = Counter('python_request_operations_total_time_route',
                      'The total number of processed requests on time route')


@app.route("/")
def hello():
    return "Hello World!"


@app.route('/time')
def time():
    graphs['t'].inc()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time


@app.route("/metrics")
def requests_count():
    res = []
    for k, v in graphs.items():
        res.append(prometheus_client.generate_latest(v))
    return Response(res, mimetype="text/plain")


# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the local development server.
    app.run(host='0.0.0.0')
