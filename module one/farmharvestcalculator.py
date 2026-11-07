# --------------- INITIALIZING FIVE FEILDS -----------------
feild_one = 120
feild_two = 85
field_three = 150
feild_four = 95
feild_five = 110

total = feild_one + feild_two + field_three + feild_four + feild_five
average = total / 5
print("Total harvest: ", total, "Kg")
print("Average harvest: ", average, "Kg")

price_per_kg = 15
earnings = total * price_per_kg
print("Total earnings: #", earnings)

Bags = total // 25
leftover = total % 25
print("Bags: ", Bags)
print("Leftover: ", leftover, "Kg")

Last_year = 500
print("Is it better than last year? ", total > Last_year)
print("Is it worse than last year? ", total < Last_year)
print("Is it equal to last year? ", total == Last_year)
print("Is it as good as last year? ", total >= Last_year)

# -----BONUS-----------------------
total += 30
print("After crop bonus, total is: ", total, "Kg")

# ------------ SEED RESERVED FOR NEXT SEASON ----------------
total -= 15
print("After the seed reserve, total is: ", total, "Kg")

# ----------------- FINAL BAR COUNT-----------------
Bags = total // 25
print("Final bags: ", Bags)