# """ Conditinal Statements
# if/elif/else
# Syntax:
# if condition1 :
#     matter
# elif conditio2 : Optional occurenece >= 0
#     matter
# else : Optional and occurenece atleast 1
#     matter

# Example:
# age=int(input("Enter your age : "))
# # if age > 18 then you r eligible or not elegible
# if age>=18 and age<=30:
#     print("Im elegible")
# elif age>30:
#     print("You are child")
# else:
#     print("Im not elegible")
# """

# """Write a program to calculate
# Area of Square,circle,triangle(all 3),rectangle
# using conditional satements
# and take input from user and print output for each of them


# Output:
# 1.Sqaure
# 2.Recatngle
# 3.Eq Triangle
# 4.Is Triangle
# 5.Scalan Triangle
# 6.Right Angled Triangle
# 7.Circle

# Enter YOur Choice : (1-7)

# ex.
# if  choice ==1 //square
#     input -> enter side
#     print -> area
#     print -> permeter
#  """

# a=int(input("length"))

# ac=int(input("breadth"))
# q=a*ac

# clear
#  print("area of squares ",q)

print("1. Square and  Perimeter")
print("2. Rectangle")
print("3. Triangle")
print("4. Eq triangle ")
print("5. Is triangle")
print("6. Circle\n")

user_choice = float(input("what do you want : "))
print("\n")
# Square
if user_choice == 1:
    sq_side = float(input("Enter Side : "))
    area = sq_side**2
    print("Area of Square :", area, "\n")
    # print('\n')
    preimeter = sq_side * 4
    print("The Preimeter is ", preimeter)

# rectangle
elif user_choice == 2:
    length = float(input("Enter the length: "))
    breadth = float(input("Enter the Breadth: "))
    area = length * breadth
    print("Area Of Rectangle is: ", area)
# ABC = √[s × (s – a) × (s – b) × (s – c)].
# A = ½[√(a2 − b2/4) × b]
# triangle

elif user_choice == 3:
    print("1.if you have 3side")
    print("2.if you have base and height")
    user_choice1 = input("enter your choice")
    if user_choice1 == "1":
        a = float(input("enter 1st side"))
        b = float(input("enter 2st side"))
        c = float(input("enter 3st side"))
        s = (a + b + c) * 2
        area = [s * (s - a) * (s - b) * (s - c)] ** 0.5
        print("area 3 side triangle")
    elif user_choice1 == "2":
        hei = float(input("enter height"))
        bas = float(input("enter base"))
        area = (hei * bas) / 2
        print("Area Of TRiangle", area)
    else:
        print("invalid choice")

elif user_choice == 4:
    a = float(input("enter side"))
    # A=((3)**0.5/4)*a**2

    area = ((3) ** 0.5 / 4) * a**2
    print(f"Area of eq trianle:{area}")

elif user_choice == 5:
    bas = float(input("enter base"))
    hei = float(input("enter height"))
    area = bas * hei / 2
    print("Area Of iso triangle", area)

elif user_choice == 6:
    rad = float(input("enter radius"))
    area = 3.14 * rad**2
    print(f"Area Of Triangle:{area}")

else:
    print("invalid choice")

    # length=float(input("Enter the height: "))
    # breadth=float(input("Enter the Breadth: "))

    # area=(length*height)/2
    # print(f"Area Of triangle: "[area])


# # '''
# What is function?

# ans : used to reduce redundancy/dupliation
# '''

# def akash_function(a):
#     print(f"Gaurand ")

# a=1
# akash_function()
# def akash_fuction1():
#     print("a")
# akash_fuction1()
