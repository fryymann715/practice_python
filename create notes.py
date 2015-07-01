__author__ = 'Ian'

# Generates the HTML for my "lesson" section

def gen_lesson(lesson_id, lesson_title):

    html_text_1 = '''<div class="lesson">
    <h1 id="'''

    html_text_2 = '''">'''

    html_text_3 = '''</h1>


</div>'''

    full_html_text = html_text_1+lesson_id + html_text_2 + lesson_title + html_text_3
    return full_html_text

# Generates the concept section complete with title, description, and body. Also adds the css id tag

def gen_concept(concept_id, concept_title, concept_desc, concept_body):

    html_text_1 = '''
        <div class="concept">
            <div class="concept-title" id="'''

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

    full_html_text = html_text_1 + concept_id + html_text_2 + concept_title + html_text_3 + concept_desc + html_text_4 + concept_body + html_text_5

    return full_html_text


# Lesson ID is a string that is inserted into the CSS id tag
# Lesson Title is obviously the title that is in the h1 tag

lesson_id = '''lesson-7'''
lesson_title = '''Control Flow & Loops'''


concept_id = '''7-3'''
concept_title = '''Or Statements'''
concept_desc = '''An or statement takes two test expressions and checks if one or the other is true.'''
concept_body = '''If statements can also have multiple test expressions connect with an or statement. By using or, the interpreter will determine whether or not to run the code in an if, so long as one of the test expressions is True.<br>
                age = 30<br>
                if age < 20 or age == 30:
                &nbsp&nbsp&nbsp&nbsp&ltcode><br>
                <br>
                The example above would send the interpreter through the if block as long as the variable 'age' is under 20 or if it is equal to 30. It will check if the first expression is true. Since 30 is not less than 20, it goes to the next expression after the or, since 30 is in fact equal to 30, it will send the interpreter through the block.'''

print gen_concept(concept_id, concept_title, concept_desc, concept_body)
print gen_lesson(lesson_id, lesson_title)