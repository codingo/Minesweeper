#!/usr/bin/python3

print("Outputting sources")

f = open('./lib/sources.txt', 'r')

count=0
for line in f:
    print(line)
    count+=1
print(count)
