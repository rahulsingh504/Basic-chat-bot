from core_modules import Bot_response
from tools import pifi


def __init__():
    pifi("Chat Bot")
    while True:
        print("Bot: " + Bot_response(input("You: ")))

__init__()