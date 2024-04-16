'''a Python function to check if a given string is a palindrome. 
(A palindrome is a word, phrase, number, or other sequence of characters 
that reads the same forward and backward.)'''


sent = (input('enter a string: '))

#print(sent)
print(len(sent))



def rev_string(s):
    went = "" #empty string
    i=0
    while i<len(sent):
        j= len(sent)-1-i
        went+=sent[j]   #build reversed string
        i+=1
    return went

def is_palindrome(s):
    if s == rev_string(sent):
        return True
    else:
        return False

rev = rev_string(sent)
print(is_palindrome(sent))
print(rev)

    
