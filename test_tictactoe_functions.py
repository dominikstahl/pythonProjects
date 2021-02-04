import pytest
from tictactoe_functions import *

def test_doBestTurn_1():
    r = doBestTurn(({0},set()),2)
    assert r==4
