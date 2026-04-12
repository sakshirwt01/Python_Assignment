String Programming Questions
Basic
1. Write a program to count the number of vowels in a string.

s=input("Enter string:")
count=0
for ch in s:
    if ch.lower() in "aeiou":
        count+=1
print("Vowels:",count)

2. Reverse a string without using built-in functions.

s=input("Enter string:")
rev=""
for ch in s:
    rev=ch+rev
print("Reversed:",rev)

3. Check whether a string is a palindrome.

s=input("Enter string:")
rev=""
for ch in s:
    rev=ch+rev
if s==rev:
    print("palindrome")

4. Count uppercase and lowercase letters in a string.

s=input("Enter string:")
upper=lower=0
for ch in s:
    if ch.isupper():
        upper+=1
    elif ch.islower():
        lower+=1
print("Uppercase:",upper)
print("Lowercase:",lower)

5. Replace all spaces in a string with _.

s="Hello World"
result=""
for ch in s:
    if ch==" ":
        result+="_"
    else:
        result+=ch
print(result)


Intermediate


6. Find the frequency of each character in a string.

s=input("Enter string:")
freq={}
for ch in s:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]+1
print(freq)

7. Remove duplicate characters from a string.

s=input("Enter string:")
result=""
for ch in s :
if ch not in result:
    result+=ch
print(result)


8. Find the first non-repeating character in a string.

s=input("Enter string:")
for ch in s:
    if s.count(Ch)==1:
        print("First non repeating:",ch)
        break
        
9. Check if two strings are anagrams.

s1=input("Enter string:")
s2=input("Enter string:")
if sorted(S!)==sorted(S2):
    print("Anagram")
else:
    print(Not Anagram")
    
10. Convert "hello world" → "Hello World" (title case without using .title()).

s="hello world:
words=s.split()
result=""
for w in words:
    result+=w[0].upper()+w[1:]+""
print(result,strip())

Tricky

11. Find the longest word in a sentence.

s=input("Enter string:")
words=x.split()
longest=""
for word in words:
    if len(word)>len(longest):
        longest=word
print("Longest word:",longest)

12. Compress a string like "aaabbc" → "a3b2c1".

13. Count words, characters, and digits in a string.

s=input("Enter string:")
words=len(s.split())
chars=len(S)
digits=0
for ch in s:
    if ch.isdigit():
        digits+=1
print("Words:",words)
print("Characters:",chars)
print("Digits:",digits)

14. Rotate a string left by n positions.

s="abcdef"
n=2
print(s[n:]+s[:n])

15. Find all substrings of a given string.

s="abc"
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        print(s[i:j])
