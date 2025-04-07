class ExampleClass:
    def __init__(self):
        self.data = []
    
    def add_data(self, data):
        self.data.append(data)
    
    def print_data(self):
        print(self.data)

example_class = ExampleClass()
data1 = [1, 2, 3]
data2 = [4, 5, 6]

example_class.add_data(data1)
example_class.add_data(data2)
example_class.print_data()
