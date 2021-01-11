def convert(number):
    # initialize string output variable
    string_output = ""
    
    # check if number is a multiple of 3
    if number % 3 == 0:
        string_output = "Pling"
    # check if number is a multiple of 5
    if number % 5 == 0:
        string_output = string_output + "Plang"
    # check if number is a multiple of 7
    if number % 7 == 0:
        string_output = string_output + "Plong"

    # if number is NOT a multiple of 3, 5, 7 return the number
    if string_output != "":
        return string_output
    else:
        return str(number)