from src.operations.suma import sumar

def test_sumar():
    assert sumar(2, 3) == 5
    assert sumar(2, 5) == 7