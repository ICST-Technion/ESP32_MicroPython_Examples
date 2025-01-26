import ubluetooth
from machine import Pin

class ESP32_BLE
    def __init__(self, name=ESP32_UART)
        self.ble = ubluetooth.BLE()
        self.ble.active(True)
        self.ble.irq(self.ble_irq)
        self.name = name
        self.tx_handle = None
        self.rx_handle = None
        self.connected = False
        self.register_services()
        self.advertise()

    def ble_irq(self, event, data)
        if event == 1  # _IRQ_CENTRAL_CONNECT
            print(Device connected)
            self.connected = True
        elif event == 2  # _IRQ_CENTRAL_DISCONNECT
            print(Device disconnected)
            self.connected = False
            self.advertise()  # Restart advertising
        elif event == 3  # _IRQ_GATTS_WRITE
            # Data written to RX characteristic
            buffer = self.ble.gatts_read(self.rx_handle)
            message = buffer.decode(utf-8).strip()
            print(Received, message)
            self.send(Echo  + message)  # Echo received message

    def register_services(self)
        # Define the Nordic UART Service (NUS) UUIDs
        NUS_UUID = ubluetooth.UUID(6E400001-B5A3-F393-E0A9-E50E24DCCA9E)
        RX_UUID = ubluetooth.UUID(6E400002-B5A3-F393-E0A9-E50E24DCCA9E)  # Write
        TX_UUID = ubluetooth.UUID(6E400003-B5A3-F393-E0A9-E50E24DCCA9E)  # Notify

        # Setup service and characteristics
        RX_CHAR = (RX_UUID, ubluetooth.FLAG_WRITE)
        TX_CHAR = (TX_UUID, ubluetooth.FLAG_NOTIFY)
        NUS_SERVICE = (NUS_UUID, (TX_CHAR, RX_CHAR,))
        SERVICES = (NUS_SERVICE,)

        ((self.tx_handle, self.rx_handle,),) = self.ble.gatts_register_services(SERVICES)

    def send(self, message)
        if self.connected
            self.ble.gatts_notify(0, self.tx_handle, message)

    def advertise(self)
        # Configure advertising data
        name = bytes(self.name, utf-8)
        adv_data = bx02x01x06 + bytes((len(name) + 1,)) + bx09 + name
        self.ble.gap_advertise(100000, adv_data)  # Advertise for 100 seconds
        print(fAdvertising as {self.name}...)

# Instantiate the BLE class
ble = ESP32_BLE(ESP32_UART)

# Keep the program running
while True
    pass

