# JSON - JavaScript Object Notation
import json

# Python object থেকে JSON string (Serialization)
data = {
    "name": "Shahriar",
    "active": True,
    "score": None
}
json_string = json.dumps(data)
print(json_string)

# JSON file থেকে Python object (Deserialization)
with open("017_csv_json/shahriar.json", "r") as f:
    config = json.load(f)  
    print(config)
    print(config.keys)
    print(type(config))

# print(config)