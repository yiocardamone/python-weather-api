from flask import Flask

from routes import get_weather

app = Flask(__name__)


# регистрируем обработчик
app.add_url_rule("/weather", "get_weather", get_weather, methods=["GET"])

if __name__ == "__main__":
    app.run()
