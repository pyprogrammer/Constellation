from ..compute import Pattern

Add = Pattern("Add", (2,), 1)
Mul = Pattern("Mul", (2,), 1)
Div = Pattern("Div", (1, 1), 1)
Pow = Pattern("Pow", (1, 1), 1)
Neg = Pattern("Neg", (1,), 1)
Sub = Pattern("Sub", (1, 1), 1)
