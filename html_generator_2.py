__author__ = 'Ian'
import os
import notes

lessonfile =  open("C:\python_playground\Intro_to_Programming\Lesson 9 Notes.txt")
LESSON_TEXT = lessonfile.read()

# function that finds the number of concepts in the lesson string by counting the amount of TITLE tasgs it finds
def get_num_of_concepts(text):
    number_concepts = 0
    while text.find('TITLE:') != -1:
        number_concepts += 1
        next_spot = text.find('TITLE:')
        text = text[next_spot+6:]
    return number_concepts

# pulls the lesson number from the lesson string and turns it into an integer
def get_lesson_id(text):
    start_location = text.find('LESSON: ')
    end_location = text.find('NAME: ')
    lesson_id = text[start_location+8:end_location]
    #lesson_object.id_number(lesson_id)
    return lesson_id

# takes the number that is passed to it and increments it by 1
def gen_concept_id(id_number):
    id_number += 1
    return id_number

# pulls the lesson name from the lesson string
def get_lesson_name(text):
    start_location = text.find('NAME: ') + 6
    end_location = text.find('TITLE: ')
    lesson_name = text[start_location:end_location-1]
    #lesson_object.name = lesson_name
    return lesson_name

# pulls an individual concept from a chunk of the lesson string
def get_title(concept):
    start_location = concept.find('TITLE: ') + 7
    end_location = concept.find('DESC: ')
    concept_title = concept[start_location:end_location-1]
    return concept_title

# grabs the description portion of the raw concept text
def get_desc(concept):
    start_location = concept.find('DESC: ') + 6
    end_location = concept.find('TITLE: ', start_location)
    concept_desc = concept[start_location:end_location]
    return concept_desc

# loops through all the concepts and fills a list containing all the concepts' info
def fill_concepts(text, number_of_concepts):
    counter = 0
    concept_list = []
    while counter < number_of_concepts:
        concept_id = gen_concept_id(counter)
        this_concept_start = text.find('TITLE:')
        this_concept_end = text.find('TITLE:', this_concept_start + 1)
        raw_concept = text[this_concept_start:this_concept_end]
        concept = notes.Concept(get_title(raw_concept), get_desc(raw_concept), concept_id)
        #concept.id_number = concept_id
        #concept.title = get_title(raw_concept)
        #concept.desc = get_desc(raw_concept)
        concept_list.append(concept)
        text = text[this_concept_end:]
        counter += 1
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


def gen_notes(lesson):
    concept_sublist = lesson.concept_list
    l_html_text_1 = '''<div class="lesson">
        <h1 id="lesson-'''
    l_html_text_2 = '">Lesson '
    l_html_text_3 = ': '
    l_html_text_4 = '''</h1>'''

    closing_div_tag = '''
    </div>'''
    full_html = l_html_text_1 + lesson.id_number + l_html_text_2 + str(lesson.id_number) + l_html_text_3 + lesson.name + l_html_text_4

    for concept in concept_sublist:
        full_html = full_html + generate_concept_html(lesson.id_number, concept.id_number, concept.title, concept.desc)
    full_html = full_html + closing_div_tag

    return full_html


num_of_concepts = get_num_of_concepts(LESSON_TEXT)

def preprocess_lesson():
    lesson = notes.Lesson(get_lesson_id(LESSON_TEXT), get_lesson_name(LESSON_TEXT))
    # (LESSON_TEXT, lesson)
    # get_lesson_name(LESSON_TEXT, lesson)
    list_of_concepts = fill_concepts(LESSON_TEXT, num_of_concepts)
    lesson.concept_list.append(list_of_concepts)
    return lesson


print gen_notes(preprocess_lesson())
