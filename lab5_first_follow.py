
grammar = {
    'E': ['TR'],
    'R': ['+TR','ε'],
    'T': ['FY'],
    'Y': ['*FY','ε'],
    'F': ['(E)','i']
}

first={}

def find_first(symbol):

    if symbol not in grammar:
        return {symbol}

    result=set()

    for production in grammar[symbol]:
        first_symbol=production[0]
        result |= find_first(first_symbol)

    return result

for non_terminal in grammar:
    first[non_terminal]=find_first(non_terminal)

print("FIRST Sets")

for k,v in first.items():
    print(k,"=",v)
