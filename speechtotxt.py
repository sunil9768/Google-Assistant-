import speech_recognition as sr
import webbrowser

r = sr.Recognizer()

with sr.Microphone() as mp:
    print('say')
    audio = r.listen(mp)
    
    
tar=r.recognize_google(audio)
print(tar)
a=tar.replace(" ","+")
nk=("http://google.com/search?q="+a)
webbrowser.get('firefox').open(nk)


