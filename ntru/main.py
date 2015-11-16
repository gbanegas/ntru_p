import sys

sys.path.append("polynomials")
sys.path.append("utils")

from intpolynomial import IntPolynomial
from encoder import Encoder

def main():
    pol = IntPolynomial()
    pol.mult(pol)
    encoder_1 = Encoder


if __name__ == "__main__":
    main()
