import math

def compound_interest(principal,rate,time):
    return principal*(1+rate/100)**time

def area_of_circle(radius):
    return math.pi *radius**2

def factorials(n):
    return math.factorial(n)

def trigonometry(op,value):
    functions={"sin":math.sin,"cos": math.cos,"tan":math.tan}
    return functions[op](math.radians(value))if op in functions else None

def logarithms():
    pass