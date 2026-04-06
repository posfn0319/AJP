# This is a work in progress.
# Average Jones Polynomial (AJP) Calculator
This repository contains the implementation of the algorithm for calculating the AJP of oriented knot shadows. (See: https://doi.org/10.5281/zenodo.18005335)

By factorizing the state sum into local weights, the algorithm computes the AJP in $O(2^n \cdot poly(n))$ time complexity, a significant improvement over the $O(4^n)$ complexity of the brute-force method.

## Features
* `trefoil.py`: Calculates the AJP of the shadow of the trefoil knot.
* To be added

## How to use
1. You'll need the `sympy` library to run `trefoil.py`.
```bash
pip install sympy
```
2. `git clone` this repository and run, or just copy and paste the source code and run.

## Example Output
Running `trefoil.py` will return the AJP of the shadow of the trefoil knot:
```
-0.125*A**16 + 0.125*A**12 + 0.125*A**4 + 0.75 + 0.125/A**4 + 0.125/A**12 - 0.125/A**16
```