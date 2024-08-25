import pandas as pd

df = pd.DataFrame(
    {
        "name": ["John", "Jane", "Bob", "Alice", "Tom"],
        "age": [25, 30, 35, 28, 40],
        "experience": [
            "Опыт работы 8 лет 3 месяца",
            "Опыт работы 3 года 5 месяцев",
            "Опыт работы 1 год 9 месяцев",
            "Опыт работы 3 месяца",
            "Опыт работы 6 лет",
        ],
        # Add other columns as needed (salary, department, etc.)
    }
)


def get_experience(arg):
    arr = arg.split(" ")
    res = 0
    for idx, substr in enumerate(arr, start=0):
        if idx + 1 < len(arr):
            if "мес" in arr[idx + 1]:
                res = res + int(substr)
            elif "г" in arr[idx + 1] or "л" in arr[idx + 1]:
                res = res + int(substr) * 12
    return res


df["experience"] = df["experience"].apply(get_experience)
print(df)
