#Simple Morse Code Converter

#Dictionary which maps characters to their corresponding morse code

morse = {'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 
         'e':'.', 'f':'..-.', 'g':'--.', 'h':'....', 
         'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 
         'm':'--', 'n':'-.', 'o':'---', 'p':'.--.', 
         'q':'--.-', 'r':'.-.', 's':'...', 't':'-', 
         'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 
         'y':'-.--', 'z':'--..', 
         ' ':'/',
         '1':'.----', '2':'..---', '3':'...--', '4':'....-', 
         '5':'.....', '6':'-....', '7':'--...', '8':'---..', 
         '9':'----.', '0':'-----', 
         ':':'---...', '.':'.-.-.-', '?':'..--..', '/':'-..-.', 
         '-':'-....-', '(':'-.--.', ')':'-.--.-', '\'':'.----.',
         ',':'--..--', '\"':'.-..-.'}

#Dictionary which maps morse code to corresponding characters by inverting the above dictionary 

a_morse = {v:k for k,v in morse.items()}

print("DO YOU WANT TO 'ENCRYPT' OR 'DECRYPT'? :")
user_in = input().upper()

if user_in == "ENCRYPT":  
    print("Please enter the word(s) you want to encrypt:")
    user_txt = input().lower()
    
    out = []

    for m in user_txt:
        if m in morse:
            out.append(morse.get(m))
    print('\nHere is your encrypted text:')
    print(" ".join(out))
    
elif user_in == "DECRYPT":
    print("===============================================")
    print(">>>PUT 1 SPACE BETWEEN EVERY LETTER\n>>>USE '.' AND '-'\n>>>PUT / BETWEEN DIFFERENT WORDS\n>>>PUT SPACE BEFORE AND AFTER '/' TOO")
    print("===============================================")

    print("\nEnter the morse code:")
    user_mor = input()  
    li = list(user_mor.split(' '))

    result = []
    for x in li:
        result.append(a_morse.get(x))
    
    print("HERE IS YOUR DECRYPTED TEXT:")
    print("".join(result).upper())
    
