from unittest import result

from icecream import ic

print("#" * 100)
print("Functions")
print("#" * 100)

print("#" * 40, "Task 1", "#" * 40)


def print_personal_data(**kwargs):
    kwargs = dict(sorted(kwargs.items()))
    for key, value in kwargs.items():
        ic(f"{key}: {value}")


print_personal_data(
    first_name="John", last_name="Doe", age=28, position="Python developer"
)
# age: 28
# first_name: John
# last_name: Doe
# position: Python developer

print_personal_data(
    first_name="Jack",
    last_name="Smith",
    age=32,
    work_experience="5 years",
    position="Project manager",
)
# age: 32
# first_name: Jack
# last_name: Smith
# position: Project manager
# work_experience: 5 years

print("#" * 40, "Task 2", "#" * 40)


def get_words_list(text):
    punctuation_list = [".", ",", ";", ":", "...", "!", "?", "-", '"', "(", ")"]
    for punctuation in punctuation_list:
        text = text.replace(punctuation, "")
    return text.lower().split()


text_example = "Arrakis, the planet known as Dune, is forever his place."

ic(get_words_list(text=text_example))
# ['arrakis', 'the', 'planet', 'known', 'as', 'dune', 'is', 'forever', 'his', 'place']

print("#" * 40, "Task 3", "#" * 40)


def get_unique_words(words_list):
    return sorted(set(words_list))


words_list_example = [
    "and",
    "take",
    "the",
    "most",
    "special",
    "care",
    "that",
    "you",
    "locate",
    "muad'dib",
    "in",
    "his",
    "place",
    "the",
    "planet",
    "arrakis",
    "do",
    "not",
    "be",
    "deceived",
    "by",
    "the",
    "fact",
    "that",
    "he",
    "was",
    "born",
    "on",
    "caladan",
    "and",
    "lived",
    "his",
    "first",
    "fifteen",
    "years",
    "there",
    "arrakis",
    "the",
    "planet",
    "known",
    "as",
    "dune",
    "is",
    "forever",
    "his",
    "place",
]

ic(get_unique_words(words_list=words_list_example))
## ['and', 'arrakis', 'as', 'be', 'born', 'by', 'caladan', 'care', 'deceived', 'do', 'dune', 'fact', 'fifteen', 'first', 'forever', 'he', 'his', 'in', 'is', 'known', 'lived', 'locate', 'most', "muad'dib", 'not', 'on', 'place', 'planet', 'special', 'take', 'that', 'the', 'there', 'was', 'years', 'you']


print("#" * 40, "Task 4", "#" * 40)


def get_most_frequent_word(text):
    def get_words_list(text):
        punctuation_list = [".", ",", ";", ":", "...", "!", "?", "-", '"', "(", ")"]
        for punctuation in punctuation_list:
            text = text.replace(punctuation, "")
        return text.lower().split()

    def get_unique_words(words_list):
        return sorted(set(words_list))

    words_list = get_words_list(text=text)
    unique_words = get_unique_words(words_list=words_list)
    max_count = 0
    result = ""
    for word in unique_words:
        count = words_list.count(word)
        if count > max_count:
            max_count = count
            result = word
    return result


text_example = "A beginning is the time for taking the most delicate care that the balances are correct. This every sister of the Bene Gesserit knows. To begin your study of the life of Muad'Dib, then take care that you first place him in his time: born in the 57th year of the Padishah Emperor, Shaddam IV. And take the most special care that you locate Muad'Dib in his place: the planet Arrakis. Do not be deceived by the fact that he was born on Caladan and lived his first fifteen years there. Arrakis, the planet known as Dune, is forever his place."
ic(get_most_frequent_word(text_example))
# the

text_example = "Есть урок, который идет не сорок пять минут, а всю жизнь. Этот урок проходит и в классе, и в поле, и дома, и в лесу. Я назвал этот урок седьмым потому, что в школе обычно бывает не больше шести уроков. Не удивляйтесь, если я скажу, что учителем на этом уроке может быть и береза возле вашего дома, и бабушка, и вы сами (В. Песков)"
ic(get_most_frequent_word(text_example))
# и

print("#" * 40, "Task 5", "#" * 40)


def get_total_score(data):
    result = []
    for student in data:
        result.append(student + (sum(student[1:]),))
    result.sort(key=lambda x: x[-1])
    return result


data = [
    ("Amanda", 37, 78, 67),
    ("Patricia", 78, 93, 68),
    ("Marcos", 79, 67, 89),
    ("Dmitry", 67, 68, 100),
    ("Andrey", 100, 78, 76),
    ("Victoria", 93, 69, 96),
]

ic(get_total_score(data))
# [('Amanda', 37, 78, 67, 182), ('Marcos', 79, 67, 89, 235), ('Dmitry', 67, 68, 100, 235), ('Patricia', 78, 93, 68, 239), ('Andrey', 100, 78, 76, 254), ('Victoria', 93, 69, 96, 258)]

print("#" * 40, "Task 6", "#" * 40)


def find_video(data):
    result = []
    if "videoID" in data:
        result.append(data["videoID"])
    for item in data["links"]:
        result.append(item["videoID"])
        if "links" in item:
            result.extend(find_video(item))
    return sorted(list(set(result)))


data = {
    "type": "video",
    "videoID": "vid001",
    "links": [
        {"type": "video", "videoID": "vid002", "links": []},
        {
            "type": "video",
            "videoID": "vid003",
            "links": [
                {"type": "video", "videoID": "vid004"},
                {"type": "video", "videoID": "vid005"},
            ],
        },
        {"type": "video", "videoID": "vid006"},
        {
            "type": "video",
            "videoID": "vid007",
            "links": [
                {
                    "type": "video",
                    "videoID": "vid008",
                    "links": [
                        {
                            "type": "video",
                            "videoID": "vid009",
                            "links": [{"type": "video", "videoID": "vid010"}],
                        }
                    ],
                }
            ],
        },
    ],
}
ic(find_video(data))
# ['vid001', 'vid002', 'vid003', 'vid004', 'vid005', 'vid006', 'vid007', 'vid008', 'vid009', 'vid010']
