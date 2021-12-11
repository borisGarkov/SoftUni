countries = input().split(", ")
capitals = input().split(", ")
matches = zip(countries, capitals)

data_dict = {key: value for (key, value) in matches}
[print(f"{key} -> {value}") for key,value in data_dict.items()]
