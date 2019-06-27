#!/usr/bin/python
import os
import sys

students_input = [
    'Brittany Johnson', 'Sarah Klein', 'Drew Thompson', 'Jimmy Parker',
    'Jill Kelly', 'Heidi Howard', 'Jonathan Watkins', 'Terri Allen',
    'Angela Reyes', 'Suzanne Roberts', 'daniel burgess MD',
    'Cristina Daniels', 'Sandra Vargas', 'Rachel Weeks', 'Nathaniel Mills',
    'Brittany Barnes', 'Brian Jennings', 'Alexandra Walker',
    'Robert Berry', 'John Mann', 'Erica Russell'
    ]

def find_first_names(students_input):
    """
    Takes a list of student first and last names and sort in alphabetical order
    via first name.
    ---
    args: students_input: list of student names (list)
    return: first_names: returns list of sorted first names
    """

    return sorted([name.split()[0].capitalize() for name in students_input])
print(find_first_names(students_input))
