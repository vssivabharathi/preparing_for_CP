def splitting(total, divide):
    divided = total / divide
    leftout = total % divide
    fin = int(divided)
    print(fin)
    print(leftout)
    print(f"The number of friends in each team is {fin} and left out is {leftout}")
    return 0

total = int(input(""))
divide = int(input(""))
splitting(total, divide)
