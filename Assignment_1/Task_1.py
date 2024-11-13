num_dishes = int(input("How many dishes did you order? Please enter the quantity as a number (for example, 3): "))
total_dish_cost = 0
for i in range(1, num_dishes + 1):
    dish_price = float(input(f"Please enter the price of dish {i} in dollars: "))
    total_dish_cost += dish_price
tip_percentage = int(input("Please enter the percentage of the check you would like to leave as a tip. Just enter a number, for example 10, 15, or 20: "))
if total_dish_cost < 2000:
    tip_amount = total_dish_cost / 100 * tip_percentage
    total_cost_with_tip = total_dish_cost + tip_amount
    print(f"Your order total, including tip, is ${total_cost_with_tip}. Thank you for choosing our restaurant!")
if total_dish_cost > 2000:
    discounted_dish_cost = total_dish_cost - total_dish_cost * 0.1
    tip_amount_after_discount = discounted_dish_cost / 100 * tip_percentage
    total_cost_after_discount_and_tip = discounted_dish_cost + tip_amount_after_discount
    print("Your order is over $2000, so we are offering you a 10% discount!Thank you for choosing our restaurant!")
    print(f"The total cost of your order, including discount and tip, is ${total_cost_after_discount_and_tip}. We look forward to seeing you again!")