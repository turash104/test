# Python 2.x program for Speech Recognition

import speech_recognition as sr
# install: pip install --upgrade arabic-reshaper
# import arabic_reshaper

import sys

import pyttsx3

# install: pip install python-bidi
# from bidi.algorithm import get_display
import sounddevice as sd
print(sd.query_devices()) 
# enter the name of usb microphone that you found
# using lsusb
# the following name is only used as an example
mic_name = "Jabra EVOLVE 65"

# Sample rate is how often values are recorded
sample_rate = 4800

# Chunk is like a buffer. It stores 2048 samples (bytes of data)
# here.
# it is advisable to use powers of 2 such as 1024 or 2048
chunk_size = 2048

# Initialize the recognizer
r = sr.Recognizer()

# generate a list of all audio cards/microphones
mic_list = sr.Microphone.list_microphone_names()

# the following loop aims to set the device ID of the mic that
# we specifically want to use to avoid ambiguity.
for i, microphone_name in enumerate(mic_list):
    print(microphone_name)
    if microphone_name == mic_name:
        print("found")
        device_id = i

#print(device_id)
#print(sample_rate)
#print(chunk_size)
# use the microphone as source for input. Here, we also specify
# which device ID to specifically look for incase the microphone
# is not working, an error will pop up saying "device_id undefined"
'''
text = "ذهب الطالب الى المدرسة"
text=text.encode("utf-8")
sys.stdout.buffer.write(text)
'''
with sr.Microphone() as source:

    # wait for a second to let the recognizer adjust the
    # energy threshold based on the surrounding noise level
    #r.adjust_for_ambient_noise(source, duration = 1)
    print("Say Something")

    # listens for the user's input
    audio = r.listen(source)
    print("heard...")
    try:
        #text = r.recognize_google(audio, language="ar-SA")
        text = r.recognize_google(audio)
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        f=open("out.txt", "w", encoding="utf-8")
        f.write(text)
        f.close()
        text = text.encode("utf-8")
        sys.stdout.buffer.write(text)
    # error occurs when google could not understand what was said

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")

    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
