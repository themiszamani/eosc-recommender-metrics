from flask import Flask, render_template, jsonify
import json, os
from dotenv import load_dotenv


app = Flask('RS_EVALUATION')
dotenv_path = os.path.join(app.instance_path, '.env')
load_dotenv(dotenv_path)

app.config['RS_EVALUATION_METRICS'] = os.environ.get('RS_EVALUATION_METRICS')


@app.route("/")
def main_page():
    '''Serve the main page that constructs the report view'''
    # Render the report template and specifiy metric resource to be '/api' since the report is hosted in the webservice
    return render_template('./report.html.prototype',metric_source='/api')   


@app.route("/api")
def api_metrics():
    '''Serve the metrics data in json format as a default api response'''
    result = {}

    with open(app.config['RS_EVALUATION_METRICS'], 'r') as f:
      result = json.load(f)
      f.close()
    return jsonify(result)