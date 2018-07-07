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
    engine.say(resp)
    engine.runAndWait()