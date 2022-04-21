import random
import time


def randomMatrix(matrixSize, size):
    # Initializing the matrix
    matrix = [[0 for _ in range(matrixSize)] for _ in range(matrixSize)]
    # Filling the matrix with random integers
    for i in range(matrixSize):
        for j in range(matrixSize):
            matrix[i][j] = random.randint(0, size)

    return matrix


def sumMatrix(matrixSize, matrixA, matrixB):
    # Initializing the matrix
    results = [[0 for _ in range(matrixSize)] for _ in range(matrixSize)]
    # Filling the matrix with the sum of the matrices
    for i in range(matrixSize):
        for j in range(matrixSize):
            results[i][j] = matrixA[i][j] + matrixB[i][j]

    return results


if __name__ == '__main__':
    start = time.perf_counter()
    size = 100000
    matrixSize = 40

    for i in range(size):
        # Creating the first matrix
        matrixA = randomMatrix(matrixSize, size)
        # Creating the second matrix
        matrixB = randomMatrix(matrixSize, size)
        # Adding both matrices
        matrixC = sumMatrix(matrixSize, matrixA, matrixB)
        # 10 seconds delay every 1000 iterations
        if i % 1000 == 0:
            time.sleep(10)
    
    # Execution time
    finish = time.perf_counter()
    print(f'\nFinished in {round(finish - start, 2)} second(s)')
