#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if roman_string != str(roman_string):
        return 0
    roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    num = 0
    i = 0
    while i < len(roman_string):
        if i != len(roman_string) - 1:
            if roman[roman_string[i]] < roman[roman_string[i + 1]]:
                num = num - roman[roman_string[i]]
            else:
                num = num + roman[roman_string[i]]
        else:
            num = num + roman[roman_string[i]]
        i = i + 1
    return num
