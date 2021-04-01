
from statistics import mean, stdev, median

path = "avocado.csv"                                # global variable to enable access inside or outside of the function

def readFile(header):
    """This readFile() is to access file and return with """

    with open(path) as infile:                      # with statement allows automatically close the file
        columnValue = getColumn(infile, header)     # call getColumn function to extract only specific header's column

        return columnValue


def getColumn(inFile, header):
    """This getColumn() is to retrieve values from the specific column called"""

    columnValue = []
    index = None

    for lineNum, line in enumerate(inFile):         # enumerate default column start with 0
        if lineNum == 0:                            # get header column
            headerLines = line.strip().split(",")   # clean inessential \n abd separate with comma

            i = 0
            for head in headerLines:
                if head == header:                  # find header position in the header row
                    index = i                       # store position in index variable
                i += 1

        else:

            noneHeaders = line.strip().split(",")  # the rest of rows will be determined and clean here

            k = 0
            for noneHeader in noneHeaders:
                if k == index:                     # at the same col with header
                    nonHeader = float(noneHeader)  # convert string to float type
                    columnValue.append(nonHeader)  # store in the list
                k += 1

    return columnValue


def meanHG(lineList):
    """This meanHG() is to calculate mean with homegrown formula, used in readAndComputeMean_HG function"""

    mean_hg = sum(lineList) / len(lineList)

    return mean_hg


def stdDevHG(lineList):
    """This stdDevHG() is to calculate standard deviation with homegrown formula,
    used in readAndComputeSD_HG function"""

    mean_hg = meanHG(lineList)
    std = sum((x - mean_hg) ** 2 for x in lineList)
    stdDev = std / (len(lineList) - 1)
    stdDevSqr = stdDev ** 0.5

    return stdDevSqr


def medianHG(lineList):
    """This medianHG() is to calculate median with homegrown formula,
    used in used in readAndComputeMedian_HG function"""

    lst = sorted(lineList)                              # rearrange list in ascending
    num = len(lineList)                                 # find size of the list

    if num % 2 == 0:
        med1 = lst[num // 2]
        med2 = lst[num // 2 - 1]
        med = (med1 + med2) / 2
    else:
        med = lst[num // 2]

    return med


def readAndComputeMean_SM(header):
    """This readAndComputeMean_SM() is to calculate mean by applying statistics module"""

    lineList = readFile(header)
    computedMean = mean(lineList)

    return computedMean


def readAndComputeSD_SM(header):
    """This readAndComputeSD_SM() is to calculate SD by applying statistics module"""

    lineList = readFile(header)
    computedSD = stdev(lineList)

    return computedSD


def readAndComputeMedian_SM(header):
    """This readAndComputeMedian_SM() is to calculate Median by applying statistics module"""

    lineList = readFile(header)
    computedMed = median(lineList)

    return computedMed


def readAndComputeMean_HG(header):
    """This readAndComputeSD_HG() is to calculate SD by applying meanHG function"""

    lineList = readFile(header)
    computedMean_HG = meanHG(lineList)

    return computedMean_HG


def readAndComputeSD_HG(header):
    """This readAndComputeSD_HG() is to calculate SD by applying stdDevHG function"""

    lineList = readFile(header)
    computedSD_HG = stdDevHG(lineList)

    return computedSD_HG


def readAndComputeMedian_HG(header):
    """This readAndComputeMedian_HG() is to calculate median by applying medianHG function"""

    lineList = readFile(header)
    computedMed_HG = medianHG(lineList)

    return computedMed_HG

def headerCol_MML(header):
    """This headerCol_MML() is to find index of header column"""

    index = 0
    with open(path) as infile:                                     # with statement to automatically close file
        line = infile.readline().strip().split(",")                # read and clean line

        for column in line:
            if column != header:                                   # not wanted column
                index += 1
            elif column == header:                                 # matched column
                index += 0

                return index

def readAndComputeMean_MML(header):
    """This readAndComputeMean_MML() is to calculate mean with least memory usage"""

    index = headerCol_MML(header)                                  # call headerCol_MML function to get index

    with open(path) as infile:

        sumColumn = 0
        count = 0

        for column in infile.readlines()[1:]:                      # begin iteration from row 1 - non-header
            line = column.strip().split(",")                       # clean inessential and separate with comma
            sumColumn += float(line[index])                        # store only sum value
            count += 1
        return sumColumn / count


def readAndComputeSD_MML(header):
    """This readAndComputeSD_MML() is to calculate SD with least memory usage"""

    index = headerCol_MML(header)                                  # call headerCol_MML function to get index
    meanMML = readAndComputeMean_MML(header)                       # utilize mean MML function

    with open(path) as infile:
        std = 0
        count = 1

        for column in infile.readlines()[1:]:                      # begin iteration from row 1 - non-header
            line = column.strip().split(",")
            value = float(line[index])
            std += (value - meanMML) ** 2                          # store the value of final variance before cal SD
            count += 1

        return (std / (count - 2)) ** 0.5


def minAndMax_MML(header):
    """This function is to find min and max values"""

    index = headerCol_MML(header)                                       # get index value

    with open(path) as file:

        file.readline()                                                 # header line
        minVal = float(file.readline().strip().split(',')[index])       # get minVal from specific column
        maxVal = minVal

        for line in file.readlines():                                   # iterate through line by line at a time
            val = float(line.strip().split(',')[index])
            if val < minVal:                                            # consider min value
                minVal = val                                            # if yes, store in minVal at a time
            if val > maxVal:                                            # consider max value
                maxVal = val                                            # if yes, store in maxVal at a time

        return minVal, maxVal


def readAndComputeMedian_MML(header):
    """This function is to apply the binary search concept for finding median"""

    index = headerCol_MML(header)
    minVal = minAndMax_MML(header)[0]                                   # get min value
    maxVal = minAndMax_MML(header)[1]                                   # get max value

    with open(path) as file:

        while minVal != maxVal:                                        # loop while min not equal max

            upper = 0                                                  # count of upper element
            lower = 0                                                  # count of lower element
            midVal = minVal + (maxVal-minVal) / 2                      # mid value
            newMin = maxVal
            newMax = minVal

            file.seek(0)                                               # set file's position at 0th
            file.readline()                                            # read header row

            for line in file:
                element = float(line.strip().split(",")[index])

                if element < midVal:                                   # element goes left
                    lower += 1                                         # adding 1, if element less than midVal
                    if element > newMax:                               # if element greater than minVal
                        newMax = element                               # update newMax boundary
                if element >= midVal:                                  # element goes right
                    upper += 1                                         # adding 1, if element more or equal midVal
                    if element < newMin:                               # if element within maxVal
                        newMin = element                               # update newMin boundary

            if upper == lower:
                return newMin
            if upper > lower:
                minVal = newMin
            if upper < lower:
                maxVal = newMax

        return minVal


def testCode(x, y, z):
    """This testCode function is to compare all values in different methods"""

    if (x == y) and (x == z):
        return True
    else:
        return False


def main():
    """This is a main function where organized entire program to compare values of different methods"""

    a = 'Total Volume'
    meanSM = round(readAndComputeMean_SM(a))
    meanHG = round(readAndComputeMean_HG(a))
    meanMML = round(readAndComputeMean_MML(a))
    if testCode(meanSM, meanHG, meanMML):
        print("-" * 55)
        print("Value of Mean in SD = {}, HG = {}, MML = {}".format(meanSM, meanHG, meanMML))
        print("All means are equal!")
        print("-" * 55)
    else:
        print("Means are not equal")
    sdSM = round(readAndComputeSD_SM(a))
    sdHG = round(readAndComputeSD_HG(a))
    sdMML = round(readAndComputeSD_MML(a))
    if testCode(sdSM, sdHG, sdMML):
        print("Value of SD in SD = {}, HG = {}, MML = {}".format(sdSM, sdHG, sdMML))
        print("All SD are equal!")
        print("-" * 55)
    else:
        print("SD are not equal")
    medSM = round(readAndComputeMedian_SM(a))
    medHG = round(readAndComputeMedian_HG(a))
    medMML = round(readAndComputeMedian_MML(a))
    if testCode(medSM, medHG, medMML):
        print("Value of Median in SD = {}, HG = {}, MML = {}".format(medSM, medHG, medMML))
        print("All median are equal!")
        print("-" * 55)
    else:
        print("Medians are not equal")


if __name__ == "__main__":

    main()




