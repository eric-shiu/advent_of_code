import os

import pandas as pd

def read_input(fname):
    with open(fname, 'r') as f:
        input = f.read()
    return input


def get_calorie_stats(input):
    groups = []
    this_group = []
    for line in input.splitlines():
        if len(line) > 0:
            this_group.append(int(line))
        else:
            groups.append(this_group)
            this_group = []

    calorie_stats = {i+1:sum(g) for i, g in enumerate(groups)}
    return calorie_stats


def find_max_calorie(calorie_stats):
    df = pd.Series(calorie_stats)
    return df.max()


def find_top3_total_calories(calorie_stats):
    df = pd.Series(calorie_stats)
    top3 = df.sort_values(ascending=False).iloc[:3]
    return top3.sum()


if __name__ == '__main__':
    dir = os.path.dirname(os.path.realpath(__file__))
    input = read_input(dir + '/input.txt')
    calorie_stats = get_calorie_stats(input)
    ans1 = find_max_calorie(calorie_stats)
    ans2 = find_top3_total_calories(calorie_stats)
    print(ans2)