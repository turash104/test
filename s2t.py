import speech_recognition as sr
import sys
import pyttsx3
import sounddevice as sd

mic_name = "Jabra EVOLVE 65"
sample_rate = 4800
chunk_size = 2048

r = sr.Recognizer()
mic_list = sr.Microphone.list_microphone_names()

for i, microphone_name in enumerate(mic_list):
    if microphone_name == mic_name:
        device_id = i

text = "ذهب الطالب الى المدرسة"
text=text.encode("utf-8")
sys.stdout.buffer.write(text)

with sr.Microphone() as source:
    print("Say Something")
    audio = r.listen(source)
    print("heard...")
    try:
        text = r.recognize_google(audio)
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        f=open("out.txt", "w", encoding="utf-8")
        f.write(text)
        f.close()
        text = text.encode("utf-8")
        sys.stdout.buffer.write(text)

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")

    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
