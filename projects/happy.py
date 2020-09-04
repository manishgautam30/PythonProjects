import pyttsx3
engine = pyttsx3.init()
engine.say('welcome  amitiush')
engine.runAndWait()
while True: 
    text =input('Your Text: ')
    if(text=='exit'):
        exit()
    else:
        engine.say(text)
        engine.runAndWait()

