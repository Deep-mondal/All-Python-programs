class person:
    def __init__(ref):
        ref.name=input("Enter your name")
        ref.age=int(input("Enter your age"))
    def display(ref):
        print(ref.name)
        print(ref.age)
p1=person()
p1.display()

