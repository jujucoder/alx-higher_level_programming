#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary or type(a_dictionary[max(a_dictionary)]) != int:
        return None
    return max(a_dictionary)
