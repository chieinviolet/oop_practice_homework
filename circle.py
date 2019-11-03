"""
関連しそうな属性
radias
"""


class Circle:
    pai = 3.14
    def __init__(self, radias):

        self.radias = radias

    def area(self):
        return self.radias ** 2 * pai

    def perimeter(self):
        return self.radias * 2 * π


circle1 = Circle(1)
print(circle1.area())  # 3.14
print(circle1.perimeter())  # 6.28

# 半径3の円
circle3 = Circle(radius=3)
print(circle3.area())  # 28.27
print(circle3.perimeter())  # 1 8.85
