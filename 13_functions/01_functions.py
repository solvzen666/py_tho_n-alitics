# def factorial(n):
#    f = 1
#    for i in range(2, n + 1):
#         f = f * i
#     return f

# factorial(3)
# print(f)

# NameError: name 'f' is not defined

def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f
print(factorial(5))