#!usr/bin/python3

"""
Author: Iem-Prog
Date: 14/10/2017
Description:
"""
from string import ascii_lowercase
from random import shuffle

alphabets = list(ascii_lowercase)
shuffle(alphabets)                             #Shuffle the letters
print(alphabets)

codebook ={x: alphabets.pop() for x in ascii_lowercase}     #alphabets{letter: alternative}
#print(codebook)

message = input("Enter text:")

def Encipher(text):
    encoded = ''.join(codebook.get(m, '') for m in text)
    return encoded

reverse_codebook ={v:k for k,v in codebook.items()}
def Decipher(cipher):
    decoded = ''.join(reverse_codebook.get(m, '') for m in cipher)
    return decoded

CipherText = Encipher(message)
PlainText = Decipher(CipherText)

print("You cipher is: " + CipherText)
print("You text is: " + PlainText)
