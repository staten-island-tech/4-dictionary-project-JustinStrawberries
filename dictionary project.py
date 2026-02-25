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

# while input not in items:
#     stuff = input("What wold you like in your cart")

# def skibidi():
#     if stuff not in items:
#         return


purchase = input("What will you put in your cart?: ")
cart = []
if purchase in "name":
    print("This is what is in your cart: ", purchase)
else:
    print("No match")


