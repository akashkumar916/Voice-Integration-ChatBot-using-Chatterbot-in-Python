# Voice ChatBot-using-chatterbot-in-Python

Voice ChatBot using chatterbot in Python

Follow my steps

default make sure you know pyton

1.Install python 2 or above
 
2.Star this project at right corner

3.open your terminal and import pytssx and chatterbot one for Chatbot and other for Voice Integration

pip install pytssx
pip install chatterbot

4.make a folder inside it make a chatbot python file eg.chat.py 

5.Inside that folder make a txt file chat.txt  and Download my chat.txt from above and copy the content 

and paste into yours

5.Paste this in your python file


import pyttsx3

from chatterbot.trainers import ListTrainer

from chatterbot import ChatBot

engine=pyttsx3.init()

bot=ChatBot('Akash chatbot')

con=open('chat.txt','r').readlines()

bot.set_trainer(ListTrainer)

bot.train(con)

while True:

    res=input("you:")
    
    resp=bot.get_response(res)
    
    print('Bot:',resp)
    
    engine.say(resp)   #for voice
    
    engine.runAndWait()
    
    
    

6.save and Run this into yours terminal  or cmd


python yourfile.py

7.Done , Congralution  you made your Chatbot

<br/>
<img src="Screenshot (152).png"/>
