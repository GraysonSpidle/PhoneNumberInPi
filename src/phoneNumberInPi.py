''' Finds a number in Pi ignoring the '.' in pi
Exclusively commandline '''

from sys import argv

number = argv[1]

try:
    piFilePath = str(argv[2]) # If you wanted to use a different pi file. Perhaps one with 1 billion decimals.
except IndexError:
    piFilePath = "pi-50_4-million.txt" # The default file

file = open(piFilePath, "r") # Open the file
selection = file.read(len(number) + 1).replace('.','') # remove the '.' because pi is 3.1415...

while len(selection) == len(number): # While there are new numbers left to check
    if selection == number:
        print(file.tell() - len(number)) # Print the result
        break
    selection = selection[1:] + file.read(1) # Remove the first number of the selection and append a new one.

file.close() # Be sure to close the file!
