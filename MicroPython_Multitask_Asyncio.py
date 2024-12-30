import uasyncio as asyncio
from machine import Pin

# Set up the built-in blue LED (on GPIO 2)
led = Pin(2, Pin.OUT)

# Task to blink the LED
async def blink_led():
    while True:
        led.on()                 # Turn the LED on
        await asyncio.sleep(1)   # Wait for 1 second
        led.off()                # Turn the LED off
        await asyncio.sleep(1)   # Wait for 1 second

# Task to print "Hello, World!"
async def print_message():
    while True:
        print("Hello, World!")   # Print the message
        await asyncio.sleep(2)   # Wait for 2 seconds

# Main function
async def main():
    # Start the two tasks
    asyncio.create_task(blink_led())
    asyncio.create_task(print_message())
    # Keep the program running
    while True:
        await asyncio.sleep(1)

# Start the asyncio event loop
asyncio.run(main())

