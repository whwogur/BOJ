# 백준 1991
import sys
input = sys.stdin.readline

n = int(input().rstrip())
tree = {}

for _ in range(n):
    root, left, right = input().rstrip().split()
    tree[root] = [left, right]

def preOrder(root):
    if root != '.':
        print(root, end='') # root
        preOrder(tree[root][0]) # l
        preOrder(tree[root][1]) # r

def inOrder(root):
    if root != '.':
        inOrder(tree[root][0]) # l
        print(root, end='') # root
        inOrder(tree[root][1]) # r

def postOrder(root):
    if root != '.':
        postOrder(tree[root][0]) # l
        postOrder(tree[root][1]) # r
        print(root, end='') # root

preOrder('A')
print()
inOrder('A')
print()
postOrder('A')