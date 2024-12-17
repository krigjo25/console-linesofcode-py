#   Importing Python responsories
import sys

def parsefile(file):
    
    #   Initializing the list
    lines = []

    #  Open the file and read the lines
    with open(f"{file}", "r") as f:
        lines = [str(i).lstrip() for i in f.readlines() if i.strip()]

    #  Remove the comments
    lines = [i for i in lines if not i.startswith("#")]
    
    return lines

def ArgumentCheck():

    if len(sys.argv) != 2:
        raise Exception("Usage python lines.py ")

    if ".py" not in sys.argv[1]:
        raise Exception("Please Choose a python file. (.py)")

def main():
    """
    #   Author      :    krigjo25
    #   Date        :      26.08-22
    #   Description :   Implements a command-line program to read python files.
    """
    try:
        ArgumentCheck()

    except Exception as e:

        sys.exit(f"{e}")

    print(parse_file(sys.argv[1]))

if __name__ == '__main__':
    main()
