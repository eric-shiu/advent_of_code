import os

import pandas as pd
import numpy as np


def read_input(fname):
    with open(fname, 'r') as f:
        input = f.read()
    return input


def process_input(input):
    data = []
    for line in input.splitlines():
        data.append([int(h) for h in line])
    return np.array(data)


def tallest_from_dir(data, axis: int, dir: int):
    n_row, n_col = data.shape
    tallest_so_far = np.zeros_like(data)
    assert axis in (0, 1)
    assert dir in (1, -1)
    if axis == 1 and dir == 1:
        for j in range(1, n_col)[::dir]: 
            tallest_so_far[:, j] = data[:, 0:j].max(axis=axis)
    elif axis == 1 and dir == -1:
        for j in range(0, n_col-1)[::dir]: 
            tallest_so_far[:, j] = data[:, j+1:].max(axis=axis)
    elif axis == 0 and dir == 1:
        for i in range(1, n_row)[::dir]: 
            tallest_so_far[i, :] = data[0:i, :].max(axis=axis)
    elif axis == 0 and dir == -1:
        for i in range(0, n_row-1)[::dir]: 
            tallest_so_far[i, :] = data[i+1:, :].max(axis=axis)
    return tallest_so_far
        

def count_visible(data):
    n_row, n_col = data.shape
    counter = 0
    is_visible = np.zeros_like(data)
    tallest_sofar_from_top = tallest_from_dir(data, axis=0, dir=1)
    tallest_sofar_from_bottom = tallest_from_dir(data, axis=0, dir=-1)
    tallest_sofar_from_left = tallest_from_dir(data, axis=1, dir=1)
    tallest_sofar_from_right = tallest_from_dir(data, axis=1, dir=-1)
    for i in range(n_row):
        for j in range(n_col):
            if (i == 0) | (j == 0) | (i == n_row - 1) | (j == n_col - 1):
                counter += 1
                is_visible[i,j] = 1
            elif (
                (data[i,j] > tallest_sofar_from_top[i,j])
                | (data[i,j] > tallest_sofar_from_bottom[i,j])
                | (data[i,j] > tallest_sofar_from_left[i,j])
                | (data[i,j] > tallest_sofar_from_right[i,j])
            ):
                counter += 1
                is_visible[i,j] = 1
    
    return counter, is_visible


def calc_trees_viewable(height, trees):
    if len(trees) == 0:
        return 0
    elif trees[0] >= height:
        return 1
    n_view = 0
    for t in trees:
        n_view += 1
        if t < height:
            pass
        else:
            break
    return n_view


def calc_scenic_score(data):
    n_row, n_col = data.shape
    up_score = np.zeros_like(data)
    down_score = np.zeros_like(data)
    left_score = np.zeros_like(data)
    right_score = np.zeros_like(data)
    scenic_score = np.zeros_like(data)
    for i in range(n_row):
        for j in range(n_col):
            trees_above = data[0:i, j][::-1]
            up_score[i,j] = calc_trees_viewable(data[i,j], trees_above)
            trees_below = data[i+1:, j]
            down_score[i,j] = calc_trees_viewable(data[i,j], trees_below)
            trees_left = data[i, 0:j][::-1]
            left_score[i,j] = calc_trees_viewable(data[i,j], trees_left)
            trees_right = data[i, j+1:]
            right_score[i,j] = calc_trees_viewable(data[i,j], trees_right)
            scenic_score[i,j] = up_score[i,j] * down_score[i,j] * left_score[i,j] * right_score[i,j]
    return scenic_score
            


if __name__ == '__main__':
    dir = os.path.dirname(os.path.realpath(__file__))
    input = read_input(dir + '/input.txt')
    data = process_input(input)
    counter, is_visible = count_visible(data)
    scenic_score = calc_scenic_score(data)
    # print(counter)
    # print(is_visible)
    print(scenic_score.max())
    print(scenic_score)