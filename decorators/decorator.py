import time
from math import ceil
from functools import wraps
import json 
import cherrypy
# def do_twice(func):
#     def wrapper(*args,**kwargs):
#         func(*args,**kwargs)
#         func(*args,**kwargs)
#     return wrapper

# def timeit(func):
#     def wrapper(*args,**kwargs):
#         start_time= time.time()
#         result =func(*args,**kwargs)
#         end_time = time.time()
#         total = (end_time-start_time)*1000
#         print(f"Function : {func.__name__} Execution Time: {ceil(total)} seconds")
#         return result 
#     return wrapper

# class A:
#     def process_data(self):
#         print("Processing A with", self)

# def get_instance(func):
#     def wrapper(instance,*args,**kwargs):
#         if instance.clo is None:
#             print("Not INitailixecd")
#             instance.clo= A()
#         return func(instance,*args,**kwargs)
#     return wrapper

# class MyClass:
#     def __init__(self):
#         self.clo = None
#         print("MyClass instance initialized")

#     @get_instance
#     def process_data(self):
#         print("Processing data with", self)


# obj  =MyClass()
# obj.process_data()

def validate_service(func):
    @wraps(func)
    def wrapper(instance,service_name,*args,**kwargs):
        headers = cherrypy.request.headers
        if service_name not in instance.services_list.keys():
            raise ValueError(400,f"Invalid service")
        elif instance.service is None:
            raise ValueError(400,"Connect to the service")
        return func(instance,service_name,*args,**kwargs)
    return wrapper
class AdminController:

    def __init__(self):
        with open('/Users/dharan-19096/VisualStudioProjects/WeaviateAdmin/conf/services.json','r') as service_file:
            json_string=service_file.read()
            self.services_list = json.loads(json_string)['services']
           
        self.service=None

    @validate_service
    def do_service(self,service_name):
        print(f"{service_name} is active")

    def connect_to_service(self,service_name):
        if service_name not in self.services_list.keys():
            raise ValueError(404,"Invalid Service")
        self.service=service_name

ac =AdminController()

ac.connect_to_service(service_name="deduplication")
ac.do_service(service_name="deduplicion")