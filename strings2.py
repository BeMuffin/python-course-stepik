s = input()
t = input()

count = 0
for i in range(len(s)):
    if s.startswith(t, i, len(s)):
        count+=1

print(count)
