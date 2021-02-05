import pytest
from tictactoe_functions import *


def test_do_best_turn_1():
    r = do_best_turn(({0}, set()), 2)
    assert r == 4


def test_do_best_turn_2():
    r = do_best_turn(({1}, set()), 2)
    assert r == 0 or r == 2 or r == 4 or r == 7


def test_do_best_turn_3():
    r = do_best_turn(({2}, set()), 2)
    assert r == 4


def test_do_best_turn_4():
    r = do_best_turn(({3}, set()), 2)
    assert r == 0 or r == 4 or r == 5 or r == 6


def test_do_best_turn_5():
    r = do_best_turn(({4}, set()), 2)
    assert r == 0 or r == 2 or r == 6 or r == 8


def test_do_best_turn_6():
    r = do_best_turn(({5}, set()), 2)
    assert r == 2 or r == 3 or r == 4 or r == 8


def test_do_best_turn_7():
    r = do_best_turn(({6}, set()), 2)
    assert r == 4


def test_do_best_turn_8():
    r = do_best_turn(({7}, set()), 2)
    assert r == 1 or r == 4 or r == 6 or r == 8


def test_do_best_turn_9():
    r = do_best_turn(({8}, set()), 2)
    assert r == 4


def test_do_best_turn_10():
    r = do_best_turn(({0}, {1}), 1)
    assert r == 3 or r == 4 or r == 6


def test_do_best_turn_11():
    r = do_best_turn(({0}, {2}), 1)
    assert r == 3 or r == 6 or r == 8


def test_do_best_turn_12():
    r = do_best_turn(({0}, {3}), 1)
    assert r == 1 or r == 2 or r == 4


def test_do_best_turn_13():
    r = do_best_turn(({0}, {5}), 1)
    assert r == 2 or r == 4 or r == 6


def test_do_best_turn_14():
    r = do_best_turn(({0}, {6}), 1)
    assert r == 1 or r == 2 or r == 8


def test_do_best_turn_15():
    r = do_best_turn(({0}, {7}), 1)
    assert r == 2 or r == 4 or r == 6


def test_do_best_turn_16():
    r = do_best_turn(({0}, {8}), 1)
    assert r == 2 or r == 6


def test_who_wins_1():
    r = who_wins(({3}, set()), 2)
    assert r == 0


def test_who_wins_2():
    r = who_wins(({3}, {4}), 1)
    assert r == 0


def test_who_wins_3():
    r = who_wins(({0, 3}, {4}), 2)
    assert r == 0


def test_who_wins_4():
    r = who_wins(({0, 3}, {4, 6}), 1)
    assert r == 0


def test_who_wins_5():
    r = who_wins(({0, 2, 3}, {4, 6}), 2)
    assert r == 0


def test_who_wins_6():
    r = who_wins(({0, 2, 3}, {1, 4, 6}), 1)
    assert r == 0


def test_who_wins_7():
    r = who_wins(({0, 2, 3, 7}, {1, 4, 6}), 2)
    assert r == 0


def test_check_victory_1():
    r = check_victory(({0, 2, 3, 7, 8}, {1, 4, 5, 6}))
    assert r == 0


def test_check_victory_2():
    r = check_victory(({0, 1, 2}, {3, 4}))
    assert r == 1


def test_check_victory_3():
    r = check_victory(({0, 1, 8}, {2, 4, 6}))
    assert r == 2


def test_check_victory_4():
    r = check_victory(({0, 1, 3, 8}, {2, 4, 5, 6}))
    assert r == 2


def test_check_victory_5():
    r = check_victory(({1, 4, 7}, {3, 6}))
    assert r == 1


def test_check_victory_6():
    r = check_victory(({1, 2, 3, 5, 6, 7}, {0, 4}))
    assert r == 0


def test_check_victory_7():
    r = check_victory(({2, 4}, {0, 1, 3, 5, 7, 8}))
    assert r == 0
