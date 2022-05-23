import argparse
from random import choice
from string import ascii_lowercase, ascii_uppercase, digits, punctuation

parser = argparse.ArgumentParser()
parser.add_argument("length", help="Length of password", type=int)
parser.add_argument("-d", help="Include digits", action=argparse.BooleanOptionalAction)
parser.add_argument("-s", help="Include symbols", action=argparse.BooleanOptionalAction)
parser.add_argument("-u", help="Include uppercase letters", action=argparse.BooleanOptionalAction)
parser.add_argument("-l", help="Include lowercase letters", action=argparse.BooleanOptionalAction)
args = parser.parse_args()

length = args.length
include_Digits = args.d
include_Symbols = args.s
include_Uppercase = args.u
include_Lowercase = args.l

def generate_Password(length, include_Digits, include_Symbols, include_Uppercase, include_Lowercase):
    password = ''
        
    for i in range(length):
        random_Digit = choice(digits)
        random_Symbol = choice(punctuation)
        random_Uppercase = choice(ascii_uppercase)
        random_Lowercase = choice(ascii_lowercase)
        
        include = []
        if include_Digits:
            include.append(random_Digit)
        if include_Symbols:
            include.append(random_Symbol)
        if include_Lowercase:
            include.append(random_Lowercase)
        if include_Uppercase:
            include.append(random_Uppercase)
        if include == []:
            include.append(random_Digit)
            include.append(random_Uppercase)
            include.append(random_Lowercase)
            include.append(random_Symbol)

        password += choice(include)
    
    return password

print(generate_Password(length, include_Digits, include_Symbols, include_Uppercase, include_Lowercase))
