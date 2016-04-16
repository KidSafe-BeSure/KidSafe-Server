from gcm import GCM

def send_all(lst):
    for i in lst[0]:
        format_to_send(i, "True")
    for i in lst[1]:
        format_to_send(i, "False")

def format_to_send(dic, is_bulied):
    send(dic["message"], find_insulting(dic["message"]), is_bulied, dic["from"]["name"])
    return

def send(msg, summ, is_bullied, bully):
    gcm = GCM("AIzaSyDjXNoiS_0OzWwiajVsi1GIAJFvkN47qPk")

    data = {'message': msg, 'summ': summ, 'is_bullied' : is_bullied, 'bully' : bully}

    topic = 'global'
    gcm.send_topic_message(topic=topic, data=data)
    return

def find_insulting(text):
    f = open("insulting_words.txt", "r")
    insulting_words = f.read().split("\n")
    for word in insulting_words:
        if word.lower() in text:
            return word
    return False
