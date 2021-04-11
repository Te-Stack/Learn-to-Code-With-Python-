def add_positive_numbers(a,b):
    try:
        if a <= 0 or b <= 0:
            raise ValueError("One or both of the value is invalid .Both number must be positive")
        return a + b
        
    except ValueError as e:
        return f"Caught the ValueError:{e}"



print(add_positive_numbers(4,2))
print(add_positive_numbers(1,-4))