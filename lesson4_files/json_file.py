import json

#dumps() - Python -> JSON-строка (работает со строкой)
#loads() - JSON -> Python (работает со строкой)


#dump() - Python ->JSON.file (работает с файлом)
#load() - JSON.file - Python (работает с файлом)

user = {"username":"Egor", "age":30, "is_admin":True}

json_string = json.dumps(user)
print(json_string)
print(type(json_string))

user = json.loads(json_string)
print()
print(user)
print(type(user))
print(user["username"])
print()

test_config = {
    "base_url":"https://api.example.com",
    "timeout": 10,
    "retries":3
}

with open("config.json", "w", encoding="utf-8") as file:
    json.dump(test_config,file,indent=2,ensure_ascii= False)

with open("config.json", "r", encoding="utf-8") as file:
    loaded_config = json.load(file)

    print(loaded_config)
    print(loaded_config["base_url"])

