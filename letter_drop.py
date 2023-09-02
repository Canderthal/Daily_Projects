import time
import os
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', " ", 
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

message = input("Please reveal message")
text = ""
breakdown = []
for letter in message:
    breakdown.append(letter)
count = 0
cracking = True
while cracking:
    for letter in letters:
        time.sleep(0.02)
        if text == message:
            cracking = False
            os.system("cls")
            print(text,letter)
            break
        if letter == breakdown[count]:
            text += letter
            print(text)
            count += 1
            break
        else:
            os.system("cls")
            print(text,letter)

