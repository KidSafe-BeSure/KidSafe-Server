import facebook
import sys

def get_texts(user, acsses_token):
    graph = facebook.GraphAPI(access_token=acsses_token, version='2.3')

    result = graph.request('/me/inbox')

    recived_ins_msgs = []
    sent_ins_msgs = []

    for conv in  result["data"]:
        if "comments" in conv.keys():
            for msg in conv["comments"]["data"]:
                if "message" in msg.keys() and "from" in msg.keys():
                    if is_insulting(msg["message"]):
                        if msg["from"]["name"] == user:
                            sent_ins_msgs.append(msg)
                        else:
                            recived_ins_msgs.append(msg)

    #print recived_ins_msgs
    #print sent_ins_msgs
    return recived_ins_msgs, sent_ins_msgs


def is_insulting(text):
    f = open("insulting_words.txt", "r")
    insulting_words = f.read().split("\n")

    for word in insulting_words:
        if word in text:
            return True
    return False

