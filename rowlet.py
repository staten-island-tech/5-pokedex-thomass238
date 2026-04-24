import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)



# for index, item in enumerate(data):
#     print(item["name"])

# lang=input("What language do you prefer: english, japanese, chinese, or french?         ")
# for d in data:
#     print(d["name"][lang])


psearch = input("Input a keyword for Pokemon         ")
for d in data:
    if psearch in (d["name"]["english"]):
        print (d["name"]["english"])

# tsearch = input("Input a type           ")
# for thomas in data:
#     if tsearch in (thomas["type"]):
#         print(thomas["name"]["english"])

