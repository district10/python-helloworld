#!/bin/python3

import sys

def read_groundtruth(filename):
    try:
        lines = [line.strip() for line in open(filename)]
        return [list(map(float, line.split())) for line in lines]
    except:
        return [[]]

if __name__ == '__main__':
    filename = sys.argv[1] if len(sys.argv) > 1 else 'res/groundtruth.txt'
    matrix = read_groundtruth(filename)
    xs = list(map(lambda nums: nums[1], matrix))
    ys = list(map(lambda nums: nums[2], matrix))
    zs = list(map(lambda nums: nums[3], matrix))
    xmean = sum(xs) / len(xs)
    ymean = sum(ys) / len(ys)
    zmean = sum(zs) / len(zs)
    print(xmean, ymean, zmean)
