# ESP32 MicroPython Examples

## Multitasking with uasyncio

This code uses the MicroPython uasyncio library to concurrently run two tasks on an ESP32: 
1. blinking the built-in LED 
2. printing "Hello, World!" to the console.

## Multitasking with \_thread

This code uses the \_thread module to run two tasks concurrently on an ESP32:
1. Continuously blinking the built-in LED.
2. Printing "hello world" to the console every 2 seconds.