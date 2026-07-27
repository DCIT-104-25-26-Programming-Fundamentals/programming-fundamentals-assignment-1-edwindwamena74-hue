# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


 # ---------------------------------------------------------
# Matrix Operations
# ---------------------------------------------------------


def read_matrix(rows, cols, name):
    print(f"\nEnter elements for Matrix {name}:")
    matrix = []

    for i in range(rows):
        row = []
        for j in range(cols):
            value = int(input(f"Enter element [{i+1}][{j+1}]: "))
            row.append(value)
        matrix.append(row)

    return matrix



def display_matrix(matrix, title):
    print(f"\n{title}")
    for row in matrix:
        for value in row:
            print(f"{value:6}", end="")
        print()



def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    result = []

    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        result.append(new_row)

    return result



def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])

    result = []

    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    return result



def multiply_matrices(matrix1, matrix2):
    rows_a = len(matrix1)
    cols_a = len(matrix1[0])
    cols_b = len(matrix2[0])

    result = []

    for i in range(rows_a):
        row = []
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += matrix1[i][k] * matrix2[k][j]
            row.append(total)
        result.append(row)

    return result

print("PART A - Matrix Transpose")

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = read_matrix(rows, cols, "A")

display_matrix(matrix, "Original Matrix")
display_matrix(transpose(matrix), "Transpose")



print("\nPART B - Matrix Addition")

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix1 = read_matrix(rows, cols, "A")
matrix2 = read_matrix(rows, cols, "B")

sum_matrix = add_matrices(matrix1, matrix2)

display_matrix(matrix1, "Matrix A")
display_matrix(matrix2, "Matrix B")
display_matrix(sum_matrix, "A + B")



print("\nPART C - Matrix Multiplication")

m = int(input("Enter rows of Matrix A (M): "))
n = int(input("Enter columns of Matrix A / rows of Matrix B (N): "))
p = int(input("Enter columns of Matrix B (P): "))

matrixA = read_matrix(m, n, "A")
matrixB = read_matrix(n, p, "B")

product = multiply_matrices(matrixA, matrixB)

display_matrix(matrixA, "Matrix A")
display_matrix(matrixB, "Matrix B")
display_matrix(product, "A x B")

