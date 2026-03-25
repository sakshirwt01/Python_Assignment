"""
Q1.Check whether a number is divisible by 5 and 11.

num=int(input("Enter number:"))
if num%5==0 and num%11==0:
    print("divisible by 5 and 11")
else:
    print("not divisible")
    
Q2.Check if a person is eligible for loan:
● age ≥ 21
● salary ≥ 25,000
● credit score ≥ 700

age=int(input("Enter age :"))
salary=int(input("Enter salary:"))
credit_score=int(input("Enter credit score:"))
if age>=21 and salary>=25000 and credit_score >700:
    print("Eligible for loan")
else:
    print("Not eligible for loan")

Q3.Validate login using username AND password.

num=int(input("Enter number:"))
if num>=10 and num<=100:
    print("number is between 10 and 100")
else:
    print("number is outside the range")

Q4. Check student pass condition:
● All subjects ≥ 40
● Average ≥ 50

s1=int(input("Enter marks:"))
s2=int(input("Enter marks:"))
s3=int(input("Enter marks:"))
avg=(s1+s2+s3)/3
if s1>=40 and s2>=40 and s3>=40 and avg>=50:
    print("Pass")
else:
    print("fail")
    
Q5.Check if a number lies between 10 and 100.

num=int(input("Enter number:"))
if num>=10 and num<=100:
    print("number is between 10 and 100")
else:
    print("Not in range")

Q6. Check exam eligibility:
● attendance ≥ 75% OR
● medical certificate available

attendance=int(input("Enter attendance %:"))
medical=input("Medical certificate(yes/no):")
if attendance>=75 or medical == yes"
    print("eligible for exam")
else:
    print("not eligible for exam")


Q7.Validate a date using conditions.

day=int(input("Enter day:"))
month=int(input("Enter month:"))
if 1<=day <=31 and 1<=month <=12:
    print("Valid date")
else:
    print("Invaild date")

Q8.Check whether an email format is valid.

email=input("Enter email:")
if "@" in email and "." in email:
    print("valid email")
else:
    print("Invalid email")
    
Q9. Determine insurance eligibility using age, health status, and income

age=int(input("Enter age:"))
health=input("Enter health  condition:")
income=int(input("Enter income:"))
if age>18 and health=="good" and income>20000:
    print("Eligible for insurance")
else:
    print("not eligible")

Q10.Check leap year using complete leap year logic.

year=int(input("Enter year:"))
if year%4==0:
    print("leap year")
else:
    print("not leap year")
"""
