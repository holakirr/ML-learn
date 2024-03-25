import numpy as np
from icecream import ic

arr, step = np.linspace(-6, 21, 60, endpoint=True, retstep=True)
ic(step)

arr, step = np.linspace(-6, 21, 60, endpoint=False, retstep=True)
ic(step)
