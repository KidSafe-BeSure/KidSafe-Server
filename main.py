import send
import get_texts
import sys

def main():
    send.send_all(get_texts.get_texts("Adam Shem-ur", sys.argv[1]))
    #print get_texts.get_texts("Adam Shem-ur", sys.argv[1])
main()
