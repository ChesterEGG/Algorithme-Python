def is_power_of_two(number: int) -> bool:
    """
    Return True if this number is power of 2 or False otherwise.

    >>> is_power_of_two(0)
    True
    >>> is_power_of_two(1)
    True
    >>> is_power_of_two(2)
    True
    >>> is_power_of_two(4)
    True
    >>> is_power_of_two(6)
    False
    >>> is_power_of_two(8)
    True
    >>> is_power_of_two(17)
    False
    >>> is_power_of_two(-1)
    Traceback (most recent call last):
        ...
    ValueError: number must not be negative
    >>> is_power_of_two(1.2)
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for &: 'float' and 'float'

    # Test all powers of 2 from 0 to 10,000
    >>> all(is_power_of_two(int(2 ** i)) for i in range(10000))
    True
    """
    if number < 0:
        raise ValueError("number must not be negative")
    return number & (number - 1) == 0