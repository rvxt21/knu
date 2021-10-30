class Shape:
    def __init__(self,line_color='blue',line_thickness=123):
        self._line_color=line_color #защищенный(protected)
        self._line_thickness = line_thickness  # защищенный(protected)

class Square(Shape): #наследуемый класс от Shape
    def __init__(self,side,line_color, line_thickness):
        super().__init__(line_color, line_thickness)
        self._side=side
    def area(self):
        return(self._side*self._side)
    def perimeter(self):
        return(self._side*4)

class Rectangle(Square): #наследуемый класс от Square
    def __init__(self,length,width,line_color,line_thickness):
        super().__init__(line_color,line_thickness)
        self._lenght=length
        self._width=width
    def area1(self):
        return(self._lenght*self._width)
    def perimeter1(self):
        s=(self._lenght+self._width)*2
        return(s)

square1=Square(5,'red',145)
print("Площадь квадрата=",square1.area())
print("Периметр квадрата=",square1.perimeter())

rectangle1=Rectangle(2,13,'pink',45)
print("Площадь прямоугольника=",rectangle1.area1())
print("Периметр прямоугольника=",rectangle1.perimeter1())