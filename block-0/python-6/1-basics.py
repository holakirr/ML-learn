from icecream import ic

print("#" * 100)
print("Practice")
print("#" * 100)

print("#" * 40, "Task 1", "#" * 40)
python_string = "Hello! My name is Python. I will help you to analyze some data."
ic(python_string[18:24])

print("#" * 40, "Task 2", "#" * 40)
python_string = "Hello! My name is Python. I will help you to analyze some data."
## result = 250047

python_string = (
    "Привет! Меня зовут Питон. Я помогу вам проанализировать некоторые данные."
)
## result = 389017

result = len(python_string) ** 3
ic(result)

print("#" * 40, "Task 3", "#" * 40)
predicted_time = 67.321
real_time = 59.839
## absolute_error = 7

predicted_time = 38.873
real_time = 26.124
## absolute_error = 13

absolute_error = round(predicted_time - real_time)
ic(absolute_error)

print("#" * 40, "Task 4", "#" * 40)
input_string = "Hello! My name is Python. I will help you to analyze some data."
## count_words = 13

input_string = "There are many great articles about Artificial Intelligence and its benefits for business and society. However, many of these articles are too technical for the average reader."
## count_words = 27

count_words = len(input_string.split())
ic(count_words)

print("#" * 40, "Task 5", "#" * 40)
file_path = "data/images/train/10394.jpg"
## file_name = '10394'
## file_extension = 'jpg'

file_path = "data/images/validation/748923.gif"
## file_name = '748923'
## file_extension = 'gif'

file_path = "data/images/384300.png"
## file_name = '384300'
## file_extension = 'png'

full_file_name = file_path.split("/")[-1]

file_name = full_file_name.split(".")[0]
file_extension = full_file_name.split(".")[1]
ic(file_name, file_extension)

print("#" * 40, "Task 6", "#" * 40)
generated_text = "глаза нее на поднял он и она попросила что-нибудь скажи"
## updated_text = "скажи что-нибудь попросила она и он поднял на нее глаза"

generated_text = "задачи своей решения способ или информацию ищет он поисковик в запрос вводит человек когда"
## updated_text = когда человек вводит запрос в поисковик он ищет информацию или способ решения своей задачи

updated_text = " ".join(generated_text.split()[::-1])
ic(updated_text)

print("#" * 40, "Task 7", "#" * 40)


def change_password(user_name, new_password):
    return "Пользователь {} сменил пароль на {}".format(user_name, new_password)


ic(change_password("Andrey", "31andrey12QK"))
## Пользователь Andrey сменил пароль на 31andrey12QK

ic(change_password("Vasilisk", "uaf12laK"))
## Пользователь Vasilisk сменил пароль на uaf12laK
