# Импортируем библиотеку для выполнения HTTP-запросов в интернет
from math import log

import requests

# Читаем текстовый файл по url-ссылке
data = requests.get(
    "https://raw.githubusercontent.com/SkillfactoryDS/Datasets/master/war_peace_processed.txt"
).text

# Предобрабатываем текстовый файл
data = data.split("\n")
data.remove("")
data = data + ["[new chapter]"]
# Превращаем список в множество, удаляя дублирующиеся слова
word_set = set(data)
# Удаляем из множества слово, символизирующее раздел между главами
word_set.discard("[new chapter]")
# Выводим результаты
print("Общее количество слов: {}".format(len(data)))
print("Общее количество уникальных слов: {}".format(len(word_set)))

# Инициализируем пустой словарь
word_counts = {}
# Инициализируем количество глав
count_chapter = 0
# Создаем цикл по всем словам из списка слов
for word in data:
    # Проверяем, что текущее слово - обозначение новой главы
    if word == "[new chapter]":
        # Если условие выполняется, то увеличиваем количество глав на 1
        count_chapter += 1
        # Переходим на новую итерацию цикла
        continue
    # Проверяем, что текущего слова еще нет в словаре слов
    if word not in word_counts:
        # Если условие выполняется, инициализируем новый ключ 1
        word_counts[word] = 1
    else:
        # В противном случае, увеличиваем количество слов на 1
        word_counts[word] += 1

# Выводим количество глав
print("Количество глав: {}".format(count_chapter))

# Создаем цикл по ключам и их порядковым номерам полученного словаря
for i, key in enumerate(word_counts):
    # Выводим только первые 10 слов
    if i == 10:
        break
    print(key, word_counts[key])

# Инициализируем общий список, в котором будем хранить списки слов в каждой главе
chapter_data = []
# Инициализируем список слов, в котором будет хранить слова одной главы
chapter_words = []

# Создаем цикл по всем словам из списка
for word in data:
    # Проверяем, что текущее слово - обозначение новой главы
    if word == "[new chapter]":
        # Если условие выполняется, добавляем список со словами из главы в общий список
        chapter_data.append(chapter_words)
        # Обновляем (перезаписываем) список со словами из текущей главы
        chapter_words = []
    else:
        # В противном случае, добавляем текущее слово в список со словами из главы
        chapter_words.append(word)

# Проверяем, что у нас получилось столько же списков, сколько глав в произведении
print("Вложенный список содержит {} внутренних списка".format(len(chapter_data)))
print(chapter_data[15][100])

# Инициализируем список, в котором будем хранить словари
chapter_words_count = []

# Создаем цикл по элементам внешнего списка со словами
for chapter_words in chapter_data:
    # Инициализируем пустой словарь, куда будем добавлять результаты
    temp = {}
    # Создаем цикл по элементам внутреннего списка
    for word in chapter_words:
        # Проверяем, что текущего слова еще нет в словаре
        if word not in temp:
            # Если условие выполняется, добавляем ключ в словарь
            temp[word] = 1
        else:
            # В противном случае, увеличиваем количество влождений слова в главу
            temp[word] += 1
    # Добавляем получившийся словарь в список
    chapter_words_count.append(temp)
print(chapter_words_count[15]["князю"])

print("_" * 100)
print("Задание 1.")
target_word = "гостья"
target_chapter = 15

# Ваш код здесь
term_frequency = chapter_words_count[target_chapter][target_word] / len(
    chapter_words_count[target_chapter].keys()
)
print(term_frequency)

print("_" * 100)
print("Задание 2.")
target_word = "человек"

# Ваш код здесь
word_count = 0
document_frequency = None
for chapter in chapter_words_count:
    if not target_word in chapter:
        continue
    else:
        word_count += chapter[target_word]
document_frequency = word_count / len(chapter_words_count)
print(document_frequency)

print("_" * 100)
print("Задание 3.")
target_word = "анна"
target_chapter = 4

# Ваш код здесь
term_frequency = chapter_words_count[target_chapter][target_word] / len(
    chapter_words_count[target_chapter].keys()
)
word_count = 0
document_frequency = None
for chapter in chapter_words_count:
    if not target_word in chapter:
        continue
    else:
        word_count += chapter[target_word]
document_frequency = word_count / len(chapter_words_count)
tf_idf = term_frequency * log(1 / document_frequency)
print(tf_idf)

print("_" * 100)
print("Задание 4.")
target_chapter = 3

# Ваш код здесь
three_words = {}
words_tf_idf = {}
for word in chapter_words_count[target_chapter]:
    term_frequency = chapter_words_count[target_chapter][word] / len(
        chapter_words_count[target_chapter].keys()
    )
    word_count = 0
    document_frequency = None
    for chapter in chapter_words_count:
        if not word in chapter:
            continue
        else:
            word_count += chapter[word]
    document_frequency = word_count / len(chapter_words_count)
    tf_idf = term_frequency * log(1 / document_frequency)
    words_tf_idf[word] = tf_idf

top_3_words = []
for i in range(3):
    max_value = 0
    max_word = None
    for word, tf_idf in words_tf_idf.items():
        if tf_idf > max_value and word not in top_3_words:
            max_value = tf_idf
            max_word = word
    top_3_words.append(max_word)

print(top_3_words)
