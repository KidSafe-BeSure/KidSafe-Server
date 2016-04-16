# Install the Python Requests library:
# `pip install requests`

import requests

def add_word(word):
    # Request built with RapidAPI (POST http://caring-siberiantiger-ocof.rapidapi.io/add-word)

    try:
        r = requests.post(
            url="http://caring-siberiantiger-ocof.rapidapi.io/add-word",
            data = {
                "word":word,
            },
        )
        print('Response HTTP Status Code   : {status_code}'.format(status_code=r.status_code))
        print('Response HTTP Response Body : {content}'.format(content=r.content))
    except requests.exceptions.RequestException as e:
        print('HTTP Request failed')
    return

def load_database(words):
    f = open(words, "r")
    for word in f.read().split("\n"):
        add_word(word)
    print("ALL DONE")
            
load_database("insulting_words.txt")
