sandwich_orders = [
    'veggie', 'pastrami','cheese', 'grilled cheese', 'pastrami', 'chicken' , 'grilled chicken', 'pastrami']
finished_sandwiches = []

print("I'm sorry, we're out of pastrami today.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')  

print ("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print ("I'm almost done making your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print ("I made your " + sandwich + " sandwich.")