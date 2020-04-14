import re
import math


def add(a, b): return a + b


def sub(a, b): return a - b


def mul(a, b): return a * b


def div(a, b): return a / b


def gcd(a, b): return math.gcd(int(a), int(b))


line = ""
variables = {}
function_pattern = re.compile(r'\s*([a-zA-Z]+)\s*:=\s*([a-zA-Z]+)\(\s*([\w\.]+)\s*,\s*([\w\.]+)\s*\)\s*')
assign_pattern = re.compile(r"\s*([a-zA-Z]+)\s*:=\s*([\w\.]+)")
number_pattern = re.compile(r"\d+(\.)*\d*")
functions = {
    "add": add,
    "sub": sub,
    "mul": mul,
    "div": div,
    "pow": math.pow,
    "gcd": gcd,
    "log": math.log
}
while line != "end":
    line = input()
    if line == "end":
        break
    if function_pattern.match(line):
        ident, func, arg1, arg2 = function_pattern.findall(line)[0]
        if number_pattern.match(arg1):
            try:
                arg1 = float(arg1)
            except ValueError as v:
                print(str(arg1) + " is not a number")
                continue
        elif arg1 in variables:
            arg1 = variables[arg1]
        else:
            print("variable error")
            continue

        if number_pattern.match(arg2):
            try:
                arg2 = float(arg2)
            except ValueError as v:
                print(str(arg2) + " is not a number")
                continue
        elif arg2 in variables:
            arg2 = variables[arg2]
        else:
            print("variable error")
            continue

        if func in functions:
            variables[ident] = functions[func](arg1, arg2)
        else:
            print("function not found")
    elif assign_pattern.match(line):
        ident, val = assign_pattern.findall(line)[0]
        if number_pattern.match(val):
            try:
                variables[ident] = float(val)
            except ValueError  as v:
                print(val + " is not a number")
                continue
        elif val in variables:
            variables[ident] = variables[val]
        else:
            print("variable error")
            continue

    else:
        line.strip()
        if line in variables:
            print("{0:.3f}".format(variables[line]))
        else:
            print("variable not found")
