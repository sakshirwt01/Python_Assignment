Set Programming Questions
Basic
1. Create a set and add elements dynamically.

s=set()
n=int(input("enter elements:"))
for i in range(n):
    val=input("Enter element:")
    s.add(val)
print(s)

2. Find the union and intersection of two sets.

a={1,2,3}
b={2,3,4}
print("Union:"a|b)
print("Intersection:"a&b)

3. Remove duplicate elements from a list using a set.

li=[1,2,2,3,4,4]
unique=list(set(li))
print(unique)

4. Check if an element exists in a set.

s={10,20,30,40}
x=int(input("Enter element:"))
if x in s:
    print("Exists")
else:
    print("Not found")
    
5. Find the difference between two sets.

a={1,2,3}
b={2,3}
print(a-b)

Intermediate
6. Find common elements in two lists using sets.

li1=[1,2,3,4,5]
li2=[3,4,5,6]
common=set(li1) &set(li2)
print(common)

7. Check whether one set is a subset of another.

a={1,2}
b={1,2,3,4,5}
print(a.issubset(b))

8. Find symmetric difference of two sets.

a={1,2,3}
b{3,4,5}
print(a^b)

9. Count unique elements in a list using a set.

li=[1,2,3,3,4,5,5]
print("Unique count:",len(set(li)))

10. Remove all common elements from two sets.

a={1,2,3}
b={2,3,4}
result=a^b
print(result)

Tricky
11. Find missing numbers from 1 to n using sets.

n=5
arr=[1,2,4]
print(set(range(1,n+1))-set(arr))

12. Check if two lists have any common elements.

li1=[1,2,3]
li2=[2,3,5]
if set(li1) &set(li2):
    print("Common elements exist")
else:
    print("No common elements")
    
13. Convert a set of strings into uppercase.

s={"hello","world"}
result={word.upper() for word in s}
print(result)

14. Identify unique vowels in a given string using a set.

s=input("Enter string:")
vowels=set()
for ch in s.lower():
    if ch in "aeiou":
        vowels.add(ch)
print(vowels)

15. Find elements that appear only once in a list.

li[1,2,3,3,4,5,5]
unique=[]
for num in li:
    if li.count(num)==1:
        unique.append(num)
print(unique)
