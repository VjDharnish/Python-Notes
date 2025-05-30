AttributeError: 'WeaviateQuery' object has no attribute '_WeaviateAdminController__get_collection_tenant'

is happening because the method __get_collection_tenant is defined with double underscores, which triggers Python’s name mangling.

Why This Happens

When a method or variable starts with double underscores (e.g. __get_collection_tenant), Python “mangles” the name internally to prevent accidental access from outside its class. For example:

class MyClass:
    def __my_private_method(self):
        ...

will internally be renamed to _MyClass__my_private_method.

So in your case, if __my_private_method is defined in MyClass, then accessing it from another_class_instance.my_class.__my_private_method.  will not work, because:
	•	it’s been mangled to _Another_Class__my_private_method
	•	and MyClass does not own it.

 How to Fix It

✅ Option 1: Rename method to use single underscore (recommended)
    This avoids name mangling and still signals it’s a “protected” method by convention.
⛔ Option 2: Access the mangled name (not recommended)
    But this is ugly and breaks encapsulation, and will fail if the method is actually defined in another class like WeaviateAdminController.
