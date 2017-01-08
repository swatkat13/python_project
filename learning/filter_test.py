words = "The sentence  A quick brown fox jumps over the lazy dog  contains every single letter in the English alphabet. Such sentences are called pangrams. You are to write a program which takes a sentence and outputs all the letters it is missing which prevent it from being a pangram. You should ignore the case of the letters in the input sentence, and your output should be all lowercase letters in alphabetical order. You should also ignore all non US-ASCII characters. In case the input sentence is already a pangram, output the string NULL. A happy number is defined by the following process. Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers jiju these are two programes asked in interview print words "



print words

list_words = words.split(' ')

print list_words

print filter(lambda word: word == 'dog', list_words)