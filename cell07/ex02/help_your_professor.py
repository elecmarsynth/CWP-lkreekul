#!/usr/bin/env python3

def average(class_dict):
    if not class_dict:
        return 0
    total_score = 0
    for score in class_dict.values():
        total_score += score
    return total_score / len(class_dict)

class_3B = {
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9
}

class_3C = {
    "quentin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
}

print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")