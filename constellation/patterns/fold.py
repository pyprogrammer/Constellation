import typing

from ..compute import Pattern, Function

__all__ = ["fold"]


def fold_validator(parameters):
    return len(parameters) == 2 and isinstance(parameters[0], Function)


Map = Pattern(
    "fold", fold_validator, typing.Tuple[Function, typing.Any]
)
