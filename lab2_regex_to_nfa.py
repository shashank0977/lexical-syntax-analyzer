class State:
    def __init__(self):
        self.edges = {}

class NFA:
    def __init__(self, start, end):
        self.start = start
        self.end = end

def symbol_nfa(symbol):
    s = State()
    e = State()
    s.edges[symbol] = [e]
    return NFA(s, e)

def concat(nfa1, nfa2):
    nfa1.end.edges['ε'] = [nfa2.start]
    return NFA(nfa1.start, nfa2.end)

a = symbol_nfa('a')
b = symbol_nfa('b')
result = concat(a, b)

print("NFA constructed for 'ab'")
