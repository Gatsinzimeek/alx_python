def multiply_list_map(my_list=[], number=0):
    newList = map(lambda val: val * number, my_list)
    return list(newList)