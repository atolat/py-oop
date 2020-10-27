class A(object): 
    uniqueInstance = None
    
    @staticmethod
    def __new__(cls): 
        if cls.uniqueInstance == None:
            print("Creating instance") 
            cls.uniqueInstance = super(A, cls).__new__(cls)
        return cls.uniqueInstance 
    
if __name__ == '__main__':
    singleton1 = A()
    singleton2 = A()
    assert singleton1 == singleton2