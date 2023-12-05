import os

import pandas as pd


def read_input(fname):
    with open(fname, 'r') as f:
        input = f.read()
    return input


def process_input(input):
    data = []
    for line in input.splitlines():
        range1, range2 = line.split(',')
        data.append([
            [int(r) for r in range1.split('-')], 
            [int(r) for r in range2.split('-')]
        ])
    return data

def check_fully_contain(data):
    count = 0
    for range1, range2 in data:
        range1_min, range1_max = range1
        range2_min, range2_max = range2
        if (
            (range1_min <= range2_min) & (range1_max >= range2_max)
            | (range1_min >= range2_min) & (range1_max <= range2_max)
        ):
            count+=1
    return count

def check_overlap(data):
    count = 0
    for range1, range2 in data:
        range1_min, range1_max = range1
        range2_min, range2_max = range2
        if len(set(range(range1_min, range1_max+1)) & set(range(range2_min, range2_max+1))):
            count+=1
    return count

if __name__ == '__main__':
    dir = os.path.dirname(os.path.realpath(__file__))
    input = read_input(dir + '/input.txt')
    data = process_input(input)
    result = check_fully_contain(data)
    result2 = check_overlap(data)
    print(result)
    print(result2)