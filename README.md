# Matrix Diagonalizability Checker

This project contains a Python script that checks whether an input square matrix is diagonalizable using eigenvalues and eigenvectors. It also computes the matrix power A^n when the matrix is diagonalizable.

## Overview

The script performs the following key steps:

1. Reads the dimension `n` for an `n x n` matrix.
2. Accepts `n` rows of matrix entries from the user.
3. Uses NumPy to compute eigenvalues and eigenvectors.
4. Calculates algebraic multiplicity (AM) for each eigenvalue.
5. Computes geometric multiplicity (GM) using the null space dimension of `(A - λI)`.
6. Compares AM and GM to decide if the matrix is diagonalizable.
7. Optionally computes `A^power` when the matrix is diagonalizable.

## File

- `code.py` - main Python script for matrix diagonalizability checking.

## Requirements

- Python 3.x
- NumPy

Install NumPy with pip if needed:

```bash
pip install numpy
```

## How to Run

Open a terminal in the project folder and execute:

```bash
python code.py
```

Then follow the prompts:

1. Enter the matrix size, for example `3` for a 3×3 matrix.
2. Enter each matrix row on a new line, with values separated by spaces.
3. The script prints eigenvalues, eigenvectors, and multiplicity analysis.
4. If the matrix is diagonalizable, it prompts for a power `n` and prints `A^n`.

## Example Input

For a 2×2 matrix:

```text
Enter matrix size (n x n): 2
enter matrix values row:
1 2
3 4
```

## What the Script Checks

### Algebraic Multiplicity (AM)

- AM is the number of times an eigenvalue appears in the characteristic polynomial.
- The script counts repeated eigenvalues using NumPy output.

### Geometric Multiplicity (GM)

- GM is the dimension of the eigenspace for a given eigenvalue.
- It is computed as:
  - `GM = n - rank(A - λI)`
- A matrix is diagonalizable only if, for every eigenvalue, `AM = GM`.

### Diagonalizability Decision

The script prints whether the matrix is diagonalizable based on the AM = GM condition.

It also performs a reconstruction step using `P @ D @ P_inverse` to validate the diagonalization process.

## Limitations and Notes

- The script assumes the input matrix is square and numeric.
- It does not validate row length or the squareness of the matrix before processing.
- The eigenvector matrix `P` must be invertible for the reconstruction step to work.
- If eigenvalues are repeated and eigenvectors are not independent, the matrix is not diagonalizable.

## Suggested Improvements

The current script can be enhanced by:

- validating that each input row has the correct number of entries,
- checking that the matrix is square before computing eigenvalues,
- handling singular matrix `P` inversion errors,
- formatting printed results with rounding for readability,
- checking eigenvector independence explicitly when repeated eigenvalues appear.

## Mathematical Background

A matrix `A` is diagonalizable if it can be written as:

```text
A = P D P^{-1}
```

where:

- `D` is a diagonal matrix of eigenvalues,
- `P` is a matrix whose columns are linearly independent eigenvectors of `A`.

For an `n × n` matrix, diagonalizability requires that for every eigenvalue `λ`, the algebraic multiplicity equals the geometric multiplicity.

## Contact

This README is generated to explain the purpose and behavior of the project. If you want to extend the script, use the notes in the `Suggested Improvements` section as a starting point.
