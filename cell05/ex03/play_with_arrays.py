#!/usr/bin/env python3

arr = [2, 8, 9, 48, 8, 22, -12, 2]
new = []

for num in arr:
    if num > 5:
        temp = num + 2
        if temp not in new:
            new.append(temp)

print(arr)
print(set(new))