
result = ""

# with open("input.txt", "r") as f:
with open("input2.txt", "r") as f:
    for line in f:
        for char in line:
            x = ord(char)
            if x >= 65 and x <= 90:
                if (x - 21) < 65:
                    x = x + 26
                result = result + chr(x - 21)
            else:
                result = result + char
                
print(result)
