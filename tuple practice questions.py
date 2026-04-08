Python Programming Questions – TUPLE

Basic Level

1. Write a Python program to create a tuple and print its elements.

t=(52,66,23,77,78,10)
print(t)

2. Write a program to find the length of a tuple.

t=(52,66,23,77,78,10)
print(len(t))

3. Write a program to find the maximum and minimum element in a tuple.

t=(52,66,23,77,78,10)
print(max(t))
print(min(t))

4. Write a program to convert a tuple into a list.

t=(52,66,23,77,78,10)
li=list(t)
print(li)


5. Write a program to check if an element exists in a tuple.

t=(52,66,23,77,78,10)
num=int(input("Enter number:"))
if num in t :
    print("Element exists")
else:
    print("Not found")


6. Write a program to count occurrences of an element in a tuple.

t=(10,20,30,40,50,60)
slice_tuple=t[1:5]
print("Original tuple:",t)
print("Sliced tuple :",slice_tuple)

Intermediate Level
7. Write a program to slice a tuple and display the result.

t=(52,66,23,77,78,10,77)
print(t)
print(t[2:5])

8. Write a program to find repeated elements in a tuple.

t=(1,2,3,2,3,4,5,3,6,2)
repeated = []

for i in t:
    if t.count(i) > 1 and i not in repeated:
        repeated.append(i)

print("Repeated elements:", repeated)


9. Write a program to merge two tuples.

t1(1,2,3,4)
t2(5,6,7,8)
merged =t1+t2
print("Merged tuples:",merged)

10. Write a program to unpack elements of a tuple into variables.
t=(10,20,30,40)
a,b,c=t
print("a=",a)
print("b=",b)
print("c"=c)

11. Write a Python program to sort a tuple.
t=(52,66,23,77,78,10,77)
sorted_tuple=tuple(sorted(t))
print("sorted tuple:",sorted_tuple)

12. Write a program to convert a list of tuples into a dictionary.

li=[("a",1),("b",2),("c",3)]
d={}
for key,value in li:
    d[key]=value
print("Dictionary:",d)

Advanced Level
13. Write a program to find the index of an element in a tuple.

t=(10,20,30,40,50)
x=30
for i in range(len(t)):
    if t[i]==x:
        print("Index:",i)
        break

14. Write a program to remove an element from a tuple (without directly modifying it).

t=(10,20,30,40,50)
x=30
for i in t:
    if i !=x:
        result +=(i,)
print("New tuple:",result)

15. Write a program to find common elements between two tuples.

t1=(1,2,3,4)
t2=(3,4,5,6)
common=()
for i in t1:
    if i in t2:
        common +=(i,)
print("Common elements:",common)

16. Write a Python program to check if a tuple is a palindrome.

t=(1,2,3,2,1)
if t==t[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
    

17. Write a program to find the element with maximum frequency.

t = (1,5,5,78,9,4,653,2,4,6,78,6,4,4,5,3,45,6,7,56,4,4)
maxx = t.count(t[0])
e = t[0]
for m in t:
    if maxx<t.count(m):
        maxx = t.count(m)
        e = m
print( e, maxx )

18.Write a program to create a nested tuple and acesss its elements.

"""

