from subject import Subject

class Timetable:
    def __init__(self):
        self.subjects = []

    def __str__(self):
        to_print = ""
        for subject in self.subjects:
            to_print += "Term {}: {}".format(subject.terms[0], subject.name) + f"\n"
        return to_print


    def add_subject(self, subject):
        self.subjects.append(subject)
