import pyttsx3
engine = pyttsx3.init()
for i in range(100): 
    text =input()
    if(text=='exit'):
        exit()
    else:
        engine.say(text)
        engine.runAndWait()