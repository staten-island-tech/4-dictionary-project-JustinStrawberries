print("Welcome to Trader Joe's, here is our catalog!")

items = [
{
    "name": "carrots",
    "price": 43.50,
    "aisle": "vegetables"
},
{
    "name": "apples",
    "price": 5.50,
    "aisle": "fruits"
},
{
    "name": "strawberry",
    "price": 1.00,
    "aisle": "fruits"
},
{
    "name": "lettuce",
    "price": 12.50,
    "aisle": "vegetables"
},
{
    "name": "raddish",
    "price": 2.50,
    "aisle": "vegetables"
}
]

for a in items:
    print(a["name"])

cart = []
reciept = []
purchase = input("What will you put in your cart?: ")

while True:
    if purchase == ("done"):
        break
    found = False
    for a in items:
        if purchase == a["name"]:
            found = True
            purchase = input("What else will you put in your cart? or are you done: ")
            cart.append({
                    "name": a["name"],
                    "price": a["price"]
                     })
            break
    if found == False:
        print ("Item is not found")
        purchase = input("What will you put in your cart? or are you done: ")

cost = 0

print("This is your final cart:")
print("Cart:", cart)
for item in cart:
    cost += item["price"]
print(cost)