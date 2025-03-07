def is_polindrome(string):
    if str==str[::-1]:
        return True
    else:
        return False
    
str=input("Enter a string: ")
 
if is_polindrome(str):
    print("Polindrome")
else:
    print("Not Polindrome")
    
