import json

with open("words_lib/words10000.json", "r", encoding="utf-8") as read:
    answer = json.load(read)
    print(len(answer))
