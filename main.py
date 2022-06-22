from flask import Flask, Response
from datetime import datetime
# from helpers.middleware import setup_metrics
# import prometheus_client
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
# setup_metrics(app)
metrics = PrometheusMetrics(app, group_by='endpoint')

# CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')

@app.route('/')
@metrics.counter(
    'cnt_collection', 'Number of invocations per collection', labels={
        'collection': lambda: request.view_args['collection_id'],
        'status': lambda resp: resp.status_code
    })
def hello_world():
	return 'Hello World'

@app.route('/time')
def time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

# @app.route('/metrics')
# def metrics():
#     return Response(prometheus_client.generate_latest(), mimetype=CONTENT_TYPE_LATEST)

# metrics.start_http_server(5001)

# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	app.run(host='0.0.0.0')

