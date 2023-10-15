import string

n = int(input())
num = (n*n//26+1)
print(num)
x = string.ascii_uppercase * num

print(x)