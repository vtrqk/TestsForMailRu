import pytest
import unittest
from pytest import ExitCode


#функции для тестов str

def my_index(a, b):
    return  (str(a))[b]

def my_concat(a, b):
    return a + b

def my_len(a):
    return len(a)


#функции для тестов list    

def my_remove(testlist, x):
    testlist.remove(x)
    return testlist

def my_append(testlist, x):
    testlist.append(x)
    return testlist

def my_count(testlits, x):
    return testlits.count(x)



#тесты str

@pytest.mark.parametrize("a,b, expected_result", [("ab","bc", "abbc"),
                                                   ("123", "456", "123456"),
                                                   ("3.14", " Pi", "3.14 Pi")])
def test_concat(a, b, expected_result):
    assert my_concat(a, b) == expected_result


def test_index():
    assert my_index("1234", 3)  == '4' 

def test_len():
    assert my_len("aabb") == 4



#тесты list

@pytest.mark.parametrize("tlist, x, expected_result", [([1,2,3], 7, [1,2,3,7]),
                                                         ([6.6,9.5,10], 15, [6.6,9.5,10,15]),
                                                         (["a", "b", "c"], "d", ["a", "b", "c", "d"])])
def test_append(tlist, x, expected_result):
    assert my_append(tlist, x) == expected_result



def test_remove():
    assert my_remove([1, 2, 3, 4], 3) == [1, 2, 4]


def test_count():
    assert my_count(["this", "is", "list", "and", "it", "is", "last", "test"], 'is') == 2
