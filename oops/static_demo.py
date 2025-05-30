class MyClass:
    @staticmethod
    def static_method():
        print("This is a static method")

    def instance_method(self):
        print("This is an instance method")
        # Attempting to call the static method using self
        self.static_method()

# Calling static method using the class
MyClass.static_method()  # This works

# Creating an instance of MyClass
obj = MyClass()

# Calling instance method
obj.instance_method()  # This works, and it will call the static method within the instance method

# Calling static method using the instance
obj.static_method()  # This works, but it's not the recommended way to call static methods
