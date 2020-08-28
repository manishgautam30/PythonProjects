import pyttsx3
engine = pyttsx3.init()
for i in range(1000000): 
    text =input('Write Text Here: ')
    if(text=='exit'):
        exit()
    else:
        engine.say(text)
        engine.runAndWait()