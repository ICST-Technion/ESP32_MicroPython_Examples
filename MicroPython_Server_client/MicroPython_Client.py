import network
import urequests
import time

# Wi-Fi credentials
SSID = "enter_your_wifi_ssid"
PASSWORD = "enter_your_wifi_password"


# Connect to Wi-Fi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Connecting to Wi-Fi...")
        wlan.connect(SSID, PASSWORD)
        while not wlan.isconnected():
            time.sleep(1)
    print("Connected to Wi-Fi:", wlan.ifconfig())


# Send HTTP GET request to a server
def send_http_get_request():
    url = "http://httpbin.org/get"  # Example URL
    response = urequests.get(url)

    print("Response status code:", response.status_code)
    print("Response content:", response.text)


# Main execution
connect_wifi()
send_http_get_request()
