from polygon import Polygon

## craete a class rectangle
class Rectangle(Polygon):
    
    def area(self):
        #return self.__width * self.__height  ## here we are defining the private member of the polygon class
        return self.get_height() * self.get_width()     ## these are public methods, can be used outside the class polygon.