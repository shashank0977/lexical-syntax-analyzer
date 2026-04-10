nfa = {
    0: {'ε':[1,2]},
    1: {'a':[1]},
    2: {'b':[2]}
}

def epsilon_closure(states):
    stack=list(states)
    closure=set(states)
    while stack:
        s=stack.pop()
        for nxt in nfa.get(s,{}).get('ε',[]):
            if nxt not in closure:
                closure.add(nxt)
                stack.append(nxt)
    return closure

def move(states, sym):
    res=set()
    for s in states:
        res.update(nfa.get(s,{}).get(sym,[]))
    return res

start=frozenset(epsilon_closure({0}))
dfa={}
unmarked=[start]
symbols=['a','b']

while unmarked:
    state=unmarked.pop()
    dfa[state]={}
    for sym in symbols:
        new=frozenset(epsilon_closure(move(state,sym)))
        dfa[state][sym]=new
        if new not in dfa:
            unmarked.append(new)

print("DFA:")
for k,v in dfa.items():
    print(k,"->",v)
