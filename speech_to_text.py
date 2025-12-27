import speech_recognition as sr
import os

def speech_to_text(audio_file):
    if not os.path.exists(audio_file):
        return ""

    r = sr.Recognizer()

    try:
        with sr.AudioFile(audio_file) as source:
            audio = r.record(source)
        text = r.recognize_google(audio)
        return text

    except sr.UnknownValueError:
        return ""

    except sr.RequestError:
        return ""

    except Exception as e:
        print("Speech Error:", e)
        return ""
