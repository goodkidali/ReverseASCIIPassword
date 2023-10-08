s = input("Enter String: ")  # 8910140179382350180156 --> Test Case
s = s[::-1]
i = 0
result = ""
while(i < len(s)-1):
    x = s[i] + s[i+1]
    if x == "32":
        result = result + " "
    elif int(x) in range(65, 91) or int(x) in range(97, 100):
        result = result + chr(int(x))
    elif i+2 < len(s):
        x = x+s[i+2]
        result = result + chr(int(x))
        i += 1
    i += 2
print(result)
