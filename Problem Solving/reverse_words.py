""" 
Code Wars 

https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/train/python

Problem: Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

Examples:

"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps" 
"""

""" 
def reverse_words(text):
  #go for it """


#text = "this is hossam"
#string_list = text.split(" ")
#print(string_list)


""" def reverse_words(text):

    string_list = text.split(" ")
    rev_list = string_list[::-1]
    rev_result = " ".join(rev_list)

    #string_list = [item for item in string_list if item != ""]
   for word in rev_list:
         
        print(word[::-1],end=" ")
        
    
    return rev_result """


def reverse_words(text):
    string_list = text.split(" ")
    rev_list = string_list[::-1]
    rev_result = " ".join(rev_list)
    return rev_result

#reverse_words("apple")
#print("")
#reverse_words("a b c d")
#print("")
reverse_words("he quick brown fox jumps over the lazy dog.")
#print("")
#reverse_words("double  spaced  words")


     
