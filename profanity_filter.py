__author__ = 'ideans'

def read_text():
    quotes = open("C:\Users\ideans\Documents\Python_Playground\movie_quotes")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()

read_text()