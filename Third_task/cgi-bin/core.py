#!/usr/bin/env python3

print("Content-type: text/html")
print()

with open("temp/index.html", "r") as index_file:
    for _ in index_file:
        print(_)
