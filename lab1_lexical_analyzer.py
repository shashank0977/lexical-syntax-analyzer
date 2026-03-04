
import re

keywords = ['int','float','if','else','while','return']

code = input("Enter code: ")

tokens = code.split()

for token in tokens:
    if token in keywords:
        print(token,"-> KEYWORD")
    elif re.match(r'^[0-9]+$',token):
        print(token,"-> NUMBER")
    elif re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$',token):
        print(token,"-> IDENTIFIER")
    elif token in ['+','-','*','/','=','==']:
        print(token,"-> OPERATOR")
    else:
        print(token,"-> UNKNOWN")
