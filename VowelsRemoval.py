# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 18:46:01 2019

@author: aljas

project to remove vowels from a text
"""

vowels=("a","e","i","o","u","A","E","I","O","U")
Message=input("Enter a Message: ")

MessageWithoutVowels=""

for letters in Message:
    if letters not in vowels:
        MessageWithoutVowels=MessageWithoutVowels+letters
        
print("Message Without Vowels:\n {}".format(MessageWithoutVowels))