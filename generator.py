import time


def generator_function():
    nums = [1,9,2]
    for i in nums:
        yield i
start  = time.time()
gen = generator_function()
print(next(gen))
print(next(gen))
print(next(gen))


#Syntax 2
syntax2 =  (i for i in range(100) if i%2==0)   # Called generator Expression
print(syntax2)

print(next(syntax2))
print(next(syntax2))
print(next(syntax2))
print(next(syntax2))

