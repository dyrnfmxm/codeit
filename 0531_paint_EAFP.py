class Paint:
    """그림판 프로그램 클래스"""
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape: Shape):
        """그림판에 도형 인스턴스 shape를 추가한다. 단, shape는 추상 클래스 Shape의 인스턴스여야 한다."""
        self.shapes.append(shape)
        
    def total_area_of_shape(self):
        """그림판에 있는 모든 도형의 넓이의 합을 구한다"""
        total_area = 0

        for shape in self.shapes:
            try:
                total_area += shape.area()
            except (AttributeError, TypeError):
                print("그림판에 area메소드가 없거나 잘못 정의되어 있는 인스턴스 {}가 있습니다.".format(shape))
        
    def total_perimeter_of_shapes(self):
        """그림판에 있는 모든 도형의 둘레의 합을 구한다"""
        total_perimeter = 0

        for shape in self.shapes:
            try:
                total_perimeter += shape.perimeter()
            except (AttributeError, TypeError):
                print("그림판에 perimeter 메소드가 없거나 잘못 정의도어 있는 인스턴스 {}가 있습니다.".format(shape))
        
    def __str__(self):
        """그림판에 있는 각 도형들의 정보를 출력한다"""
        res_str = "그림판 안에 있는 도형들:\n\n"
        for shape in self.shapes:
            res_str += str(shape) + "\n"
        return res_str


# Shape 클래스를 상속받는 클래스의 인스턴스들
right_triangle = RightTriangle(3, 4)
equilateral_triangle = EquilateralTriangle(3)
circlr = Circle(4)
rectangle = Rectangle(3, 4)

# Shape 클래스를 상속받지 않고 area, perimeter 메소드도 없는 클래스의 인스턴스
cylinder = Cylinder(4, 3)

# 그림판 인스턴스 생성
paint_program = Paint()

# 그림판에 인스턴스들 추가
paint_program.add_shape(cylinder)
paint_program.add_shape(right_triangle)
paint_program.add_shape(equilateral_triangle)
paint_program.add_shape(circlr)
paint_program.add_shape(rectangle)

# 그림판에 추가된 인스턴스들의 총 넓이합과 둘레합 계산
print(paint_program.total_area_of_shapes())
print(paint_program.total_perimeter_of_shaped())

# 그림판의 도형들의 정보 출력
print(paint_program)
