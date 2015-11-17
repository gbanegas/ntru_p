
import array

class Curve25519():

    KEY_SIZE = 32

    ZERO = bytes([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    ORDER = bytes([237, 211, 245, 92, 26,  99,  18,  88, 214, 156, 247, 162,222, 249, 222, 20,0,   0,   0,   0, 0,   0,   0,   0, 0,   0,   0,   0, 0,   0,   0, 16])
    PRIME = bytes([237, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 127])

    def clamp(self, k):
        k[31] &= 0x7F
		k[31] |= 0x40
		k[ 0] &= 0xF8

    def unpack(self, dx, m):
        dx[0] = ((m[0] & 0xFF)) | ((m[1] & 0xFF))<<8 | (m[2] & 0xFF)<<16 | ((m[3] & 0xFF)& 3)<<24;
        dx[1] = ((m[3] & 0xFF)&~ 3)>>2  | (m[4] & 0xFF)<<6 | (m[5] & 0xFF)<<14 | ((m[6] & 0xFF)& 7)<<22
        dx[2] = ((m[6] & 0xFF)&~ 7)>>3  | (m[7] & 0xFF)<<5 | (m[8] & 0xFF)<<13 | ((m[9] & 0xFF)&31)<<21
        dx[3] = ((m[9] & 0xFF)&~31)>>5  | (m[10] & 0xFF)<<3 |	(m[11] & 0xFF)<<11 | ((m[12] & 0xFF)&63)<<19
        dx[4] = ((m[12] & 0xFF)&~63)>>6 | (m[13] & 0xFF)<<2 |	(m[14] & 0xFF)<<10 |  (m[15] & 0xFF)    <<18
        dx[5] = (m[16] & 0xFF) | (m[17] & 0xFF)<<8 | (m[18] & 0xFF)<<16 | ((m[19] & 0xFF)& 1)<<24
        dx[6] = ((m[19] & 0xFF)&~ 1)>>1 | (m[20] & 0xFF)<<7 | (m[21] & 0xFF)<<15 | ((m[22] & 0xFF)& 7)<<23
        dx[7] = ((m[22] & 0xFF)&~ 7)>>3 | (m[23] & 0xFF)<<5 |	(m[24] & 0xFF)<<13 | ((m[25] & 0xFF)&15)<<21
        dx[8] = ((m[25] & 0xFF)&~15)>>4 | (m[26] & 0xFF)<<4 | 	(m[27] & 0xFF)<<12 | ((m[28] & 0xFF)&63)<<20
        dx[9] = ((m[28] & 0xFF)&~63)>>6 | (m[29] & 0xFF)<<2 | (m[30] & 0xFF)<<10 |  (m[31] & 0xFF)<<18


    def set(self, dx, n):
        dx[0] = n
        dx[1] = 0
        dx[2] = 0
        dx[3] = 0
        dx[4] = 0
        dx[5] = 0
        dx[6] = 0
        dx[7] = 0
        dx[8] = 0
        dx[9] = 0

    def add(self, xy, x, y):
        xy[0] = x[0] + y[0]
        xy[1] = x[1] + y[1]
        xy[2] = x[2] + y[2]
        xy[3] = x[3] + y[3]
        xy[4] = x[4] + y[4]
        xy[5] = x[5] + y[5]
        xy[6] = x[6] + y[6]
        xy[7] = x[7] + y[7]
        xy[8] = x[8] + y[8]
        xy[9] = x[9] + y[9]

    def sub(self, xy, x, y):
        xy[0] = x[0] - y[0]
        xy[1] = x[1] - y[1]
        xy[2] = x[2] - y[2]
        xy[3] = x[3] - y[3]
        xy[4] = x[4] - y[4]
        xy[5] = x[5] - y[5]
        xy[6] = x[6] - y[6]
        xy[7] = x[7] - y[7]
        xy[8] = x[8] - y[8]
        xy[9] = x[9] - y[9]

    def cpy(self, out, ins):
        out[0] = ins[0]
        out[1] = ins[1]
        out[2] = ins[2]
        out[3] = ins[3]
        out[4] = ins[4]
        out[5] = ins[5]
        out[6] = ins[6]
        out[7] = ins[7]
        out[8] = ins[8]
        out[9] = ins[9]

    def mul(self, xy, x, y):
        long t = (x[0]*y[8]) + (x[2]*y[6]) + (x[4]*y[4]) + (x[6]*y[2]) + (x[8]*y[0])+2*((x[1]*y[7])+(x[3]*y[5])+(x[5]*y[3])+(x[7]*y[1])) + 38*(x[9]*y[9]);

    def mont_prep(self, t1, t2, ax, az):
        self.add(t1, ax, az)
        self.sub(t2, ax, az)

    def mont_add(self, t1, t2, t3, t4, ax, az, dx):
        self.mul(ax, t2, t3)
        self.mul(az, t1, t4)
        self.add(t1,ax,az)
        self.sub(t2, ax, az)
        self.sqr(ax, t1)
        self.sqr(t1, t2)
        self.mul(az, t1, dx)


    def keygen(self, P, s, k):
        self.clamp(k)
        self.core(P, s, k, None)

    def curve(self, Z, k, P):
        self.core(Z, None, k, P)

    def core(self, Px, s, k, Gx):
        dx = array.array('L')
        t1 = array.array('L')
        t2 = array.array('L')
        t3 = array.array('L')
        t4 = array.array('L')

        x = array.array('L', array.array('L'))
        z = array.array('L', array.array('L'))

        if Gx <> None:
            self.unpack(dx, Gx)
        else:
            self.set(dx, 9)

        self.set(x[0], 1)
        self.set(z[0], 0)

        for i in xrange(32,-1,-1):
            for j in xrange(8,0,-1):
                bit1 = (k[i] & 0xFF) >> j & 1
                bit0 = not(k[i] & 0xFF) >> j & 1
                ax = array.array('L', x[bit0])
                az = array.array('L', z[bit0])
                bx = array.array('L', x[bit1])
                bz = array.array('L', z[bit1])
                self.mont_prep(t1, t2, ax, az)
                self.mont_prep(t3, t4, bx, bz)
                self.mont_add(t1, t2, t3, t4, ax, az, dx)
                self.mont_tbl(t1, t2, t3, t4, bx, bz)
