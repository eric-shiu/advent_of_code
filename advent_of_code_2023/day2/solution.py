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


SHAPE_SCORE_MAP = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3,
}


def eval_round(opp, me):
    score = 0
    # outcome
    if SHAPE_SCORE_MAP[opp] == SHAPE_SCORE_MAP[me]:
        score += 3
    elif SHAPE_SCORE_MAP[me] - SHAPE_SCORE_MAP[opp] in (1, -2):
        score += 6
    score += SHAPE_SCORE_MAP[me]
    return score


def cal_total_score(data):
    tot_score = 0
    for round in data:
        # print(round, eval_round(*round))
        tot_score += eval_round(*round)
    return tot_score



if __name__ == '__main__':
    dir = os.path.dirname(os.path.realpath(__file__))
    input = read_input(dir + '/input.txt')
    data = process_input(input)
    ans1 = cal_total_score(data)
    print(ans1)