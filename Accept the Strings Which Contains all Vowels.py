#my method

# user_input=input("enter set elements seprated with:")
# my_set=set(user_input)
# if 'a' in my_set and 'e' in my_set and 'i' in my_set and 'o' in my_set and 'u'in my_set:
#     print(f"set accepted{my_set}")
# else:
#     print("set rejected")



# Better method that i learn from online


user_input=input("enter a string:")
def set_checker(str):
    str=str.lower()
    vowels=set('aeiou')
    s=set(str)
    subset=vowels.issubset(str)
    if subset:
        print("set passed")
    else:
        print("set did not pass")
set_checker(user_input)

#
def check(string):
    if len(set(string.lower()).intersection("aeiou")) >= 5:
        return ('accepted')
    else:
        return ("not accepted")