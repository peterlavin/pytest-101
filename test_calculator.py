
import pytest 
from calculator import Calculator, CalculatorError

# From youtube.com/watch?v=etosV2IWBF0
# More at... https://www.youtube.com/watch?v=fv259R38gqc

""" To run in Eclipse/pydev, Run As > Run Configurations > 
Select 'Py.test runner' in dropdown, use tick to add arguments """

def test_add():
    # Arrange
    calc = Calculator()
    # Act
    result = calc.add(2,3)
    # Assert
    assert result == 5



def test_subtract():
    calc = Calculator()
    result = calc.subtract(3,2)
    assert result == 1

def test_multiply():
    calc = Calculator()
    result = calc.multiply(5,4)
    assert result == 20


def test_divide():
    calc = Calculator()
    result = calc.divide(16,4)
    assert result == 4


""" Testing unexpected arguments, or expectation violations """

def test_add_with_string():
    calc = Calculator()
    with pytest.raises(CalculatorError):
        calc.add("two", 3)


def test_add_with_two_strings():
    """ This test passes because the correct error is raised, not because it can add two strings,
        but because the Calculator code can handle the mistake gracefully """
    calc = Calculator()
    with pytest.raises(CalculatorError) as context:
        calc.add("two", "three")

    assert str(context.value) == '"two" is not a number'

def test_divide_by_zero():
    calc = Calculator()
    with pytest.raises(CalculatorError):
        calc.divide(5,0)
