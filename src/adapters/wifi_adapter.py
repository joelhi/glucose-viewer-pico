import network
import urequests as requests
from time import sleep
from config import CONFIG

def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(CONFIG["WIFI_SSID"], CONFIG["WIFI_PASSWORD"])
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    print(wlan.ifconfig())