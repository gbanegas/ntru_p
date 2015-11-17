import sys

sys.path.append("polynomials")
sys.path.append("utils")
sys.path.append("encrypt")

from intpolynomial import IntPolynomial
from encoder import Encoder
from ntruencrypt import NTRUEncrypt

def main():
    pol = IntPolynomial()
    pol.mult(pol)
    ntru = NTRUEncrypt()
    encoder_1 = Encoder


if __name__ == "__main__":
    main()
