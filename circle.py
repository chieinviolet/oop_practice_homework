"""
関連しそうな属性
radias
"""


class Circle:
    def __init__(self, radias):
        π = 3.14
        self.radias = radias
        self.area = self.radias ** 2 * π
        self.perimeter = self.radias * 2 * π


circle1 = Circle(1)
print(circle1.area())  # 3.14
print(circle1.perimeter())  # 6.28

# 半径3の円
circle3 = Circle(radius=3)
print(circle3.area())  # 28.27
print(circle3.perimeter())  # 1 8.85
