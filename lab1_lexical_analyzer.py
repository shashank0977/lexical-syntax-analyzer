import re

keywords = {'int','float','if','else','while','return'}
operators = {'+','-','*','/','=','=='}

code = input("Enter code: ")

tokens = re.findall(r'[A-Za-z_]\w*|\d+|==|[+\-*/=]', code)

for token in tokens:
    if token in keywords:
        print(token, "-> KEYWORD")
    elif token in operators:
        print(token, "-> OPERATOR")
    elif token.isdigit():
        print(token, "-> NUMBER")
    else:
        print(token, "-> IDENTIFIER")
