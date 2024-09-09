def encrypt(txet,s):
    result=""
    for i in range(len(txet)):
        char=text[i]
        if(char.isupper()):
            result+=chr((ord(char)+s-65)%26+65)
        else:
            result=+chr((ord(char)+s-97)%26+97)
    return result
text="ATTACKATONCE"
s=4
print("txet:",text)
print("shift:",str(s))
print("cipher:",encrypt(text,s))
