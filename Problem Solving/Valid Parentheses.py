""" 
Code Wars 

https://www.codewars.com/kata/6411b91a5e71b915d237332d/train/python 

Problem:Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid.
 The function should return true if the string is valid, and false if it's invalid.

"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
"""

opening = []
closing = []

def valid_parentheses(parentheses):
    if parentheses == "":
        return True 
    else:
        for i in range(len(parentheses)):
            if parentheses[0] == ")":
                #print(False) 
                break
            else:
                if parentheses[i] == "(":
                    opening.append(parentheses[i])
                elif parentheses[i] == ")":
                    closing.append(parentheses[i])


        if len(closing) == len(opening) and len(opening) >0 :
            return True 
        else:
            return False
valid_parentheses("")