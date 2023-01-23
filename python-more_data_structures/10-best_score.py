#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    sorted_dic = sorted(a_dictionary.items())
    return sorted_dic[-1][0]
