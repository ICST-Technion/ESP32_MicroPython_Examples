import network
import ntptime
import time

ssid = "enter_your_wifi_ssid"
password = "enter_your_wifi_password"

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

if not sta_if.isconnected():
    print("Connecting to Wi-Fi...")
    sta_if.connect(ssid, password)
    for _ in range(10):  # Wait up to 10 seconds
        if sta_if.isconnected():
            break
        time.sleep(1)

if not sta_if.isconnected():
    print("Failed to connect to Wi-Fi.")
else:
    print("Connected to Wi-Fi:", sta_if.ifconfig())

    # Get NTP time
    try:
        ntptime.settime()
        utc_time = time.time()
        israel_time_seconds = utc_time + 2 * 3600
        israel_time_tuple = time.localtime(israel_time_seconds)
        print("Israel Time:", israel_time_tuple)
    except Exception as e:
        print("NTP time sync failed:", e)

