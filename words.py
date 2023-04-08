import json

f = open("data.json")
data = json.load(f)
words_list = data["data"]

f.close()
