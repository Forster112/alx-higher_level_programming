# 0x08-python-more_classes
* A class of a rectangle that calculates area, perimeter of a rectangle
* Handles str, repr, del


## Tasks
| File | Prototype or Class | Duty |
| ---- | ------------------ | ---- |
| [0-rectangle.py](0-rectangle.py) | Class Rectangle: | A class that does nothing |
| [1-rectangle.py](1-rectangle.py) | Class Rectangle: | checks if the width and height of a rectangle is integer and >= 0 from [0-rectangle.py](0-rectangle.py) |
| [2-rectangle.py](2-rectangle.py) | def area(self): , def perimeter(self): | Calculates area and perimeter of a rectangle from [1-rectangle.py](1-rectangle.py) |
| [3-rectangle.py](3-rectangle.py) | def \_\_str\_\_(self): | prints a rectangle with # continued from [2-rectangle.py](2-rectangle.py) |
| [4-rectangle.py](4-rectangle.py) | def \_\_repr\_\_(self): | prints an instance of the rectangle [3-rectangle.py](3-rectangle.py) |
| [5-rectangle.py](5-rectangle.py) | def \_\_del\_\_(self): | prints the the message Bye rectangle... when an instance of the rectangle is delted from [4-rectangle.py](4-rectangle.py) |
| [6-rectangle.py](6-rectangle.py) | None | added a puclic class attribute "number_of_instances" initialized to 0 increases when an instance is added, reduce when deleted |
