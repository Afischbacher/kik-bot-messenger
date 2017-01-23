import re


class ResponseLogic():
    def __init__(self, recievedMessage):

        if re.search("[Hh]ey | hello | how are you", recievedMessage, re.IGNORECASE):
            self.say_hello()
        elif re.search("[Cc]olor | [Cc]olour", recievedMessage, re.IGNORECASE):
            self.get_favourite_color()
        elif re.search("[Ww]hat is your name", recievedMessage, re.IGNORECASE):
            self.get_name()
        else:
            self.i_dont_know()

    def say_hello(self):
        return "Hey I'm Andre, this is my chat bot, hope you like it! To get started ask me a question" \
               "(I might not know all the answers to them though)"

    def get_favourite_color(self):
        return "My favourite color is blue !, its also the color of my eyes"

    def get_name(self):
        return "My name is Andre Fischbacher! Nice to meet you."

    def i_dont_know(self):
        return "I don't know the answer to that one, sorry!"
