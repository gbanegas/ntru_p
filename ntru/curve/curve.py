
import array

class Curve25519():

    KEY_SIZE = 32
    P25=33554431
    P26=67108863

    ZERO = bytes([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    ORDER = bytes([237, 211, 245, 92, 26,  99,  18,  88, 214, 156, 247, 162,222, 249, 222, 20,0,   0,   0,   0, 0,   0,   0,   0, 0,   0,   0,   0, 0,   0,   0, 16])
    PRIME = bytes([237, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 127])
    ORDER_TIMES_8 = bytes([104, 159, 174, 231, 210, 24,  147, 192, 178, 230, 188, 23, 245, 206, 247, 166, 0,   0,   0,   0, 0,   0,   0,   0, 0,   0,   0,   0,  0,   0,   0,   128])
    BASE_R2Y = array.array('L',[5744, 8160848, 4790893, 13779497, 35730846, 12541209, 49101323, 30047407, 40071253, 6226132])

    def clamp(self, k):
        k[31] = k[31] & 0x7F
        k[31] = k[31] | 0x40
        k[0] = k[0] & 0xF8

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
        dx.insert(0, n)
        dx.insert(1, 0)
        dx.insert(2, 0)
        dx.insert(3, 0)
        dx.insert(4, 0)
        dx.insert(5, 0)
        dx.insert(6, 0)
        dx.insert(7, 0)
        dx.insert(8, 0)
        dx.insert(9, 0)


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
        t = (x[0]*y[8]) + (x[2]*y[6]) + (x[4]*y[4]) + (x[6]*y[2]) + (x[8]*y[0])
        t2 =  2*((x[1]*y[7])+(x[3]*y[5])+(x[5]*y[3])+(x[7]*y[1])) + 38*(x[9]*y[9])
        t = t + t2
        xy[8] = (t & ((1 << 26) - 1))
        t = (t >> 26)+(x[0]*y[9])+(x[1]*y[8])+(x[2]*y[7])+(x[3]*y[6]) + (x[4]*y[5]) + (x[5]*y[4])+(x[6]*y[3])+(x[7]*y[2])+(x[8]*y[1])+(x[9]*y[0])
        xy[9] = (t & ((1 << 25) - 1))
        t = (x[0]*y[0]) + 19 * ((t >> 25) + (x[2]*y[8]) + (x[4]*y[6])	+ (x[6]*y[4]) + (x[8]*y[2])) + 38*((x[1]*y[9]) + (x[3]*y[7]) + (x[5]*y[5]) + (x[7]*y[3]) + (x[9]*y[1]))
        xy[0] = (t & ((1 << 26) - 1))
        t = (t >> 26) + (x[0]*y[1]) + (x[1]*y[0]) + 19 * ((x[2]*y[9])+ (x[3]*y[8]) + (x[4]*y[7]) + (x[5]*y[6]) +(x[6]*y[5]) + (x[7]*y[4]) + (x[8]*y[3]) +	(x[9]*y[2]))
        xy[1] = (t & ((1 << 25) - 1))
        t = (t >> 25) + (x[0]*y[2]) + (x[2]*y[0]) + 19 * ((x[4]*y[8]) + (x[6]*y[6]) + (x[8]*y[4])) + 2 * (x[1]*y[1]) + 38 * ((x[3]*y[9]) + (x[5]*y[7]) + (x[7]*y[5]) + (x[9]*y[3]))
        xy[2] = (t & ((1 << 26) - 1))
        t = (t >> 26) + (x[0]*y[3]) + (x[1]*y[2]) + (x[2]*y[1]) +(x[3]*y[0]) + 19 * ((x[4]*y[9]) + (x[5]*y[8]) +(x[6]*y[7]) + (x[7]*y[6]) +(x[8]*y[5]) + (x[9]*y[4]))
        xy[3] = (t & ((1 << 25) - 1))
        t2 = 2 * ((x[1]*y[3]) + (x[3]*y[1])) + 38 *((x[5]*y[9]) + (x[7]*y[7]) + (x[9]*y[5]))
        t = (t >> 25) + (x[0]*y[4]) + (x[2]*y[2]) + (x[4]*y[0]) + 19 *((x[6]*y[8]) + (x[8]*y[6])) + t2
        xy[4] = (t & ((1 << 26) - 1))
        t2 = (x[4]*y[1]) + (x[5]*y[0]) +  19 *((x[6]*y[9]) + (x[7]*y[8]) + (x[8]*y[7]) + (x[9]*y[6]))
        t = (t >> 26) + (x[0]*y[5]) + (x[1]*y[4]) + (x[2]*y[3]) +(x[3]*y[2]) + t2
        xy[5] = (t & ((1 << 25) - 1))
        t = (t >> 25) + (x[0]*y[6]) + (x[2]*y[4]) + (x[4]*y[2]) +(x[6]*y[0]) + 19 * (x[8]*y[8]) + 2 * ((x[1]*y[5]) +(x[3]*y[3]) + (x[5]*y[1])) + 38 *((x[7]*y[9]) + (x[9]*y[7]))
        xy[6] = (t & ((1 << 26) - 1))
        t = (t >> 26) + (x[0]*y[7]) + (x[1]*y[6]) + (x[2]*y[5]) +(x[3]*y[4]) + (x[4]*y[3]) + (x[5]*y[2]) +(x[6]*y[1]) + (x[7]*y[0]) + 19 * ((x[8]*y[9]) +(x[9]*y[8]))
        xy[7] = (t & ((1 << 25) - 1))
        t = (t >> 25) + xy[8]
        xy[8] = (t & ((1 << 26) - 1))
        xy[9] += (t >> 26)
        return xy

    def sqr(self, x2, x):
        t = (x[4]*x[4]) + 2 * ((x0*x[8]) + (x2*x6)) + 38 *(x[9]*x[9]) + 4 * ((x1*x[7]) + (x3*x5));
        x2[8] = (t & ((1 << 26) - 1));
        t = (t >> 26) + 2 * ((x0*x[9]) + (x1*x[8]) + (x2*x[7]) +(x3*x6) + (x[4]*x5))
        x2[9] = (t & ((1 << 25) - 1));
        t = 19 * (t >> 25) + (x0*x0) + 38 * ((x2*x[8]) + (x[4]*x6) + (x5*x5)) + 76 * ((x1*x[9])	+ (x3*x[7]));
        x2[0] = (t & ((1 << 26) - 1));
        t = (t >> 26) + 2 * (x0*x1) + 38 * ((x2*x[9]) +	(x3*x[8]) + (x[4]*x[7]) + (x5*x6));
        x2[1] = (t & ((1 << 25) - 1));
        t = (t >> 25) + 19 * (x6*x6) + 2 * ((x0*x2) +(x1*x1)) + 38 * (x[4]*x[8]) + 76 *((x3*x[9]) + (x5*x[7]));
        x2[2] = (t & ((1 << 26) - 1));
        t = (t >> 26) + 2 * ((x0*x3) + (x1*x2)) + 38 *((x[4]*x[9]) + (x5*x[8]) + (x6*x[7]));
        x2[3] = (t & ((1 << 25) - 1));
        t = (t >> 25) + (x2*x2) + 2 * (x0*x[4]) + 38 *((x6*x[8]) + (x[7]*x[7])) + 4 * (x1*x3) + 76 *(x5*x[9]);
        x2[4] = (t & ((1 << 26) - 1));
        t = (t >> 26) + 2 * ((x0*x5) + (x1*x[4]) + (x2*x3))+ 38 * ((x6*x[9]) + (x[7]*x[8]));
        x2[5] = (t & ((1 << 25) - 1));
        t = (t >> 25) + 19 * (x[8]*x[8]) + 2 * ((x0*x6) +(x2*x[4]) + (x3*x3)) + 4 * (x1*x5) +	76 * (x[7]*x[9]);
        x2[6] = (t & ((1 << 26) - 1));
        t = (t >> 26) + 2 * ((x0*x[7]) + (x1*x6) + (x2*x5) +(x3*x[4])) + 38 * (x[8]*x[9]);
        x2[7] = (t & ((1 << 25) - 1));
        t = (t >> 25) + x2[8];
        x2[8] = (t & ((1 << 26) - 1));
        x2[9] += (t >> 26);
        return x2

    def mul_small(self, xy, x, y):
		t = (x[8]*y);
		xy[8] = (t & ((1 << 26) - 1));
		t = (t >> 26) + (x[9]*y);
		xy[9] = (t & ((1 << 25) - 1));
		t = 19 * (t >> 25) + (x[0]*y);
		xy[0] = (t & ((1 << 26) - 1));
		t = (t >> 26) + (x[1]*y);
		xy[1] = (t & ((1 << 25) - 1));
		t = (t >> 25) + (x[2]*y);
		xy[2] = (t & ((1 << 26) - 1));
		t = (t >> 26) + (x[3]*y);
		xy[3] = (t & ((1 << 25) - 1));
		t = (t >> 25) + (x[4]*y);
		xy[4] = (t & ((1 << 26) - 1));
		t = (t >> 26) + (x[5]*y);
		xy[5] = (t & ((1 << 25) - 1));
		t = (t >> 25) + (x[6]*y);
		xy[6] = (t & ((1 << 26) - 1));
		t = (t >> 26) + (x[7]*y);
		xy[7] = (t & ((1 << 25) - 1));
		t = (t >> 25) + xy[8];
		xy[8] = (t & ((1 << 26) - 1));
		xy[9] += (t >> 26);
		return xy;

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

    def mont_dbl(self, t1, t2, t3, t4, bx, bz):
        self.sqr(t1, t3)
        self.sqr(t2, t4)
        self.mul(bx, t1, t2)
        self.sub(t2, t1, t2)
        self.mul_small(bz, t2, 121665)
        self.add(t1, t1, bz)
        self.mul(bz, t1, t2)

    def recip(self, y, x, sqrtassist):
        t0 = array.array('L')
        t1 = array.array('L')
        t2 = array.array('L')
        t3 = array.array('L')
        t4 = array.array('L')
        ## the chain for x^(2^255-21) is straight from djb's implementation */
        self.sqr(t1, x);#	#  2 == 2 * 1	*/
        self.sqr(t2, t1);#	#  4 == 2 * 2	*/
        self.sqr(t0, t2);#	#  8 == 2 * 4	*/
        self.mul(t2, t0, x);#	#  9 == 8 + 1	*/
        self.mul(t0, t2, t1);#	# 11 == 9 + 2	*/
        self.sqr(t1, t0);#	# 22 == 2 * 11	*/
        self.mul(t3, t1, t2);#	# 31 == 22 + 9	== 2^5   - 2^0	*/
        self.sqr(t1, t3);#	# 2^6   - 2^1	*/
        self.sqr(t2, t1);#	# 2^7   - 2^2	*/
        self.sqr(t1, t2);#	# 2^8   - 2^3	*/
        self.sqr(t2, t1);#	# 2^9   - 2^4	*/
        self.sqr(t1, t2);#	# 2^10  - 2^5	*/
        self.mul(t2, t1, t3);#	# 2^10  - 2^0	*/
        self.sqr(t1, t2);#	# 2^11  - 2^1	*/
        self.sqr(t3, t1);#	# 2^12  - 2^2	*/
        for i in xrange(1, 5):
            self.sqr(t1, t3);
            self.sqr(t3, t1);

        self.mul(t1, t3, t2);	# 2^20  - 2^0	*/
        self.sqr(t3, t1);	# 2^21  - 2^1	*/
        self.sqr(t4, t3);	# 2^22  - 2^2	*/
        for i in xrange(1, 10):
            self.sqr(t3, t4)
            self.sqr(t4, t3)

        self.mul(t3, t4, t1);	# 2^40  - 2^0	*/

        for i in xrange(0, 5):
            self.sqr(t1, t3);
            self.sqr(t3, t1);


        self.mul(t1, t3, t2);	# 2^50  - 2^0	*/
        self.sqr(t2, t1);	# 2^51  - 2^1	*/
        self.sqr(t3, t2);	# 2^52  - 2^2	*/
        for i in xrange(1,25):
            self.sqr(t2, t3);
            self.sqr(t3, t2);
		 # t3 */		# 2^100 - 2^50 */
        self.mul(t2, t3, t1);	# 2^100 - 2^0	*/
        self.sqr(t3, t2);	# 2^101 - 2^1	*/
        self.sqr(t4, t3);	# 2^102 - 2^2	*/
        for i in xrange(0,50):
			self.sqr(t3, t4);
			self.sqr(t4, t3);

        self.mul(t3, t4, t2);	# 2^200 - 2^0	*/
        for i in xrange(0, 25):
			self.sqr(t4, t3);
			self.sqr(t3, t4);
		 # t3 */		# 2^250 - 2^50	*/
        self.mul(t2, t3, t1);	# 2^250 - 2^0	*/
        self.sqr(t1, t2);	# 2^251 - 2^1	*/
        self.sqr(t2, t1);	# 2^252 - 2^2	*/
        if (sqrtassist <> 0):
			self.mul(y, x, t2);	# 2^252 - 3 */
        else:
			self.sqr(t1, t2);	# 2^253 - 2^3	*/
			self.sqr(t2, t1);	# 2^254 - 2^4	*/
			self.sqr(t1, t2);	# 2^255 - 2^5	*/
			self.mul(y, t1, t0);	# 2^255 - 21	*/

    def is_overflow(self, x):
        t = ((x[0] > P26-19))
        t1 = ((x[1] & x[3] & x[5] & x[7] & x[9]) == P25)
        t2 = (x[2] & x[4] & x[6] & x[8]) == P26
        t3 = (x[9] > P25)
        result =  (t and t1 and t2) or t3
        return result

    def pack(self, x, m):
        ld = 0
        ud = 0
        ld = 0
        if is_overflow(x):
            if (x[9] < 0):
                ld = 0
            else:
                ld = 1
        else:
            if x[9] < 0:
                ld = 1
            else:
                ld = 0

		ud = ld * -(P25+1);
		ld *= 19;
		t = ld + x[0] + (x[1] << 26);
		m[ 0] = t;
		m[ 1] = (t >> 8);
		m[ 2] = (t >> 16);
		m[ 3] = (t >> 24);
		t = (t >> 32) + (x[2] << 19);
		m[ 4] = t;
		m[ 5] = (t >> 8);
		m[ 6] = (t >> 16);
		m[ 7] = (t >> 24);
		t = (t >> 32) + (x[3] << 13);
		m[ 8] = t;
		m[ 9] = (t >> 8);
		m[10] = (t >> 16);
		m[11] = (t >> 24);
		t = (t >> 32) + (x[4] <<  6);
		m[12] = t;
		m[13] = (t >> 8);
		m[14] = (t >> 16);
		m[15] = (t >> 24);
		t = (t >> 32) + x[5] + (x[6] << 25);
		m[16] = t;
		m[17] = (t >> 8);
		m[18] = (t >> 16);
		m[19] = (t >> 24);
		t = (t >> 32) + (x[7] << 19);
		m[20] = t;
		m[21] = (t >> 8);
		m[22] = (t >> 16);
		m[23] = (t >> 24);
		t = (t >> 32) + (x[8] << 12);
		m[24] = t;
		m[25] = (t >> 8);
		m[26] = (t >> 16);
		m[27] = (t >> 24);
		t = (t >> 32) + ((x[9] + ud) << 6);
		m[28] = t;
		m[29] = (t >> 8);
		m[30] = (t >> 16);
		m[31] = (t >> 24);

    def is_negative(self, x):
        if self.is_overflow(x) or x[9] < 0:
            return int(1 & (x[0] & 1))
        else:
            return int(0 & (x[0] & 1))


    def cpy32(self, d, s):
        for i in xrange(0,32):
            d[i] = s[i]

    def mula_small(self, p, q, m, x, n, z):
		v=0;
		for i in xrange(0, n+1):
			v+=(q[i+m] & 0xFF)+z*(x[i] & 0xFF);
			p[i+m]=v;
			v>>=8;

		return v;

    def div_mod(self,  q, r,  n,  d, t):
        rn = 0
        dt = ((d[t-1] & 0xFF) << 8)
        if t > 1:
            dt |= (d[t-2] & 0xFF)

        while n >= t:
            n -= 1
            z = (rn << 16) | ((r[n] & 0xFF) << 8);
            if (n>0):
				z |= (r[n-1] & 0xFF);

            z = z / dt
            rn += self.mula_small(r,r, n-t+1, d, t, -z);
            q[n-t+1] = ((z + rn) & 0xFF);
            self.mula_small(r,r, n-t+1, d, t, -rn);
            rn = (r[n] & 0xFF);
            r[n] = 0;

            r[t-1] = rn;

    def numsize(self, x, n):
        while n <> 0 and x[n] == 0:
            n = n-1

        return n+1


    def egcd32(self, x, y, a, b):
        bn = 32
        an = 0
        qn = 0
        for i in xrange(0, 31):
            x[i] = y[i] = 0;

        x[0] = 1;
        an = self.numsize(a, 32);

        if an==0:
            return y;

        temp = []
        while (True):
			qn = bn - an + 1;
			self.div_mod(temp, b, bn, a, an);
			bn = self.numsize(b, bn);
			if (bn==0):
				return x;
			self.mula32(y, x, temp, qn, -1);

			qn = an - bn + 1;
			self.div_mod(temp, a, an, b, bn);
			an = self.numsize(a, an);
			if (an==0):
				return y;
			self.mula32(x, y, temp, qn, -1);


    def keygen(self, P, s, k):
        self.clamp(k)
        self.core(P, s, k, None)

    def curve(self, Z, k, P):
        self.core(Z, None, k, P)

    def sign(self, v, h, x, s):
        tmp1 = []
        tmp2 = []
        w = 0
        for i in xrange(0, 32):
            v[i] = 0
        i = self.mula_small(v, x, 0, h, 32, -1)
        self.mula_small(v,v,0, ORDER, 32, ((15-v[31])/16))
        self.mula32(tmp1, v, s, 32, 1)
        self.div_mod(tmp2, tmp1, 64, ORDER, 32)
        for i in xrange(0, 32):
            v[i] = tmp1[i]
            w |= v[i]

        return (w <>  0)

    def core(self, Px, s, k, Gx):

        dx = array.array('L')
        t1 = array.array('L')
        t2 = array.array('L')
        t3 = array.array('L')
        t4 = array.array('L')

        x = array.array('L', array.array('L'))
        x.insert(0, array.array('L'))
        z = array.array('L', array.array('L'))
        z.insert(0, array.array('L'))

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
                self.mont_dbl(t1, t2, t3, t4, bx, bz)

        recip(t1, z[0], 0);
        mul(dx, x[0], t1);
        pack(dx, Px);

        	# calculate s such that s abs(P) = G  .. assumes G is std base point */
        if (s <> None):
            self.x_to_y2(t2, t1, dx);	# t1 = Py^2  */
            self.recip(t3, z[1], 0);	# where Q=P+G ... */
            self.mul(t2, x[1], t3);	# t2 = Qx  */
            self.add(t2, t2, dx);	# t2 = Qx + Px  */
            t2[0] += 9 + 486662;	# t2 = Qx + Px + Gx + 486662  */
            dx[0] -= 9;		# dx = Px - Gx  */
            self.sqr(t3, dx);	# t3 = (Px - Gx)^2  */
            self.mul(dx, t2, t3);	# dx = t2 (Px - Gx)^2  */
            self.sub(dx, dx, t1);	# dx = t2 (Px - Gx)^2 - Py^2  */
            dx[0] -= 39420360;	# dx = t2 (Px - Gx)^2 - Py^2 - Gy^2  */
            self.mul(t1, dx, BASE_R2Y);	# t1 = -Py  */
            if (is_negative(t1)!=0):	# sign is 1, so just copy  */
                self.cpy32(s, k);
            else:
                self.mula_small(s, ORDER_TIMES_8, 0, k, 32, -1);

			# reduce s mod q * (is this needed?  do it just in case, it's fast anyway) */
			#divmod((dstptr) t1, s, 32, order25519, 32);

			# take reciprocal of s mod q */
            temp1=[];
            temp2=[];
            temp3=[];
            self.cpy32(temp1, ORDER);
            self.cpy32(s, egcd32(temp2, temp3, s, temp1));
            if ((s[31] & 0x80)<>0):
                self.mula_small(s, s, 0, ORDER, 32, 1);
