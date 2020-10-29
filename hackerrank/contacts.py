#!/bin/python3

import os
import sys

#
# Complete the contacts function below.
#
class Trie:
    def __init__(self):
        self.root = {}
        self.end = '*'
        self.counter = 0

    def add_word(self, string):
        node = self.root
        for char in string:
            if char not in node:
                node[char] = {}
            node = node[char]
        node[self.end] = True

    def prefix_number(self, string):
        node = self.root
        for char in string:
            if char not in node:
                return self.counter
            node = node[char]
        self.dfs_traverse(node)
        counter = self.counter
        self.counter = 0
        return counter

    def dfs_traverse(self, node):
        if self.end in node:
            self.counter += 1
        for char in node:
            if char != self.end:
                new_node = node[char]
                self.dfs_traverse(new_node)

def contacts(queries):
    #
    # Write your code here.
    #
    myTrie = Trie()
    # print(queries)
    ans = []
    for item in queries:
        if item[0] == "add":
            myTrie.add_word(item[1])
        else:
            ans.append(myTrie.prefix_number(item[1]))
    # for a in ans:
    #     print(a)
    return ans

if __name__ == '__main__':
    
    queries = [['add', 'hack'],['add', 'hacm'],['find', 'hac'],['add', 'hacx'], ['find', 'ha']]

    print(contacts(queries))