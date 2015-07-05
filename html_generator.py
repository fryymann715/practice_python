__author__ = 'Ian'
LESSON_TEXT = '''
LESSON: 8
NAME: Structured Data
TITLE: Lists
DESC: Lists are structured data types that hold a 'list' of variables which can include both integers and strings as well as other lists.
TITLE: Mutation
DESC: One of the differences between a list and a string is that a list can be manipulated through mutation, meaning that the list's values can be changed rather than reassigning a whole new value to the variable representing it.<br>
This assigns the value 5 to the variable a:
a = 5<br>
This replaces the value assigned to a with a whole new value that is the result of its old held value + 5<br>
a = a + 5<br>
The append() function is an example of mutation, it adds a single entry to the end of a list, essentially changing the value of the list without reassigning the entire variable.<br>
mylist.append(5) if previously mylist = [1, 2, 3, 4], it would now be [1, 2, 3, 4, 5]. If we then did: mylist.append([6, 7, 8]) mylist would then be [1, 2, 3, 4, 5, [6, 7, 8]] because append only adds one entry but it does not reassign any of the values held in the other slots.
TITLE: Aliasing
DESC: Lists can also be aliased, This is handy when you need a function to modify the values of a list that exists outside the function itself. Aliasing works much like it does with superheroes, Batman and Bruce Wayne are two identities for the same person. What happens to Batman also happens to Bruce Wayne.
TITLE: For Loops
DESC: For loops are especially useful when working with lists. A for loops is a loop that will perform it's block of code for every slot in the list and break out of this loop once it reaches the end of the entries in the list. Very useful when cycling through list and arrays.
TITLE: Index and In
DESC: Index is a built in function that finds the location of a specified value within a list and returns the location number where it was found. If said value is not found, it produces an error. <em>in</em> checks inside a list to see if a specified value is present, and returns a boolean value. On the same side other hand, you could use <em>not in</em> to make sure a value is not found within a list.
TITLE: Problem Solving
DESC: Sometimes there are some steps that need to be taken before code is written, a programmer has to know how they are going to solve the problem before the start coding. First step is Don't Panic, next ask: What is the problem? What are the inputs? What are the outputs?  Then work through some examples by hand to try and figure out how to get the outputs from the inputs using pseuo code. Pseudo code is kind of like writing in programming languages in a very vague and general way. Syntax usage isnt exact but one writes pseudo code using the same concepts as programming. Try to use simple mechanical solutions and once you start coding, develop your code incrementally using small functions and test them as you go.
TITLE: Defensive Programming
DESC: A really good way to make sure your code will work correctly is to be defensive, have checks in place to make sure the inputs are even valid inputs and use assertions to test your functions as you write them. An assertion is a check to see if a function's output is what you expect it to be. The line of code below shows an example of making sure that the function daysBetweenDates() returns the value it should return for the case given:<br>
assert daysBetweenDates(2013, 1, 1, 2013, 1, 1) == 0<br>
If this assertion is not true, it stops the program and throws an error while compiling. This makes it easier to search for and destroy bugs within your code.
'''

# function that finds the number of concepts in the lesson string by counting the amount of TITLE tasgs it finds
def get_num_of_concepts(text):
    number_concepts = 0
    while text.find('TITLE:') != -1:
        number_concepts += 1
        next_spot = text.find('TITLE:')
        text = text[next_spot+6:]
    return number_concepts

# pulls the lesson number from the lesson string and turns it into an integer
def get_lesson_id(text, lesson_list):
    start_location = text.find('LESSON: ')
    end_location = text.find('NAME: ')
    lesson_id = text[start_location+8:end_location]
    lesson_list[0] = int(lesson_id)

# takes the number that is passed to it and increments it by 1
def gen_concept_id(id_number):
    id_number += 1
    return id_number

# pulls the lesson name from the lesson string
def get_lesson_name(text, lesson_list):
    start_location = text.find('NAME: ') + 6
    end_location = text.find('TITLE: ')
    lesson_name = text[start_location:end_location-1]
    lesson_list[1] = lesson_name

# pulls an individual concept from a chunk of the lesson string
def get_title(concept):
    start_location = concept.find('TITLE: ') + 7
    end_location = concept.find('DESC: ')
    concept_title = concept[start_location:end_location-1]
    return concept_title


def get_desc(concept):
    start_location = concept.find('DESC: ') + 6
    end_location = concept.find('TITLE: ', start_location)
    concept_desc = concept[start_location:end_location]
    return concept_desc


def fill_concepts(text, number_of_concepts):
    counter = 0
    concept_list = []
    while counter < number_of_concepts:
        concept_id = gen_concept_id(counter)
        counter += 1
        concept = [0] * 3
        this_concept_start = text.find('TITLE:')
        this_concept_end = text.find('TITLE:', this_concept_start + 1)
        raw_concept = text[this_concept_start:this_concept_end]
        concept[0] = concept_id
        concept[1] = get_title(raw_concept)
        concept[2] = get_desc(raw_concept)
        concept_list.append(concept)
        text = text[this_concept_end:]
    return concept_list


def generate_concept_html(lesson_id, concept_id, concept_title, concept_desc):
    concept_id = str(concept_id)
    html_text_1 = '''
        <div class="concept">
            <div class="concept-title" id="lesson'''
    lesson_id_string = '-'
    html_text_2 = '''">'''
    html_text_3 = '''</div>
            <span class="concept-desc">'''
    html_text_4 = '''</span>
            <p>
            '''
    html_text_5 = '''
            </p>
         </div>
     '''
    full_html_text = html_text_1 + str(lesson_id) + lesson_id_string + concept_id + html_text_2 + concept_title + html_text_3 + html_text_4 + concept_desc + html_text_5
    return full_html_text


def gen_notes(lesson_list):
    concept_sublist = lesson_list[2]
    l_html_text_1 = '''<div class="lesson">
        <h1 id="lesson-'''
    l_html_text_2 = '">Lesson '
    l_html_text_3 = ': '
    l_html_text_4 = '''</h1>'''

    closing_div_tag = '''
    </div>'''
    full_html = l_html_text_1 + str(lesson_list[0]) + l_html_text_2 + str(lesson_list[0]) + l_html_text_3 + lesson_list[1] + l_html_text_4

    for concept in concept_sublist:
        full_html = full_html + generate_concept_html(lesson_list[0], concept[0], concept[1], concept[2])
    full_html = full_html + closing_div_tag

    return full_html


num_of_concepts = get_num_of_concepts(LESSON_TEXT)

def preprocess_lesson():
    LESSON = [0] * 2
    get_lesson_id(LESSON_TEXT, LESSON)
    get_lesson_name(LESSON_TEXT, LESSON)
    list_of_concepts = fill_concepts(LESSON_TEXT, num_of_concepts)
    LESSON.append(list_of_concepts)
    return LESSON


print gen_notes(preprocess_lesson())
