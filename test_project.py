import pytest
from project import append_expense
from project import get_graph_input
from project import validate_input


def test_validate_input():
    assert validate_input('food', 20) == ('Food', 20) 
    assert validate_input('TRAVEL', 10) == ('Travel', 10)
    with pytest.raises(ValueError):
        validate_input('gift', 100)
        validate_input('travel', -50)
        validate_input('10', 10)
        validate_input('', 20)


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


def test_get_graph_input():
    budget = [['Category', 'Max Expense'], ['Food', '800'], ['Stationary', '200'], ['Travel', '200'], ['Entertainment', '100'], ['Gifts', '200']]
    
    assert get_graph_input([['Category', ' Your Expense'],
                                    ['Food', '0'],
                                    ['Stationary', '0'],
                                    ['Travel', '0'], 
                                    ['Entertainment', '0'], 
                                    ['Gifts', '0']], [['Category', 'Max Expense'], 
                                                        ['Food', '800'], 
                                                        ['Stationary', '200'], 
                                                        ['Travel', '200'], 
                                                        ['Entertainment', '100'], 
                                                        ['Gifts', '200']]) == ([0, 0, 0, 0, 0],
                                                                                [800, 200, 200, 100, 200],                                                                                     
                                                                                ['Food', 'Stationary', 'Travel', 'Entertainment', 'Gifts'])

    assert get_graph_input([['Category', ' Your Expense'],
                                    ['Food', '100'],
                                    ['Stationary', '50'],
                                    ['Travel', '100'], 
                                    ['Entertainment', '50'], 
                                    ['Gifts', '0']], [['Category', 'Max Expense'], 
                                                        ['Food', '800'], 
                                                        ['Stationary', '200'], 
                                                        ['Travel', '200'], 
                                                        ['Entertainment', '100'], 
                                                        ['Gifts', '200']]) == ([100, 50, 100, 50, 0],
                                                                                [800, 200, 200, 100, 200], 
                                                                                ['Food', 'Stationary', 'Travel', 'Entertainment', 'Gifts'])


