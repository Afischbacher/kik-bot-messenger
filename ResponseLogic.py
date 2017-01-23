import re


def route_response_logic(recieved_message):
    if re.search("[[Hh]ey", recieved_message, re.IGNORECASE):
        return "Hey I'm Andre, this is my chat bot, hope you like it! To get started ask me a question" \
           "(I might not know all the answers to them though)"
