"""
WAP to create a text file "notes.txt" and display the count of alphabets, digits, and special characters stored in it.
"""

file = open('notes.txt', 'r')
data = file.read()
alpha = 0
digit = 0
special = 0
for i in data:
    if i.isalpha():
        alpha += 1
    elif i.isdigit():
        digit += 1
    else:
        special += 1
print('Total Alphabets in document is ', alpha)
print('Total Digits in document is ', digit)
print('Total Special Characters in document is ', special)
file.close()
