import os
import sys


input_path = os.path.join(os.path.dirname(__file__), "4763.txt")

if os.path.exists(input_path):
    print("connected")
    sys.stdin = open(input_path, "r", encoding="utf-8")

n = int(input())
hate = [0]
for _ in range(n):
    hate.append(list(set(map(int,input()))))

