user_details=[]
print("""Press 1. for sign up
         Press 2. for exit""")

user_choise=int(input("Enter your choise:"))
if(user_choise==1):
    while True:
        user_name=input("Enter your name:")
        user_pass=input("Enter your password")
        user_pass_confirmation=input("retype your password")
        if(user_pass==user_pass_confirmation):
            print("your account created successfully")
        else:
            print("your password does not match")
        if(user_name=="q"):
            print(user_details)
            exit()
        user_details.append(user_name)
else:
    exit()