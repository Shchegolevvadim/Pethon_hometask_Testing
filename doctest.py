
def is_rectangle(side_a: float, side_b: float) -> bool:
    """
    >>> is_rectangle(5, 6)
    If the number Perimetr is 22, and Square is 30
    True
    >>> is_rectangle(-5, 12)
    If the number Perimetr is 14, and Square is -60
    True
     >>> is_rectangle(-12, 302)
    If the number Perimetr is 580, and Square is -3624
    True
    """
    if (side_a + side_b) * 2 == (side_a + side_b) * 2:
        return True
    else:
        return False

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)