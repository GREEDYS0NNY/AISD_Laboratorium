from Zadanie_1 import Stack


def parChaker(SymbolString):
    s = Stack()
    index = 0
    balanced = True
    while index < len(SymbolString) and balanced:
        symbol = SymbolString[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index += 1

    if balanced and s.isEmpty():
        return True
    else:
        return False


print(parChaker('(((())))'))
print(parChaker('('))
