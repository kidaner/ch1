file = open("spider.txt")

print(file.readline())
print(file.read())
file.close()

with open("spider.txt") as file:
    for line in file:
        print(line.strip().upper())

with open("novel.txt", "w") as novel:
    novel.write("It was a dark and stormy night")
