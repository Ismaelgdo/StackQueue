# palindrome.py
from MyQueue import Queue
from Stack import Stack
import string

#------------------------------------------------------------

def isPalindrome(phrase):
    forward = Queue()
    reverse = Stack()
    extractLetters(phrase, forward, reverse)
    return sameSequence(forward, reverse)

#------------------------------------------------------------

def extractLetters(phrase, q, s):
    for ch in phrase:
        if ch.isalpha():
            ch = ch.lower()
            q.enqueue(ch)
            s.push(ch)

#------------------------------------------------------------

def sameSequence(q, s):
    while q.size() > 0:
        ch1 = q.dequeue()
        ch2 = s.pop()
        if ch1 != ch2:
            return False
    return True


if __name__ == '__main__':
    
    while True:
        word = input("Please enter a word: ")
        w = isPalindrome(word)
        if w:
            print("Word is a palindrome!")
        else:
            print("Word is not a palindrome!")

"""
Please enter a word: bob
Word is a palindrome!
Please enter a word: nouu
Word is not a palindrome!
Please enter a word: dfgd
Word is not a palindrome!
Please enter a word: oso
Word is a palindrome!
Please enter a word: racecar
Word is a palindrome!
Please enter a word: tacocat
Word is a palindrome!
Please enter a word:
"""
