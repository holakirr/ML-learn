import numpy as np
from icecream import ic

print("#" * 100)
print("Tasks")
print("#" * 100)

print("#" * 40, "Task 1", "#" * 40)
mystery = np.array(
    [
        [-13586, 15203, 28445, -27117, -1781, -17182, -18049],
        [25936, -30968, -1297, -4593, 6451, 15790, 7181],
        [13348, 28049, 28655, -6012, 21762, 25397, 8225],
        [13240, 7994, 32592, 20149, 13754, 11795, -564],
        [-21725, -8681, 30305, 22260, -17918, 12578, 29943],
        [-16841, -25392, -17278, 11740, 5916, -47, -32037],
    ],
    dtype=np.int16,
)

elem_5_3 = mystery[4, 2]
ic(elem_5_3)
last = mystery[-1, -1]
ic(last)
line_4 = mystery[3]
ic(line_4)
col_2 = mystery[:, -2]
ic(col_2)
part = mystery[1:4, 2:5]
ic(part)
rev = mystery[::-1, -1]
ic(rev)
trans = mystery.transpose()
ic(trans)

print("#" * 40, "Task 2", "#" * 40)
mystery = np.array(
    [
        12279.0,
        -26024.0,
        28745.0,
        np.nan,
        31244.0,
        -2365.0,
        -6974.0,
        -9212.0,
        np.nan,
        -17722.0,
        16132.0,
        25933.0,
        np.nan,
        -16431.0,
        29810.0,
    ],
    dtype=np.float32,
)

nans_index = np.isnan(mystery)
n_nan = np.sum(nans_index)
mystery_new = mystery.copy()
mystery_new[nans_index] = 0
mystery_int = mystery_new.astype(np.int32)
array = np.sort(mystery)
table = array.reshape(5, 3, order="F")
col = table[:, 1]
