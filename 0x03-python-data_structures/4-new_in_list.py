#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list

    length = len(my_list)

    if idx > length:
        return my_list

    list_new = my_list.copy()
    
    list_new[idx] = element
    return list_new
