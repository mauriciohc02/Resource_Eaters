import time


if __name__ == '__main__':
    start = time.perf_counter()
    size = 1000
    numStrings = 1000000
    
    for i in range(size):
        # Creating a file named deleteMe(i).txt
        newFile = open("deleteMe" + str(i) + ".txt", "a")
        # Writing in the file a simple String
        newFile.write("This is the Example File Number " + str(i) + "\n")
        # Writing in the file n times
        for j in range(numStrings):
            newFile.write("[String " + str(j) + "] ")
        # Closing the file
        newFile.close()
        # Opening the file in read mode
        readFile = open("deleteMe" + str(i) + ".txt", "r")
        infoFile = readFile.read()
        
        time.sleep(10)

    # Execution time
    finish = time.perf_counter()
    print(f'\nFinished in {round(finish - start, 2)} second(s)')
