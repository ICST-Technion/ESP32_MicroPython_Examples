This MicroPython code is designed to play a WAV audio file using an ESP32 connected to a MAX98357A audio module via I2S. The code initializes the I2S interface, checks for the existence of the specified audio file, and plays it if found. Finally, it cleans up the I2S interface after playback.

---

### I2S Setup:

Initializes the I2S interface for transmitting audio data to the MAX98357A audio module. It specifies:

- Pin assignments for BCLK, LRC, and DIN.
- A 16-bit MONO audio format.
- A sample rate of 16 kHz.

### WAV File Playback:

Implements a function to read audio data from a WAV file and stream it to the MAX98357A module, skipping the 44-byte WAV file header.
**NOTICE: because the header is being skipped, if the WAV file is not in the proper format, it will not be detected.**

### File Validation:

Checks whether the specified audio file exists on the ESP32 filesystem. If the file is missing, it prints an error message.

### Cleanup:

Ensures the I2S interface is properly deinitialized after use.

---

### Function Descriptions:

#### 1. `play_wav(filename)`

**Purpose:** Plays a WAV file by reading its data and streaming it via the I2S interface.

**Steps:**
1. Opens the specified file in binary read mode.
2. Skips the first 44 bytes of the file (standard WAV header).
3. Reads the file in chunks of 1024 bytes and writes them to the I2S interface.
4. Closes the file after playback and prints a completion message.

---

#### 2. File Validation and Playback

**Purpose:** Ensures the specified file exists before attempting playback.

**Steps:**
1. Checks the file existence using `os.listdir()`.
2. If the file exists, calls `play_wav()` to play it.
3. If the file is missing, prints an error message.

---

#### 3. `audio_out.deinit()`

**Purpose:** Deinitializes the I2S interface to release resources after playback.

---

**Note:** Once you complete the code, you can get any .mp3 file and convert it to a WAV format and save it onto the ESP32. You can open the ESP32 filesystem using the built-in open folder option in Thonny in the top left corner, and run the code using this file.

**Keep in mind that the code has specific audio configurations for the audio file we used. In case you want to use an audio file with different settings (e.g., 32-bit, 64-bit, or different sample rate), you might need to change the code configuration.**

### Resources and Websites:

[MicroPython I2S Examples](https://github.com/miketeachman/micropython-i2s-examples/blob/master/examples/play_tone.py)
