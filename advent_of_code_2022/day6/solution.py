import os

import pandas as pd


def read_input(fname):
    with open(fname, 'r') as f:
        input = f.read()
    return input


def process_input(input):
    data = []
    for line in input.splitlines():
        data.append(tuple(line.split()))
    # print(data)
    return data

def read_datastream(input, unique_seq_len):
    seq = []
    for cur, char in enumerate(input):
        if len(seq) < unique_seq_len:
            seq.append(char) 
        else:
            seq = seq[1:] + [char]
        if len(set(seq)) == unique_seq_len:
            return cur + 1 # off by 1


if __name__ == '__main__':
    dir = os.path.dirname(os.path.realpath(__file__))
    input = read_input(dir + '/input.txt')
    ans1 = read_datastream(input, 14)
    print(ans1)