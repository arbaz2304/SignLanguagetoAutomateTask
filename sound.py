import pyttsx3
def speak(text):
    engine = pyttsx3.init()
    engine.say(str(text)+" " + str(text))

    # engine.run()
    engine.runAndWait()

def speak_2(text):
    engine = pyttsx3.init()
    engine.say(text)
    # engine.run()
    engine.runAndWait()

# speak("I am bad boy")