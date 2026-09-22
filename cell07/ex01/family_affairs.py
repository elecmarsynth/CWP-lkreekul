#!/usr/bin/env python3

def find_the_redheads(dupont_family):
    def is_redhead(name):
        return dupont_family[name] == "red"

    return list(filter(is_redhead, dupont_family))

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))