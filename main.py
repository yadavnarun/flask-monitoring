from flask import Flask, request
from datetime import datetime
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app, group_by='path')

# static information as metric
metrics.info('app_info', 'Application info', version='1.0.0')


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/time')
@metrics.counter('invocation_by_type', 'Number of invocations by type',
                 labels={'item_type': lambda: request.view_args['type']})
def time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time


# main driver function
if __name__ == '__main__':

    # run() method of Flask class runs the application
    # on the local development server.
    app.run(host='0.0.0.0')
