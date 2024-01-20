from config import CONFIG
import urequests
import json

# api-endpoint
BASE_URL = "https://api.libreview.io"

LOG_IN_URL = BASE_URL + "/llu/auth/login"

CONNECTIONS_URL = "http://api.libreview.io/llu/connections"

HEADERS = {
    'Content-type': 'application/json',
    'product': 'llu.android',
    'version': '4.7',
    'Authorization': 'Bearer ' + CONFIG["API_TOKEN"]
}

LOGIN_HEADERS = {
    'Content-type': 'application/json',
    'product': 'llu.android',
    'version': '4.7'
}

AUTH_PARAMS = {"email": CONFIG["API_USER"], "password": CONFIG["API_PASSWORD"]}

def login():
    res = urequests.post(url=LOG_IN_URL, headers=LOGIN_HEADERS, json=AUTH_PARAMS)
    jsonresults = json.loads(res.content)
    if res.status_code == 200:
        print("Successfully signed in as ",jsonresults["data"]["user"]["firstName"],jsonresults["data"]["user"]["lastName"])
        print("Your token is-> ")
        print(jsonresults["data"]["authTicket"]["token"])
    else:
        print("Failed to login.")
    


def fetch_glucose_data():
    r = urequests.get(url=CONNECTIONS_URL, headers=HEADERS)
    if r.status_code != 200:
        return (False, [])
    data = r.json()
    # extracting data in json format
    return (True, [data["data"][0]["glucoseMeasurement"]["Value"],
            data["data"][0]["glucoseMeasurement"]["Timestamp"],
            data["data"][0]["glucoseMeasurement"]["TrendArrow"],
            data["data"][0]["glucoseMeasurement"]["MeasurementColor"]])

def fetch_graph_data():
    raise NotImplementedError()
