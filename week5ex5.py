def diagonal_sum(matrix):
    """
    Calculate the sum of both diagonals of a square matrix.

    Counts the center element only once when the matrix dimension is odd.

    Args:
        matrix (list of list of numbers): An n x n square matrix.

    Returns:
        int or float: The sum of the primary and secondary diagonals.
    """
    n = len(matrix)
    total = 0

    for i in range(n):
        total += matrix[i][i]  
        total += matrix[i][n - 1 - i]  

    if n % 2 == 1:
        center = matrix[n // 2][n // 2]
        total -= center

    return total


if __name__ == "__main__":
    sample_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(diagonal_sum(sample_matrix)) 
