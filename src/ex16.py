from sys import argv
script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C(^C).")
print("If you do want that , hit RETURN")
input("?")
print("Opening the file...")
target = open(filename,'w')
print("Truncating the file. GoodBye!")
target.truncate()

line = input("Enter a line that you want to write to the file and hit RETURN: ")
target.write(line)
target.write("\n")
print("And we finally close the file.")
target.close()



