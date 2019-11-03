"""
データ型(クラス名)宣言: UserName
   属性:(変数)height width

   ルール:
     ・ユーザー名は4文字以上20文字以下である
   できること
   長方形の広さ
   長方形の対角線
"""
import math


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def diagonal(self):
        return round(math.sqrt(self.height ** 2 + self.width ** 2), 2)


rectangle1 = Rectangle(height=5, width=6)
print(rectangle1.area())  # 30.00
print(rectangle1.diagonal())  # 7.81

rectangle2 = Rectangle(height=3, width=3)
print(rectangle2.area())  # 9.00
print(rectangle2.diagonal())  # 4.24
