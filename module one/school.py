# ---------------- SCHOOL CLUB MEMBER BADGE ----------------

name = input("Member name: ")
club = input("Club name: ")
member_index = 8
points = 9.5
is_active = True
print("Member index: ", member_index, "- type: ", type(member_index))
print("Points: ", points, "- type: ", type(points))
print("Active: ", is_active, "- type: ", type(is_active))

badge_code = name[0:3] + club[-1:] + str(member_index)
print("Badge code: ", badge_code)

print("======= CLUB BADGE=========")
print("Member name: ", name)
print("Club name: ", club)
print("code: ", badge_code)
print("Points: ", str(points), "| Active: ", str(is_active))