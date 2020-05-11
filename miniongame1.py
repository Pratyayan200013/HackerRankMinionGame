#With linear time complexity O(n)
s=input('')
vowels='AEIOU'
kevin=0
stuart=0
for i in range(len(s)):
    if s[i] in vowels:
        kevin+=(len(s)-i)
    else:
        stuart+=(len(s)-i)
if kevin==stuart:
    print("Draw")
elif kevin>stuart:
    print(f"Kevin{kevin}")
else:
    print(f"Stuart{stuart}")
        
