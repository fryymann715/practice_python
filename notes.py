__author__ = 'ideans'

class Lesson():

    def __init__(self, lesson_id, lesson_name):
        self.id_number = lesson_id
        self.name = lesson_name
        self.concept_list = []


class Concept():

    def __init__(self, concept_title, concept_desc, concept_id):
        self.title = concept_title
        self.desc = concept_desc
        self.id_number = concept_id
