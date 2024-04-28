import sys

def print_to_txt(filename):
    sys.stdout = open(filename, 'w')

