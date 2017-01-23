import re, random
from TextLogic import *


def route_response_logic(recieved_message):
    if re.search('Hey | Hello | How\sare\syou | W(.*?)s\sup | Whats\sGo(.*?)d ', recieved_message, flags=re.I | re.X):
        return "{0} {1}".format(random.choice(greeting_options), ask_me_a_question)
    else:
        return ""
