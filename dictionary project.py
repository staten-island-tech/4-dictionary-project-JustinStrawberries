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

for a, i in enumerate(items):
    print(a, ":", i["name"])
    # print(stuff["price"])

found = False
purchase = input("What will you put in your cart?: ")

for purchase in items["names"]:
    print("This is what is in your cart: ", purchase)
    found = True
    break

if not found:
    print("No match")


