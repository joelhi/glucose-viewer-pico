from config import CONFIG
import urequests

# api-endpoint
BASE_URL = "https://api.libreview.io"

LOG_IN_URL = BASE_URL + "/llu/auth/login"

GET_USER_URL = "https://api.libreview.io/user"

CONNECTIONS_URL = "http://api.libreview.io/llu/connections"

HEADERS = {
    'Content-type': 'application/json',
    'product': 'llu.android',
    'version': '4.7',
    'Authorization': 'Bearer ' + CONFIG["API_TOKEN"]
}

AUTH_PARAMS = {"username": CONFIG["API_USER"], "password": CONFIG["API_PASSWORD"]}

def fetch_glucose_data():
    r = urequests.get(url=CONNECTIONS_URL, headers=HEADERS)
    data = r.json()
    # extracting data in json format
    return [data["data"][0]["glucoseMeasurement"]["Value"],
            data["data"][0]["glucoseMeasurement"]["Timestamp"],
            data["data"][0]["glucoseMeasurement"]["TrendArrow"],
            data["data"][0]["glucoseMeasurement"]["MeasurementColor"]]

def fetch_graph_data():
    raise NotImplementedError()