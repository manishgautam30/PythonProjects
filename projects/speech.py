exitimport speech_recognition as sr

r=sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source,duration=1)
    # r.energy_threshold()
    print("WELCOME....!  GENIUS  chatter bot here Start chatting using audio : ")
    for i in range (1,100):
        audio= r.listen(source)
        try:
            text = r.recognize_google(audio)
            print('YOU : ',text)
            if('hello' in text):
                print('GENIUS : Hi there!')
            elif('exit' in text):
                break
            elif('about' in text):
                print('GENIUS : Myself "Genius" a chatter bot version 1.0.1 made by Manish Gautam and configured to understand the various functions')
            else:
                print('GENIUS : Inavailable')
        except:
            print("Sorry, could not recognise your voice")
            

