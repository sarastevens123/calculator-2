
def print_customer_payment_statement(orders):
    file = open(orders)
    for words in orders:
        line = words.rstrip()
        item = line.split('|')
        full_name = item[1]
        first_name = full_name.split(" ")[0]
        purchase_amount = float(item[2])
        actual_price = float(item[3])
        
        if purchase_amount > actual_price:
            difference = purchase_amount - actual_price
            print(f"{first_name} overpaid by {difference}")
        elif purchase_amount < actual_price:
            difference = actual_price - purchase_amount
            print(f"{first_name} underpaid by {difference} ")
    file.close()
print(print_customer_payment_statement("customer-orders.txt"))


          
