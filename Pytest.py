import pytest

def sum_two_num(a, b):
    return a + b
    # return f'{a}{b}'

def test_sum():
    assert sum_two_num(5, 6) == 11, 'Математика покинула чат'

if __name__=='__main__':
    pytest.main()