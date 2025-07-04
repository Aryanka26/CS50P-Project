import pytest
from project import append_expense

def test_append_expense():
    assert append_expense([['Food', '30'],
                           ['Stationary', '30'],
                           ['Travel', '100'],
                           ['Entertainment', '59'],
                           ['Gifts', '40']], 'Food', 20) == [['Food', 50],
                                                               ['Stationary', '30'],
                                                               ['Travel', '100'],
                                                               ['Entertainment', '59'],
                                                               ['Gifts', '40']]
    assert append_expense([['Food', '0'],
                           ['Stationary', '0'],
                           ['Travel', '0'],
                           ['Entertainment', '0'],
                           ['Gifts', '0']], 'Stationary', 50) == [['Food', '0'],
                                                                    ['Stationary', 50],
                                                                    ['Travel', '0'],
                                                                    ['Entertainment', '0'],
                                                                    ['Gifts', '0']]


def test_():
    
    