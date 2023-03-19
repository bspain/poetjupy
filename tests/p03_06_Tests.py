
from poetjupy import p03_06_Solution as h

def test_hexToDec():
    assert h.hexToDec('A') == 10
    assert h.hexToDec('0') == 0
    assert h.hexToDec('1B') == 27
    assert h.hexToDec('3C0') == 960
    assert h.hexToDec('A6G') == None
    assert h.hexToDec('ZZTOP') == None
    assert h.hexToDec('EAD') == 3757
    assert h.hexToDec('1111') == 4369
    assert h.hexToDec('DEADBEEF') == 3735928559