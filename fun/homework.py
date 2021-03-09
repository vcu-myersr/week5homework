"""Homework file for my students to have fun with some algorithms! """


def find_greatest_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the largest number in the list.
    """
    incoming_list.sort()
    x = incoming_list.len() - 1
    print("The highest value is ", incoming_list[x])


def find_least_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the smallest/least number in the list.
    """
    incoming_list.sort()
    x = incoming_list[0]
    print("The lowest value is ", x)


def add_list_numbers(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Add all the values together and return it.
    """
    total = 0
    
    for i in range(0, len(incoming_list)):
        total += incoming_list[i]

    print("Sum of values in list is ", total)
    


def longest_value_key(incoming_dict):
    """
    Required parameter, incoming_dict, should be a dict.
    Find the KEY that has a value with the highest length, use the len() function
    """
    pass
