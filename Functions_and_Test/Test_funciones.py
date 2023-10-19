import pytest
from funciones import sumar_digitos
@pytest.mark.parametrize("num, res",[
    (10, 1),
    (38, 11),
])
def test_sumar_digitos (num ,res):
    assert sumar_digitos(num)==res