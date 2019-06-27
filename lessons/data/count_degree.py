
import os
import re
from collections import defaultdict

import csv
import re
from collections import defaultdict
faculty_path = 'faculty.csv'


def count_degrees(csv_file_name):

    """
    Function to open a the faculty .csv file, clean the degree' column, and
    output a dictionary object where the key is the degree and the value is
    the number of occurences of each degree
    ---
    args: faculty_path = 'faculty.csv'
    output: degree_counter, defaultdict object {key=degree, val = occurences}
    """

    with open(faculty_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        csv_reader.__next__()

        output_list = [ ]
        cleaned_list = [ ]
        degree_counter = defaultdict(int)

        degree_list = [row[1].strip() for row in csv_reader]

        for entry in degree_list:
            if len(entry)>5:
                output_list.extend(re.split('\s+', entry))
            else:
                output_list.append(entry)

        cleaned_list = [(re.sub('\.+','',degree)) for degree in output_list]

        for deg in cleaned_list:
            degree_counter[deg] += 1
        return(degree_counter)

count_degrees(filename)
