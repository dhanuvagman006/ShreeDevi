# Speech Recognition Using Artificial Intelligence  

This project demonstrates how to convert speech into text using Python and the **SpeechRecognition** library.  

## Getting Started  

### Prerequisites  
Ensure Python is installed on your system. You can download it from [here](https://www.python.org/downloads/).  

### Install Required Libraries  
Open VS Code or any terminal and run the following commands:  

```
pip install speechrecognition
pip install pyaudio
```

If there are issues installing `pyaudio`, try installing it manually:  

- **Windows**: Download the appropriate `.whl` file from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and install it using:  
  ```
  pip install path_to_downloaded_file.whl
  ```
- **Mac/Linux**:  
  ```
  brew install portaudio
  pip install pyaudio
  ```

### Code Implementation  
Create a Python script (e.g., `speech_to_text.py`) and add the following code:  

#### Import Required Modules  

```
import speech_recognition as sr
```

The `speech_recognition` module is imported and assigned an alias for easier usage.

#### Initialize Recognizer  

```
recognizer = sr.Recognizer()
```

An instance of the `Recognizer` class is created, which will handle the speech recognition process.

#### Capture Audio Input  

```
with sr.Microphone() as source:
    print("Please start speaking...")
    recognizer.adjust_for_ambient_noise(source)
    audio_data = recognizer.listen(source)
```

- The `Microphone()` function is used to access the default microphone.
- `adjust_for_ambient_noise(source)` helps reduce background noise for better accuracy.
- `listen(source)` records the audio input from the microphone.

#### Convert Speech to Text  

```
try:
    text = recognizer.recognize_google(audio_data)
    print(text)
```

- `recognize_google(audio_data)` sends the recorded audio to Google’s speech recognition API and converts it into text.
- The recognized text is printed.

#### Handle Errors  

```
except:
    print("We got some error")
    exit()
```

If speech recognition fails due to an issue, an error message is displayed, and the program exits.

#### Exit Command  

```
if "exit" in text:
    exit()
```

If the recognized text contains the word "exit," the program terminates.

### Running the Script  
Save the file and execute it using:  

```
python speech_to_text.py
```

## Troubleshooting  
- If the microphone is not detected, check the device settings and ensure it is properly connected.  
- If the script fails with `"No Default Input Device Available"`, install missing audio drivers.  
- Reduce background noise for better recognition accuracy.  