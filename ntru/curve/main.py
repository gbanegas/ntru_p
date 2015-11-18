from curve import Curve25519
import random

def main():
    curve = Curve25519()
    pub = []
    priv = [111,85,-46,-73,11,32,108,14,-7,4,36,-65,-124,84,43,63,31,-62,60,110,-125,108,79,-81,-1,100,59,-20,-128,63,-107,67]
    #priv = random.SystemRandom().getrandbits(256)
    curve.keygen(pub, None, priv)


if __name__ == "__main__":
    main()
