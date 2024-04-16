'''a Python function to check if a given string is a palindrome. 
(A palindrome is a word, phrase, number, or other sequence of characters 
that reads the same forward and backward.)'''

#Recursive implementation

#inputs string
string = input("Enter a string: ")

#function to reverse the string recursively
def is_palindrome(s):
    #base case
    if(len(s)<=1):
        return True # A single character or an empty string is a palindrome
    else:
        #recursively calls  is_palindrome() for segment of the string
        if(s[0]==s[-1]): #checks if  first and last characters are equal
            return is_palindrome(s[1:len(s)-1])
        else:
            #terminates the loop if even one instannce is false
            return False
        
 #prints the output while calling the output of is_palindrome       
print("Given string being a palindrome is ", is_palindrome(string))