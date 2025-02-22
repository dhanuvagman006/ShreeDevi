# Text-to-Speech (TTS) Using Python

## This project demonstrates how to implement a text-to-speech (TTS) system using the pyttsx3 library in Python.

## Prerequisites
Ensure you have Python installed on your system. You can download it from the official Python website.

## Install Required Library
To use the TTS feature, install pyttsx3 using the following command:
```bash
pip install pyttsx3
```

## Code Implementation

### 1. Import the Required Module
```python
import pyttsx3
```
**Explanation:**
- The `pyttsx3` module is used for converting text into speech.
- It is an offline text-to-speech conversion library that does not require an internet connection.

### 2. Initialize and Configure the Speech Engine
```python
def init_speaker():
    speak = pyttsx3.init()
    voices = speak.getProperty('voices')
    speak.setProperty('rate', 160)
    speak.setProperty('volume', 0.9)
    speak.setProperty('voice', voices[1].id)
    return speak
```
**Explanation:**
- `pyttsx3.init()`: Initializes the text-to-speech engine.
- `getProperty('voices')`: Retrieves available voices from the system.
- `setProperty('rate', 160)`: Adjusts the speaking speed (words per minute). A lower value makes it slower, while a higher value makes it faster.
- `setProperty('volume', 0.9)`: Sets the volume level, where `0.0` is mute and `1.0` is the highest volume.
- `setProperty('voice', voices[1].id)`: Selects a specific voice from the list of available voices.
  - `voices[0]`: Typically a male voice.
  - `voices[1]`: Typically a female voice.
- The function returns a configured speech engine instance that can be used for speaking text.

### 3. Convert Text to Speech
```python
def speakfun(speak, text):
    speak.say(text)
    speak.runAndWait()
```
**Explanation:**
- `speak.say(text)`: Takes a string as input and converts it into speech.
- `speak.runAndWait()`: Ensures that the speech is played before moving to the next command. Without this, the program might terminate before the speech is heard.

### 4. Example Usage
```python
speak = init_speaker()
speakfun(speak, "Hello, how can I assist you?")
```
**Explanation:**
- `init_speaker()`: Initializes and configures the text-to-speech engine.
- `speakfun(speak, "Hello, how can I assist you?")`: Calls the function with the text message, and the system will read it out loud.
- This script enables the computer to audibly say "Hello, how can I assist you?" when executed.

## Running the Script
Save the script as `speech.py` and run it using:
```bash
python speech.py
```
**Explanation:**
- This will execute the script and make the computer speak the text passed to `speakfun()`.
- Ensure that your device’s speakers are turned on to hear the output.

## Customization
- Modify the `rate` value to speed up or slow down the speech.
- Change the `volume` value for louder or softer output.
- Experiment with different voices using `voices[x].id` (change `x` to `0, 1, 2`, etc., depending on available voices in your system).