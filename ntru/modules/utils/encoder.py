import math

class Encoder(Object):
COEFF1_TABLE = [0, 0, 0, 1, 1, 1, -1, -1]
COEFF2_TABLE = [0, 1, -1, 0, 1, -1, 0, 1]

BIT1_TABLE = [1, 1, 1, 0, 0, 0, 1, 0, 1]
BIT2_TABLE = [1, 1, 1, 1, 0, 0, 0, 1, 0]
BIT3_TABLE = [1, 0, 1, 0, 0, 1, 1, 1, 0]
THREE = 3
    def encodeModQ(self, a, q):
        bits = math.floor(math.log(q, 2))
        numBits = len(a) * bits
        numBytes = (numBits+7) / 8
        data = []
        bitIndex = 0
        byteIndex = 0
        for i in xrange(0, len(a)):
            for j in xrange(0, len(bits)):
                current = (a[i] >> j) & 1
                data[byteIndex] |= currentBit << bitIndex
                if bitIndex == 7:
                    bitIndex = 0
                    byteIndex++
                else:
                    byteIndex++

        return data

    def encodeModQ(self, a, q):
        bits = math.floor(math.log(q, 2))
        numBits = len(a) * bits
        numBytes = (numBits+7) / 8
        data = []
        bitIndex = 0
        byteIndex = 0
        for i in xrange(0, len(a)):
            for j in xrange(0, len(bits)):
                current = (a[i] >> j) & 1
                data[byteIndex] |= currentBit << bitIndex
                if bitIndex == 7:
                    bitIndex = 0
                    byteIndex++
                    if byteIndex >= numBytes:
                        return data
                else:
                    byteIndex++

        return data


    def decodeModQ(self, data, n, q):
        bits = math.floor(math.log(q, 2))
        coeffs = []
        mask = (-1) >>> (32 - bits)
        byteIndex = 0
        bitIndex = 0
        coeffBuf = 0
        coeffBits = 0
        coeffIndex = 0
        while(coeffIndex < n):
            while (coeffBits < bits):
                coeffBuf += (data[byteIndex]&0xFF) << coeffBits
                coeffBits += 8 - bitIndex
                byteIndex++
                bitIndex = 0

            coeffs[coeffIndex] = coeffBuf & mask
            coeffIndex++
            coeffBuf >>>= bits
            coeffBits -= bits

        return coeffs
