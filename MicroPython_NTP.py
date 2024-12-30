import network
import ntptime
import time

# Connect to Wi-Fi
ssid = 'oneplus10'
password = 'm3a5zry8'

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(ssid, password)

while not sta_if.isconnected():
    time.sleep(1)

print('Connected 1  to Wi-Fi')

# Set the time from NTP server (UTC time)
ntptime.settime()

# Get the current UTC time in seconds since the epoch
utc_time = time.time()

# Add the Israel Standard Time offset (2 hours)
# Adjust this offset based on Daylight Saving Time (DST) if necessary
israel_time_seconds = utc_time + 2 * 3600

# Convert the adjusted time to a tuple representing local time
israel_time_tuple = time.localtime(israel_time_seconds)

# Print the Israel time
print(israel_time_tuple)
