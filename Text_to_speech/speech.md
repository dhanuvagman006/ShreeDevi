# Text-to-Speech (TTS) Using Python

### This project demonstrates how to implement a text-to-speech (TTS) system using the pyttsx3 library in Python.

### Prerequisites

## Ensure you have Python installed on your system. You can download it from here.

## Install Required Library

### To use the TTS feature, install pyttsx3 using the following command:
```
pip install pyttsx3
```

### Code Implementation

1. Import the Required Module
```
import pyttsx3
```
#The pyttsx3 module is used for converting text into speech.

2. Initialize and Configure the Speech Engine
```
def init_speaker():
    speak = pyttsx3.init()
    voices = speak.getProperty('voices')
    speak.setProperty('rate', 160)
    speak.setProperty('volume', 0.9)
    speak.setProperty('voice', voices[1].id)
    return speak
```
### pyttsx3.init(): Initializes the text-to-speech engine.

### getProperty('voices'): Retrieves available voices from the system.

### setProperty('rate', 160): Adjusts the speaking speed (words per minute).

### setProperty('volume', 0.9): Sets the volume level between 0.0 (mute) and 1.0 (maximum).

### setProperty('voice', voices[1].id): Selects a specific voice.

### voices[0]: Usually the default male voice.

### voices[1]: Typically the female voice.

### This function returns a configured speech engine instance.

### 3. Convert Text to Speech
```
def speakfun(speak, text):
    speak.say(text)
    speak.runAndWait()
```
### speak.say(text): Takes a string as input and converts it into speech.

### speak.runAndWait(): Ensures the speech is played before moving to the next command.

### 4. Example Usage
```
speak = init_speaker()
speakfun(speak, "Hello, how can I assist you?")
```
### Initializes the TTS engine using init_speaker().

### Calls speakfun() with a text message, and the system will read it out loud.

## Running the Script

### Save the script as speech.py and run it using:
```
python speech.py
```
### The program will speak out the text passed to speakfun().

## Customization

### Modify the rate to speed up or slow down the speech.

### Change the volume for louder or softer output.

### Experiment with different voices using voices[x].id.