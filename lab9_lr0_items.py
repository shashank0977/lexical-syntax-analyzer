productions=['E->E+T','E->T','T->T*F','T->F','F->(E)','F->id']
for prod in productions:
    for i in range(len(prod)):
        print(prod[:i]+'.'+prod[i:])