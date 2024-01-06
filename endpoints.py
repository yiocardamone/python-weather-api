from flask import Flask
from model.test_class_model import *

import json

app = Flask(__name__)


@app.route("/weather", methods=['GET'])  # здесь один endpoint, он один - общий можно добавлять, но они не меняются.
def getting():
    # handlers внутри сервера на flask.
    result = TestClassModel('Moscow').response_conversion()
    return json.dumps(result.__dict__)
