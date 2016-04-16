  # Install the Python Requests library:
# `pip install requests`

import requests
import json

def load_file():
    # Request built with RapidAPI (POST http://caring-siberiantiger-ocof.rapidapi.io/load-words)

    try:
        r = requests.post(
            url="http://caring-siberiantiger-ocof.rapidapi.io/load-words",
            data = {
            },
        )
        #print('Response HTTP Status Code   : {status_code}'.format(status_code=r.status_code))
        #print('Response HTTP Response Body : {content}'.format(content=r.content))
    except requests.exceptions.RequestException as e:
        print('HTTP Request failed')

    words = []
    f = open("insulting_words.txt", "w")
    for i in range(len(json.loads(r.content))-1):
        f.write((json.loads(r.content)[i]["word"])+"\n")
    if range(len(json.loads(r.content))) > 0:
        f.write((json.loads(r.content)[-1]["word"]))
    words = json.dumps(words)
    
print load_file()

