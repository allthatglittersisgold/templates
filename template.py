# import 
import sys
import math
import random
import bisect
from sys import stdin,stdout
from math import gcd, floor, sqrt, log
from collections import defaultdict as dd
from bisect import bisect_left as bl, bisect_right as br

# sys.setrecursionlimit(100000000)

# string input
inp     = lambda: int(input())
strng   = lambda: input().strip()
jn      = lambda x, l: x.join(map(str,l))
strl    = lambda: list(input().strip())
mul     = lambda: map(int, input().strip().split())
mulf    = lambda: map(float, input().strip().split())
seq     = lambda: list(map(int, input().strip().split()))

# misc
ceil    = lambda x: int(x) if x == int(x) else int(x)+1
floor   = lambda x: int(x) if x == int(x) else int(x)-1
ceildiv = lambda x, d: x//d if x%d == 0 else x//d+1

# stin/out
flush   = lambda: stdout.flush()
stdstr  = lambda: stdin.readline()
stdint  = lambda: int(stdin.readline())
stdpr   = lambda x: stdout.write(str(x))

# common mod
mod     = 1000000007

# main()
