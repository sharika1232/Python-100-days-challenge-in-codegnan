# check whether the number is Ever or Odd:

num=int(input("Enter the number:"))
if num%2==0:
    print("The number is Ever number")
else:
    print ("The number is odd number")

# find the large of two numbers:

a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
if a>b:
    print("A is greaterthan B")
elif b>a:
    print("B is greaterthan A")
else:
    print("Both are equal")

#check Eligibility to vote:


age=int(input("Enter the number:"))
if age>18:
    print("You are eligible for vote")
else:
    print("You are not eligible for vote")

#Grade Calculation:

m=int(input("Enter the number:"))
if m>=90:
    print("grade A")
elif 75<=m<90:
    print("grade B")
elif 50<=m<75:
    print("grade c")
else:
    print("fail")

#In three integers a,b,c. check the largest number among them:

a=int(input("Enter the 1st number:"))
b=int(input("Enter the 2nd number:"))
c=int(input("Enter the 3rd number:"))
if a>b and a>c:
    print ("A is largest number")
elif b>a and b>c:
    print("B is largest number")
else:
    print("c is largest number")

    
