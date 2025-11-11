import sys

flag_1 = True

while flag_1:

    while True:
        age = input("Enter your age (or write 'Exit' to finish): ")

        if age.lower() == "exit":
            print("Finished program.")
            sys.exit()
            break
        
        elif age.isdigit():
            if 0 < int(age) < 18:
                infoage = "minor"
                break
            elif 17 < int(age) < 100:
                infoage = "adult"
                break
            else:
                print("Invaled age, try again.")
                continue
            
        elif not age.isdigit():
            print("Invalid, try again.")
            continue
    
    while True:
            gender = input("""Please select your gender:

    -M for male.
    -F for female.
    -O for other.

please select one: """).lower()
        
            if gender.lower() == "exit":
                    print("Finished program.")
                    sys.exit()
            
            elif gender in ['m', 'f', 'o']:
                
                if gender == 'm':
                    gender = 'Male'
                    break

                elif gender == 'f':
                    gender = 'Female'
                    break

                elif gender == 'o':
                    gender = 'Barbie'
                    break
                else:
                    continue
                
            else:
                print("Invalid gender, try again.\n")
                continue

    print (f"""


    You are a {infoage} {gender}          

""".title())

    while True:
        Answer =input("""Do you wanna try this code again?.
                    
                - Y for Yes.
                - N for No.
                    
            Select one: """).lower()

        if Answer == 'y':
                flag_1 = True
                break
        
        elif Answer == 'n':
                print("Finished program.")
                sys.exit()

        else:
            print ("Invalid input, finished program.")
            continue