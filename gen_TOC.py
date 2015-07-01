__author__ = 'Ian'

def gen_concept_number(lesson_number):
    concept_number = lesson_number + .1
    print concept_number
    return concept_number

concept_test_list = '''one/two/three/'''

def seperate_concept_names(concept_list):
    #blank_space = ' '
    #current_letter = concept_list[0]
    concept_name_counter = 0
    temp_list = []
    current_concept_name = ' '
    while concept_list[concept_list.find('/')] != -1:

        if concept_list[0] == '/':
            temp_list.append(current_concept_name)
            concept_list = concept_list[1:]
            print temp_list
            current_concept_name = ' '

        current_concept_name = current_concept_name + concept_list[0]
        concept_list = concept_list[1:]
        print current_concept_name
        print concept_list



    return temp_list






def gen_toc_entry(lesson_id, lesson_name, concept_name):

    concept_id = gen_concept_number(int(lesson_id))
    concept_id_2 = gen_concept_number(concept_id)

    html_text_1 = ''' <div class="flex-item">
        <a href="#lesson-'''
    html_text_2 = '">'
    html_text_3 = ''' </a>
        <ul>
            <li><a href="#'''
    html_text_4 = '">'
    html_text_5 = '''</a></li>
            <li><a href="#'''

    full_html_text = html_text_1 + lesson_id + html_text_2 + lesson_name +  html_text_3
    return full_html_text

lessons_id = '7'
lessons_name = 'Functions'
print gen_toc_entry(lessons_id, lessons_name, 'concept one')
print seperate_concept_names(concept_test_list)