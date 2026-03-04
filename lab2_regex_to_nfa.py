
class State:
    def __init__(self):
        self.edges = {}

class NFA:
    def __init__(self,start,accept):
        self.start=start
        self.accept=accept

def regex_to_nfa(symbol):
    start=State()
    accept=State()
    start.edges[symbol]=accept
    return NFA(start,accept)

regex=input("Enter symbol regex: ")

nfa=regex_to_nfa(regex)

print("NFA Created")
print("Start State:",nfa.start)
print("Accept State:",nfa.accept)
