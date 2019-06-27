#!/usr/bin/python
import os
import sys

def calc_row_value(input_string):
    """
    This function takes a string input, converts it to an integer value and
    then outputs a "new value".
    ---
    args:
        input_string(str): input string
    returns:
        calc_value (int): output value
    """

    if type(input_string) != str:
        raise ValueError("input_string must be a string type!")

    str_conv = [int(d) for d in input_string if d.isdecimal()]
    calc_value = 0
    for index, digit in enumerate(str_conv):
        num_index = index + 1
        if num_index % 2 != 0:
            calc_value += digit * num_index
        else:
            calc_value -= digit * 5
    return calc_value

input_string = input("Please enter a number to convert:\n")

print("The converted number is:",calc_row_value(input_string))
