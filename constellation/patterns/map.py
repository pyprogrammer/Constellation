from ..compute import Pattern, Function

__all__ = ["Map"]


def map_validator(parameters):
    return len(parameters) == 1 and isinstance(parameters[0], Function)


Map = Pattern(
    "Map", (1,), 1, map_validator, Function
)
