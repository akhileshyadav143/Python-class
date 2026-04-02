# print("Hello World!")
# wap to degree calcious 

# degree =float (input("Enter the degree in celsius velue"))
# f=(degree*9/5)+32
# print(f)


# wapn which take the radius has ainput and calculate the area of circle or circumfrance 
# radius= float(input("Enter the radius of circle"))
# area = 3.14 * radius* radius
# circum = 3.14 * 2 * radius
# print ("readius of the circle",area)
# print("Circum of circle ",circum)



# conditinal statement

# wap which will check if the vote or not

# age=int(input("enter the age"))
# if age>=18:
#     print("you are vote")
# else:
#     print("you cannot vote")


# wap to determin grade based on marks

# marks=int(input("enter your marks"))
# if marks>=90:
#     print("Grade=A")
# elif marks>=80:
#          print("Grade=B")
# elif marks>=70:
#          print("Grade=C")
# elif marks>=60:
#         print("Grade=D") 
# else :
#      print("Grade=E")       


# wap ot find largest of three numbers

# number1=int(input("enter the  number"))
# number2=int(input("enter the  number"))
# number3=int(input("enter the  number"))
# if number1>=number2 and number1>=number3:
#                             print("number1 is greater")
# elif number2>=number1 and number2>=number3:
#                            print("number2 is greater")
# else:
#    print("greater number3" )            

# wap determine if a triangle is equlateral,isodceles,or scalene
# side1=float(input("Enter the side 1 of triangle:"))
# side2=float(input("Enter the side 2 of triangle:"))
# side3=float(input("Enter the side 3 of triangle:"))
# if side1 == side2 == side3 :
#     print("the triangle is a eqivalent triangle.")
# elif side1 == side2 or side1 == side3 or side2 == side3 :
#         print("the triangle is a isodceles triangle.")
# else:
#     print("the triangle is scalar triangle")

year=int(input("enter leap year"))
if (year%4==0 and year!=100 )or (year%400==0) :
    print(f"{year} is a leap year")
else :
        print("It is not a leap year")