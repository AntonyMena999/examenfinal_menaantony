from app import sumar



def test_suma_basica():
    assert sumar(2, 3) == 5


def test_suma_negativos():
    assert sumar(-2, -3) == -5


def test_suma_decimales():
    assert sumar(1.5, 2.5) == 4.0
