import json

from model.simplified_inheritance import SimplifiedInheritance


def get_weather():  # здесь один endpoint, он один - общий можно добавлять, но они не меняются.
    # handlers внутри сервера на flask.
    result = SimplifiedInheritance("55.75, 37.62").request_conversion()
    return json.dumps(result.__dict__)
