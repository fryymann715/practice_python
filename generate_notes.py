__author__ = 'Ian'


LESSON_TEXT = '''LESSON: 7
 NAME: Control Flow & Loops
 TITLE: Boolean Values
 DESC: Boolean values are essentially just, True or False. If using the code: print True or False. The python interpreter checks to see if the first expression is true, if so, it stops there and prints True. If we did: print False or True, the interpreter checks the first expression, being false, it will continue to the next expression. Sine the next expression is true, it will print True.
 TITLE: If Statements
 DESC: An If statement is a way to run a block of code as long as the stated text expression's value is True. If the test expression is False then it will skip the code contained within the If.<br><br>
            if &lttest expresson>:<br>
            &nbsp&nbsp&nbsp&nbsp&ltcode block><br>
            <br>
            If statements typically use comparisons to determine if their code should be ran.(&lt, >, ==, !=, &lt=, >=)<br>

            a = 0<br>
            if a < 10:<br>
            &nbsp&nbsp&nbsp&nbspprint a<br>
            &nbsp&nbsp&nbsp&nbspa = a + 1<br>
            <br>
            The above if statement will run so long as the variable 'a' is smaller than 10. Inside the code it prints the value of 'a' then adds 1 to it and the interpreter is sent back to the begining of the if statement. One the value of 'a' reaches 10, 10 is not less than 10 so the interpreter now skips over the code inside the if.
TITLE: Or Statements
DESC: If statements can also have multiple test expressions connect with an or statement. By using or, the interpreter will determine whether or not to run the code in an if, so long as one of the test expressions is True.<br>
              age = 30<br>
              <br>
              if age < 20 or age == 30:<br>
              &nbsp&nbsp&nbsp&nbsp&ltcode><br>
              <br>
              The example above would send the interpreter through the if block as long as the variable 'age' is under 20 or if it is equal to 30. It will check if the first expression is true. Since 30 is not less than 20, it goes to the next expression after the or, since 30 is in fact equal to 30, it will send the interpreter through the block.
              '''
lesson = []


def get_lesson_id(text, lesson_list):
    start_location = text.find('LESSON: ')
    end_location = text.find('NAME: ')
    lesson_id = text[start_location+8:end_location]
    lesson_list[0] = lesson_id
    print lesson[0]
    return

def get_lesson_name(text):
    start_location = text.find('NAME: ') + 6
    end_location = text.find('TITLE: ')
    lesson_name = text[start_location:end_location]
    return lesson_name

def get_concept_by_number(text, concept_number):
    counter = 0
    while counter < concept_number:
        counter = counter + 1
        next_concept_start = text.find('TITLE:')
        next_concept_end   = text.find('TITLE:', next_concept_start + 1)
        concept = text[next_concept_start:next_concept_end]
        text = text[next_concept_end:]
    return concept

def gen_concept_id(id_number):
    concept_id = id_number + .1
    return concept_id

def get_title(concept):
    start_location = concept.find('TITLE: ') + 7
    end_location = concept.find('DESC: ')
    concept_title = concept[start_location:end_location]
    return concept_title

def get_desc(concept):
    start_location =concept.find('DESC: ') + 6
    end_location = concept.find('TITLE: ', start_location)
    concept_desc = concept[start_location:end_location]
    return concept_desc

def generate_concept_html(concept_id, concept_title, concept_desc):
    concept_id = str(concept_id)
    html_text_1 = '''
        <div class="concept">
            <div class="concept-title" id="'''
    html_text_2 = '''">'''
    html_text_3 = '''           </div>
            <span class="concept-desc">'''
    html_text_4 = '''</span>
            <p>
            '''
    html_text_5 = '''
            </p>
         </div>
     '''
    full_html_text = html_text_1 + concept_id + html_text_2 + concept_title + html_text_3 + html_text_4 + concept_desc + html_text_5
    return full_html_text

def generate_lesson_html(lesson_id, lesson_name, concept_1, concept_2, concept_3):

    html_text_1 = '''<div class="lesson">
        <h1 id="#lesson-'''
    html_text_2 = '">Lesson '
    html_text_3 = ': '
    html_text_4 = '''       </h1>'''

    closing_div_tag = '''
    </div>'''

    full_html_text = html_text_1 + str(lesson_id) + html_text_2 + str(lesson_id) + html_text_3 + lesson_name + html_text_4 + concept_1 + concept_2 + concept_3 + closing_div_tag
    return full_html_text



LESSON_ID = get_lesson_id(LESSON_TEXT, lesson)
LESSON_NAME = get_lesson_name(LESSON_TEXT)

CONCEPT_1 = get_concept_by_number(LESSON_TEXT, 1)
CONCEPT_1_ID = gen_concept_id(LESSON_ID)
CONCEPT_1_TITLE = get_title(CONCEPT_1)
CONCEPT_1_DESC = get_desc(CONCEPT_1)
CONCEPT_1_HTML = generate_concept_html(CONCEPT_1_ID, CONCEPT_1_TITLE, CONCEPT_1_DESC)

CONCEPT_2 = get_concept_by_number(LESSON_TEXT, 2)
CONCEPT_2_ID = gen_concept_id(CONCEPT_1_ID)
CONCEPT_2_TITLE = get_title(CONCEPT_2)
CONCEPT_2_DESC = get_desc(CONCEPT_2)
CONCEPT_2_HTML = generate_concept_html(CONCEPT_2_ID, CONCEPT_2_TITLE, CONCEPT_2_DESC)

CONCEPT_3 = get_concept_by_number(LESSON_TEXT, 3)
CONCEPT_3_ID = gen_concept_id(CONCEPT_2_ID)
CONCEPT_3_TITLE = get_title(CONCEPT_3)
CONCEPT_3_DESC = get_desc(CONCEPT_3)
CONCEPT_3_HTML = generate_concept_html(CONCEPT_3_ID, CONCEPT_3_TITLE, CONCEPT_3_DESC)


#CONCEPT_4 = get_concept_by_number(LESSON_TEXT, 4)
#CONCEPT_5 = get_concept_by_number(LESSON_TEXT, 5)
#CONCEPT_6 = get_concept_by_number(LESSON_TEXT, 6)

print LESSON_ID



#print generate_lesson_html(LESSON_ID, LESSON_NAME, CONCEPT_1_HTML, CONCEPT_2_HTML, CONCEPT_3_HTML)