import network
import urequests
import time

# Firebase details
FIREBASE_URL = "https://fir-esp32-4e74e-default-rtdb.firebaseio.com/"  # Replace with your database URL
API_KEY = "AIzaSyCyB_uigGhUuOGLcaULp4DOI2pLFeutVRQ"  # Replace with your Web API key

# WiFi details
SSID = "oneplus10"
PASSWORD = "m3a5zry8"

# Connect to WiFi
def connect_to_wifi():
    print("Connecting to WiFi...")
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    while not wlan.isconnected():
        print("Connecting...")
        time.sleep(1)
    print("Connected to WiFi!")
    print(wlan.ifconfig())

# Push data to Firebase
def push_data(path, data):
    url = f"{FIREBASE_URL}/{path}.json?auth={API_KEY}"
    headers = {"Content-Type": "application/json"}
    try:
        response = urequests.post(url, json=data, headers=headers)
        print("Push Response:", response.text)
    except Exception as e:
        print(f"Failed to push data: {e}")
    finally:
        if response:
            response.close()

# Retrieve data from Firebase
def get_data(path):
    url = f"{FIREBASE_URL}/{path}.json?auth={API_KEY}"
    try:
        response = urequests.get(url)
        if response and response.status_code == 200:
            print("Get Response:", response.text)
            data = response.json()
        else:
            print(f"HTTP Error: {response.status_code if response else 'No response'}")
            data = None
    except Exception as e:
        print(f"Exception occurred: {e}")
        data = None
    finally:
        if response:
            response.close()
    return data

# Main program
def main():
    connect_to_wifi()

    # Example: Pushing data
    print("Pushing data...")
    push_data("test_path", {"temperature": 25, "humidity": 60})

    # Example: Retrieving data
    print("Retrieving data...")
    data = get_data("test_path")
    if data is not None:
        print("Retrieved data:", data)
    else:
        print("Failed to retrieve data. Check your Firebase configuration or network.")

if __name__ == "__main__":
    main()

