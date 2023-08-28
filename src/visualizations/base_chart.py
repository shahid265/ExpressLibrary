class BaseChart:
    def __init__(self, data, x, y):
        self.data = data
        self.x = x
        self.y = y
    
    def load_data(self, data):
        self.data = data
    
    def set_axes(self, x, y):
        self.x = x
        self.y = y
    
    def basic_styling(self):
        # basic styling attributes
        pass