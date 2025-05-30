def parent(num):
    def first_child(name):
        return f"Hi, I am {name}"
    def second_child(name):
        return f"Call me {name}"

    if num == 1:
        return first_child
    else:
        return second_child
first = parent(1)
second = parent(2)
print(second("Dharun")) # Call me Dharun