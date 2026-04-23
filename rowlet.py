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


user = input("Pick a Pokemon type: Normal, Fighting, Flying, Poison, Ground, Rock, Bug, Ghost, Steel, Fire, Water, Grass, Electric, Psychic, Ice, Dragon, Dark, Fairy")

for d in data:
    print(d["Ice"])

