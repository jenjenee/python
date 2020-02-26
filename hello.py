#!/usr/bin/env python
# -*- encoding: utf8 -*-

#for n in range(height + 1):
 #   print(" " * n, "*" * (height - n))

#height = 10
#for n in range(height + 1):
#    print("*")


height = 10

for n in range(height):
    for s in range(height):
        if s >= n:
            print('*', end='')
    print()

for n in range(height):
    print("" * n, "*" * (height - n))

#for n in range(height)

print("Hello World!")