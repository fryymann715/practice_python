__author__ = "ideans"
import noteclasses
import os
import lessonlib

lessonfile = open("C:\Users\Ian\Documents\Intro to Programming\Lesson 8 Notes.txt")
LESSON_TEXT = lessonfile.read()
lessonfile.close()

def process_lesson_text():
    concept_list_string = lessonlib.fill_concepts(LESSON_TEXT, lessonlib.get_num_of_concepts(LESSON_TEXT))
    lesson_list = [lessonlib.get_lesson_name(LESSON_TEXT), lessonlib.get_lesson_id(LESSON_TEXT),
                   concept_list_string]
    return lesson_list



#concept_list_string = [
# ['Concept 1', 1, 'First concept.'], ['Concept 2', 2, 'Second concept.'], ['Concept 3', 3, 'Third concept']
#]
lesson_list = process_lesson_text()

lesson10 = noteclasses.Lesson(lesson_list[0], lesson_list[1], lesson_list[2])
#print(lesson10.concept_list[0].id_number)
#print(lesson10.concept_list[0].title)
#print(lesson10.id_number)
print(lesson10.get_html())