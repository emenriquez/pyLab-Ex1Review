import random
# from solution import * # used for play test only
from functions import *

def test_list():
    tList1 = random.choices(range(100), k=5)
    factor = random.choice(range(10))
    newList = listMult(tList1, factor)
    assert newList[2] == factor*tList1[2]

def test_string():
    str1 = "This is a quick test"
    str2 = "This is not a test"
    str3 = "But this is definitely a test"
    assert str1 == vowelComp(str1, str2)
    assert str3 == vowelComp(str3, str2)
    assert str3 == vowelComp(str1, str3)

def test_branch():
    x = 0
    y = 5
    z = 9999
    f = 22
    assert "rich in spirit" == richCalc(x)
    assert "kind of rich" == richCalc(y)
    assert "rich" == richCalc(f)
    assert "super rich" == richCalc(z)
    assert "rich" in richCalc(random.choice(range(101)))

def test_import():
    a = random.choice(range(10))
    assert funcSub(a) == (math.cos(a) - math.sin(a))*math.factorial(a)