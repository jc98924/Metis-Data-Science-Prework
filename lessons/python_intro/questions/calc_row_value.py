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
    calc_value = 0
    str_conv = [d for d in input_string if d.isdecimal()]

    for index, digit in enumerate(str_conv):
        num_index = index + 1
        if digit % 2 == 0:
            calc_value -= digit * 5
        else:
            calc_value += digit * num_index
    return calc_value
