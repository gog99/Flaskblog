from core import add
import pytest


def test_add():
  x=1
  y=2

  assert 3 == add(x,y)


@pytest.mark.parametrize("x,y,result",((1,3,4),(3,4,7)))
def test_add2(x,y,result):
  assert result==add(x,y)
