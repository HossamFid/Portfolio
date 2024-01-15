'''test.assert_equals(rot13('test'), 'grfg', 'Returned solution incorrect for fixed string = test')
        test.assert_equals(rot13('Test'), 'Grfg', 'Returned solution incorrect for fixed string = Test')
        test.assert_equals(rot13('aA bB zZ 1234 *!?%'), 'nN oO mM 1234 *!?%', 'Returned solution incorrect for fixed string = aA bB zZ 1234 *!?%')'''






alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M' \
         , 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowercase_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', \
                       'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


iterations = 25


def rot13(text):
    cipher = ''

    for letter in text:
        if letter in alphabet:
            #print(f'Letter : {letter}, alphabet index : {alphabet.index(letter)}')
            letter_index = alphabet.index(letter)  + 13 
            #print(f'Letter index : {letter_index}')
        
            #print(f'Letter IS : {alphabet[letter_index]}')
            if letter_index > iterations:
                new_index = letter_index % iterations 
                #print(f'New Index: {new_index +1}')
                #print(f'Letter IS : {alphabet[new_index]}')
                cipher = cipher + alphabet[new_index]
            else:
                cipher = cipher + alphabet[letter_index] 
            
        elif letter in lowercase_alphabet:
            print(f'Letter : {letter}, lowercase_alphabet index : {lowercase_alphabet.index(letter)}')
            letter_index = lowercase_alphabet.index(letter)  + 13 
            print(f'Letter index : {letter_index}')
        
            print(f'Letter IS : {lowercase_alphabet[letter_index]}')
            if letter_index > iterations:
                new_index = letter_index % iterations 
                print(f'New Index: {new_index }')
                print(f'Letter IS : {lowercase_alphabet[new_index]}')
                cipher = cipher + lowercase_alphabet[new_index]
            else:
                cipher = cipher + lowercase_alphabet[letter_index ] 
        else:
            cipher = cipher + letter
    print(cipher )
# nopqrstuvwxyzabcdefghijklm
rot13('o')