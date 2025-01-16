This code implements a Bluetooth Low Energy (BLE) communication
interface for the ESP32 using the MicroPython ubluetooth module. It
provides basic functionality to act as a BLE peripheral device with a
custom service (Nordic UART Service). The ESP32 can advertise itself,
accept connections from a central device (e.g., a smartphone), and
exchange messages via the BLE protocol.

Function-Specific Explanations:
\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

\_\_init\_\_(self, name=\"ESP32_UART\")

Purpose: Initialize the BLE functionality and set up the device\'s name
and BLE configuration.

What it does: Activates BLE, sets up the interrupt handler, initializes
variables, defines BLE services via register_services, and starts
advertising with advertise.

This is the constructor that initializes the Bluetooth Low Energy (BLE)
object. It sets the BLE device to active mode, assigns an interrupt
handler (ble_irq), and configures its name. It initializes variables for
the transmit (TX) and receive (RX) handles and connection state. It also
calls register_services to define the BLE services and starts
advertising to make the device discoverable.

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

ble_irq(self, event, data)

Purpose: Handle various BLE events such as connection, disconnection,
and data write.

What it does: If a device connects, it prints a connection message and
sets the connection state to True. If a device disconnects, it prints a
disconnection message, sets the connection state to False, and restarts
advertising. If data is written to the RX characteristic, it decodes and
prints the message, then sends an echo back to the central device.

This function handles BLE events. It reacts to specific events:

Event 1 (\_IRQ_CENTRAL_CONNECT): Triggered when a device connects. It
prints a connection message and sets self.connected to True. Event 2
(\_IRQ_CENTRAL_DISCONNECT): Triggered when a device disconnects. It
prints a disconnection message, sets self.connected to False, and
restarts advertising. Event 3 (\_IRQ_GATTS_WRITE): Triggered when data
is written to the RX characteristic. It reads the received data, decodes
it, and prints it. It also sends an echo message back using self.send.

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

register_services(self)

Purpose: Define the BLE service and its characteristics.

What it does: Uses the Nordic UART Service (NUS) UUID to set up a
service with two characteristics: RX (Receive): Allows the central
device to send data to the ESP32. TX (Transmit): Allows the ESP32 to
send notifications to the central device. Registers the service and
stores the TX and RX handles for later use.

This function defines the BLE services and characteristics. It uses the
Nordic UART Service (NUS) UUIDs for communication. The RX_UUID is for
receiving data (write characteristic), and the TX_UUID is for sending
data (notify characteristic). The service and its characteristics are
registered with the BLE stack, and the handles for TX and RX are stored.

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

send(self, message)

Purpose: Send a message to the connected central device.

What it does: Checks if a device is connected and uses the TX
characteristic handle to send the message via BLE notifications.

This function sends a message to the connected central device using the
TX characteristic. It ensures a connection exists before attempting to
notify the central device.

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

advertise(self)

Purpose: Make the ESP32 discoverable to BLE scanners.

What it does: Constructs advertising data, including the device name,
and starts advertising for 100 seconds. Prints a message to indicate the
device is advertising.

This function starts BLE advertising, making the device discoverable by
nearby BLE scanners. It constructs advertising data that includes the
device name and advertises it for 100 seconds. The function also prints
a message to indicate the device is in advertising mode.

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

ble = ESP32_BLE(\"ESP32_UART\")

Purpose: Create an instance of the ESP32_BLE class.

What it does: Initializes the BLE setup with the name \"ESP32_UART\" and
starts advertising.

This line creates an instance of the ESP32_BLE class, initializing the
BLE device with the name \"ESP32_UART.\"

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Resources and websites:

1.https://www.chatgpt.com/ 2.https://www.perplexity.ai/
