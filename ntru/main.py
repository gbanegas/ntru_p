import sys
sys.path.append("polynomials")

from intpolynomial import IntPolynomial

def main():
    pol = IntPolynomial()
    pol.mult(pol)


if __name__ == "__main__":
    main()
