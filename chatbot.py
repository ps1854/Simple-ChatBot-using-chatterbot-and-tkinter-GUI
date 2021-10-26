# importing packages 
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from tkinter import *

# create chatbot instance
# name - name of Python chatbot
my_bot = ChatBot(name = "ChatterBot", storage_adapter = "chatterbot.storage.SQLStorageAdapter")

# training the chatbot
trainer = ChatterBotCorpusTrainer(my_bot)
trainer.train("chatterbot.corpus.english")

def chat():
    output.delete(1.0, "end")
    text = str(input.get(1.0, "end"))
    response = my_bot.get_response(text)
    input.delete(1.0, "end")
    output.insert(1.0, response)
    input.focus_set()

# creating a tkinter window
chatbot_wd = Tk()
chatbot_wd.geometry("300x300")
chatbot_wd.title("ChatBot")
chatbot_wd["bg"] = "cyan"

input_label = Label(chatbot_wd, text = "How may I help you?", background = "cyan")
input_label.grid(row = 0, column = 1, padx = 5, pady = 5)

# taking input
input = Text(chatbot_wd, width = 15, height = 2)
input.grid(row = 1, column = 1, padx = 5, pady = 5)

send = Button(chatbot_wd, command = chat, text = "SEND")
send.grid(row = 1, column = 3, padx = 5, pady = 5)

# giving output
output = Text(chatbot_wd, width = 25, height = 8)
output.grid(row = 2, column = 1, columnspan = 3, padx = 10, pady = 5)

input.focus_set()

chatbot_wd.mainloop()