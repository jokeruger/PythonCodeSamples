#Program to change format of addresses imported from a file
#Written by Joe Kruger


# get the file names
infileName = input("What file holds the input data? ")
outfileName = input("What file will hold the output? ")

# open the files
infile = open(infileName, 'r')
outfile = open(outfileName, 'w')

# tests each line in the file, and changes it accordingly
for line in infile:
    line=line.upper()

    #check if each line is a name
    hasNum = 0
    for char in line:
        if char.isdigit()==1:
            hasNum=1
            
    #depending on the type of line read, reformat it
    if hasNum==0:                   #if the line has no numbers, it's a name
            first, last = line.rsplit(' ',1)
            last = last.strip()     #the last name has a new line character attached to the end of it
            newLine = last + ', ' + first + '\n'
        
    elif line[0].isdigit()==0:      #if the first character is a number, it's a street address
        city, zipcode = line.rsplit(' ',1)
        newLine = city + '\n' + zipcode + '\n'
    else:                           #if it has a number anywhere else, it's a city/state/zip
        newLine = line
    outfile.write(newLine)

print("The data in",infileName,end='')
print("has been reformatted and written to", outfileName, "as follows:\n")

# close both files
infile.close()
outfile.close()

#print the results
printfile = open(outfileName, 'r')
for line in printfile:
    print (line, end='')
printfile.close()
