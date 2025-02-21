import speech_recognition as sr

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print("Please Start Speaking...")
    recognizer.adjust_for_ambient_noise(source)
    audio_data = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio_data)
        print(text)
    except:
        print("WE GOT SOME ERROR")
        exit()
    if "exit" in text:
        exit()