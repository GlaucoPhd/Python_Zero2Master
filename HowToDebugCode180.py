# Linting, IDE,
# Learn Read error
# PDB python debuger stop on the line we write it
import pdb


def add(num1,  num2):
    pdb.set_trace()
    return num1 + num2

# pdb help , use the commands to understand the situation
add(4, 'gla')

