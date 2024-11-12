try:
    with open("text.txt") as file:
        print(file.readline().strip())
except FileNotFoundError:
    print("!")
