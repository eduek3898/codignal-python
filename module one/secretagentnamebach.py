# frist step is getting agent details
name = input("enter your real name ,Agent: ")
gadget = input("enter your favourite gadget: ")

# step two is storing agent details using different data types
agent_number = 7
speed_rating = 9.5
mission_count = 12
height_m = 1.65
is_active = True

# step three is creating each detail along with it's data type
print("Agent Name: ", name, "Data Type: ", type(name))
print("Favourite Gadget: ", gadget, "Data Type: ", type(gadget))
print("Agent Number: ", agent_number, "Data Type: ", type(agent_number))
print("Speed Rating: ", speed_rating, "Data Type: ", type(speed_rating))
print("Mission Count: ", mission_count, "Data Type: ", type(mission_count))
print("Height in meters: ", height_m, "Data Type: ", type(height_m))
print("Is Active: ", is_active, "Data Type: ", type(is_active))

# step 4 is typecasting the numbers and true and false values into text
agent_number_text = str(agent_number)
mission_count_text = str(mission_count)
speed_rating_text = str(speed_rating)
status_text = str(is_active)

print("Agent Number: ", agent_number_text, "Data Type: ", type(agent_number_text))
print("Mission Count: ", mission_count_text, "Data Type: ", type(mission_count_text))
print("Speed Rating: ", speed_rating_text, "Data Type: ", type(speed_rating_text))
print("Is Active: ", status_text, "Data Type: ", type(status_text))

# step five is slicing the name to create a secret code name
first_three = name[0:3]
last_letter = name[-1]
code_name = first_three + last_letter
print("first three letters of your name: ", first_three)
print("last letter of your name: ", last_letter)
print("your secret code name is: ", code_name)

# step six is reverse gadget name using slicing
reversed_gadget = gadget[::-1]
print ("Reversed gadget name: ", reversed_gadget)

# step seven is to join everything together using the final badge message
badge_line_one = "AGENT" + code_name.upper()
badge_line_two = "ID: " + agent_number_text + "Missions: " + mission_count_text
badge_line_three = "SPEED: " + speed_rating_text + "ACTIVE: " + status_text
badge_line_four = "SECRET GADGET CODE: " + reversed_gadget.upper()

 #step eight is print a complete secret agent badge
print("")
print("====== SECRET AGENT BADGE ======")
print(badge_line_one)
print(badge_line_two)
print(badge_line_three)
print(badge_line_four)
print("================================")