import sys

your_ideas_file =open("ideabank.txt", "a")
your_ideas_file.writelines(input("New best idea? :) : ")+ "\n")
your_ideas_file.close

your_ideas_file =open("ideabank.txt", "r")
print("\nYour ideabank: ")
idea_list = your_ideas_file.readlines()
count = 1
for line in idea_list:

    print(str(count) + ". ",end='' )
    print(line.strip())
    count +=1
your_ideas_file.close
print()
