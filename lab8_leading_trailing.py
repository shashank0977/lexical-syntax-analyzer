grammar={'E':['E+T','T'],'T':['T*F','F'],'F':['(E)','i']}
leading={}
trailing={}
for nt in grammar:
    leading[nt]={p[0] for p in grammar[nt]}
    trailing[nt]={p[-1] for p in grammar[nt]}
print('LEADING:',leading)
print('TRAILING:',trailing)