"""
Python While Loop Exercise
Part 1 – Basic Level
1. Print numbers from 1 to 10 using a while loop.
a=1
while a<=10:
    print(a)
    a+=1

2. Print even numbers from 1 to 20.
a=1
while a<=20:
      if a%2==0:
          print(a)
      a+=1


3. Print odd numbers from 1 to 20.
a=1
while a<=20:
    if a%2!=0:
        print(a)
    a+=1

4. Print numbers from 10 to 1 (reverse order).

a=10
while a>=1:
    print(a)
    a-=1

5. Print multiplication table of 5 using while loop.

num=int(input("Enter number:"))
a=1
while a<=11:
    print(num*a)
    a+=1
    
Part 2 – Intermediate Level
6. Find the sum of first 10 natural numbers using while loop.


a=1
total=0
while a<=10:
    total+=a
    a+=1
print("sum:",total)


7. Find factorial of a number entered by user.

num=int(input("Enter number:"))
fact=1
i=1
while i<=num:
    fact*=i
    i+=1
print(fact)


8. Count number of digits in a given number.

num=int(input("Enter number:"))
count=0
while num!=0:
    num=num//10
    count+=1
print(count)

9. Reverse a number using while loop.
HINT:-   3846   =>  6483 (Reverse)

num = int(input("Enter A Number : "))   
add = 0
while num>0:
    rem = num%10
    add = add*10+rem
    num = num//10
print("Reverse Number :",add)


10. Check whether a number is palindrome or not using while loop.

num=int(input("Enter number:"))
temp=num
add=0
while num>0:
    rem=num%10
    reverse=reverse*10+rem
    num=num//10
if temp==reverse:
    print("Palindrome Number")
else:
    print("Not Palindrome")


Part 3 – Pattern Based
11. Print pattern:
*
**
***
****
*****

a=1
while a<=5:
    print("*"*a)
    a+=1


12. Print pattern:
1
12
123
1234
12345

i=1
while i<=5:
    j=1
    while j<=i:
        print(j,end="")
        j+=1
    print()
    i+=1


Part 4 – Logical / Real Scenario
13. Ask user to enter password until correct password is entered.

password=""
while password!="admin123":
    password=input("Enter password:")
print("Correct Password")    

14. Create a number guessing game:
• Generate a random number (1–10)
• Keep asking user until they guess correctly.

import random
secret=random.randint(1,10)
guess=0
while guess !=secret:
    guess =int(input("Guess number (1-10):"))
    if guess<secret:
        print("too low!")
    elif guess>secret:
        print("Too high!")
print("correct!")


15. Keep taking input numbers until user enters 0, then print total sum.
Bonus Challenge (Interview Level).

add = 0
while True:
    num = int(input("Enter A Number(0 for Exit) : "))
    add = add + num
    if num==0:
        break
print("Total :",add)

16. Print Fibonacci series up to N terms using while loop.

a = 0
b = 1
terms = 10
i = 1
while i<=10:
    c = a+b
    print(c)
    a = b
    b = c
    i+=1


17. Check whether a number is Armstrong number.

153 =>  1**3 + 5**3 + 3**3 => 1 + 125 + 27 => 153 (Armstrong)
num = 153
copy = num
add = 0
while num>0:
    rem = num%10
    add = add+rem**3
    num = num//10
print("New Number : ",add)
if copy==add:
    print("Armstrong")
else:
    print("Not Armstrong")

18. Print prime numbers between 1 to 50 using while loop.

i = 2
while i <= 50:
    j = 2
    is_prime = True

    while j < i:
        if i % j == 0:
            is_prime = False
            break
        j = j + 1
    if is_prime:
        print(i)
    i = i + 1



"""

    if is_prime:
        print(i)
    i = i + 1
