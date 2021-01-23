a = 0
def print_a():
    global a
    print(a)
    a=a+1


print_a()
a=1
print_a()
print_a()