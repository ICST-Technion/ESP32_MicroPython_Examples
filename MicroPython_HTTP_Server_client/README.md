# ESP32 MicroPython HTTP Server / client examples

## Static HTTP page - Example_1

This code sets up an HTTP server on an ESP32 device. The ESP32 connects to a specified Wi-Fi network, listens for incoming client connections on port 80, and responds with a static HTML page.

## Database Query - Example_2

This code is the same as the one in Example_1 but with the addition of two databases (Animals, Major). You can query the data inside the databases by adding the required parameters in the URL. Once you run the server and open a web browser, type in the following URL: `IP_OF_SERVER/Animals/1`. The response you'll get would be: `"Cats"` :)

## HTTP client

This code demonstrates how to connect an ESP32 to a Wi-Fi network and perform an HTTP GET request using MicroPython. The device connects to a specified Wi-Fi network and sends a request to the `http://httpbin.org/get` API, printing the response.
