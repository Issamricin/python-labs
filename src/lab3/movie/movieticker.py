
ticket_amount= input("How many tickets do you want to buy? ")
ticket_amount= int(ticket_amount)

adult_number = input("How many tickers are for adults? ")
adult_number= int(adult_number)

number_of_children = tickes_amount- adult_number

total_price = children_number*child_price + adult_number*adult_price

print("You will pay:")
print(total_price)
