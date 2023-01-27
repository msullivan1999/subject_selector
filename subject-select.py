from subject import Subject
from timetable import Timetable

import pandas as pd
import sys
import math

NUM_TERMS = 6

# the main function of the program
def select():
    starting_term = parse()
    subjects = create_subjects()
    timetable = create_timetable(starting_term, subjects)

    print(timetable)

# creat instances of the subject class for each row in the CSV
def create_subjects():
    subjects = []
    data = pd.read_csv("subjects.csv")
    # print(data)
    for index, row in data.iterrows():
        if math.isnan(row["second_term"]):
            subject = Subject(row["name"], [row["first_term"]])
        else:
            subject = Subject(row["name"], [int(row["first_term"]), int(row["second_term"])])
        subjects.append(subject)
    return subjects

# perform initial argument checking
def parse():
    # add additonal argument checking at the end (e.g. num type etc.)
    if len(sys.argv) == 1:
        starting_term = 1
    elif len(sys.argv) == 2:
        starting_term = int(sys.argv[1])
    else:
        print("Incorrect number of arguments")
        print("Usage: python3 subject-select.py [starting_term]")
        return
    return starting_term

# simple timetable creation algorithm
def create_timetable(starting_term, subjects):
    current_term = starting_term
    timetable = Timetable()
    for i in range(NUM_TERMS):
        for subject in subjects:
            if subject.terms[0] == current_term:
                timetable.add_subject(subject)
                current_term = update_term(current_term)
                subjects.remove(subject)
        current_term = update_term(current_term)
               


    return timetable 


def update_term(current_term):
    if current_term == NUM_TERMS:
        current_term = 1
    else:
        current_term += 1
    return current_term

# run the program
select()