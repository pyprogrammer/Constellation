import typing
import abc


import functools
import operator


class DataType:
    @property
    @abc.abstractmethod
    def size(self) -> int:
        return 0


class Integer(DataType):
    def __init__(self, signed: bool, bits: int):
        """
        :param signed: Whether or not the integer type is signed
        :param bits: Number of numerical bits (ignoring the sign bit if present)
        """
        self._signed = signed
        self._bits = bits

    @property
    def signed(self):
        return self._signed

    @property
    def bits(self):
        return self._bits

    @property
    def size(self):
        return self.signed + self.bits


class FixedPoint(DataType):
    def __init__(self, signed: bool, integer_bits: int, mantissa_bits: int):
        """
        :param signed: Whether or not the type is signed
        :param integer_bits: Number of bits for integer portion
        :param mantissa_bits: Number of bits for fractional portion
        """
        self._signed = signed
        self._integer = integer_bits
        self._mantissa = mantissa_bits


    @property
    def signed(self):
        return self._signed

    @property
    def integer_bits(self):
        return self._integer

    @property
    def mantissa_bits(self):
        return self._mantissa

    @property
    def size(self):
        return self.signed + self.integer_bits + self.mantissa_bits


class Struct(DataType):
    def __init__(self, types: typing.Tuple[DataType]):
        self._types = types

    @property
    def types(self):
        return self._types

    @property
    def size(self):
        return sum([t.size for t in self.types])


class Array(DataType):
    def __init__(self, datatype: DataType, dimensions: typing.Tuple[int, ...]):
        self._type = datatype
        self._dims = dimensions


    @property
    def type(self):
        return self._type

    @property
    def ndim(self):
        return len(self._dims)

    @property
    def size(self):
        return functools.reduce(operator.mul, self._dims) * self.type.size


class DataFormat:
    def __init__(self, format: typing.Union[str, DataType]):
        pass
