age = input("Are you a cigarette addict older than 75 years old? (Yes or No) ")
chronic = input("Do you have a chronic disease? ")
immune = input("Is your immune system too weak? ")

if age.title().strip() == "Yes" or chronic.title().strip() == "Yes" or immune.title().strip() == "Yes" :
    print("You are in risky group!")
else :
    print("You are not in risky group!")

