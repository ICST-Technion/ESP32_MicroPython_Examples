import machine
import uio
import os
import time

# Updated I2S Pin Assignments
i2s_id = 0
sck_pin = machine.Pin(27)  # BCLK (Bit Clock)
ws_pin = machine.Pin(26)  # LRC (Word Select)
sdout_pin = machine.Pin(25)  # DIN (Data In)

# Initialize I2S
audio_out = machine.I2S(
    i2s_id,
    sck=sck_pin,
    ws=ws_pin,
    sd=sdout_pin,
    mode=machine.I2S.TX,
    bits=16,
    format=machine.I2S.MONO,
    rate=16000,
    ibuf=20000
)


# Function to play a WAV audio file
def play_wav(filename):
    print("Playing:", filename)

    # Open the WAV file
    wav = open(filename, "rb")

    # Skip the WAV header (44 bytes)
    wav.seek(44)

    # Stream the audio data to the MAX98357A
    while True:
        data = wav.read(1024)
        if not data:
            break
        audio_out.write(data)

    wav.close()
    print("Playback finished")


# Check if the audio file exists and play it
filename = "audio_tone.wav"  # Replace with your file name

if filename in os.listdir():
    play_wav(filename)
else:
    print("Audio file not found. Please upload 'audio_tone.wav'.")

# Clean up I2S
audio_out.deinit()

