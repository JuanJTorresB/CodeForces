def make_operation (operation :str, x :int):
    if operation.__contains__("++"):
        x+=1
    else:
        x-=1
    return x

n = int(input())

x = 0

for i in range(n):
    x = make_operation(str(input()),x)
    

print(x)