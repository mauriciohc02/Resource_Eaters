import random
import time


def randomList(size):
    dataList = []
    # Filling the List with random floats
    for _ in range(size):
        # Getting a random float with limited decimal
        numRandom = round(random.uniform(-size, size), 3)
        # Appending the number gotten
        dataList.append(numRandom)

    return dataList


def bubbleSort(dataList):
    listSize = len(dataList)
    # Loop to access each List element
    for i in range(listSize):
        # Loop to compare List elements
        for j in range(listSize - i - 1):
            # Comparing two elements
            if dataList[j] > dataList[j + 1]:
                # Swapping elements
                dataList[j], dataList[j + 1] = dataList[j + 1], dataList[j]

    return dataList


if __name__ == '__main__':
    start = time.perf_counter()
    # List size
    size = 500000
    # Creating a List with random numbers
    data = randomList(size)
    print("Our List!")
    print(data)
    # Getting a new List with sorted data
    sortedData = bubbleSort(data)
    print("Sorted List in Ascending Order!")
    print(sortedData)

    # Execution time
    finish = time.perf_counter()
    print(f'\nFinished in {round(finish - start, 2)} second(s)')
