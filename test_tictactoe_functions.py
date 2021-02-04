import pytest
from tictactoe_functions import *

def test_doBestTurn_1():
    r = doBestTurn(({0},set()),2)
    assert r==4

def test_doBestTurn_2():
    r = doBestTurn(({1},set()),2)
    assert r==0 or r==2 or r==4 or r==7

def test_doBestTurn_3():
    r = doBestTurn(({2},set()),2)
    assert r==4

def test_doBestTurn_4():
    r = doBestTurn(({3},set()),2)
    assert r==0 or r==4 or r==5 or r==6

def test_doBestTurn_5():
    r = doBestTurn(({4},set()),2)
    assert r==0 or r==2 or r==6 or r==8

def test_doBestTurn_6():
    r = doBestTurn(({5},set()),2)
    assert r==2 or r==3 or r==4 or r==8

def test_doBestTurn_7():
    r = doBestTurn(({6},set()),2)
    assert r==4

def test_doBestTurn_8():
    r = doBestTurn(({7},set()),2)
    assert r==1 or r==4 or r==6 or r==8

def test_doBestTurn_9():
    r = doBestTurn(({8},set()),2)
    assert r==4

def test_doBestTurn_10():
    r = doBestTurn(({0},{1}),1)
    assert r==3 or r==4 or r==6

def test_doBestTurn_11():
    r = doBestTurn(({0},{2}),1)
    assert r==3 or r==6 or r==8

def test_doBestTurn_12():
    r = doBestTurn(({0},{3}),1)
    assert r==1 or r==2 or r==4

def test_doBestTurn_13():
    r = doBestTurn(({0},{5}),1)
    assert r==2 or r==4 or r==6

def test_doBestTurn_14():
    r = doBestTurn(({0},{6}),1)
    assert r==1 or r==2  or r==8

def test_doBestTurn_15():
    r = doBestTurn(({0},{7}),1)
    assert r==2 or r==4 or r==6

def test_doBestTurn_16():
    r = doBestTurn(({0},{8}),1)
    assert r==2 or r==6

def test_whoWins1():
    r = whoWins(({3},set()),2)
    assert r==0

def test_whoWins2():
    r = whoWins(({3},{4}),1)
    assert r==0

def test_whoWins3():
    r = whoWins(({0,3},{4}),2)
    assert r==0

def test_whoWins4():
    r = whoWins(({0,3},{4,6}),1)
    assert r==0

def test_whoWins5():
    r = whoWins(({0,2,3},{4,6}),2)
    assert r==0

def test_whoWins6():
    r = whoWins(({0,2,3},{1,4,6}),1)
    assert r==0

def test_whoWins7():
    r = whoWins(({0,2,3,7},{1,4,6}),2)
    assert r==0

def test_checkVictory1():
    r = checkVictory(({0,2,3,7,8},{1,4,5,6}))
    assert r==0

def test_checkVictory2():
    r = checkVictory(({0,1,2},{3,4}))
    assert r==1

def test_checkVictory3():
    r = checkVictory(({0,1,8},{2,4,6}))
    assert r==2

def test_checkVictory4():
    r = checkVictory(({0,1,3,8},{2,4,5,6}))
    assert r==2

def test_checkVictory5():
    r = checkVictory(({1,4,7},{3,6}))
    assert r==1

def test_checkVictory6():
    r = checkVictory(({1,2,3,5,6,7},{0,4}))
    assert r==0

def test_checkVictory7():
    r = checkVictory(({2,4},{0,1,3,5,7,8}))
    assert r==0
