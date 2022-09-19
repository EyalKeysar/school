# This code calculates the equations in the text file.
import os

# r"C:\Networks\school\cyber\homework\3#\input.txt"
PATH_TO_INPUT = r"C:\Networks\school\cyber\homework\3#\input.txt"
PATH_TO_OUTPUT = r"C:\Networks\school\cyber\homework\3#\output.txt"

def solve(args, line):
    '''
    This function solves 1 group of arguments.
    '''
    match args[1]:
        case "+":
            solved = line + " = " + str(int(args[0]) + int(args[2]))
        case "-":
            solved = line + " = " + str(int(args[0]) - int(args[2]))
        case "*":
            solved = line + " = " + str(int(args[0]) * int(args[2]))
        case "/":
            solved = line + " = " + str(int(args[0]) / int(args[2]))
    return solved

def read_and_solve(file):
    '''
    This file read and solve give file.
    '''
    solves = []
    lines = file.read().split("\n") # Read file and split its lines
    for line in lines:
        solved = ""
        args = line.split(" ")
        if(len(args) == 3):
            if(args[0].isnumeric() and args[1] in "+-/*" and args[2].isnumeric()):
                solved = solve(args, line)  # If line was written by the protocol - solve it.
        solves.append(solved)
    solves = remove_empty(solves)  # Remove empty lines
    return solves

def write(solves):
    '''
    This function write data to file
    '''
    f = open(PATH_TO_OUTPUT, "w")
    f.write("\n".join(solves))

def remove_empty(arr):
    '''
    This function remove empty strings from a list
    '''
    return [i for i in arr if (i != "")]
def main():
    if(os.path.exists(PATH_TO_INPUT)):
        f = open(PATH_TO_INPUT, "r")
        solves = read_and_solve(f)
        write(solves)
    else:
        print("file does not exists")

if __name__ == "__main__":
    main()

