import math

# t1 = input()
# t2 = input()

with open("input.txt", "r") as f:
    t1 = f.readline().strip('\n')
    t2 = f.readline()

t1 = t1.split(" ")
t2 = t2.split(" ")

t1[0] = t1[0].split(":")
t2[0] = t2[0].split(":")

t1[0] = list(map(int, t1[0]))
t2[0] = list(map(int, t2[0]))

x = (t2[0][0] - t1[0][0]) * 60 * 60
x += (t2[0][1] - t1[0][1]) * 60
x += (t2[0][2] - t1[0][2])

diff = math.floor(x/60)

if t1[1] == t2[1] and diff < 0:
    diff += 1440

if t1[1] != t2[1] and diff > 0:
    diff += 720

if t1[1] != t2[1] and diff < 0:
    diff += 1440

if diff < 0:
    diff += 720

print(diff)
print(diff/60)