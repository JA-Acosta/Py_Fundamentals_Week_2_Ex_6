'''
>>> JAAR
>>> 07/29/2023
>>> Practicing Fundamentals Program 12
>>> Version 2
'''

'''
>>> Generates a program that compares two lists after removing all duplicates and sorting them. If the lists are unique, the list will be merged such that they are still sorted. The program will then report the common elements between both lists as well as the unique elements. Finally, the program will report which values were duplicates in each individual list.
'''

import re

def list_input()->list :
    '''
    >>> Asks the user for a list and verifies that all elements are integers. Otherwise, asks the user to enter another list.

    >>> Returns: list
    '''
    while True :
        try :
            int_list = list(map(int, re.split(r'[,\s]+', input('Enter a list of integers separated by commas: '))))
        except ValueError :
            print('Your input was invalid!')
        else :
            return int_list

def count_duplicates(int_list : list)->dict :
    '''
    >>> Takes a list and checks for any duplicates in the list. if the list contains duplicates, will record how many times the number occurred.

    >>> Param: (list) int_list
    >>> Return: (dict) duplicates
    '''
    duplicate = {}
    for x in int_list :
        count = sum(1 for y in int_list if y == x)
        if 1 < count :
            duplicate[x] = count
    return duplicate

def main() :
    int_list_I = list_input()
    list_I_duplicates = count_duplicates(int_list_I)
    int_list_II = list_input()
    list_II_duplicates = count_duplicates(int_list_II)
    list_sort = lambda int_list : sorted(list(set(int_list)))
    if list_sort(int_list_I) == list_sort(int_list_II) :
        print(f"Both list (sans duplicates) are identical: {', '.join(map(str, list_sort(int_list_I)))}")
    else :
        merged_list = int_list_I + int_list_II
        common = lambda x, y : list(set(x).intersection(set(y)))
        unique = lambda x, y : list(set(x).difference(set(y)))
        print(f"""
    Merging both list we get:     {', '.join(map(str, list_sort(merged_list)))}
    Common integers:              {', '.join(map(str, sorted(common(int_list_I, int_list_II))))}
    Unique integers for list I:   {', '.join(map(str, sorted(unique(merged_list, int_list_II))))}
    Unique integers for list II:  {', '.join(map(str, sorted(unique(merged_list, int_list_I))))}""")

    if list_I_duplicates :
        print('List I Duplicates:')
        for key in list_I_duplicates.keys() :
            print(f'\t{key}: x{list_I_duplicates[key]}')
    if list_II_duplicates :
        print('List II Duplicates:')
        for key in list_II_duplicates.keys() :
            print(f'\t{key}: x{list_II_duplicates[key]}')

if __name__ == '__main__' :
    main()