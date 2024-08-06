import speech_recognition as sr

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 0.6
        audio = r.listen(source)

    try:
        ask = r.recognize_google(audio, language='en-us')
        print(f"you said : {ask}")
    except Exception:
        print("say that again....")
        return""
    
    return ask
command()