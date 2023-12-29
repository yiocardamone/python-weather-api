from flask import Flask
from model.test_class_model import *

app = Flask(__name__)

api_key = "f5b39ac7a82e4dbd8a5120339231312"  # Paste Your API ID Here
final_URL = "http://api.weatherapi.com/v1/current.json?key=" + api_key + "&q={}&aqi={}"


@app.route("/")
def index():
    return "Index Page"


@app.route("/weather")  # здесь один эндпоинт он один общий можно добавлять, но они не меняются
def getting():
    # handlers внутри сервера на flask
    result = TestClassModel('Moscow').request_conversion()
    return str(result.temperature) + " " + str(result.lat) + " " + str(result.lon)