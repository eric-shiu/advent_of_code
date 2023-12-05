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
}

OUTCOME_SCORE_MAP = {
    'X': 0,
    'Y': 3,
    'Z': 6,
}


def eval_round(opp, outcome):
    score = 0
    # outcome
    score += OUTCOME_SCORE_MAP[outcome]
    # shape
    if outcome == 'Y':
        shape_score = SHAPE_SCORE_MAP[opp]
    elif outcome == 'X':
        shape_score = (SHAPE_SCORE_MAP[opp] + 1) % 3 + 1
    elif outcome == 'Z':
        shape_score = (SHAPE_SCORE_MAP[opp]) % 3 + 1
    # print(shape_score)
    score += shape_score
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
    ans1 = cal_total_score(data[:])
    print(ans1)