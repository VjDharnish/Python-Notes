from decorator import do_twice,timeit


@do_twice
@timeit   #decorator order matters

def greeting(name):
    print("Hello "+name+" !")

greeting("Dharun")


