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
}
]

for a in items:
    print(a["name"])

cart = []
while True:
    purchase = input("What will you put in your cart?: ")

    if purchase == "done":
        break

found = False

for a in items:
    if purchase == a["name"]:
        found = True
        purchase = input("What else will you put in your cart?: ")
        break

    if not found:
        print ("Item is not found")
        purchase = input("What will you put in your cart?: ")





