def encrypt(text,s):
    r=""
    for i in range(len(text)):
        char=text[i]
        if(char.isupper()):
            r+=chr((ord(char)+s-65)%26+65)
        else:
            r+=chr((ord(char)+s-97)%26+97)
    return r
text="CHARAN_ANNA"
s=1
print("text:",text)
print("shift:",str(s))
print("cipher:",encrypt(text,s))
