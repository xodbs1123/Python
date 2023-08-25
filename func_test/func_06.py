# a = 10

# def add(x):
#     global a
#     a += x

# add(100)
# print(a)

x = 100

def out(y):
    def inner():
        global x
        nonlocal y
        print(x)
        print(y)
        y += 10
        x += y
    return inner()


out(100)
print(x)