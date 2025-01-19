import network
import socket
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
    return wlan.ifconfig()[0]  # Return the IP address


# Setup HTTP server
def start_http_server(ip):
    addr = socket.getaddrinfo(ip, 80)[0][-1]  # Use the actual IP address
    s = socket.socket()
    s.bind(addr)
    s.listen(1)

    print('Listening on', addr)
    while True:
        cl, addr = s.accept()
        print('Client connected from', addr)
        request = cl.recv(1024)
        print("Request received:", request)

        # Simple HTTP response
        response = """HTTP/1.1 200 OK
Content-Type: text/html

<!DOCTYPE html>
<html>
<head><title>ESP32 HTTP Server</title></head>
<body>
    <h1>Welcome to ESP32 HTTP Server!</h1>
</body>
</html>"""

        cl.send(response)
        cl.close()


# Main execution
ip = connect_wifi()
start_http_server(ip)

