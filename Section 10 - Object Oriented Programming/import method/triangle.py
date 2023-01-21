from polygon import Polygon

## create a class for trianle

class Triangle(Polygon):
    
    def area(self):
        #return (self.__width * self.__height) / 2  ## here we are defining the private member of the polygon class
        return int((self.get_height() * self.get_width()) / 2)