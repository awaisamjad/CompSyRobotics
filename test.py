from typing import Union

def test(a: Union[int, str]) -> None:
    if not isinstance(a, (int, str)):
        raise TypeError('a must be int')
    print(a)
    
test(1)
test('1')
test(1.0)
test([1, 2, 3])