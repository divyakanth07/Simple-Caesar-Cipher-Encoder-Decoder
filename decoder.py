def decrypt(text, s):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            result += chr((ord(char) - s - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - s - 97) % 26 + 97)
        else:
        	result += char
    return result

text = input("What happened to ceaser? ")
s = int(input("What number is under that rock ???"))
print("CEASERRRRRRRRRRRRRRRRRRRR :"+ text)
print("CEASERRRRRRRRRRRRRRRRRRRRrrrrrrrrrrrrr:" + str(s))
print("ccccCCeaserrrrrrrrrrrrrrrRRRRRRRRRRRRRRRRRRRRRRRRRRR: " + decrypt(text,s))


