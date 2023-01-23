#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for value in range(len(my_list)):
        new_list.append(my_list[value])
    for element in range(len(new_list)):
        if new_list[element] == search:
            new_list[element] = replace
    return new_list
