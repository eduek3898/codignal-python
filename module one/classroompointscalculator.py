# --------------CLASSROOM POINTS CALCULATOR-----------------

team_one = 90
team_two = 85
team_three = 110
team_four = 70
team_five = 130
# ----------CALCULATING TOTAL AND AVERAGE POINTS-----------------
total = team_one + team_two + team_three + team_four + team_five
average = total / 5
print("Total points: ", total)
print("Average points: ", average)
# ----------CALCULATING REWARD STARS-----------------
stars_per_point = 2
Rewarded_stars = total * stars_per_point
print("Total stars rewarded: ", Rewarded_stars)
# ----------USING FLOOR DIVISION AND MODULUS TO CALCULATE BOXES AND LEFTOVER STARS-----------------
boxes = Rewarded_stars // 25
leftover = Rewarded_stars % 25
print("Boxes: ", boxes)
print("Leftover stars: ", leftover)
# ------------COMPARING WITH LAST WEEK-----------------
lastweek = 400
print("Is it better than last week? ", total > lastweek)
print("Is it the same as last week? ", total == lastweek)
print("Is it atleast as good as last week? ", total >= lastweek)
# -----------UPDATE THE TOTAL POINTS-----------------
total += 20
print("After bonus points, total is: ", total)
total -= 10
print("After mised tasks, total is: ", total)
Rewarded_stars = total * stars_per_point
boxes = Rewarded_stars // 25
print("Final boxes packed: ", boxes)