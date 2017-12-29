import re

print("My Calculator")
print("Type 'quit' to exit")

previous = 0
run = True

def perform_Math():
    global run
    global previous
    if previous == 0:
        equation = input("Enter equation:")
    else:
        equation = input(str(previous))

    if equation == "quit":
        run = False
        print("Thanks for using it!")
    else:
        equation = re.sub('[a-zA-Z,.:()" "]', '', equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)


while run:
    perform_Math()
