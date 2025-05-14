#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    else:
        roman_int = 0
        dict_roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                      'C': 100, 'D': 500, 'M': 1000}
        list_roman = list(roman_string)
        if len(list_roman) > 1:
            i = len(list_roman) - 1
            while i > 0:
                roman = dict_roman.get(list_roman[i])
                roman_after = dict_roman.get(list_roman[i - 1])

                if roman <= roman_after and i != 1:
                    roman_int += roman

                elif roman <= roman_after and i == 1:
                    # print(i,dict_roman.get(list_roman[i]))
                    roman_int += roman
                    roman_int += roman_after
                    i -= 1

                elif roman > roman_after and i != 1:
                    roman_int += roman - roman_after
                    i -= 1
                else:
                    # print(i,dict_roman.get(list_roman[i]))
                    roman_int += roman - roman_after
                # print(i,dict_roman.get(list_roman[i]))
                i -= 1

        else:
            # print(0, dict_roman.get(list_roman[0]))
            roman_int += dict_roman.get(list_roman[0])
        return roman_int
