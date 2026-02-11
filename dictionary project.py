print("Welcome to Trader Joe's, here is our catalog!")

items = [
{
    "name": "carrots",
    "price": 12.50,
    "aisle": "vegetables"
},
{
    "name": "apples",
    "price": 12.50,
    "aisle": "vegetables"
},
{
    "name": "strawberry",
    "price": 12.50,
    "aisle": "vegetables"
},
{
    "name": "lettuce",
    "price": 12.50,
    "aisle": "vegetables"
},
{
    "name": "raddish",
    "price": 12.50,
    "aisle": "vegetables"
},
]

for index, items in enumerate(items, start=0):
    print(items["name"])
purchase = input("What will you put in your cart?: ")