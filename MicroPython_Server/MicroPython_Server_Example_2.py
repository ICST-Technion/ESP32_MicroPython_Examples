import network
import socket
import time

# Wi-Fi credentials
SSID = "your_wifi_ssid"  # ENTER_WIFI_NAME
PASSWORD = "your_wifi_password"  # ENTER_WIFI_PASSWORD


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


# Databases
databases = {
    "animals": ["cats", "dogs"],
    "major": ["computer science", "electrical engineering"]
}


# Parse request to determine resource and option
def parse_request(request):
    try:
        # Decode the request
        request_line = request.decode().split("\r\n")[0]
        # Extract the path (e.g., /animals/1)
        path = request_line.split(" ")[1]
        # Split the path into parts
        parts = path.strip("/").split("/")
        if len(parts) == 2:  # Expecting resource/option
            resource, option = parts
            option = int(option)  # Convert to integer
            return resource, option
    except Exception as e:
        print("Error parsing request:", e)
    return None, None


# Start HTTP server
def start_http_server(ip):
    addr = socket.getaddrinfo(ip, 80)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    print("Listening on", addr)

    while True:
        cl, addr = s.accept()
        print("Client connected from", addr)
        request = cl.recv(1024)
        print("Request received:", request)

        # Parse the request
        resource, option = parse_request(request)

        # Generate response
        if resource in databases and 1 <= option <= len(databases[resource]):
            # Valid request: return the selected option
            response_body = databases[resource][option - 1]
        else:
            # Invalid request: return an error message
            response_body = "Invalid request. Check the URL and try again."

        # Send HTTP response
        response = f"""HTTP/1.1 200 OK
Content-Type: text/plain

{response_body}"""
        cl.send(response)
        cl.close()


# Main execution
ip = connect_wifi()
start_http_server(ip)
