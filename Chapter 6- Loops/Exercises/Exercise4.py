sandwich_orders = ['pastrami ', 'grilled chicken ', 'egg ', 'ice cream ']
finished_sandwiches=[]

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm almost done making your  " + current_sandwich + "sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I made your " + sandwich + "sandwich.")