# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved.

from __future__ import absolute_import, division, print_function, unicode_literals

import sys
import random
import replies
from random import shuffle

from wit import Wit

token = "UZUN2W2TQIFHG4YGAUNWM57SZT573HS7"

client = Wit(access_token=token)

def get_responsefronwit(text):
    resp = client.message(text)
    print("response from api :-",resp)
    resp = handle_response(resp)
    return resp




# Joke example
# See https://wit.ai/aleka/wit-example-joke-bot

all_jokes = {
    "chuck": [
        "Chuck Norris counted to infinity - twice.",
        "Death once had a near-Chuck Norris experience.",
    ],
    "tech": [
        "Did you hear about the two antennas that got married? The ceremony was long and boring, but the reception was great!",
        "Why do geeks mistake Halloween and Christmas? Because Oct 31 === Dec 25.",
    ],
    "default": [
        "Why was the Math book sad? Because it had so many problems.",
    ],
}

jokes_array = [
"Chuck Norris counted to infinity - twice.",
 "Death once had a near-Chuck Norris experience.",
"Why was the Math book sad? Because it had so many problems.",
"Why do geeks mistake Halloween and Christmas? Because Oct 31 === Dec 25."
]
greet_words = [
    'how are you doing today?',
    'hello dear',
    'hello, how can i help you?',
    'how s your day going?'
]

exception_array = [
    'please ask only course related content',
    'can you rephrase it, its hard to understand',
    'sorry,can not, answer that'
]
def first_value(obj, key):
    if key not in obj:
        return None
    val = obj[key][0]["value"]
    if not val:
        return None
    return val


def select_joke(category):
    jokes = all_jokes[category or "default"]
    shuffle(jokes)
    return jokes[0]


def get_greeting():
    shuffle(greet_words)
    return greet_words[0]

def get_joke():
    shuffle(jokes_array)
    return jokes_array[0]

def get_exceptions():
    shuffle(exception_array)
    return exception_array[0]

def find_intent(intents_arr):
    if not intents_arr:
        return get_exceptions()

    value = intents_arr[0]['name']
    return value

def get_response(resp):
    return "got it"

def handle_response(response):
    traits = response["traits"]
    intents_array = response['intents']
    value = find_intent(intents_array)
    print("here is response", response)
    print("intents:-", value)
    reply = ""

    if value == 'greet':
        reply = get_greeting()
    elif value == 'dissertationWordLimit':
        reply = replies.Dissertation_wordLimit[0]
    elif value == 'dissertationRefrences':
        reply = replies.no_refrences[0]
    elif value == 'dissertationTemplate':
        reply = replies.template[0]
    elif value == 'joke':
        reply = get_joke()


    else:
        reply = get_exceptions()

    return reply





#client.interactive(handle_message=handle_response)
