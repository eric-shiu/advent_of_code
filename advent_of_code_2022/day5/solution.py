import os
import re

import pandas as pd


def read_input(fname):
    with open(fname, 'r') as f:
        input = f.read()
    return input


def process_input(input):
    crates_raw, instructions_raw = input.split('\n\n')
    crates = []
    for line in crates_raw.splitlines():
        if '[' in line:
            crates.append([re.sub('\\W', '',line[i*4:(i+1)*4]) for i in range(len(line)//4 + 1)])
    instructions = []
    for line in instructions_raw.splitlines():
        matches = re.search('move ([0-9]+) from ([0-9]+) to ([0-9]+)', line)
        if matches:
            instructions.append([int(x) for x in matches.groups()])
    return crates, instructions


class Stack:
    def __init__(self):
        # Initialize an empty list for the stack
        self.items = []

    def push(self, item):
        # Append the item to the top of the stack
        self.items.append(item)

    def push_list(self, n_items):
        # Append list of items to top of the stack, order preserving
        for item in n_items:
            self.items.append(item)

    def pop(self):
        # Remove and return the item from the top of the stack
        return self.items.pop()

    def pop_n(self, n):
        # Remove n items from the top of the stack, order preserving
        n_items = self.items[-n:]
        self.items = self.items[0:-n]
        return n_items

    def peek(self):
        # Return the item from the top of the stack without removing it
        return self.items[-1]

    def is_empty(self):
        # Return True if the stack is empty, otherwise return False
        return len(self.items) == 0

    def size(self):
        # Return the number of items in the stack
        return len(self.items)


def gen_crate_stack(crates):
    stacks = dict()
    for row in crates[::-1]: # parse from bottom
        # print(row)
        for c, crate in enumerate(row):
            # print(c, crate)
            if crate != '':
                stacks[c+1] = stacks.get(c+1, Stack())
                stacks[c+1].push(crate)
        # show_stacks(stacks)
    # show_stacks(stacks)
    return stacks

def show_stacks(stacks):
    for line in [f"{key}: {s.items}" for key, s in stacks.items()]:
        print(line)


def execute(stacks, instructions):
    for N, orig, dest in instructions:
        for n in range(N):
            stacks[dest].push(stacks[orig].pop())
    return stacks

def execute2(stacks, instructions):
    for N, orig, dest in instructions:
        stacks[dest].push_list(stacks[orig].pop_n(N))
    return stacks

if __name__ == '__main__':
    dir = os.path.dirname(os.path.realpath(__file__))
    input = read_input(dir + '/input.txt')
    crates, instructions = process_input(input)
    stacks = gen_crate_stack(crates)
    print('execute below')
    # stacks = execute(stacks, instructions)
    stacks = execute2(stacks, instructions)

    # print(crates)
    # print(instructions)
    show_stacks(stacks)
    print(str(''.join([s.peek() for key, s in stacks.items() if not s.is_empty()])))