import pwd

def isdigit(string): # "333" or maybe "banana"
    digits = ["0","1","2","3","4","5","6","7","8","9"]
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    # if the string has any letters return false
    if letters in pwd:
        print("The password may not contain words")
    # if the string has only numbers return true