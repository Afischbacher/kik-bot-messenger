import re


class ResponseLogic():
    def __init__(self, recievedMessage):

        if re.findall("hey | hello | how are you", recievedMessage):
            self.say_hello()
        elif re.findall("color | colour", recievedMessage):
            self.get_favourite_color()
        elif re.findall("what is your name", recievedMessage):
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