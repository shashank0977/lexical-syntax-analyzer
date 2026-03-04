
grammar = {
    "A": ["Aα","β"]
}

A="A"

alpha=[]
beta=[]

for rule in grammar[A]:
    if rule.startswith(A):
        alpha.append(rule[1:])
    else:
        beta.append(rule)

print("After Removing Left Recursion:\n")

print(A,"->", " | ".join([b+A+"'" for b in beta]))
print(A+"' ->", " | ".join([a+A+"'" for a in alpha]),"| ε")
