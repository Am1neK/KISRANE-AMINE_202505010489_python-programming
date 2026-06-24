choice = "y"
while choice == "y":

    quiz1 = float(input("Enter Quiz 1 mark: "))
    quiz2 = float(input("Enter Quiz 2 mark: "))
    quiz3 = float(input("Enter Quiz 3 mark: "))

    average = (quiz1 + quiz2 + quiz3) / 3

    print("Average =", average)

    if average >= 50:
        print("PASS")
    else:
        print("FAIL")
    
    choice = input("Continue? Select Y/N: ")
print("Program Ended")
