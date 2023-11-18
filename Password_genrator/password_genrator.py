import random
import string

def pass_genrator(length,numbers,special_char):
    #password varible
    pwd=""

    #creating actual password
    while len(pwd) < length:
        if numbers:
            pwd += random.choice(string.digits)
        if special_char:
            pwd += random.choice(string.punctuation)
        pwd += random.choice(string.ascii_letters)
    
    #shuffling the password
    pwd = list(pwd)
    random.shuffle(pwd)
    
    #turning the password back into the string
    pwd="".join(pwd)

    print(pwd)


def user_input():
    min_length=3

    #asking password length
    while True:
        pass_length_input=input("Enter the length of password you want : ")
        if pass_length_input.isdigit():
            pass_length_input=int(pass_length_input)
            if pass_length_input < min_length:
                print("minimum length is 3")
                continue
            else:
                break    
        else:
            print("Please enter a number : ")


    #asking if user want a number in their password
    has_number_input=input("Do you want to add numbers in your password. Press Y for yes or any other key to no : ")
    if has_number_input.lower() == 'y':
        has_number_input=True
        print("true")
    else:
        has_number_input=False
        print("false")


    #asking if user want a special character in their password   
    has_special_input=input("Do you want to add special character in your password. Press Y for yes or any other key to no : ")
    if has_special_input.lower() == 'y':
        has_special_input=True
        print("true")
    else:
        has_special_input=False
        print('false')


    #calling the function
    pass_genrator(pass_length_input,has_number_input,has_special_input)
    input("press enter or any other key to exit:")

user_input()