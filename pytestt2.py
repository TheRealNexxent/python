#More assertions
def add(a,b):
    return a+b

def divide(a,b):
    if b == 0:
        raise ValueError("Cannot divide by Zero!")
    else:
        return a/b
    
