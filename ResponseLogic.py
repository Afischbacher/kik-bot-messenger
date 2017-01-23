import re
import random
from TextLogic import greeting_options
import math


def route_response_logic(recieved_message):
    if re.search('\bWhats\b | \bHey\b | \bHello\b | \bHi\b | \bGr(.*?)s\b', recieved_message, flags=re.I | re.X):
        return "{0}, ask me a question to get to know me".format(random.choice(greeting_options))
    else:
        return "I am not quite sure I have the answer to that question, ask me later ! Sorry"
