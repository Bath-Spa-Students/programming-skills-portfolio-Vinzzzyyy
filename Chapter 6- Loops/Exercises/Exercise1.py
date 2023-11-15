prompt = "\nWhat toppings would you like on your pizza?"
prompt += "\nEnter 'quit' when you are done: "

while True:
    toppings= input(prompt)
    if toppings != 'quit':
        print("I will add " + toppings + "to your pizza.")
    else:
        break
