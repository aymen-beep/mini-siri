import os
import speech_recognition as sr

# this program is devoted to open webs site by saying the name of the website

def vo():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        r.adjust_for_ambient_noise(source,duration=0.75)
        audio = r.listen(source)
        answer = r.recognize_google(audio)
        print(answer)
    return answer
# it only work with www.*****.com


print("say start +'you web'")
answer = vo()
answer = 'www.'+answer+'.com'

os.system(answer)