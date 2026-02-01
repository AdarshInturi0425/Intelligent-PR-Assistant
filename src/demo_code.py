def simple_function():
    print("This is clean code.")

def complex_logic_function():
    # This has 4 levels of nesting - our tool should flag this!
    for i in range(10):
        if i > 5:
            for j in range(10):
                if j < 5:
                    print(i, j)