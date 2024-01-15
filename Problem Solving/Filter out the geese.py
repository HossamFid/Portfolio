""" 
Code Wars 

https://www.codewars.com/kata/57ee4a67108d3fd9eb0000e7/train/python

Problem: Write a function that takes a list of strings as an argument and returns a filtered list containing the same elements but with the 'geese' removed.

The geese are any strings in the following array, which is pre-populated in your solution:

Examples:
The geese are any strings in the following array, which is pre-populated in your solution:

["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

For example, if this array were passed as an argument:

["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]

Your function would return the following array:

["Mallard", "Hook Bill", "Crested", "Blue Swedish"]

""" 
geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]



def goose_filter(birds):
    not_geese = list()
    for i in birds:
        #print(i)
        if i not in geese:
            #print(f'not geese {i}')
            not_geese.append(i)
    return not_geese
    #return list(word for word in birds if word not in geese)
goose_filter(["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"])

