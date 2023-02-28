def readArrFromFile():
    f = open('input.txt')
    array = [int(i) for i in f.readline().split()]
    f.close()
    return array

def writeAnswerToFile(array):
    f = open("output.txt", 'w')
    f.write(str((array)))

def arrayToTuple(array):
    return tuple(array)


def findD(a1, a2, i, j):
    return ((a2 - a1)/(j-i))


def main():
    arr = readArrFromFile()
    tup = arrayToTuple(arr)
    dictt = { }
    for i in range(len(tup) - 1):
        for j in range(1, len(tup)):

    return 0



print("Press F to start programm:")
main()
