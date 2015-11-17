from random import shuffle
from intpolynomial import IntPolynomial

class DesePolynomial(IntPolynomial):

    def __init__(self):
        pass


    def generateRandom(self, N, numOne, numNeg):
        coeffs_1 = [1]*numOne
        coeffs_negative = [-1]*numNeg
        coeffs = coeffs_1 + coeffs_negative
        while len(coeffs) < N:
            coeffs.append(0)

        coeffs_shuffled = shuffle(coeffs)

        return DesePolynomial(coeffs)
