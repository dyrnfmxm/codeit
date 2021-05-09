from math import pi, sqrt # 원주율, 제곱
from abc import ABC, abstractmethod

class Shape(ABC):
    """도형 클래스"""
    @abstractmethod # 데코레이터를 이용해 추상 메소드로
    def area(self) -> float: #Type Hinting
        """도형 넓이를 리턴 : 자식 클래스에서 오버라이딩"""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """도형 둘레를 리턴 : 자식 클래스에서 오버라이딩"""
        pass


class Rectangle(Shape):
