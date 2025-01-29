import json
x = {
    "name":"nagarjuna",
    "age":22,
    "city":'blr'
}
y=json.dumps(x)             #If you have a Python object, you can convert it into a JSON string by using the json.dumps() method
print(y)
z = json.loads(y)           #If you have a JSON string, you can parse it by using the json.loads() method.
print(z["city"])
