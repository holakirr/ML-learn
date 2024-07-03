import numpy as np
from icecream import ic


def get_chess(n):
    res = np.zeros((n, n))
    res[1::2, ::2] = 1
    res[::2, 1::2] = 1
    return res


get_chess(1)
# array([[0.]])

get_chess(4)
# array([[0., 1., 0., 1.],
#        [1., 0., 1., 0.],
#        [0., 1., 0., 1.],
#        [1., 0., 1., 0.]])


def shuffle_seed(array):
    seed = np.random.randint(int(1e9))
    np.random.seed(seed)
    np.random.shuffle(array)
    return array, seed


array = [1, 2, 3, 4, 5]
shuffle_seed(array)
# (array([1, 3, 2, 4, 5]), 2332342819)
shuffle_seed(array)
# (array([4, 5, 2, 3, 1]), 4155165971)

vec1 = np.array([1, 2, 3])
vec2 = np.array([4, 5, 6])
vec3 = np.array([7, 8, 9])


def min_max_dist(*vectors):
    res = []
    for i in range(len(vectors)):
        for j in range(i + 1, len(vectors)):
            res.append(np.linalg.norm(vectors[i] - vectors[j]))
    return min(res), max(res)


min_max_dist(vec1, vec2, vec3)
# (5.196152422706632, 10.392304845413264)


vec1 = np.array([2, 1])
vec2 = np.array([-1, 2])
vec3 = np.array([3, 4])


def any_normal(*vectors):
    for i in range(len(vectors)):
        for j in range(i + 1, len(vectors)):
            if np.dot(vectors[i], vectors[j]) == 0:
                return True
    return False


print(any_normal(vec1, vec2, vec3))
# True


def get_loto(n):
    return np.random.randint(1, 101, (n, 5, 5))


print(get_loto(3))
# array([[[ 35,  66,  38,  11,  32],
#        [ 32,   7,  37,  83,  42],
#        [ 89,  37,  19,  51,  89],
#        [ 70, 100,  83,   5,  11],
#        [ 20,  13,  60,  26,  41]],

#       [[ 23,  49,  76,  44,  43],
#        [ 59,  63,  99,  92,   2],
#        [ 83,   4,  25,  73,  19],
#        [ 10,  18,  40,  11,  21],
#        [ 58,  45,  73,  93,  61]],

#       [[100,  88,  70,  34,  51],
#        [  5,  35,  36,  85,  88],
#        [ 72,  23,  87,  30,  40],
#        [ 29,  21,  51,  73,  81],
#        [ 91,  19,  87,  60,  27]]])


def get_unique_loto(n):
    res = np.zeros((n, 5, 5))
    for i in range(n):
        while True:
            res[i] = np.random.randint(1, 101, (5, 5))
            if len(set(res[i].flatten())) == 25:
                break
    return res


print(get_unique_loto(3))
# array([[[26, 91, 73,  7, 16],
#        [46, 85, 78, 77, 51],
#        [84, 86, 55, 71, 58],
#        [17, 61, 50, 30, 97],
#        [66, 29, 38, 41, 32]],

#       [[49, 32,  3, 21, 85],
#        [45,  8, 94, 46, 96],
#        [41, 38, 58, 37, 98],
#        [66, 77, 54, 80, 26],
#        [62, 63, 72,  5, 43]],

#       [[55, 60,  6, 80, 97],
#        [23, 69, 94,  9, 24],
#        [17, 98, 27, 63, 79],
#        [84, 74, 51, 39, 54],
#        [77, 30, 48, 75, 85]]])

a = get_unique_loto(10)

check = []
for i in a:
    check.append(len(set(i.flatten())))


print(check)
# [25, 25, 25, 25, 25, 25, 25, 25, 25, 25]
