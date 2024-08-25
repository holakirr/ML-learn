import pandas as pd
from icecream import ic

data = pd.read_csv(
    "https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/ufo.csv"
)

ic(data)

# В каком году отмечается наибольшее количество случаев наблюдения НЛО в США?

data["Time"] = pd.to_datetime(data["Time"])
ic(data["Time"].dt.year.value_counts().idxmax())

# Найдите средний интервал времени (в днях) между двумя последовательными случаями наблюдения НЛО в штате Невада (NV).
# Чтобы выделить дату из столбца Time, можно воспользоваться атрибутом datetime date.

# Чтобы вычислить разницу между двумя соседними датами в столбце, примените к нему метод diff().

# Чтобы перевести интервал времени в дни, воспользуйтесь атрибутом timedelta days.

nv_rest = data[data["State"] == "NV"]
nv_rest["Rest Days"] = nv_rest["Time"].diff()
mean_rest_days = nv_rest["Rest Days"].dt.days.mean()
ic(mean_rest_days)
