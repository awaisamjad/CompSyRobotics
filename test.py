from typing import Union
from enum import Enum

class Color(Enum):
    RED = 1
    BLUE = 2
    GREEN = 3
    
def test(x: Union[int, Color]) -> None:
    print(x)
    
test(1)
test(Color.RED)