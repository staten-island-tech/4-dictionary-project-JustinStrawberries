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
    "aisle": "fruits"
},
{
    "name": "strawberry",
    "price": 12.50,
    "aisle": "fruits"
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

for index, items in enumerate(items, start=1):
    print(items ["name"],end=" ")
    print(items ["price"])

cart = []

purchase = input("What will you put in your cart?: ")
for items in purchase:
    print("This is what is in your cart: ", items)