stack=[]
input_str=list(input('Enter string: '))+['$']
print('Stack\tInput\tAction')
while True:
    if ''.join(stack)=='E' and input_str==['$']:
        print(stack,input_str,'Accepted')
        break
    if input_str:
        stack.append(input_str.pop(0))
        print(stack,input_str,'Shift')