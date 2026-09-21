#!/usr/bin/env python3
import sys

if len(sys.argv) == 3:
    start = int(sys.argv[1])
    end = int(sys.argv[2])

    result = list()
    for i in range(start, end+1) :
        result.append(i)

    print(result)
else:
    print("none")
