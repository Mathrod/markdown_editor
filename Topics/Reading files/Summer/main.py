#  write your code here
text = open("input.txt", "r")
count = 0
for x in text.readlines():
    print(x)
    if x == "summer\n":
        count += 1
        print(count)



file.close()
print(count)
