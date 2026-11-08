# ------------------ ASK FOR TODAY'S TEMPERATURE ------------------ #
temperature = int(input("Enter the current temperature in Celsius: "))


# -------------------- DECIDE WHAT TO WEAR -------------------- #
if temperature < 20:
    outfit = "jacket"
    print("It is cold today.")
    print("You should wear a :", outfit)
else:
    outfit = "t_shirt"
    print("It is warm today.")
    print("You should wear a :", outfit)

# ---------------------------- ASK WHETHER IT IS RAINING ---------------------------- #
is_raining = input("Is it raining today? (yes/no): ")

# --------------------ADD AN UMBRERLLA IF IT IS RAINING -------------------- #
if is_raining == "yes":
    print("Don't forget to take an umbrella!")

# --------------------- ASK FOR WIND SPEED --------------------- #
wind_speed = int(input("Enter the wind speed in km/h: "))

# -------------------- DECIDE WHETHER TO WEAR A WIND BREAKER IS NEEDED BASED ON WIND SPEED -------------------- #
if wind_speed > 20:
    need_wind_breaker = "yes"
    print("It is windy today.")
    print("You should wear a wind breaker.", outfit)

# --------------------ASK WHETHER IF THERE ARE PUDDLES ON THE GROUND -------------------- #
has_puddles = input("Are there puddles on the ground? (yes/no): ")

# -------------------- DECIDE WHETHER TO WEAR RAIN BOOTS OR SNEEKERS BASED ON PUDDLES -------------------- #
if has_puddles == "yes":
    footwear = "rain_boots"
    print("There are puddles on the ground.")
    print("You should wear:", footwear)
else:
    footwear = "sneakers"
    print("There are no puddles on the ground.")
    print("You should wear:", footwear)

# -------------------- WEATHER CHECK COMPLETE -------------------- #
print("Weather check complete!")

# --------------------FINAL OUTFIT SUMMARY-------------------- #
print("WEATHER OUTFIT PICKER: ")
print("Temperature: ", temperature, "°C")
print("Outfit: ", outfit)
print("Is it raining?: ", is_raining)
print("Should i wear a wind breaker?: ", need_wind_breaker)
print("Shoes chosen: ", footwear)