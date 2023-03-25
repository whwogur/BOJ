# 백준 1991
import sys
input = sys.stdin.readline

n = int(input().rstrip())
tree = {}

for _ in range(n):
    root, left, right = input().rstrip().split()
    tree[root] = [left, right]

def preOrderTraversal(root):
    if root != '.':
        print(root, end='') # root
        preOrderTraversal(tree[root][0]) # l
        preOrderTraversal(tree[root][1]) # r

def inOrderTraversal(root):
    if root != '.':
        inOrderTraversal(tree[root][0]) # l
        print(root, end='') # root
        inOrderTraversal(tree[root][1]) # r

def postOrderTraversal(root):
    if root != '.':
        postOrderTraversal(tree[root][0]) # l
        postOrderTraversal(tree[root][1]) # r
        print(root, end='') # root

preOrderTraversal('A')
print()
inOrderTraversal('A')
print()
postOrderTraversal('A')