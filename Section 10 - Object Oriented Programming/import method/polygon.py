## create a polygon class
class Polygon:
    
    __width = None
    __height = None
    
    def set_values(self, width, height):
        self.__width = width    ## this is a private member
        self.__height = height  ## this is a private member
        
    ## define the get height method
    def get_height(self):  ## get_height is a public member.
        return self.__height   ## this is a private member
    
    ## define the get width method
    def get_width(self):   ## get_width is a public member.
        return self.__width    ## this is a private member