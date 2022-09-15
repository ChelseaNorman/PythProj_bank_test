def main():

    greeting = input("Greeting: ")
    output = value(greeting)
    print(output)

def value(greeting):
    greeting = greeting.lstrip().casefold()
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
