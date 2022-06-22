'''
Created on 22 June 2022

@author: Craig

Take a comma delimited string and sort each item alphabetically

'''

# Import Regex
import re

# Functions
def alphaSort(subjects):
    delim = ', '
    reSub = re.sub(r'(?<=[.,])(?=[^\s])', r' ', subjects)
    res = delim.join(sorted(reSub.split(', ')))
    return res

def printNorm(subjects):
    print("Original String: " + str(subjects))
    
def printForm(subjects):
    print("Sorted String: " + alphaSort(str(subjects)))

subjects = 'Double Award Science,English, Math, History,ICT, Religious Education, French'

printNorm(subjects)
printForm(subjects)

inputSubjects = input("Please enter a comma delimited string: ")

printNorm(inputSubjects)
printForm(inputSubjects)
