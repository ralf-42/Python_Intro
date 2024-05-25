def greet():
    name = input("Bitte Namen eingeben: ")
    return f"Hello, {name}!"
    
if __name__ == "__main__":
    print(greet())