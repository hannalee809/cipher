from cipher2 import *

def test_shiftLetter():
    assert shiftLetter("A", 2) == "C"
    assert shiftLetter("!", 2) == "!"

# class test_shiftLetter:
#     def test01(self):
#         assert shiftLetter(char = "A", shift = 2) == "C"

#     def test02(self):
#         assert shiftLetter(char = "!", shift = 2) == "!"
       