age = int(input("Please enter your age: "))

gender = str(input("""Please select your gender:
                      -M for Male.
                      -F for female.
                      -O fot other.
                      
                   select one: """).lower())

if  0 < age < 18 and gender == 'f':
    print("You are a minor female.")
elif 17 < age < 100 and gender == 'f':
    print("You are an adult female.")
elif 0 < age < 18 and gender == 'm':
    print("You are a minor male.")
elif 17 < age < 100 and gender == 'm':
    print("You are an adult male.")
elif 0 < age < 18 and gender == 'o':
    print("You are a little barbie.")
elif 17 < age < 100 and gender == 'o':
    print("You are an barbie.")
else:
    print("Invalid input.")