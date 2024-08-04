class Myclass:
    def method(self, a, b=None):
        if b is None:
            print(a)
        else:
            print(a + b)

# Example usage
obj = Myclass()
obj.method(3)    
obj.method(3, 4)
