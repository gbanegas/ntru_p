from abc import ABCMeta, abstractmethod


class Polynomial:
    __metaclass__ = ABCMeta

    @classmethod
    def version(self): return "1.0"

    @abstractmethod
    def mult(self, Object): raise NotImplementedError

    @abstractmethod
    def mult_mod(self, Object, modulus): raise NotImplementedError

    @abstractmethod
    def to_int_polynomial(self): raise NotImplementedError

    @abstractmethod
    def mult_big_pol(self, Object): raise NotImplementedError
    
