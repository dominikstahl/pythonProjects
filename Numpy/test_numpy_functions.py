import pytest
from numpy_functions import *


def test_det_1():
    r = det(np.array([[-2,2,-3],[-1,1,3],[2,0,-1]]))
    assert r == 18

def test_det_2():
    with pytest.raises(Exception) as excinfo:
        r = det(np.array([[1,2],[3,4],[5,6]]))
    assert "matrix not quadratic" in str(excinfo.value)

def test_det_3():
    with pytest.raises(Exception) as excinfo:
        r = det(np.array([[1,2,3,4],[3,4,5,6],[5,6,7,8]]))
    assert "matrix not quadratic" in str(excinfo.value)

def test_det_4():
    with pytest.raises(Exception) as excinfo:
        r = det(np.array([1,2]))
    assert "matrix not two-dimensional" in str(excinfo.value)

def test_det_5():
    with pytest.raises(Exception) as excinfo:
        r = det(np.array([[[1,2],[3,4]],[[5,6],[7,8]]]))
    assert "matrix not two-dimensional" in str(excinfo.value)

def test_det_6():
    r = det(np.array([[1,2,34,-53,42],[-1,-2,43,-15,-3],[2,4,1,2,0],[50,100,4,45,-70],[-2,-4,0,5,4]]))
    assert r == 0
