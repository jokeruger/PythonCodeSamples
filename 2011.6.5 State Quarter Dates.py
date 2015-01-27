#Analyze state quarter data input from a file
#Written by Joe Kruger

def main():
    stateQuarters = open("StateQuarters.txt","r")
    listOfLists = file2list(stateQuarters)
    itGoesToEleven(listOfLists)
    march(listOfLists)
    printN(listOfLists)
    emptyMonths(listOfLists)
    normalizeDate(listOfLists)

    stateQuarters.close()

#Change raw data input file to a list of groups of values for each state
def file2list(infile):
    stateList = []
    for line in infile:
        if line [0:5] == 'State':
            continue
        lineList = line.strip().split(',')
        stateList.append(lineList)
    return stateList

#Print the states whose names are 11 or more characters in length
def itGoesToEleven(listOfLists):
    print('States with names longer than 11 characters:')
    for state in range(0, 50):
        if len(listOfLists[state][0])>=11:
            print(listOfLists[state][0])

#Print alphabetically the states that became states in March
def march(listOfLists):
    print('\nStates that became states in March:')
    for state in range(0, 50):
        dateString = listOfLists[state][2]
        if 'Mar' in dateString:
            print(listOfLists[state][0])

#Print the states whose names begin with ‘N’ and their statehood dates
def printN(listOfLists):
    print()
    print('''Name and statehood date of those beginning with 'N':''')
    for state in range(0,50):
        if listOfLists[state][0][0]=='N':
            if len(listOfLists[state][0])<7:
                print(listOfLists[state][0],'\t\t',listOfLists[state][2])
            else:
                print(listOfLists[state][0],'\t',listOfLists[state][2])

#Print months when no quarters were issued
def emptyMonths(listOfLists):
    badChars = ['0','1','2','3','4','5','6','7','8','9','-']
    monthAbbreviations = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    monthAccumulator = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print('\nMonths in which no quarters were issued:')
    for state in range(0,50):
        month = listOfLists[state][1]       #month's current format is '25-Oct-04'
        for char in month:
            if char in badChars:            #trims it down to 'Oct'
                month = month.replace(char, '')
        
        monthAccumulator[monthAbbreviations.index(month)] +=1   #finds index of Oct, and increases it's count
    for index in range(12):
        if monthAccumulator[index]==0:
            print(monthAbbreviations[index])

#Print state names where the month of the quarter issue and the month of statehood are the same
def normalizeDate(listOfLists):
    monthAbbreviations = [None,'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    normalizedList = []
    for line in listOfLists:
        ymd = ''
        normalizedLine = []
        lineDate = line[2]                  #'14-Dec-1819'
        dateList = lineDate.split('-')      #['14', 'Dec', '1819']
        if dateList[1] in line[1]:
            ymd += dateList[2]              #1819
            monthNum = monthAbbreviations.index(dateList[1])
            if len(str(monthNum))==1:
                monthNum = '0'+str(monthNum)
            ymd += str(monthNum)            #181912
            ymd += dateList[0]              #18191214
            normalizedLine.append(ymd)      #['18191214']
            normalizedLine.append(line[0])  #['18191214', 'Alabama']
            normalizedList.append(normalizedLine)   #[['18191214', 'Alabama'], ['19590103', 'Alaska'], etc.]
        
    chronological = sorted(normalizedList)
    print('\nStates with quarters issued in the same month they achieved statehood:')
    for state in chronological:
        print(state[1])
    
main()
