from params import Params
from polynomials.intpolynomial import IntPolynomial
from polynomials.densepoly import DesePolynomial
class NTRUEncrypt():


    def generateKeyPair(self):
        self.N = 439
        self.q = 2048
        self.df = Params.APR2011_439_FAST[2]
        self.df1 = 9
        self.df2 = 8
        self.df3 = 5
        self.dg = 146
        self.fastFp = True
        self.sparse = True
        self.polyType = "SIMPLE"

        self.t = IntPolynomial()
        self.fq = IntPolynomial()
        self.fp = IntPolynomial()

        self.g = self.generateG();




    def generateG(self):
        temp = DensePolynomial()
        return temp.generateRandom(self.n, self.dg, self.dg-1)
