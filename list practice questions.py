"""
Python Programming Questions – LIST

Basic Level

1. Write a Python program to create a list of integers and print its elements.

li=[10,20,30,50,70,100]
print(li)

2. Write a program to find the sum and average of all elements in a list.

li=[10,20,30,50,70,100]
total=sum(li)
average=total/len(li)

print("sum":total)
print("Average:",average)

3. Write a program to find the largest and smallest element in a list.

li=[10,20,30,50,70,100]
print(max(li))
print(min(li))

4. Write a Python program to count the number of elements in a list without using len().

li[10,20,30,50,70,100]
count=0
for i in li:
    count+=1
print("Number of elements:",count)


5. Write a program to reverse a list without using built-in functions.

li = [234,6,789,89,76,45,43]
print( li )
li.reverse()
print(li)

6. Write a program to check if an element exists in a list.

li=[10,20,30,50,70,100]
x=30
if x in li:
    print(" element exists in the list")
else:
    print("element done not exists")

7. Write a Python program to remove duplicate elements from a list.

li=[3,4,6,5,1,2,3,7]
print(li)
li.pop(6)
print(li)

8. Write a program to sort a list in ascending and descending order.

li=[3,4,6,5,1,2,7]
print(li)
li.sort()
print(li)
li.sort(reverse=True)
print(li)

Intermediate Level
9. Write a program to merge two lists and remove duplicates.

li1=[1,2,3,4]
li2=[3,4,5,6]
merged=li1+li2
result=[]
for i iin merged:
    if i not in result:
        result.append(i)
print("merged list without duplicate:",result)

10. Write a program to find common elements between two lists.

li1=[1,2,3,4]
li2=[3,4,5,6]
common=[]
for i in li1:
    if i in li2:
        common.append(i)
print("common elements:",common)

11. Write a program to split a list into even and odd numbers.

li=[1,2,3,4,5,6,7,8]
even=[]
odd=[]
for i in li:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Even numbers:",even)
print("odd number:",odd)

12. Write a program to rotate a list by n positions.

li = [1,2,3,4,5,6,7,8,9,10]
print( li )
n = int(input("No of Right Rotation : "))
for i in range(n):
    val = li.pop(len(li)-1)
    li.insert(0,val)
print(li)


13. Write a Python program to find the second largest number in a list.


14. Write a program to flatten a nested list.

li = [[12,34,67],[5,6,89],[45,78,67]]
f_li = []
print("Nested List :",li)
for x in li:
    for i in x:
        f_li.append(i)
print("Flaten List :",f_li)

OR

li = [[12,34],[5,6,89],72,[45,78,67]]
f_li = []
print("Nested List :",li)
for x in li:
    if type(x)==list:
        for i in x:
            f_li.append(i)
    else:
        f_li.append(x)
print("Flaten List :",f_li)


15. Write a program to count frequency of each element in a list.

li=[1,2,2,3,3,3,3,4]
freq={}
for i in li:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print("frequenncies:",freq)

16. Write a program to replace all negative numbers with zero in a list.

li=[10,-5,20,-3,-2,0,7]
for i in range(len(li)):
    if li[i]<0:
        li[i]=0
print("updated list:",li)

Advanced Level
17. Write a program to remove all occurrences of a given element from a list.

li=[1,2,3,2,4,2,5]
x=2
result=[]
for i in li:
    if i!=x:
    result.append(li)
print("List after removal:",result)

18. Write a program to check if a list is a palindrome.

li=[1,2,3,2,1]
if li==li[[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

19. Write a Python program to find missing numbers in a given list of consecutive integers.

li=[1,2,4,6,7,9]
missing=[]
for i in range(li[0],li[-1]):
    if i not in li:
        missing.append(i)
print("Missing numbers:",missing)

20. Write a program to perform element-wise addition of two lists.

li1=[1,2,3]
li2=[4,5,6]
result=[]
for i in range(len(li1)):
    result.append(li[i]+li2[i])
print("Result:",result)


21. Write a Python program to find the longest increasing subsequence in a list.
HINT:-
li = [21,78,89,765,23,23,35,39,45,667,8,9,635,58]

li = [21,78,89,765,23,23,35,39,45,667,8,9,635,58]
longest_sub_seq = []
temp = []
for i in range(0,len(li)-1):
    if li[i]<li[i+1]:
        temp.append(li[i])
    else:
        temp.append(li[i])
        if len(temp)>len(longest_sub_seq):
            longest_sub_seq = temp
        temp = []
print(longest_sub_seq)


22. Write a program to group elements based on frequency.

li = [1,4,6,54,3,1,3,4,6,5,3,2,1,3,4,6,54,3,1,4]

li = [1,4,6,54,3,1,3,4,6,5,3,2,1,3,4,6,54,3,1,4]
group_list = []
selected = []
for x in li:
    if x not in selected:
        selected.append(x)
        for j in li:
            if x==j:
                group_list.append(j)
print(group_list)

OR

li = [1,4,6,54,3,1,3,4,6,5,3,2,1,3,4,6,54,3,1,4]
s = set(li)
print(s)
group_list = []
for x in s:
    group_list.extend([x]*li.count(x))
print(group_list)
