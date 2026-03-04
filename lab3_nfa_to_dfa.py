
nfa_states = {
    'A': {'0':['A','B'], '1':['A']},
    'B': {'1':['C']},
    'C': {}
}

dfa_states = {}

start = frozenset(['A'])
unmarked = [start]

while unmarked:
    state = unmarked.pop()

    if state not in dfa_states:
        dfa_states[state] = {}

        for symbol in ['0','1']:
            new=set()

            for s in state:
                if symbol in nfa_states[s]:
                    new.update(nfa_states[s][symbol])

            new_state=frozenset(new)

            dfa_states[state][symbol]=new_state

            if new_state not in dfa_states:
                unmarked.append(new_state)

print("DFA States:")
for k,v in dfa_states.items():
    print(k,"->",v)
