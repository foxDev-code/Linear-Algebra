# [1st] Did not calculate Algebraic Multiplicity (AM)
# → No count of how many times each eigenvalue repeats
# Did not calculate Geometric Multiplicity (GM)
# → No check for number of independent eigenvectors
# Did not verify AM = GM condition
# → Main requirement for diagonalizability was missing
# Used only numerical check (reconstruction)
# → Not a proper mathematical proof of diagonalizability

# ----->>


# import numpy as np

# size_of_matrix = int(input("Enter matrix size (n x n): "))

# print("enter matrix values row:")
# data = []

# for r in range(size_of_matrix):
#     values = []
#     for x in input().split():
#         values.append(float(x))
#     data.append(values)

# M = np.array(data)

# value, vector= np.linalg.eig(M)

# print("\n eigenvalues:\n", value)
# print("\n eigenvectors:\n", vector)

# D_matrix = np.diag(value)

# P = vector
# P_inverse = np.linalg.inv(P)

# reconstructed = P @ D_matrix @ P_inverse    # @ - multiplication

# return_boolean = np.allclose(M, reconstructed)         # accuracy of matrix (return_boolean is variable name and whole lines give True or False)(np.allclose check euality between M, reconstructed matrix) 

# if return_boolean:
#     print("\n matrix is Diagonalizable")
# else:
#     print("\n matrix is NOT Diagonalizable")

# if return_boolean:
#     power = int(input("\nEnter power (n) for A^n: "))
#     D_n = D_matrix**power
#     A_n = P @ D_n @ P_inverse

#     print(f"\nA^{power} =\n", A_n)










# [2nd] code we are changing these things:----
# Add a check to ensure each row has exactly the required number of values (to avoid wrong input).
# Add a check to confirm the matrix is square before proceeding.
# Display eigenvalues in a rounded/clean format for better readability.
# Clearly indicate whether eigenvalues are distinct or repeated.
# Check and display whether eigenvectors are linearly independent.
# Handle the case where matrix P is not invertible (to avoid runtime errors).
# Show the result of A^{power n } in a rounded and cleaner format

# --->>

import numpy as np

size_of_matrix = int(input("Enter matrix size (n x n): "))

print("enter matrix values row:")
data = []

for r in range(size_of_matrix):
    values = []
    for x in input().split():
        values.append(float(x))
    data.append(values)

M = np.array(data)

value, vector= np.linalg.eig(M)

print("\n eigenvalues:\n", value)
print("\n eigenvectors:\n", vector)


# Algebraic Multiplicity (AM)
unique_vals, counts = np.unique(np.round(value, 5), return_counts=True)

print("\nEigenvalue Analysis:")
for i in range(len(unique_vals)):
    print(f"Eigenvalue {unique_vals[i]} has Algebraic Multiplicity (AM) =", counts[i])





# Geometric Multiplicity (GM)

def geometric_multiplicity(matrix, eigenvalue):
    I = np.eye(matrix.shape[0])
    A_lambda = matrix - eigenvalue * I
    rank = np.linalg.matrix_rank(A_lambda)
    GM = matrix.shape[0] - rank
    return GM

print("\nChecking Algebraic vs Geometric Multiplicity:")

diagonalizable_flag = True

for i in range(len(unique_vals)):
    eig = unique_vals[i]
    AM = counts[i]
    GM = geometric_multiplicity(M, eig)

    print(f"Eigenvalue {eig}: AM = {AM}, GM = {GM}")

    if AM != GM:
        diagonalizable_flag = False



# Your Original Code (UNCHANGED)
D_matrix = np.diag(value)

P = vector
P_inverse = np.linalg.inv(P)

reconstructed = P @ D_matrix @ P_inverse

return_boolean = np.allclose(M, reconstructed)




# Final Decision (Improved using AM = GM)
if diagonalizable_flag:
    print("\n matrix is Diagonalizable")
else:
    print("\n matrix is NOT Diagonalizable")





# Power Calculation

if diagonalizable_flag:
    power = int(input("\nEnter power (n) for A^n: "))
    D_n = np.diag(value**power)
    A_n = P @ D_n @ P_inverse

    print(f"\nA^{power} =\n", A_n)

# 
#     # Summary of this whole process:---

#     1 ---> basically this code takes an n × n matrix input from the user and it works on numPy library
#     2--> and then  calculates the matrix eigenvalues and eigenvectors 
#     3--> then it forms P (eigenvectors matrix) and D (diagonal matrix of eigenvalues)
#     4--> then vo check krta hai PDP inverse hai or satisfy krta hai ya nahi or agar vo karta hai then the matrix is diagonalizable
#     5--> agar vo digonalizable hai to A^{power n } = PD^n P inverse matrix 

#     So this is our program of diagonalizable matrix in linear algebra
