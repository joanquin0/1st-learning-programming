"""Write a script named numberlines.py. This script creates a program listing from a source program.
This script should prompt the user for the names of two files."""

Name = input("Enter filename of file: ")
theFile = open(Name, 'r')
lines = theFile.readlines()
theFile.close()

outtext = ['%d %s' % (i, line) for i, line in enumerate(lines)]
outfile = open("the new" + Name, "w")
outfile.writelines(str("".join(outtext)))

outfile.close()
