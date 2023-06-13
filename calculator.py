import numbers, sys

class CalculatorError(Exception):
   """ An exception class for calculator """

class Calculator:
    """" A sample simple calculator """

    def add(self, a: int, b: int) -> int:
        self._check_operand(a)
        self._check_operand(b)
        return a+b

    def subtract(self, a: int, b: int) -> int:
        return a-b

    def multiply(self, a: int, b: int) -> int:
        return a*b

    def divide(self, a: int, b: int) -> int:
        try:
            return a/b
        except ZeroDivisionError:
            raise CalculatorError("You attempted to divide by zero")

    def _check_operand(self, operand):
        if not isinstance(operand, numbers.Number):
            raise CalculatorError(f'"{operand}" is not a number')

if __name__ == '__main__':
    print("Let's calculate!")
    cal = Calculator()
    ops = [cal.add, cal.subtract, cal.multiply, cal.divide]

    while True:
        for i, op in enumerate(ops, start=1):
            print(i, str(op.__name__))
        print("q: for quit")
        operation = input("Pick and operation: ")
        if operation == 'q':
            sys.exit()
        choice = int(operation)
        try:
            a = float(input('Give me a? '))
            b = float(input('Give me b? '))
        except ValueError as ex:
            print('\n',ex,'\n')

        try:
            print(ops[choice-1](a,b))
        except CalculatorError as ex:
            print('\n',ex,'\n')
