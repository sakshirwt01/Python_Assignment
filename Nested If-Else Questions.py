"""
Q1.Find the largest of three numbers.

a=int(input("Enter first number :"))
b=int(input("Enter second number :"))
c=int(input("Enter third number:"))
if a>b:
  if a>c:
    print("Largest:",a)
  else:
    print("Largest:",c)
else:
  if b>c:
    print("Largest:",b)
  else:
      print("Largest:",c)

Q2.Check whether a number is positive, negative, or zero.

num=int(input("Enter number:"))
if num>0:
    print("Positive number")
elif num<0:
    print("Negative  number")
else:
    print("zero")

Q3. Assign grades:
● A → marks ≥ 90
● B → marks ≥ 75
● C → marks ≥ 60
● Fail → below 60

marks=int(input("Entermarks:"))
if marks>=90:
    print("Grade A")
elif marks>=75:
    print("Grade B")
elif marks>=60:
    print("Grade C")
else:
    print("Fail")
    
Q4.Check whether a triangle is equilateral, isosceles, or scalene.

a= int(input("enter side 1:"))
b=int(input("Enter side 2:"))
c=int(input("Enter side 3:"))
if a==b and b==c:
    print("Equilateral triangle")
elif a==b or b==c or a==c:
    print("Isosceles triangle")
else:
    print("Scalene trianlge")


Q5.Check whether a character is uppercase, lowercase, digit, or special character.

ch= input("Enter A character:")
if ch>='0' and ch<='9':
    print("Digit")
elif ch>='A' and ch<='z':
    print("Upper  Case")
elif ch>='a' and ch<='z':
    print("Lower case")
else:
    print("Sepecial Character")

Q6.Calculate electricity bill using slab-wise rates.

units=int(input("Enter units:"))
if units<=100:
    bill=units*2
elif units<=200:
    bill=units*3
else:
    bill=units*5
    print("Electricity bill:",bill)
       
Q7.Validate login using username and password.

username=input("Enter username:")
password=input("Enter password:")
if username=="admin":
  if password=="1234":
    print("Login successful")
  else:
      print("Incorrect password")
else:
  print("Invalid username:")

Q8.Check student result using marks of 3 subjects.

s1=int(input("Enter marks for subject 1:"))
s2=int(input("Enter marks for subject 2:"))
s3=int(input("Enter marks for subject 3:"))
if s1>=40 and s2>=40 and s3>=40:
  print("pass")
else:
  print("fail")

Q29
a = 200
b = 300
c = 100

if a>b: 
    if a<c:
        print("Second Largest :",a)
    else:
        if b>c:
            print("Second Largest :",b)
        else:
            print("Second Largest :",c)
else:
    if b<c:
        print("Second Largest :",b)
    else:
        if a>c:
            print("Second Largest :",a)
        else:
            print("Second Largest :",c)  

Q10.Check loan eligibility using age, salary, and credit score.

age=int(input("Enter age:"))
salary=int(input("Enter salary:"))
credit=int(input("Enter credit score:"))
if age>=21:
    if salary>=25000:
        if credit>=650:
             print("Loan Approved")
        else:
             print("Low credit score")
    else:
        print("Salary too low")
else:
    print("Not eligible by age")
"""     
