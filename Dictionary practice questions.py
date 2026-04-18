Dictionary Programming Questions
Basic
1. Create a dictionary and print all keys and values.

d={"name":"Rahul","age":20,"city":"Delhi"}
for key,value in d.items():
    print(key,":",value)
    
2. Count frequency of each word in a sentence.

s="this is a test this is "
words=s.split()
freq={}
for w in words:
    if w in freq:
        freq[w]+=1
    else:
        freq[w]+=1
print(freq)

3. Merge two dictionaries.

d1={"a":1,"b":2}
d2={"c":3,"d":4}
merged={**d1,**d2}
print(merged)

4. Find the length of a dictionary.

d={"a":1,"b":2,"c":3}
print(len(d))

5. Check if a key exists in a dictionary.

d={name":"Rahul","age":20}
key=input("Enter key:")
if key in d:
    print("Key exists")
else:
    print("Not found")

Intermediate

6. Sort a dictionary by values.

7. Find the key with the maximum value.

d={"a":10,"b":20,"c":5}
max_key=max(d,key=d.get)
print(max_key)

8. Remove a key from a dictionary.

d={"a":1,"b":2,"c":3}
del d["b"]
print(d)

9. Convert two lists into a dictionary.

keys=["a","b","c"]
values=[1,2,3]
d=dict(zip(keys,values))
print(d)

10. Count character frequency using a dictionary.

s="hello"
freq={}
for ch in s:
    freq[ch]=freq.get(ch,0)+1
print(freq)

Tricky

11. Invert a dictionary (swap keys and values).

d={"A":1,"b":2}
inv={}
for k,v,in d.items():
    inc[v]=k
print(inv)

12. Group elements by frequency using a dictionary.

nums=[1,2,2,3,3,3]
freq={}
for n in nums:
    freq[n]=freq.get(n,0)+1
group={}
for k,v in freq..items():
    if v not in group:
       group[v]=[]
    group[v].append(k)
print(group)

13. Find duplicate values in a dictionary.

d={"a":1,"b":2,"c":1}
seen=set()
duplicates=set()
for v in d.values():
    if v in seen:
        duplicates.add(v)
    else:
        seen.add(v)
print(duplicates)

14. Create a nested dictionary for student records.

students={"John":{"age":20,"marks":85},
          "Anna":{"age":21,"marks":90}}
print(students["John"]["marks])
                       
15. Flatten a nested dictionary.

d={"a":10,"b":20}
print(sum(d.values()))

