import urllib

__author__ = 'ideans'

def read_text():
    quotes = open("C:\python_playground\movie_quotes\movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    output = connection.read()
    connection.close()
    if "true" in output:
        print("*****Der be bad words in dat der file!*****")
    elif "false" in output:
        print("This file is clean of dem curse words.")
    else:
        print("*****Daaaah... It didn't work George.*****")

read_text()