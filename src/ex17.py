from sys import argv
from os.path import exists

script,from_file,to_file = argv

print(f"Copying from {from_file} to {to_file}")
in_file = open(from_file)
in_data = in_file.read()

print(f"The input is {len(in_data)} bytes long")
print(f"Does the output file exist?{exists(to_file)}")
print(f"Does the input file exist? {exists(from_file)}")
print("Ready , hit RETURN to continue, CTRL-C to abort")
input("?")

out_file = open(to_file,'w')
out_file.write(in_data)
print("Done")
out_file.close()
in_file.close()

