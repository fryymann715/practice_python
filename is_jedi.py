# My Python Playground
# this is where I plans to play around
# in Python and do some cool shtuff.

def is_jedi(name):
    jedi_location = name.find('jedi')
    if jedi_location == -1:
        answer = '''No way Dude!
        '''
    else:
        answer = '''Yeah man, you is!
        '''
    return answer

def ask_jedi(possible_jedi):

    question = '''Oh ''' + possible_jedi+ '''
    You ask us if you are a true Jedi!?

    '''

    full_string = question + is_jedi(possible_jedi)
    return full_string

jedi_name = raw_input("What is they name? ")
print ask_jedi(jedi_name)