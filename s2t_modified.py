
import speech_recognition as sr

mic_name = input('Enter the microphone name: ')
sample_rate = 4800
chunk_size = 2048

r = sr.Recognizer()
mic_list = sr.Microphone.list_microphone_names()

for i, microphone_name in enumerate(mic_list):
    if microphone_name == mic_name:
        device_id = i
