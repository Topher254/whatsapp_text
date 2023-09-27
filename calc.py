print("HOME CALCULATOR")
print("1. Addition")
print("2. Subtraction")
print("3. Division")
print("4. Multipy")

decision =input("Hi there, what do you want to do ")

if decision == 1 or "Addition":
    nums =input("Enter your numbers ")
    adda = []
    adda.append(nums)
    for i in adda:
        solution = i+i
        print("SUM IS : ",solution)
        

# elif decision == 2 or "Subtraction":
#     numsa =int(input("Enter your numbers "))
#     subba = []
#     subba.append(numsa)
#     for i in subba:
#         solutiona = i+i
#     print("ANSWER IS : ",solutiona)
else:
    print("Try Again")

