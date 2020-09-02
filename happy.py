import pyttsx3
engine = pyttsx3.init()
engine.say('welcome to ur half project that is " text to speech converter" it is soon going to be compleat')
engine.runAndWait()
while True: 
    text =input('Your Text: ')
    if(text=='exit'):
        exit()
    else:
        engine.say(text)
        engine.runAndWait()

